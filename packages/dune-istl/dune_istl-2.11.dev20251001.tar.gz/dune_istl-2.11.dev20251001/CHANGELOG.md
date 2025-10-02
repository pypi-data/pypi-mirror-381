<!--
SPDX-FileCopyrightText: Copyright © DUNE Project contributors, see file LICENSE.md in module root
SPDX-License-Identifier: LicenseRef-GPL-2.0-only-with-DUNE-exception
-->

# Master (will become release 2.11)

- Summing a `ScaledIdentityMatrix` with a `FieldMatrix` is now supported,
  in either order.  The same holds for sums of `ScaledIdentityMatrix` and
  `DiagonalMatrix`.

- Row-wise creation of `BCRSMatrix` became faster.

- `FastAMG` can now be used with non-nested matrices of type `BCRSMatrix<T>`
  where `T` is a plain number type instead of `FieldMatrix<T,m,n>`.

# Release 2.10

- Improve testing support on Laplacian matrices with an optional diagonal regularization parameter.

- Base the implementation of `VariableBlockVector` on `std::vector` as the storage type. Note that
  this prevents from using `bool` as block type that was possible before.

- A method `BCRSMatrix::setIndicesNoSort()` was added. Similar
  to `BCRSMatrix::setIndices()` this allows to insert all indices
  of a row at once, but - incontrast to the latter - does not sort them.
  This allows to speed up insertion if indices are already sorted.

- `UMFPACK` is extended to arbitrary blocked matrix structures. This includes `MultiTypeBlockMatrix`. The external interface is unchanged.
  However, internally the `BCCSMatrixInitializer` is replaced by direct calls of `flatMatrixForEach` similar to `Cholmod`. This requires a
  compatible vector field of "ignored" degrees of freedom. The method `setSubMatrix` with a top-level index set is preserved for compatibility.

- The internal storage in `MatrixIndexSet` was changed from `std::set` to a sorted `std::vector`
  (with a `std::set` fallback for very dense rows) to improve performance. The stored index
  type was changed from `std::size_t` to `uint32_t` to reduce memory consumption and improve
  performance. Hence, `MatrixIndexSet` can no longer be used for very large matrices with more
  than 2^32 columns.

- Added flag 'useFixedOrder' to the coarsen method of AMGs ParallelIndicesCoarsener.
  If set to true, during the creation of the coarser matrix (by accumulation and restriction
  to fewer processes) the coarse matrix rows are ordered in a fixed manner, making parallel runs
  reproducible; the runtime is possibly not ideal though.
  If set to false (which is the default), the row order depends on the order of messages received from the
  processes responsible for the respective parts of the finer grid. Then the indices on the coarser grid
  may differ from run to run.

- Define `field_type` and `real_type` in `MultiTypeBlock[Matrix|Vector]` only if a common type of these
  types exist over all blocks in the container. Otherwise it is defined as `Std::nonesuch`.

## Deprecations and removals

- The deprecated CMake variables `SUPERLU_INCLUDE_DIRS`, `SUPERLU_LIBRARIES`,
  `SUPERLU_DUNE_COMPILE_FLAGS`, and `SUPERLU_DUNE_LIBRARIES` are removed, they are
  replaced by the target `SuperLU::SuperLU`.

- Multiple containers no longer provide the deprecated member function `blocklevel`. Use the free function
  `blockLevel()`.

- Removed deprecated function `initSolverFactories()`, use `initSolverFactories<O>` instead.

- Removed deprecated `MultyTypeBlockMatrix::size()`, use `N()` instead.

- Removed deprecated `MultyTypeBlockVector::count()`, use `N()` instead.

- Deprecated `writeSVGMatrix` with `std::stream` as the second argument. Use the method
  with `std::stream` as the first argument.


# Release 2.9

- Add `const` qualifier to `LinearOperator` and `ScalarProduct` in
  `IterativeSolver`. In particular, the constructors of iterative solvers have
  changed.

- Solvers are more robust if used with multiple right-hand sides and one lane starts with the exact solution.

- Added a function to write nested matrices as SVG objects: `writeSVGMatrix(...)`

- `MultiTypeBlockVector` uses now `std::common_type` of the entries for the `field_type`. The old `double`
  default is replaced by `Std::nonesuch` of an empty `MultiTypeBlockVector`.

