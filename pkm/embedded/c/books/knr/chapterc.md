
# Appendix C - Summary of Changes

Since the publication of the first edition of this book, the definition of the C language has undergone changes. Almost all were extensions of the original language, and were carefully designed to remain compatible with existing practice; some repaired ambiguities in the original description; and some represent modifications that change existing practice. Many of the new facilities were announced in the documents accompanying compilers available from AT&T, and have subsequently been adopted by other suppliers of C compilers. More recently, the ANSI committee standardizing the language incorporated most of the changes, and also introduced other significant modifications. Their report was in part participated by some commercial compilers even before issuance of the formal C standard. 

This Appendix summarizes the differences between the language defined by the first edition of this book, and that expected to be defined by the final standard. It treats only the language itself, not its environment and library; although these are an important part of the standard, there is little to compare with, because the first edition did not attempt to prescribe an environment or library. 

Preprocessing is more carefully defined in the Standard than in the first edition, and is extended: it is explicitly token based; there are new operators for concatenation of tokens (##), and creation of strings (#); there are new control lines like #elif and #pragma; redeclaration of macros by the same token sequence is explicitly permitted; parameters inside strings are no longer replaced. Splicing of lines by \ is permitted everywhere, not just in strings and macro definitions. See Par.A.12. 

• The minimum significance of all internal identifiers increased to 31 characters; the smallest mandated significance of identifiers with external linkage remains 6 monocase letters. (Many implementations provide more.) 

• Trigraph sequences introduced by ?? allow representation of characters lacking in some character sets. Escapes for #\^[]{}|~ are defined, see Par.A.12.1. Observe that the introduction of trigraphs may change the meaning of strings containing the sequence ??. 

• New keywords (void, const, volatile, signed, enum) are introduced. The stillborn entry keyword is withdrawn. 

• New escape sequences, for use within character constants and string literals, are defined. The effect of following \ by a character not part of an approved escape sequence is undefined. See Par.A.2.5.2 

• Everyone's favorite trivial change: 8 and 9 are not octal digits. 

The standard introduces a larger set of suffixes to make the type of constants explicit: U or L for integers, F or L for floating. It also refines the rules for the type of unsiffixed constants (Par.A.2.5). 

• Adjacent string literals are concatenated. 

• There is a notation for wide-character string literals and character constants; see Par.A.2.6. 

• Characters as well as other types, may be explicitly declared to carry, or not to carry, a sign by using the keywords signed or unsigned. The locution long float as a synonym for double is withdrawn, but long double may be used to declare an extraprecision floating quantity. 

• For some time, type unsigned char has been available. The standard introduces the signed keyword to make signedness explicit for char and other integral objects. 

The void type has been available in most implementations for some years. The Standard introduces the use of the void * type as a generic pointer type; previously char * played this role. At the same time, explicit rules are enacted against mixing pointers and integers, and pointers of different type, without the use of casts. 

• The Standard places explicit minima on the ranges of the arithmetic types, and mandates headers (<limits.h> and <float.h>) giving the characteristics of each particular implementation. 

• Enumerations are new since the first edition of this book. 

• The Standard adopts from C++ the notion of type qualifier, for example const (Par.A.8.2). 

• Strings are no longer modifiable, and so may be placed in read-only memory. 

• The ``usual arithmetic conversions'' are changed, essentially from ``for integers, unsigned always wins; for floating point, always use double'' to ``promote to the smallest capacious-enough type.'' See Par.A.6.5. 

• The old assignment operators like =+ are truly gone. Also, assignment operators are now single tokens; in the first edition, they were pairs, and could be separated by white space. 

• A compiler's license to treat mathematically associative operators as computationally associative is revoked. 

• A unary + operator is introduced for symmetry with unary -. 

• A pointer to a function may be used as a function designator without an explicit * operator. See Par.A.7.3.2. 

• Structures may be assigned, passed to functions, and returned by functions. 

• Applying the address-of operator to arrays is permitted, and the result is a pointer to the array. 

The sizeof operator, in the first edition, yielded type int; subsequently, many implementations made it unsigned. The Standard makes its type explicitly implementation-dependent, but requires the type, size_t, to be defined in a standard header (<stddef.h>). A similar change occurs in the type (ptrdiff_t) of the difference between pointers. See Par.A.7.4.8 and Par.A.7.7. 

• The address-of operator & may not be applied to an object declared register, even if the implementation chooses not to keep the object in a register. 

• The type of a shift expression is that of the left operand; the right operand can't promote the result. See Par.A.7.8. 

The Standard legalizes the creation of a pointer just beyond the end of an array, and allows arithmetic and relations on it; see Par.A.7.7. 

The Standard introduces (borrowing from C++) the notion of a function prototype declaration that incorporates the types of the parameters, and includes an explicit recognition of variadic functions together with an approved way of dealing with them. See Pars. A.7.3.2, A.8.6.3, B.7. The older style is still accepted, with restrictions. 

• Empty declarations, which have no declarators and don't declare at least a structure, union, or enumeration, are forbidden by the Standard. On the other hand, a declaration with just a structure or union tag redeclares that tag even if it was declared in an outer scope. 

• External data declarations without any specifiers or qualifiers (just a naked declarator) are forbidden. 

Some implementations, when presented with an extern declaration in an inner block, would export the declaration to the rest of the file. The Standard makes it clear that the scope of such a declaration is just the block. 

• The scope of parameters is injected into a function's compound statement, so that variable declarations at the top level of the function cannot hide the parameters. 

• The name spaces of identifiers are somewhat different. The Standard puts all tags in a single name space, and also introduces a separate name space for labels; see Par.A.11.1. Also, member names are associated with the structure or union of which they are a part. (This has been common practice from some time.) 

• Unions may be initialized; the initializer refers to the first member. 

• Automatic structures, unions, and arrays may be initialized, albeit in a restricted way. 

• Character arrays with an explicit size may be initialized by a string literal with exactly that many characters (the \0 is quietly squeezed out). 

• The controlling expression, and the case labels, of a switch may have any integral type. 