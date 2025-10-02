// SPDX-FileCopyrightText: Copyright © DUNE Project contributors, see file LICENSE.md in module root
// SPDX-License-Identifier: LicenseRef-GPL-2.0-only-with-DUNE-exception
// -*- tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 2 -*-
// vi: set et ts=4 sw=2 sts=2:

#include <iterator>

#include <dune/common/fmatrix.hh>
#include <dune/common/fvector.hh>
#include <dune/common/float_cmp.hh>
#include <dune/common/gmpfield.hh>
#include <dune/common/quadmath.hh>
#include <dune/common/simd/loop.hh>

#include <dune/istl/matrixmarket.hh>
#include <dune/istl/io.hh>
#include <dune/istl/bvector.hh>

#if HAVE_MPI
#include <dune/istl/paamg/test/anisotropic.hh>
#include "mpi.h"
#include <dune/istl/schwarz.hh>
#else
#include <dune/istl/operators.hh>
#include "laplacian.hh"
#endif

#if HAVE_GMP
template<unsigned int prec>
struct Dune::FloatCmp::EpsilonType<Dune::GMPField<prec>> {
  typedef float Type;
};
#endif

template <class Matrix, class Vector>
int testMatrixMarket(int N)
{
#if HAVE_MPI
  typedef int GlobalId;
  typedef Dune::OwnerOverlapCopyCommunication<GlobalId> Communication;
  Communication comm(MPI_COMM_WORLD);
  std::cout << comm.communicator().rank() << " " << comm.communicator().size() << std::endl;
  int n;
  Matrix mat = setupAnisotropic2d<typename Matrix::block_type>(N, comm.indexSet(), comm.communicator(), &n, .011);
#else
  Matrix mat;
  setupLaplacian(mat, N);
#endif

  Vector bv(mat.N()), cv(mat.N());

  int i=0;
  for(auto&& block : bv)
    for(auto&& entry : Dune::Impl::asVector(block))
      entry = (i++);

  using R = typename Dune::FieldTraits<Vector>::real_type;
  int prec = std::numeric_limits<R>::is_specialized
    ? std::numeric_limits<R>::max_digits10
    : std::numeric_limits<long double>::max_digits10;
  R eps = std::numeric_limits<R>::is_specialized
    ? std::numeric_limits<R>::epsilon()
    : R(std::numeric_limits<float>::epsilon()) ;

#if HAVE_MPI
  comm.remoteIndices().rebuild<false>();
  comm.copyOwnerToAll(bv,bv);

  Dune::OverlappingSchwarzOperator<Matrix,Vector,Vector,Communication> op(mat, comm);
  op.apply(bv, cv);
  storeMatrixMarket(mat, std::string("testmat"), comm, true, prec);
  storeMatrixMarket(bv, std::string("testvec"), comm, false, prec);
#else
  typedef Dune::MatrixAdapter<Matrix,Vector,Vector> Operator;
  Operator op(mat);
  op.apply(bv, cv);

  storeMatrixMarket(mat, std::string("testmat"), prec);
  storeMatrixMarket(bv, std::string("testvec"), prec);
#endif

  Matrix mat1;
  Vector bv1,cv1;

#if HAVE_MPI
  Communication comm1(MPI_COMM_WORLD);

  loadMatrixMarket(mat1, std::string("testmat"), comm1);
  loadMatrixMarket(bv1, std::string("testvec"), comm1, false);
#else
  loadMatrixMarket(mat1, std::string("testmat"));
  loadMatrixMarket(bv1, std::string("testvec"));
#endif

  int ret=0;
  if(mat.N()!=mat1.N() || mat.M()!=mat1.M())
  {
    ++ret;
    std::cerr<<"matrix sizes do not match"<<std::endl;
  }

  for (auto row=mat.begin(), row1=mat1.begin(); row!=mat.end(); ++row, ++row1)
    for (auto col=row->begin(), col1=row1->begin(); col!= row->end(); ++col, ++col1)
    {
      if(col.index()!=col1.index()) {
        std::cerr <<"Column indices do not match"<<std::endl;
        ++ret;
      }
      if(!Dune::FloatCmp::eq(*col, *col1)) {
        using std::abs;
        std::cerr <<"Matrix entries do not match: " << abs(*col - *col1) << std::endl;
        ++ret;
      }
    }

  for (auto entry=bv.begin(), entry1=bv1.begin(); bv.end() != entry; ++entry, ++entry1)
    if (Dune::Simd::anyTrue(abs(*entry - *entry1) > eps))
    {
      std::cerr<<"written and read vector do not match"<<std::endl;
      ++ret;
    }

  cv1.resize(mat1.M());

#if HAVE_MPI
  Dune::OverlappingSchwarzOperator<Matrix,Vector,Vector,Communication> op1(mat1, comm1);
  op1.apply(bv1, cv1);

  if(comm1.indexSet()!=comm.indexSet())
  {
    std::cerr<<"written and read idxset do not match"<<std::endl;
    ++ret;
  }
#else
  typedef Dune::MatrixAdapter<Matrix,Vector,Vector> Operator;
  Operator op1(mat1);
  op1.apply(bv1, cv1);
#endif

  for (auto entry=cv.begin(), entry1=cv1.begin(); cv.end() != entry; ++entry, ++entry1)
    if (Dune::Simd::anyTrue(abs(*entry - *entry1) > eps))
    {
      std::cerr<<"computed vectors do not match: " << *entry << " != " << *entry1 <<std::endl;
      ++ret;
    }

  return ret;
}

int main(int argc, char** argv)
{
#if HAVE_MPI
  MPI_Init(&argc, &argv);
  int size;
  MPI_Comm_size(MPI_COMM_WORLD, &size);
#endif
  const int BS=1;
  int N=2;

  if(argc>1)
    N = atoi(argv[1]);
  std::cout << "testing for N=" << N << " BS=" << BS << std::endl;

  // Test scalar matrices and vectors
  int ret = testMatrixMarket<Dune::BCRSMatrix<double>, Dune::BlockVector<double> >(N);

#if HAVE_MPI
  if(ret!=0)
    MPI_Abort(MPI_COMM_WORLD, ret);
#endif

  // Test block matrices and vectors with trivial blocks
  typedef Dune::FieldMatrix<double,BS,BS> MatrixBlock;
  typedef Dune::BCRSMatrix<MatrixBlock> BCRSMat;
  typedef Dune::FieldVector<double,BS> VectorBlock;
  typedef Dune::BlockVector<VectorBlock> BVector;

  ret |= testMatrixMarket<BCRSMat, BVector>(N);

  // test for vector with multiple lanes
  typedef Dune::BlockVector<Dune::LoopSIMD<double, 4>> BVectorSIMD;

  ret |= testMatrixMarket<Dune::BCRSMatrix<double>, BVectorSIMD>(N);

  // Test other field types
#if HAVE_QUADMATH
  std::cout << "Test Float128" << std::endl;
  ret |= testMatrixMarket<Dune::BCRSMatrix<Dune::Float128>, Dune::BlockVector<Dune::Float128>>(N);
#endif

#if HAVE_GMP
  std::cout << "Test GMPField" << std::endl;
  ret |= testMatrixMarket<Dune::BCRSMatrix<Dune::GMPField<128>>, Dune::BlockVector<Dune::GMPField<128>>>(N);
#endif

#if HAVE_MPI
  if(ret!=0)
    MPI_Abort(MPI_COMM_WORLD, ret);
#endif


#if HAVE_MPI
  MPI_Finalize();
#endif

  return ret;
}