- All vector implementations require a `FieldTraits` class specialization to export `field_type` and `real_type`
  in order to work with blocked ISTL vector types.

- MINRES: The algorithm computes the preconditioned defect during the iterations. However, the initial
  defect was computed as the defect of the original/non-preconditioned system. This is now changed so
  that the initial defect is also computed as the preconditioned defect (this is also in line with GMRes).
  In some numerical tests with a Stokes system this lead to earlier termination when using the same
  termination criterion.

- The `Cholmod` class now provides access to the `cholmod_factor` class that is
  used by `CHOLMOD` itself to store the Cholesky factor.  This can be used to
  use the more advanced features of `CHOLMOD`.

- The `Cholmod` class now has an additional template parameter `Index`, which specifies the
  type used by `CHOLMOD` for integers.  The types `int` (the default) and `SuiteSparse_long`
  (which is usually `long int`) are supported.  Use `SuiteSparse_long` if your problems
  are too big for `int`.

- You can now multiply objects of type `ScaledIdentityMatrix` by scalars
  using `operator*`.

- You can now use `std::tuple_element` to get the types of `MultiTypeBlockVector` entries
  and `MultiTypeBlockMatrix` rows.

- The SPQR solver can now work with non-square matrices (a bug which caused a segfault when previously
  attempting to do it was found and resolved).

## Deprecations and removals

- The deprecated ILU functions `bilu_backsolve`, `bilu0_decomposition`, `bilu_backsolve`,
  `firstmatrixelement`, and `bilu_decomposition` are removed. Use their camel case
  replacements.

- Remove deprecated `ImplicitModeOverflowExhausted`, use
  `ImplicitModeCompressionBufferExhausted` instead.


# Release 2.8

- Extended the MatrixMarket IO functions for reading and writing vectors with
  SIMD field_type as tall-skinny matrices.

- Added public access of the `cholmod_common` object in class `Cholmod`.

- Python bindings have been moved from the `dune-python` module which is now
  obsolete.
  Note that for `dune-istl` bindings are still very much work in progress.
  To activate Python bindings the CMake flag
  `DUNE_ENABLE_PYTHONBINDINGS` needs to be turned on (default is off).
  Furthermore, flags for either shared library or position independent code
  needs to be used.

- Added new utility functions templates `maxBlockLevel`, `minBlockLevel`, `blockLevel` in `dnue/istl/blocklevel.hh` to
  automatically determine the block level of possibly nested ISTL vectors & matrices at compile time.
  The block level cannot be always uniquely determined for `MultiTypeBlockMatrix`/`MultiTypeBlockVector` since the nesting level
  of different block types might differ. Hence, `maxBlockLevel`, `minBlockLevel` always works
  but if they yield different results `blockLevel` will not compile.
  This condition can be checked with the function template `hasUniqueBlockLevel`.

- The internal setup code of the various SuiteSparse solvers (like `UMFPack`)
  has been cleaned up.  The effects should be invisible to all regular users.
  However, if you have happened to use the `ColCompMatrix` and `ColCompMatrixInitializer`
  classes in the past you need to port your code to use `Impl::BCCSMatrix` and
  `Impl::BCCSMatrixInitializer` instead.  Their interfaces have changed a little bit;
  please look at the class documentation for details.  The old header `colcompmatrix.hh`
  is still there, but backward compatibility is only partial.

- More implementation code of the ILU preconditioners (in `ilu.hh`) has moved
  into the `ILU` namespace.  With the move, some methods have changed their names
  from std-style to CamelCase.  The old methods are still there, but they are
  deprecated now. The class `MatrixBlockError` has moved from the file `ilu.hh`
  to the file `istlexception.hh`, because it is of wider interest.

- Added the routines `flatVectorForEach` and `flatMatrixForEach` that traverse a (blocked) vector or matrix container.
  At each entry a functor is called taking the entry and the (flat) index offset.

- `Cholmod` solver can now be used with each blocked matrix/vector type compatible with `flatVectorForEach` and `flatMatrixForEach`.

## Deprecations and removals
- Drop deprecated bindings of direct solver Pardiso.

