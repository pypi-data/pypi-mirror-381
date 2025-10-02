<!--
SPDX-FileCopyrightText: Copyright © DUNE Project contributors, see file LICENSE.md in module root
SPDX-License-Identifier: LicenseRef-GPL-2.0-only-with-DUNE-exception
-->

# Master (will become release 2.11)

* The scaling of the basis functions in the `RT03DLocalFiniteElement`
  was fixed. Now the associated degrees of freedom are the face normal
  moments as in the classical literature.

* The new class template `LocalFiniteElement<LocalBasisTraits>` provides
  a type erased wrapper for finite element implementations with value
  semantics similar to `std::function`.

* Add a meta local-finite-element `DiscontinuousLocalFiniteElement` that associates
  all basis functions with the element interior by changing its local coefficients.

## Deprecations and removals

* `Dune::PQ22DLocalFiniteElement` is deprecated. The recommended replacement for mixed 2d grids
  is to use `Dune::LocalFiniteElementVariant` directly or to use the virtual interface provided
  by `Dune::LocalFiniteElementVirtualInterface`.

* Deprecate `Dune::Precision` as the definition is not clear.

* The deprecated class `LFEMatrix` has been removed.

* The deprecated utility function `Impl::makeFunctionWithCallOperator()` has been removed.

* The deprecated class `PQkLocalFiniteElementCache` has been removed.

# Release 2.10

* Fixed LocalKey codim for the Crouzeix-Raviart element

* Add new local finite element representing P1 basis functions enriched by
  a single element bubble functions on simplex elements.

* Add alias `HierarchicalP1WithElementBubbleLocalFiniteElement` for the
  `SimplexP1BubbleLocalFiniteElement` local finite-element.

* Make the class `LocalKey` usable in `constexpr` and mark all pure functions `[[nodiscard]]`.

* Extend the implementation of `HierarchicalP2WithElementBubble` basis to all dimensions. Note that
  the order of the basis functions is changed.

## Deprecations and removals

* `PQkLocalFiniteElementCache` is deprecated. `LagrangeLocalFiniteElementCache` is the recommended replacement. The latter implements a thread-safe get(gt) while the former does not.

* The deprecated support for passing functions providing
  only the old `f.evaluate(x,y)` interface has been removed.
  This interface is also no longer tested.

* The deprecated overload of the helper function
  `Impl::makeFunctionWithCallOperator(f)` for support
  of the `f.evaluate(x,y)` interface has been removed.
  The overload for the `operator()` is deprecated.
  Calling this function in downstream modules is no
  longer needed because only one function interface is supported.

* The deprecated base class `LocalFiniteElementFunctionBase` has been removed.

* The deprecated headers
  `p1.hh`, `p2.hh`, `p23d.hh`, `pk.hh`, `pk3d`, `qk.hh`,
  `prismp1.hh`, `prismp2.hh`, `pyramidp1.hh`, `pyramidp2.hh`
  and the deprecated classed `(PK1D|PK2D|Q1)LocalFiniteElement`
  in `langrange/` have been removed.
  Use `lagrange(cube|prism|pyramid|simplex).hh` and the corresponding
  classes instead.

* The deprecated functions `numLagrangePoints(topologyId,...)`
  `equidistantLagrangePoints(topologyId,...)` have been removed.

* The class `LFEMatrix` is deprecated and should be replaced by `DynamicMatrix`
  from dune-common with a few interface changes.

# Release 2.9

* The implementation of the Raviart-Thomas element now also includes 0th order shape functions on prisms and pyramids.

* FiniteElementCache is now copy and move assignable.

## Deprecations and removals

- Deprecated many of the Lagrange headers, use
  `lagrange(cube|prism|pyramid|simplex).hh` instead.


# Release 2.8

* Passing functions that support `f.evaluate(x,y)` to `interpolate()`
  is deprecated. Instead the functions should now provide `operator()`.
  Passing functions providing the old interface is still supported in 2.8.
  * `LocalFiniteElementFunctionBase` is deprecated. You can rely
    on duck-typing when passing functions with the new interface.
  * The virtual interface for interpolating functions in `LocalFiniteElementVirtualInterface`
    now uses `std::function` instead of the deprecated `VirtualFunction`
    for the passed function.
  * The virtual interface wrapper `LocalFiniteElementVirtualImp` now
    requires that the wrapped `LocalFiniteElement` implementation
    supports the new `operator()` based interpolation interface.

