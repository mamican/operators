The df.operators library
========================

Welcome to the **df.operators** library, the perfect tool to build
highly efficient, move-aware arithmetic data types with C++11.

Preface
-------

The **df.operators** library is the next logical step in the evolution of the
[Boost.Operators](http://www.boost.org/doc/libs/1_53_0/libs/utility/operators.htm) library,
whose maintainer I became in 2001. Since then, C++ has changed significiantly and
with C++11, the time has come for a complete rewrite and to get rid of some
*very* old legacy code and work-arounds.

The aim of this library is, of course, the replacement of Boost.Operators and,
eventually, the final inclusion in a future version of the C++ standard.
That will be a long way, though.

Rationale
---------

Overloaded operators for class types typically occur in groups.
If you can write `x + y`, you probably also want to be able to write `x += y`.
If you can write `x < y`, you also want `x > y`, `x >= y`, and `x <= y`.
Moreover, unless your class has really surprising behavior, some of these related operators
can be defined in terms of others (e.g. `x >= y` <=> `!(x < y)`).
Replicating this boilerplate for multiple classes is both tedious and error-prone.
The **df.operators** templates help by generating operators for you at namespace scope
based on other operators you've defined in your class.
The operators are overloaded to take full advantage of move-aware types and
are carefully written to allow the compiler to apply the
Named-Return-Value-Optimization (NRVO) when possible to avoid unneccessary temporary objects.

If, for example, you define a class like this:

```c++
#include <df/operators.hpp>

class MyInt
  : df::commutative_addable< MyInt >,
    df::multipliable< MyInt, double >
{
public:
  // create a new instance of MyInt
  MyInt( const int v );

  // copy and move constructor
  MyInt( const MyInt& v );
  MyInt( MyInt&& v );

  // copy and move assignment
  MyInt& operator=( const MyInt& v );
  MyInt& operator=( MyInt&& v );

  // addition of another MyInt
  MyInt& operator+=( const MyInt& v );
  MyInt& operator+=( MyInt&& v );

  // multiplication by a scalar
  MyInt& operator*=( const double v );
};
```

then the **df.operators** templates *generate* the following operators:

```c++
// generated by df::commutative_addable< MyInt >
MyInt   operator+( const MyInt& lhs, const MyInt& rhs );
MyInt&& operator+( const MyInt& lhs, MyInt&&      rhs );
MyInt&& operator+( MyInt&&      lhs, const MyInt& rhs );
MyInt&& operator+( MyInt&&      lhs, MyInt&&      rhs );

// generated by df::multipliable< MyInt, double >
MyInt   operator*( const MyInt& lhs, const double& rhs );
MyInt   operator*( const MyInt& lhs, double&&      rhs );
MyInt&& operator*( MyInt&&      lhs, const double& rhs );
MyInt&& operator*( MyInt&&      lhs, double&&      rhs );
```

Requirements
------------

The library uses only a single C++11 feature, move semantics (aka rvalue references),
to make it as portable as possible.
Support for this particular feature of C++11 is available in most modern compilers,
the following compilers and versions should support it:

* GCC 4.3 or newer
* Clang (any version)
* Intel C++ 11.0 or newer
* Microsoft Visual C++ 10.0 or newer

Remember to enable C++11, e.g., provide `--std=c++11` or similar options.

Installation
------------

The **df.operators** library is a header-only library. There is nothing to build or install,
just copy it somewhere and add the appropriate compiler option to add its `include` directory
to the compiler's include path, e.g., `-I /path/to/df.operators/include`.

Templates
---------

The following templates are available:

***WORK IN PROGRESS, LAYOUT CHECK***

<table>

  <tr>
    <th>Template</th><th>Provides</th><th>Requires</th>
  </tr>

  <!-- addable -->
  <tr valign="top">
    <td>
      <code>commutative_addable&lt; T &gt;</code>
    </td><td>
      <code>T operator+( const T&amp; t, const T&amp; t1 )</code><br>
      <code>T&amp;&amp; operator+( const T&amp; t, T&amp;&amp; t1 )</code><br>
      <code>T&amp;&amp; operator+( T&amp;&amp; t, const T&amp; t1 )</code><br>
      <code>T&amp;&amp; operator+( T&amp;&amp; t, T&amp;&amp; t1 )</code>
    </td><td>
      <code>T tmp( t )</code><br>
      <code>tmp += t</code><br>
      <code>tmp += std::move( t )</code>
    </td>
  </tr><tr valign="top">
    <td>
      <code>commutative_addable&lt; T, U &gt;</code>
    </td><td>
      <code>T operator+( const T&amp; t, const U&amp; u )</code><br>
      <code>T operator+( const T&amp; t, U&amp;&amp; u )</code><br>
      <code>T&amp;&amp; operator+( T&amp;&amp; t, const U&amp; u )</code><br>
      <code>T&amp;&amp; operator+( T&amp;&amp; t, U&amp;&amp; u )</code><br>
      <code>T operator+( const U&amp; u, const T&amp; t )</code><br>
      <code>T&amp;&amp; operator+( const U&amp; u, T&amp;&amp; t )</code><br>
      <code>T operator+( U&amp;&amp; u, const T&amp; t )</code><br>
      <code>T&amp;&amp; operator+( U&amp;&amp; u, T&amp;&amp; t )</code>
    </td><td>
      <code>T tmp( t )</code><br>
      <code>tmp += u</code><br>
      <code>tmp += std::move( u )</code>
    </td>
  </tr><tr valign="top">
    <td>
      <code>addable&lt; T &gt;</code>
    </td><td>
      <code>T operator+( const T&amp; t, const T&amp; t1 )</code><br>
      <code>T operator+( const T&amp; t, T&amp;&amp; t1 )</code><br>
      <code>T&amp;&amp; operator+( T&amp;&amp; t, const T&amp; t1 )</code><br>
      <code>T&amp;&amp; operator+( T&amp;&amp; t, T&amp;&amp; t1 )</code>
    </td><td>
      <code>T tmp( t )</code><br>
      <code>tmp += t</code><br>
      <code>tmp += std::move( t )</code>
    </td>
  </tr><tr valign="top">
    <td>
      <code>addable&lt; T, U &gt;</code>
    </td><td>
      <code>T operator+( const T&amp; t, const U&amp; u )</code><br>
      <code>T operator+( const T&amp; t, U&amp;&amp; u )</code><br>
      <code>T&amp;&amp; operator+( T&amp;&amp; t, const U&amp; u )</code><br>
      <code>T&amp;&amp; operator+( T&amp;&amp; t, U&amp;&amp; u )</code>
    </td><td>
      <code>T tmp( t )</code><br>
      <code>tmp += u</code><br>
      <code>tmp += std::move( u )</code>
    </td>
  </tr><tr valign="top">
    <td>
      <code>addable_left&lt; T, U &gt;</code>
    </td><td>
      <code>T operator+( const U&amp; u, const T&amp; t )</code><br>
      <code>T operator+( const U&amp; u, T&amp;&amp; t )</code><br>
      <code>T operator+( U&amp;&amp; u, const T&amp; t )</code><br>
      <code>T operator+( U&amp;&amp; u, T&amp;&amp; t )</code>
    </td><td>
      <code>T tmp( u )</code><br>
      <code>T tmp( std::move( u ) )</code><br>
      <code>tmp += t</code><br>
      <code>tmp += std::move( t )</code>
    </td>
  </tr>

  <tr>
    <th>Template</th><th>Provides</th><th>Requires</th>
  </tr>

  <!-- andable -->
  <tr valign="top">
    <td>
      <code>commutative_andable&lt; T &gt;</code>
    </td><td>
      <code>T operator&amp;( const T&amp; t, const T&amp; t1 )</code><br>
      <code>T&amp;&amp; operator&amp;( const T&amp; t, T&amp;&amp; t1 )</code><br>
      <code>T&amp;&amp; operator&amp;( T&amp;&amp; t, const T&amp; t1 )</code><br>
      <code>T&amp;&amp; operator&amp;( T&amp;&amp; t, T&amp;&amp; t1 )</code>
    </td><td>
      <code>T tmp( t )</code><br>
      <code>tmp &amp;= t</code><br>
      <code>tmp &amp;= std::move( t )</code>
    </td>
  </tr><tr valign="top">
    <td>
      <code>commutative_andable&lt; T, U &gt;</code>
    </td><td>
      <code>T operator&amp;( const T&amp; t, const U&amp; u )</code><br>
      <code>T operator&amp;( const T&amp; t, U&amp;&amp; u )</code><br>
      <code>T&amp;&amp; operator&amp;( T&amp;&amp; t, const U&amp; u )</code><br>
      <code>T&amp;&amp; operator&amp;( T&amp;&amp; t, U&amp;&amp; u )</code><br>
      <code>T operator&amp;( const U&amp; u, const T&amp; t )</code><br>
      <code>T&amp;&amp; operator&amp;( const U&amp; u, T&amp;&amp; t )</code><br>
      <code>T operator&amp;( U&amp;&amp; u, const T&amp; t )</code><br>
      <code>T&amp;&amp; operator&amp;( U&amp;&amp; u, T&amp;&amp; t )</code>
    </td><td>
      <code>T tmp( t )</code><br>
      <code>tmp &amp;= u</code><br>
      <code>tmp &amp;= std::move( u )</code>
    </td>
  </tr><tr valign="top">
    <td>
      <code>andable&lt; T &gt;</code>
    </td><td>
      <code>T operator&amp;( const T&amp; t, const T&amp; t1 )</code><br>
      <code>T operator&amp;( const T&amp; t, T&amp;&amp; t1 )</code><br>
      <code>T&amp;&amp; operator&amp;( T&amp;&amp; t, const T&amp; t1 )</code><br>
      <code>T&amp;&amp; operator&amp;( T&amp;&amp; t, T&amp;&amp; t1 )</code>
    </td><td>
      <code>T tmp( t )</code><br>
      <code>tmp &amp;= t</code><br>
      <code>tmp &amp;= std::move( t )</code>
    </td>
  </tr><tr valign="top">
    <td>
      <code>andable&lt; T, U &gt;</code>
    </td><td>
      <code>T operator&amp;( const T&amp; t, const U&amp; u )</code><br>
      <code>T operator&amp;( const T&amp; t, U&amp;&amp; u )</code><br>
      <code>T&amp;&amp; operator&amp;( T&amp;&amp; t, const U&amp; u )</code><br>
      <code>T&amp;&amp; operator&amp;( T&amp;&amp; t, U&amp;&amp; u )</code>
    </td><td>
      <code>T tmp( t )</code><br>
      <code>tmp &amp;= u</code><br>
      <code>tmp &amp;= std::move( u )</code>
    </td>
  </tr><tr valign="top">
    <td>
      <code>andable_left&lt; T, U &gt;</code>
    </td><td>
      <code>T operator&amp;( const U&amp; u, const T&amp; t )</code><br>
      <code>T operator&amp;( const U&amp; u, T&amp;&amp; t )</code><br>
      <code>T operator&amp;( U&amp;&amp; u, const T&amp; t )</code><br>
      <code>T operator&amp;( U&amp;&amp; u, T&amp;&amp; t )</code>
    </td><td>
      <code>T tmp( u )</code><br>
      <code>T tmp( std::move( u ) )</code><br>
      <code>tmp &amp;= t</code><br>
      <code>tmp &amp;= std::move( t )</code>
    </td>
  </tr>

  <!-- orable -->
  <tr valign="top">
    <td>
      <code>commutative_orable&lt; T &gt;</code>
    </td><td>
      <code>T operator|( const T&amp; t, const T&amp; t1 )</code><br>
      <code>T&amp;&amp; operator|( const T&amp; t, T&amp;&amp; t1 )</code><br>
      <code>T&amp;&amp; operator|( T&amp;&amp; t, const T&amp; t1 )</code><br>
      <code>T&amp;&amp; operator|( T&amp;&amp; t, T&amp;&amp; t1 )</code>
    </td><td>
      <code>T tmp( t )</code><br>
      <code>tmp |= t</code><br>
      <code>tmp |= std::move( t )</code>
    </td>
  </tr><tr valign="top">
    <td>
      <code>commutative_orable&lt; T, U &gt;</code>
    </td><td>
      <code>T operator|( const T&amp; t, const U&amp; u )</code><br>
      <code>T operator|( const T&amp; t, U&amp;&amp; u )</code><br>
      <code>T&amp;&amp; operator|( T&amp;&amp; t, const U&amp; u )</code><br>
      <code>T&amp;&amp; operator|( T&amp;&amp; t, U&amp;&amp; u )</code><br>
      <code>T operator|( const U&amp; u, const T&amp; t )</code><br>
      <code>T&amp;&amp; operator|( const U&amp; u, T&amp;&amp; t )</code><br>
      <code>T operator|( U&amp;&amp; u, const T&amp; t )</code><br>
      <code>T&amp;&amp; operator|( U&amp;&amp; u, T&amp;&amp; t )</code>
    </td><td>
      <code>T tmp( t )</code><br>
      <code>tmp |= u</code><br>
      <code>tmp |= std::move( u )</code>
    </td>
  </tr><tr valign="top">
    <td>
      <code>orable&lt; T &gt;</code>
    </td><td>
      <code>T operator|( const T&amp; t, const T&amp; t1 )</code><br>
      <code>T operator|( const T&amp; t, T&amp;&amp; t1 )</code><br>
      <code>T&amp;&amp; operator|( T&amp;&amp; t, const T&amp; t1 )</code><br>
      <code>T&amp;&amp; operator|( T&amp;&amp; t, T&amp;&amp; t1 )</code>
    </td><td>
      <code>T tmp( t )</code><br>
      <code>tmp |= t</code><br>
      <code>tmp |= std::move( t )</code>
    </td>
  </tr><tr valign="top">
    <td>
      <code>orable&lt; T, U &gt;</code>
    </td><td>
      <code>T operator|( const T&amp; t, const U&amp; u )</code><br>
      <code>T operator|( const T&amp; t, U&amp;&amp; u )</code><br>
      <code>T&amp;&amp; operator|( T&amp;&amp; t, const U&amp; u )</code><br>
      <code>T&amp;&amp; operator|( T&amp;&amp; t, U&amp;&amp; u )</code>
    </td><td>
      <code>T tmp( t )</code><br>
      <code>tmp |= u</code><br>
      <code>tmp |= std::move( u )</code>
    </td>
  </tr><tr valign="top">
    <td>
      <code>orable_left&lt; T, U &gt;</code>
    </td><td>
      <code>T operator|( const U&amp; u, const T&amp; t )</code><br>
      <code>T operator|( const U&amp; u, T&amp;&amp; t )</code><br>
      <code>T operator|( U&amp;&amp; u, const T&amp; t )</code><br>
      <code>T operator|( U&amp;&amp; u, T&amp;&amp; t )</code>
    </td><td>
      <code>T tmp( u )</code><br>
      <code>T tmp( std::move( u ) )</code><br>
      <code>tmp |= t</code><br>
      <code>tmp |= std::move( t )</code>
    </td>
  </tr>

  <!-- xorable -->
  <tr valign="top">
    <td>
      <code>commutative_xorable&lt; T &gt;</code>
    </td><td>
      <code>T operator^( const T&amp; t, const T&amp; t1 )</code><br>
      <code>T&amp;&amp; operator^( const T&amp; t, T&amp;&amp; t1 )</code><br>
      <code>T&amp;&amp; operator^( T&amp;&amp; t, const T&amp; t1 )</code><br>
      <code>T&amp;&amp; operator^( T&amp;&amp; t, T&amp;&amp; t1 )</code>
    </td><td>
      <code>T tmp( t )</code><br>
      <code>tmp ^= t</code><br>
      <code>tmp ^= std::move( t )</code>
    </td>
  </tr><tr valign="top">
    <td>
      <code>commutative_xorable&lt; T, U &gt;</code>
    </td><td>
      <code>T operator^( const T&amp; t, const U&amp; u )</code><br>
      <code>T operator^( const T&amp; t, U&amp;&amp; u )</code><br>
      <code>T&amp;&amp; operator^( T&amp;&amp; t, const U&amp; u )</code><br>
      <code>T&amp;&amp; operator^( T&amp;&amp; t, U&amp;&amp; u )</code><br>
      <code>T operator^( const U&amp; u, const T&amp; t )</code><br>
      <code>T&amp;&amp; operator^( const U&amp; u, T&amp;&amp; t )</code><br>
      <code>T operator^( U&amp;&amp; u, const T&amp; t )</code><br>
      <code>T&amp;&amp; operator^( U&amp;&amp; u, T&amp;&amp; t )</code>
    </td><td>
      <code>T tmp( t )</code><br>
      <code>tmp ^= u</code><br>
      <code>tmp ^= std::move( u )</code>
    </td>
  </tr><tr valign="top">
    <td>
      <code>xorable&lt; T &gt;</code>
    </td><td>
      <code>T operator^( const T&amp; t, const T&amp; t1 )</code><br>
      <code>T operator^( const T&amp; t, T&amp;&amp; t1 )</code><br>
      <code>T&amp;&amp; operator^( T&amp;&amp; t, const T&amp; t1 )</code><br>
      <code>T&amp;&amp; operator^( T&amp;&amp; t, T&amp;&amp; t1 )</code>
    </td><td>
      <code>T tmp( t )</code><br>
      <code>tmp ^= t</code><br>
      <code>tmp ^= std::move( t )</code>
    </td>
  </tr><tr valign="top">
    <td>
      <code>xorable&lt; T, U &gt;</code>
    </td><td>
      <code>T operator^( const T&amp; t, const U&amp; u )</code><br>
      <code>T operator^( const T&amp; t, U&amp;&amp; u )</code><br>
      <code>T&amp;&amp; operator^( T&amp;&amp; t, const U&amp; u )</code><br>
      <code>T&amp;&amp; operator^( T&amp;&amp; t, U&amp;&amp; u )</code>
    </td><td>
      <code>T tmp( t )</code><br>
      <code>tmp ^= u</code><br>
      <code>tmp ^= std::move( u )</code>
    </td>
  </tr><tr valign="top">
    <td>
      <code>xorable_left&lt; T, U &gt;</code>
    </td><td>
      <code>T operator^( const U&amp; u, const T&amp; t )</code><br>
      <code>T operator^( const U&amp; u, T&amp;&amp; t )</code><br>
      <code>T operator^( U&amp;&amp; u, const T&amp; t )</code><br>
      <code>T operator^( U&amp;&amp; u, T&amp;&amp; t )</code>
    </td><td>
      <code>T tmp( u )</code><br>
      <code>T tmp( std::move( u ) )</code><br>
      <code>tmp ^= t</code><br>
      <code>tmp ^= std::move( t )</code>
    </td>
  </tr>

</table>

Contact
-------

In case of any question or feedback, send email to <d.frey@gmx.de>.

License
-------

Copyright Daniel Frey 2013.<br>
Distributed under the Boost Software License, Version 1.0.<br>
(See accompanying file `LICENSE_1_0.txt` or copy at <http://www.boost.org/LICENSE_1_0.txt>)

>Boost Software License - Version 1.0 - August 17th, 2003
>
>Permission is hereby granted, free of charge, to any person or organization obtaining a copy of the software and accompanying documentation covered by this license (the "Software") to use, reproduce, display, distribute, execute, and transmit the Software, and to prepare derivative works of the Software, and to permit third-parties to whom the Software is furnished to do so, all subject to the following:
>
>The copyright notices in the Software and this entire statement, including the above license grant, this restriction and the following disclaimer, must be included in all copies of the Software, in whole or in part, and all derivative works of the Software, unless such copies or derivative works are solely in the form of machine-executable object code generated by a source language processor.
>
>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

The [Open Source Initiative](http://www.opensource.org/) certified the
[Boost Software License 1.0](http://www.opensource.org/licenses/bsl1.0.html) in early 2008.