- Remove deprecated preconditioner implementations `SeqILU0` and `SeqILUn`. Use
  `SeqILU` instead, which implements incomplete LU decomposition of any order.

- Remove deprecated methods 'BlockVector::resize' and 'BlockVector::reserve'
  with two arguments.

- Drop support SuperLU 4.

- Rename the exception `ImplicitModeOverflowExhausted` to `ImplicitModeCompressionBufferExhausted`,
  to better reflect its meaning.  The old exception is still there, but it triggers
  a deprecation warning.

- Remove deprecated `SequentialInformation::getSolverCategory()`, use
  `category()` instead.

## Known issues

- SuiteSparse's threading tends to conflict with the threading from OpenBLAS. The
  author of SuiteSparse reports cases of an
  [100 fold slowdown](https://github.com/DrTimothyAldenDavis/SuiteSparse/issues/1)
  for cholmod. See also
  [dune-istl #91](https://gitlab.dune-project.org/core/dune-istl/-/issues/91).

# Release 2.7

- New `SolverFactory` for generating sequential direct or iterative solvers and
  preconditioners from a `ParameterTree` configuration.

- `BDMatrix` objects now have the method `solve`, which implements that
  canonical way to solve block-diagonal linear systems.

- The class `VariableBlockVector::CreateIterator` is a true STL output iterator now.
  This means that you can use STL algorithms like `std::fill` or `std::copy`
  to set the block sizes.

- `MultiTypeBlockVector<Args...>` now inherits the constructors from its
  parent type (`std::tuple<Args...>`). This means you can now also construct
  `MultiTypeBlockVector`s from values or references of BlockVectors.

- All matrix and vector classes can now be instantiated with number types
  directly (A number type is any type for which `Dune::IsNumber<T>::value`
  is true).  For example, you can now use `BlockVector<double>` instead of
  the more cumbersome `BlockVector<FieldVector<double,1> >`.  Similarly, you can use
  `BCRSMatrix<double>` instead of `BCRSMatrix<FieldMatrix<double,1,1>>`.
  The old forms still work, and `FieldVector` and `FieldMatrix` types with
  a single entry can still be cast to their `field_type`.  Therefore, the
  change is completely backward-compatible.

- Added a right-preconditioned flexible restarted GMRes solver

- The UMFPack binding use the long int functions to compute larger systems.
  With the \*_dl_\* versions instead of the \*_di_\* versions UMFPACK will not
  have a memory limit of just 2 GiB.

- Support for SuiteSparse's CHOLMOD providing a sparse Cholesky
  factorization.

- The interface methods `dot()` and `norm()` of ScalarProduct are now `const`. You will
  have to adjust the method signatures in your own scalar product implementations.

- `MultiTypeBlockVector` now implements the interface method `N()`, which
  returns the number of vector entries.

- `MultiTypeBlockVector` now implements the interface method `dim()`, which
  returns the number of scalar vector entries.

- `MultiTypeBlockVector::count()` is now `const`

- `SeqILU` can now be used with SIMD data types.

## Deprecations and removals

- Deprecated support for SuperLU 4.x. It will be removed after Dune 2.7.

- Deprecated the preconditioner implementations `SeqILU0` and `SeqILUn`.
  Use `SeqILU` instead, which implements incomplete LU decomposition
  of any order.

- The method `setSolverCategory` of `OwnerOverlapCopyCommunication` is deprecated and
  will be removed after Dune 2.7. The solver category can only be set in the constructor.

- The method `getSolverCategory` of `OwnerOverlapCopyCommunication` is deprecated and
  will be removed after Dune 2.7. Use `category()` instead.

- The method `MultiTypeBlockVector::count()` has been deprecated, because its name
  is inconsistent with the name mandated by the `dune-istl` vector interface.

- The method `MultiTypeBlockMatrix::size()` has been deprecated, because its name
  is inconsistent with the name mandated by the `dune-istl` vector interface.

# Release 2.6

- `BDMatrix` objects can now be constructed and assigned from `std::initializer_list`.

- `BDMatrix` and `BTDMatrix` now implement the `setSize` method, which allows to
  resize existing matrix objects.

- The solver infrastructure was updated to support SIMD data types (see
  current changes in `dune-common`). This allows to solve multiple systems
  simultaneously using vectorization.