* Add an implementation of the Nédélec element of the first kind,
  as introduced in "Nédélec, Mixed finite elements in R^3, 1980,
  DOI: http://dx.doi.org/10.1007/BF01396415".
  Only the first-order case for triangles, tetrahedra, squares and cubes is implemented.

* Fix a bug in a shape function of the second-order Lagrange element
  on the three-dimensional pyramid.

* Add an implementation of the Raviart-Thomas element for tetrehedra with order 0.

* Remove deprecated `GenericLocalFiniteElement::topologyId()`, use
  `type().id()` instead.

* Imported the Python bindings from the 2.7 branch of dune-python.

* Replaced the combination of function arguments `topologyId` and `dim` with a single `GeometryType` argument.
  Tagged the old versions of: `numLagrangePoints`, `equidistantLagrangePoints`, `RTL2InterpolationBuilder::topologyId()`,
  `VirtualMonomialBasis(topologyId)`, `VirtualMonomialBasis::topologyId()` as deprecated.

* Add a construction algorithm for high order Nédélec elements on triangles and tetrahedra.

# Release 2.7

* The header `lagrange.hh` now includes all headers of all Lagrange implementations,
  not just the ones with run-time order.

* Introduce a run-time polymorphic container `LocalFiniteElementVariant`.
  Much like `std::variant`, it implements a type-safe
  union of different `LocalFiniteElement` implementations.  Elements of type
  `LocalFiniteElementVariant` can hold one object from a list of types
  given as template parameters.  These types must be implementations of
  the `LocalFiniteElement` interface, and the container will in turn
  implement this interface.

  Such a `variant`-based polymorphism is not as flexible as full type erasure,
  but it is much easier to implement.  What is more, it is believed that in
  many situations the restriction to a fixed set of implementation types
  is not a problem.

* Add support for `operator()` syntax to `interpolate()`. All `interpolate()`
  implementations now support functions `f` that either support `f.evaluate(x,y)`
  or `y = f(x)`.

* Add an implementation of the Crouzeix-Raviart element.

* Add an implementation of the Brezzi-Douglas-Fortin-Marini element.
  The coefficients and interpolation are implemented for arbitrary
  dimension (>1) and order (>0). The actual basis is only implemented
  for dim=2 and order=1,2,3.

  See core/dune-localfunctions!105 and core/dune-localfunctions!145

* Introduce a convenience header `hierarchical.hh` that includes
  all hierarchical FE implementations.

* Introduce a new class `LagrangeSimplexLocalFiniteElement`, which implements
  Lagrange finite elements on simplices with compile-time dimension and order.
  It currently does not cover more general dimension/order situations than
  what is already available in dune-localfunctions, but it gathers the
  plethora of different Pk3DNodal, PkNodal, P1Nodal, etc implementations
  under one single name.

* Introduce new class `BrezziDouglasMariniSimplexLocalFiniteElement`
  (and the same for cubes) that subsumes all currently existing simplex
  BDM element implementations under a single name.  Domain dimension and
  polynomial order are template parameters now.

* Introduce a convenience header `dune/localfunctions/brezzidouglasmarini.hh`
  that includes all BDM implementations.

# Release 2.6

*  The `diffOrder` value has disappeared from the `LocalBasisTraits` class.
   This value encoded the highest partial derivative order implemented by
   a local basis. Encoding this value as a compile-time parameter led to
   various problems related to the dynamic interface, mainly because it
   became part of the type of the local finite element.  At the same time,
   it was suspected that very few people ever actually used the parameter.

    More practically, two things have disappeared: the `diffOrder` member
    of the `LocalBasisTraits` class, and the 8th template parameter `dorder`
    of that class.  There is no replacement, and if you have used `diffOrder`
    then you currently have to find a way to live without it.  As mentioned
    we believe that this concerns only a very small number of people.

    If you do use `diffOrder` and you absolutely need it or something similar,
    then we'd like to hear from you.  One of the reasons why there is no
    replacement is that we couldn't really think of a good use case to begin with.

*  The `QkLocalFiniteElement` class implements second partial derivatives
   of shape functions now.

* The `clone()` method was removed from the raw (non-virtual) `LocalFiniteElement`
  implementations. If you want to copy a `LocalFiniteElement` in a portable
  way which works for raw implementations as well as for the virtual interface
  class, you have to replace `lfe.clone()` by
  `Dune::LocalFiniteElementCloneFactory<LFEType>::clone(lfe)`.
