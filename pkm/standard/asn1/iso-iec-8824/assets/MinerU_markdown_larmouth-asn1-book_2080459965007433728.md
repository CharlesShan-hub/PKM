The figure II-16 and II-17 definitions may appear more verbose (they are!) than the informal tabular notation used in figures II-13 and II-14, however, they are very explicit, but more importantly they are machine-readable, and ASN.1 tools can process them and use these definitions in checking and decoding the content of "holes" in incoming messages. 

## 7 Defining an Information Object Set

Why do we need to combine the definition of individual Information Objects into an Information Object Set? Well, we saw a use of this in defining the "&Errors" field of the OPERATION class above, but there is a more important reason. The whole purpose of defining Information Object Classes and Information Objects is to provide an ASN.1 definition of the complete (informal) table we saw earlier that determines what can fill in the holes in a carrier or generic protocol, and to link that ASN.1 definition to the "holes" in the generic or carrier protocol. 

<table><tr><td>The next step on the way. Someone has defined some Information Object Classes. We define some Information Objects. Now we pull them together into a named Information Object Set.</td></tr></table>

So we need a notation to allow us to define Information Object Sets (collections of Information Objects of a given class), with a name assigned to that set which can be used elsewhere in our specification. 

Information Object Sets are collections of Information Objects, much as types can be seen as collections or sets of values. So it is not surprising that the names for Information Object Sets are required to start with an upper-case letter. If we want a name for the collection of operations we have defined in Figure II-17, we can write: 

$$
\begin{array}{c} \text {My - ops OPERATION : : = \{order |} \\ \text {sales |} \\ \text {query |} \\ \text {status \}} \end{array}
$$

Read this as "My-ops of class OPERATION is the set consisting of the union of the objects order, sales, query, and status". 

This is the most common form, but general set arithmetic is available if needed. Suppose that A1, A2, A3, and A4 have been defined as Information Object Sets of class OPERATION. We can write expressions such as: 

$$
\text { New - Set   OPERATION }:: := \left\{ \begin{array}{l} (\text { A1   INTERSECTION   A2 }) \\ \text { UNION   (A3   EXCEPT   A4) } \end{array} \right\}
$$

but as a colleague of mine frequently says: "No-one ever does!" 

If you leave the brackets out, the most binding is EXCEPT, the next INTERSECTION, and the weakest UNION. So all the round brackets above could be omitted without change of meaning, but it is usually best to include them to avoid confusing a reader. (Some people seem to find it intuitive that "EXCEPT" should be the least binding, so clarifying brackets when "EXCEPT" is used are always a good idea.) 

I won't bore you with a long-winded example of the result for various sets A1 to A4 - invent your own and work it out - or ask your teenage daughter to help you! 

The caret character "^" is a synonym for "INTERSECTION", and the vertical bar character "|" is a synonym for "UNION". There is no single character that is a synonym for EXCEPT - you must write that out in full. 

We have already noted the similarity between Information Objects and values, and Information Object Sets and types or subtypes (collections of values). Where do classes fit into this pattern? This is less clear cut. Information Object Classes are in some ways like types, but unlike types, they start off with no Information Objects in them, merely with a mechanism for the ASN.1 user to define objects of that class. By contrast, built-in types come with a ready-made collection of values and value notation, from which you can produce subsets using constraints. 

Nonetheless, because of the similarity of objects and values, when ASN.1 was extended to introduce the information-object-related concepts, it was decided to allow the same syntax as was introduced for defining sets of objects to be used for defining sets of values (subsets of some type). Because of this, the so-called value set assignment was introduced into the ASN.1 syntax. This allows you to write (should you so wish!): 

$$
\begin{array}{l} \text {First - set   INTEGER}: := \{0.. 5 \} \\ \text {Second - set   INTEGER}: := \{1 0.. 1 5 \text {UNION} 2 0 \} \\ \text {Third - set   INTEGER}: := \\ \quad \{\text {First - set   UNION   Second - set   EXCEPT} 1 3 \} \\ \text {Fourth - set   INTEGER}: := \{0.. 5 | 1 0.. 1 2 | 1 4 | 1 5 | 2 0 \} \end{array}
$$

"Fourth-set" is, of course, exactly the same subset of INTEGER as is "Third-set". 

It is testing time! Or put it another way, time for some fun! With the above definitions, can I write 

## selected-int Fourth-set ::= 14

and as an element of a SEQUENCE 

## Third-set DEFAULT selected-int

Yes you can! This question of *exactly* what is legal ASN.1 in such cases has vexed the Standards group for several years, but is now largely resolved. It is, however, best to rely on a good tool to give you the answer, rather than to pore over the Standard text itself! Or maybe better still to keep your ASN.1 simple and straightforward! 

Before we leave this sub-clause, let us look at "My-ops" again. It is likely that in a future version of the wineco protocol, we will want to add some additional operations, and hence to extend "Myops". This has implications for version 1 systems, which will need to have some defined errorhandling if they are requested to perform an operation that they know nothing about. We will see in a moment the way the error handling is specified, but first we need to indicate that "My-ops" may be extended in the future. We do this by re-writing it as: 

$$
\text { My - ops   OPERATION }: := \left\{ \begin{array}{l} \text { order } \\ \text { sales } \\ \text { query } \\ \text { status }, \dots \end{array} \right\}
$$

with a possible version 2, with an added operation "payment", being written: 

## 8 Using the information to complete the ROSE protocol

Lets get back to our main theme. Designers of "generic" protocols want to have elements of SEQUENCES and SETS that they do not define. They want other groups to define the types to fill these positions. Frequently the other groups will want to carry many different types in these elements at different times. The Information Object concepts enable the definition of the types 

No point in defining classes, objects, and object sets unless they are going somewhere. After-all, you can't encode them and send them down the line. So what good are they? Answer: to fill in holes. 

that will fill these elements. But how are these "holes" identified in an ASN.1 type definition? And how are the Information Object (Set) definitions linked to the "holes"? 

Largely for historical reasons, ASN.1 takes a three-stage approach to this problem. The first step is to allow reference to a field of an Information Object Class to be used wherever an ASN.1 type (or in some cases an ASN.1 value) is required. The second stage is to allow an Information Object Set to be used as a constraint on such types, requiring that that element be a type (or a value) from the corresponding field of that Information Object Set. This is called a table constraint. The third step is to allow (additionally) two or more elements of a SET or SEQUENCE (that are defined as fields of the same Information Object Class) to be linked using a pointer between them (the "@" symbol is used to provide the link). Use of this linking mechanism says that the linked fields have to be filled consistently in accordance with some Information Object of the constraining Information Object Set. In other words, that the linked fields have to correspond to cells from a single row of the defining table. Constraints expressing a linkage between elements are called relational constraints. 


Figure II-18 shows a (simplified) ROSE "Invoke" datatype, illustrating these features. It uses the Information Object Set "My-ops" (of class OPERATION), defined above, in the table and relational constraints on the elements of "Invoke".


```txt
Invoke ::= SEQUENCE
{ invokeId INTEGER,
    opcode OPERATION.&operationCode
    ({My-ops} ! invoke-unrecognisedOperation),
    argument OPERATION.&ArgumentType
    ({My-ops}
    {@opcode} ! invoke-mistypedArgument) OPTIONAL }
Figure II-18: The ROSE Invoke datatype 
```

Figure 18 is quite complex! Take it a step at a time. The "opcode" element of the sequence says that it is a value from the "&operationCode" field of the class "OPERATION". In itself, this is just a synonym for 

because this is a fixed-type value field of this type. Or to put it another way, all values of this field are of this type. 

However, by referencing the type through the field of the Information Object Class, we are then allowed to constrain it with an Information Object Set ("My-ops") of that class. (Such a constraint would not be allowed if we had simply written the element as "CHOICE ... etc".) 

The curly brackets round "My-ops" are a stupidity (sorry - there are a few!) in the ASN.1 syntax. The requirement here is for the syntactic construct "ObjectSet". A reference name for an object set (which is what "My-ops" would be) is not allowed. However, we can generate an "ObjectSet" from "My-ops" by importing "My-ops" into an object set definition, that is to say, by enclosing it in curly brackets. 

Put simply, there is no good reason for it, but you have to put the curly brackets in! 

The effect of the "My-ops" constraint is to say that the only values permitted for this element are those assigned to the "&operationCode" field one of the Information Objects of "My-ops". In other words, the field must contain an op-code for one of the four (in version 1) operations defined for wineco. This is all fully machine-readable, and encoders/decoders can use this specification to help with error checking. 

The "!" introduces an exception specification, and says that if this constraint is not satisfied (a different op-code value appears), the error handling is to return a REJECT with the integer value "invoke-unrecognisedOperation". The designers of the wineco protocol need not concern themselves with specifying such error handling. This is all done within the ROSE specification. Note that this is precisely the error situation that will arise if a version 1 implementation is hit with a request to perform the "payment" operation. 

Now we move onto the "argument" element. This is the true "hole". In its unconstrained form, it simply says that this element can be "any ASN.1 type" (because any ASN.1 type can be used for this field of an Information Object of the OPERATION class). Such notation is described in ASN.1 as "Open Type" notation, and is handled rather specially by encoding rules. 

In particular, it is important that encodings enable a decoder to find the end of an open type encoding before they know in detail what type is encoded within it (the "opcode" element of the SEQUENCE could have been written after the "argument" element - there is no restriction). 

In BER, there is no problem - the end of an encoding can always be determined using the "L" field of the "TLV", for all ASN.1 BER encodings of types. In PER, however, this is not the case. Unless a decoder knows what the type being encoded is, it cannot find the end of the encoding of a value of the type. So in PER, an extra "length" wrapper is always added to an open type. 

As an aside, you will sometimes find people deliberately defining an element as an open type (typically using a class with just one field, a type field), and then constraining that element to be a single fully-defined ASN.1 type. The sole purpose of this is to produce the additional length wrapper, and relates to implementation architecture. Such constructs are used to encapsulate security-related data, where the implementation architecture is likely to be to pass an encapsulated set of octets to a security kernel, with the insecure part of the application having no detailed knowledge of the security-related data. (Government Health Warning - Figure 999 - again - you must judge for yourself whether such provision is sensible or not. It happens. At worst it just means an unnecessary length field!) 

Finally, we address the "@" part of "argument". This turns the constraint into a relational constraint, linking the "argument" and "opcode" fields, and requiring them to be consistent with some row of the constraining table. (Whoops! To be consistent with some object in the constraining Information Object Set - let's use the correct terminology!). 

The "@" construction could equally well, and with the same effect, have been placed on the "opcode" field (as well, or instead of). All that is being formally said is that the two (and there could be more) linked fields have to be consistent with an object in the set. We know, of course, that "OPERATION.&operationCode" was defined as "UNIQUE" in the class definition, so there will be at most one object in the Information Object Set that matches a value in the "opcode" field of the "Invoke" message. In the general case, this is not necessarily true, and the only requirement is that the values and/or types of linked fields are consistent with at least one of the information objects in the constraining object set (consistent with at least one row of the constraining table). 

Finally, note the "invoke-mistypedArgument" error return. In BER, there is a lot of redundancy in an encoding, and it can usually be easily detected if an encoding does not represent a value of the type we think it should (or might) be. In PER, this is not so often the case, as there is much less redundant encoding. In PER, the main detection of "invoke-mistypedArgument" will be if the encoding of the open type (as determined by the added length field) does not have the right length for some value of the type we are trying to match it with (the one identified by the "opcode" value). 

There is always an argument among protocol designers on the extent to which one should specify the actions of an implementation on receipt of erroneous material (presumably from a bust sending implementation, or due to the very very rare occurrence of undetected errors in lower layers), or whether such actions should be left as implementation-dependent. ASN.1 provides notation to go in either direction. ROSE chose to be very prescriptive on error handling, and made full use of ASN.1 exception handling to specify the required behaviour on receipt of "bad" material. If you are a protocol designer, this is a decision for you to take. ASN.1 gives you the tools to be prescriptive, but there is no requirement to use those tools, and many specifiers choose not to. 

Note that there is a certain difference between the "!" on the opcode element and that on the "argument" element. In the first case we know it can get activated if a version 2 system tries to invoke "payment" on a version 1 system. In the second case it should never get activated if systems are conforming and lower layer communications are reliable. 

## 9 The need for parameterization

I wonder how many readers noticed that the above, whilst looking attractively precise and implementable, recognised the major problem with it? 

But unfortunately it just doesn't work! Lot's of people are defining their own "My-op" object sets, but there is just one ROSE specification of "Invoke"! 

If we were to re-write the whole of ROSE in 

our wineco specification, the above would work fine. We might have a series of modules defining our main types, as illustrated in earlier chapters (call these MAIN modules) and another module defining the OPERATION and ERROR classes, and the "Invoke", "Reject", "ReturnResult", and "ReturnError" (call this the ROSE module). Then we have a final module (call this the INFORMATION OBJECTS module) that defines our information objects and the "My-op" set. 

From MAIN we export all our top-level wineco types. From the ROSE module we export our Information Object Class definitions. In the INFORMATION OBJECTS module we import the Information Object Class definitions, and export "My-op". Finally, in the ROSE module, as well as exporting the class definitions, we import "My-op" for use in the "Invoke" etc messages as described above, and define our top-level PDU that now defines our wineco abstract syntax as: 

```txt
wineco-PDU ::= CHOICE
{invoke Invoke,
reject Reject,
result ResultResult,
error ReturnError } 
```

We have a complete and working protocol. 

But this approach does not work if we want the ROSE specifications to be published totally separately from the wineco specification, with lot's of different applications (of which wineco would be just one) wanting to produce a ROSE-based specification. Copying the ROSE text for each application would not be a good idea! (That said, there are specifications about that define their own ROSE-equivalent classes and PDUs, usually in a simplified form, simply because they wish to be complete in their own right and to have control so that the ROSE part cannot change under their feet. This "copying with simplification" occurs with other popular specifications, not just with ROSE.) 

If the ROSE specification is to be independent of the wineco application, then clearly it cannot import the "My-op" type. How then can it supply a constraint to say how the hole is to be filled in? 

## Here we introduce a new and very powerful ASN.1 concept, that of parameterization.

All programmers are fully familiar with the concept of functions or subroutines or methods having a set of dummy parameters which are referred to in the body of the function or subroutine or method specification. When those functions or subroutines are called, the calling code supplies a set of actual parameters that are used instead of the dummy parameters for that call. 

ASN.1 has a very similar concept. When we define a type, such as the ROSE "Invoke" type, we can list after the type name a dummy parameter list. These dummy parameters can then be used on the right-hand side of the type definition as if they were normal reference names. We call such a type a parameterised type, and we can export parameterised types (for example from the generic ROSE specification, with import into one or more application specifications like wineco). In the importing specification (or anywhere else the parameterised type is used) we supply an actual parameter specific to that use. Figure II-19 shows the ROSE module, and Figure II-20 the wineco module. Note that now all exporting is from ROSE - ROSE does no imports at all. 

```txt
ROSE-module
{joint-iso-itu-t remote-operations(4) generic-ROS-PDUs(6)}
DEFINITIONS
AUTOMATIC TAGS
BEGIN
EXPORTS OPERATION, ERROR, Rose-PDU{};

Rose-PDU {OPERATION:User-ops} ::=
    CHOICE
{invoke    Invoke {User-ops},
reject    Reject,
result    ReturnResult {User-ops},
error    ReturnError {User-ops} }

Invoke {OPERATION:User-ops} ::= SEQUENCE
{ invokeId    INTEGER,
opcode    OPERATION.&operationCode
({User-ops} ! invoke-unrecognisedOperation),
argument    OPERATION.&ArgumentType
({User-ops}
{@opcode} ! invoke-mistypedArgument) OPTIONAL }

Reject ::= etc
ReturnResult {OPERATION:User-ops} ::= etc
ReturnError {OPERATION:User-ops} ::= etc
END

Figure II-19: Defining and exporting a parameterised type 
```

There are a few points to notice in figure II-19. We could have exported separately the Invoke, Reject, ReturnResult, and ReturnError messages, but we chose to bundle these together as a "Rose-PDU" CHOICE type and to export that. This meant that "Rose-PDU" had to be parameterised with the "User-ops" dummy parameter, with that dummy parameter supplied as the actual parameter to the use of Invoke and ReturnResult and ReturnError within that CHOICE. Invoke, ReturnResult and ReturnError slightly confusingly use the same name for their dummy parameter, which is then used for the table and relational constraint. This situation of having a dummy parameter being passed down through a chain of nested type definitions is quite common, and it is also quite common for the same name to be used each time, but please note that formally these are distinct names - as you would expect, the scope of a dummy parameter name is limited to the right-hand side of the parameterised type. 

Note also the occurrence of "{}" after Rose-PDU in the EXPORTS list (and later in the IMPORTS list of Figure II-20). This is not a requirement, but helps to clarify for a human reader that this is a parameterised type. 

The dummy parameter list in this case has just one dummy parameter (if there were more it would be a comma-separated list), and here we see the syntax for a dummy parameter that is an Information Object Set. It is the class name ("OPERATION"), a ":" (colon), then the dummy parameter name which must start with a capital letter because it is an Information Object Set. We will in the next chapter that dummy parameters can be many other things as well, and that things other than types can be parameterised, but this will suffice for now. 

Figure II-20 shows the import into Wineco-main, and the definition of the new ROSE-based abstract syntax with the supply of the wineco-specific "My-ops" as the actual parameter to the Rose-PDU parameterized type. 

```txt
Wineco-main
{ joint-iso-itu-t internationalRA(23) set(42)
    set-vendors(9) wineco(43) modules(2) main(5)}
DEFINITIONS
AUTOMATIC TAGS
BEGIN
IMPORTS
Rose-PDU{} FROM Rose-module
{joint-iso-itu-t remote-operations(4) generic-ROS-PDUs(6)}
My-Ops FROM Wineco-operations
{ joint-iso-itu-t internationalRA(23) set(42)
    set-vendors(9) wineco(43) modules(2) ops(4)};
wineco-abstract-syntax ABSTRACT-SYNTAX ::=
{ Rose-PDU{My-ops} IDENTIFIED BY
{ joint-iso-itu-t internationalRA(23) set(42)
    set-vendors(9) wineco(43) abstract-syntax(2)}
HAS PROPERTY
{handles-invalid-encodings}
-- See the Rose specification -- }
END

Figure II-20: Using the ROSE-PDU to define the Wineco abstract syntax 
```

## 10 What has not been said yet?

This chapter has hopefully given the reader a good understanding of the concepts related to Information Objects, and the principle of parameterization of ASN.1 constructs, but it has not told the full story. 

## Why is there always more to say?

In the next chapter, we will complete some more detail on the full possibilities for the sorts of fields you can define when you specify an Information Object Class. 

There is also an important facility called variable syntax which enables a more user-friendly (and sometimes less verbose) notation to be used for defining objects of a given class (replacing the notation of Figure II-17). 

On the question of constraints, we saw in earlier chapters the simple subtype constraints, and in this chapter table and relational constraints have been introduced. The next chapter will explore some further examples of constraints, and will also introduce the remaining type of constraint, the so-called user-defined constraint. 

On parameterization, there is a little more discussion to be had, including mention of so-called parameters of the abstract syntax and the extensible empty set. 

Finally, we will mention the remaining ASN.1 constructs that provide alternative means of leaving holes in specifications. Readers will be pleased to know that at the end of that chapter, they can be certified as "ASN.1 Complete" as far as the notation is concerned, and if that is their only interest in reading this book, they can stop there! 

# Chapter 7 More on classes, constraints, and parameterization

# (Or: More than you ever wanted to know!)

Summary: 

This chapter: 

• describes all the different sorts of Information Object Class Field that are available for use in a class definition; 

describes the "variable syntax" for defining Information Objects (this is arguably the most important area covered in this chapter - read that material if you read nothing else); 

• completes the discussion of constraints and of parameterization; 

• describes the TYPE-IDENTIFIER built-in class; 

• completes the discussion of ASN.1 notational support for "holes". 

## 1 Information Object Class Fields

There are many different sorts of information that generic protocol specifiers have found they wanted to collect from their users to complete their protocol, and ASN.1 allows the specification of a variety of different sorts of Information Object Class Field. Here we briefly look at each in turn. Figure II-21 gives an artificial example of an Information Object Class in which all the different sorts of field appear. 

There are many sorts of fields for Information Object Classes. Some are frequently used, some are rarely encountered. This clause lists them all! 

There are examples of all these different sorts of fields in current protocol specifications, but some are much more common than others. 

```txt
ILLUSTRATION ::= CLASS
    {&Type-field,
    &fixed-type-value-field INTEGER,
    &variable-type-value-field &Type-field,
    &Fixed-type-value-set-field My-enumeration,
    &Variable-type-value-set-field &Type-field,
    &object-field OPERATION,
    &Object-set-field ERROR }
Figure II-21: An illustration of the different sorts of field 
```

References to these fields such as 

ILLUSTRATION.&fixed-type-value-field 

are possible in ASN.1 notation (constrained by an actual object set or unconstrained). Use of this notation is called information from object class. 

It is also in general possible to have references to fields of defined Information Objects and defined Information Object Sets using notation such as 

illustration-object.&Type-field 

Illustration-object-set.&fixed-type-value-field 

Use of this notation is called information from object and information from object set. 

In some cases, such notation is forbidden (see the Standard for a simple table of what is legal and what is not, and following text for a general description). A good guide, however, is if it makes some sort of sense, then it is legal. We discuss below the meaning and usefulness of these notations for each sort of field, and the circumstances in which you might want to use them. 

## 1.1 Type fields

The type field we have already encountered. The field-name has to start with a capital letter, and may be followed immediately by a comma, or we can write, for example: 

Type fields are common and important. They fill in the holes in protocols, and the need for them drove the development of the Information Object Class concept. 

## &Type-field-optional OPTIONAL, &Type-field-defaulted DEFAULT NULL,

In the case of OPTIONAL, then that field may be left undefined when an Information Object of that class is defined. That field is then empty, and "empty" is distinct from any value that could be put into the field. The rules for applying an Information Object Set as a constraint say that a match occurs with an empty field only if the corresponding element in the SEQUENCE is missing. Thus it only makes sense to write OPTIONAL in the class definition if OPTIONAL also appears on the corresponding element (the "hole") in the type definition of the protocol. By contrast, DEFAULT places no requirements on the protocol, it merely provides the type to be used if none is specified in the definition of a particular information object. In the illustration above we have specified NULL. It could, of course, be any ASN.1 type, built-in or user-defined, but use of NULL with DEFAULT is the most common. 

If we use the "information from object class" notation unconstrained, we have what is called an "open type". This really means an incomplete specification with no indication of who will provide, and where, the completion of the specification. Such use is not forbidden, but it should have been! Don't do it! Use with a simple table constraint is not much better, as the decoder has no way of knowing which of a set of types have been encoded, and without such knowledge encodings can be ambiguous. There is a special constraint that can be supplied to an "open type" called a type constraint. This was mentioned briefly in clause 8 of the last chapter. Here we might write 

$$
\text { ILLUSTRATION. } \& \text { Type - field   (My - type) }
$$

In terms of the semantics it carries, it is exactly equivalent to writing just "My-type", but it gets an extra length wrapper in PER, and is generally handled by tools as a pointer to a separate piece of memory rather than being embedded in the containing data-structure. It is useful if there are a number of places in the protocol that have some meta-semantics associated with them (such as types carrying security data), so that by writing as an element of a SEQUENCE or SET 

$$
\text {   SECURITY - DATA.   \&   Type - field   (Data - type - 1)   }
$$

you identify the element as the ASN.1 type "Data-type-1", but clearly flag it as a "SECURITY-DATA" type. 

Use of "information from object set" for a type field is illegal. This would in general produce a set of ASN.1 types (one from each of the objects in the object set), and there is nowhere in ASN.1 where you can use a set of types. 

Use of "information from object" for a type field produces a single type, and an alternative to the previous SEQUENCE or SET element using "Data-type-1" could in suitable circumstances be 

$$
\text { object1. } \& \text { Type - field }
$$

with 

$$
\begin{array}{l} \text {object1} \quad \text {SECURITY - DATA}:: = \\ \{\& \text {Type - field} \quad \text {Data - type - 1}, \\ \text {etc} \} \end{array}
$$

Note that this latter construction flags Data-type-1 as a SECURITY-DATA type, but it does not produce the encapsulation that the earlier construct produced. Use of "object1.&Type-field" produces exactly the same encoding as use of "Data-type-1" would produce. 

## 1.2 Fixed type value fields

The names of these fields are required to begin with a lower-case letter, and the name is required to be followed by an ASN.1 type which specifies the type of the value that has to be supplied for that field. It is again permissible to include OPTIONAL and DEFAULT in this specification, and also UNIQUE (as described in the last chapter). 

Closely linked to type fields, these are again frequently encountered. 

The most common types for these fields are INTEGER or OBJECT IDENTIFIER or a choice of the two, but BOOLEAN or an ENUMERATED type are also quite common. The latter two are used when the information being collected is not designed to be carried in a protocol message, but rather completes a "hole" in the procedures. 

For example, to take our ROSE example again, suppose that we allow the possibility that for some operations "ReturnResult" carries no information. This could be handled by putting OPTIONAL in the class definition of OPERATION.&ResultType, and also on the "hole" element of the "ReturnResult" SEQUENCE. However, we may want to go further than that. In cases where there is no result type, we may want to specify that, for some non-critical operations, the "ReturnResult" is never sent (a "Reject" or "ReturnError" will indicate failure), for others it must always be sent as a confirmation of completion of the operation, and for still others it is an option of the remote system to send it or not. In this case the fixed type value field might read: 

## &returnResult ENUMERATED {always, never, optional} DEFAULT always,

and the ROSE user would specify a value of "never" or "optional" for operations where this was the required behaviour. 

The use of the "information from object class" construct in this case produces simply the type of the fixed type value field. So use of 

$$
\text { ILLUSTRATION. } \& \text { fixed - type - value - field }
$$

is (almost) exactly equivalent to writing 

## INTEGER

The difference is that you cannot apply a table constraint with an object set of class ILLUSTRATION to the type INTEGER. You can apply it (and frequently do) to the "information from object class" construct. 

Both "information from object" producing (in this illustration) a single integer value and "information from object set" producing a set of integer values (a subset of type integer) are allowed in this case. Thus with an object set "Illustration-object-set" of class ILLUSTRATION, we could write 

$$
\text { Illustration - object - set. } \& \text { fixed - type - value - field }
$$

instead of 

## ILLUSTRATION.&fixed-type-value-field (Illustration-object)

What is the difference? Not a lot! In the latter case, you could use "@" with a relational constraint (on a type field of class ILLUSTRATION) to point to this element. In the former case you could not. The latter is what you will normally see. 

## 1.3 Variable type value fields

This is probably the second least common sort of field. Its main use is to provide a default value for a type that is provided in a type field. 

<table><tr><td>Much less common. An interesting example of a theoretically useful concept!</td></tr></table>

The field name is followed by the name of some type field (&T-F say) defined in this class definition. The value supplied for the variable type value field in the definition of an information object of this class is required to be a value of the type that was supplied for the &T-F field. 

This field can be marked OPTIONAL or DEFAULT, but there are then rules that link the use of OPTIONAL and DEFAULT between this field and the field &T-F. Roughly, if it makes sense it is allowed, if it doesn't it is not! Check the Standard (or use a tool to check your ASN.1) if you are unsure what is allowed and what is not. Roughly, both this field and &T-F must have, or not have, the same use of OPTIONAL or DEFAULT, and in the latter case, the default value for this field must be a value of the default type for the &T-F field. 

As you would expect for a field which holds a single value, the field-name has a lower-case letter following the "&". 

The use of "Illustration-object-set.&variable-type-value-field" is forbidden (not legal ASN.1). The use of "illustration-object.&variable-type-field" produces the value assigned to that field. 

## 1.4 Fixed type value set fields

These are fields that hold a set of values of a fixed type, and hence the field-name starts with an upper-case letter after the ampersand. 

Quite frequently used, mainly where we need to fill in holes in the procedures of a protocol, and have a list (an enumeration) of possible actions, some of which need to be selected and others forbidden. 

The information required here is a set of values of the type following the field-name (the governor type), or in other words, a subset of that type. These values can be supplied either by a typereference to a type which is the governor type with a simple subtype constraint applied it, or can be supplied using the value-set notation described in the last chapter. 

The most common occurrence of this field is where there are a number of possibilities, and the definer of an Information Object is required to select those that are to be allowed for this Information Object. 

Thus, in a class definition: 

```txt
&Fixed-type-value-set-field
ENUMERATED {confirm-by-post, confirm-by-fax,
    confirm-registered, confirm-by-e-mail
    confirm-by-phone}, 
```

might be used to let the user specify that, for some particular information object, some subset of the enumeration possibilities can be used. It is left to the reader's imagination to flesh out the above definition into a real fictitious scenario! 

Extraction of information from both objects and object sets using this field both produce a (sub)set of values of the type used in the class definition, containing just those values that appear in any of the objects concerned. 

## 1.5 Variable type value set fields

I (the author of this text!) am not at all sure that this sort of field does actually occur in practice. It was added largely because it seemed to be needed to "complete the set" of available sorts of field! Find a good use for it! 

In this box I can say "this has never been used!". In the body of the text I am more cautious! 

It begins with an upper-case letter, and the field-name is followed by the name of some type field (&T-F) in the same class definition. The field is completed by giving a set of values (a subset) of the type that is put into &T-F. 

Extraction of information from an object gives the value assigned to that field, but notation to extract information from an object set is illegal for this field type. 

## 1.6 Object fields

Perhaps surprisingly, this is less common than the object set field described below, but it is used. 

The object field carries the identification (an information object reference name) of some object of the class that follows the field name. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/82be3e32aad5fc93c00ad9efa888e80cb54f2c3cdc9d2b59bfb0cf2fbe169555.jpg)


This is the object-and-class equivalent of the fixed type value field. 

Its main use is to help in the structuring of information object definitions. If every object of one class (MAIN-CLASS say) is going to require certain additional information to be specified which would add a number of fields to MAIN-CLASS (and if the same additional information is likely to be specified frequently for different objects of MAIN-CLASS) then it makes sense to define a separate class (ADDITIONAL-INFO-CLASS say). Objects of ADDITIONAL-INFO-CLASS carry just the additional information, and references to them are included in an object field of MAIN-CLASS. 

Information from an object and from an object set produces a single object or a set of objects respectively. Use of these constructions is mainly useful if we have two classes defined that are closely related (the Directory OPERATION-X and CHAINED-OPERATION-X are examples), with one having the fields of the other as a subset of its fields. In this case it can avoid "fingertrouble" in the definition (and provide a clearer specification) if objects defined for CHAINED-OPERATION-X have the fields that correspond to OPERATION-X defined by extracting information from the corresponding OPERATION-X object, rather than repeating the definition over again. (This point actually applies to the use of information from object for all the different sorts of field.) 

## 1.7 Object set fields

We have already seen this in use to list the errors associated with an operation. As expected for something that is a set of objects, the & is followed by an upper-case letter. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/1ccdf5e6f929fbb27707a243fef4077073b18378fe72a03ccde7f772a1651715.jpg)


Information from object and from object set is again permitted, with the obvious results. 

## 1.8 Extended field names

When you are referencing fields of a class, object, or object set, you may end up with something that is itself a CLASS or object or object set (for example, OPERATION.&Errors delivers the ERROR class). When this happens, you are able to add a further "." (dot) followed by a field-name of the class you obtained. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/11978dc52e3176e9c15a1df4f9325167713b6f19473e0396bc50b272e70e663c.jpg)


Thus 

OPERATION.&Errors.&ParameterType 

and 

OPERATION.&Errors.&errorCode 

are valid notations, and are equivalent to: 

and 

ERROR.&ParameterType 

ERROR.&errorCode 

Similar constructions using an information object set of class OPERATION are more interesting. 

Here 

My-ops.&Errors.&errorCode 

delivers the set of values that are error codes for any of the operations in "My-ops", and 

my-look-up-operation.&Errors.&errorCode 

delivers that set of values that identify the possible errors of "my-look-up-operation". 

Of course, this can proceed to any length, so if we have an object set field of class OPERATION that is itself a set of objects of class OPERATION (this does actually occur in ROSE - the field is called "&Linked" and records so-called "linked operations"), we can write things like: 

my-op.&Linked.&Linked.&Linked.&Linked.&Errors.&errorCode 

This stuff is utterly fascinating - yes? But the reader is challenged to find a real use for it! (To be fair to ASN.1, these sorts of notation come out naturally if one wants consistency and generality in the notation, and cost little to provide. It is better that they are allowed than that what are fairly obvious notations be disallowed.) 

## 2 Variable syntax for Information Object definition

Historically, before the concept of Information Object Classes was fully-developed, an earlier feature of ASN.1 (now withdrawn), the so-called macro notation, was used by ROSE (and others) to provide users with a notation for defining the 

A few techies define information object classes, but a lot of users define objects of those classes, and even more (non-techie) people read those definitions. We need a human-friendly notation to define objects of a given class. "Variable syntax" is important and much used. 

information needed to fill in the holes in their protocols. The notation that ROSE (and others) provided was quite human-friendly. It certainly did not contain the "&" character, and often did not contain any commas! It frequently read like an English sentence, with conjunctions such as "WITH" being included in the notation, or as a series of keyword-value pairs. 

For example, to define a ROSE operation, you would write: 

```txt
my-op OPERATION
    ARGUMENT Type-for-my-op-arg
    RESULT Type-for-my-op-result
    ERRORS {error1, error4}
::= local 1 
```

(In the following text, we call this the ad-hoc-notation.) 

This was ad-hoc-notation defined by ROSE. (Other groups would define similar but unrelated syntax - in particular, some used comma to separate lists of things, others used vertical bar). 

It is important to note here that when this syntax was provided (in advance of the Information Object Class concept) there was little semantics associated with it. The above notation formally (to an ASN.1 tool) was nothing more than a convoluted syntax for saying: 

```txt
my-op CHOICE {local INTEGER, global OBJECT IDENTIFIER} ::= local:1 
```

and typically the value reference "my-ops" was never used anywhere. A lot of information was apparently being collected, but was then "thrown on the ground" (in terms of any formal model of what the text meant). 

(As an aside, the inclusion of the ":" (colon) above after "local" is not fundamental to this discussion - it resulted from the fact that a choice value was expressed in early work as (eg) "local 1" and post-1994 as "local:1"). 

The above notation was, however, designed really to serve the same purpose that you would get today with the object definition: 

```txt
my-op OPERATION ::=
    {&operationCode local:1,
    &ArgumentType Type-for-my-op-arg,
    &ResultType Type-for-my-op-result,
    &Errors {error1 | error4} } 
```

(We call this below the object-definition-notation.) 

We can observe a number of things. First, the ad-hoc-notation is probably easier for a human to read than the object-definition-notation, although the lack of a clear semantic under-pinning would confuse more intelligent readers! Second, because the notation was ad hoc, it was very difficult to produce any tool support for it. Third, because the notation was ad hoc, a tool had no means of knowing when this ad hoc notation terminated and we returned to normal ASN.1 (there were no brackets around the ad-hoc-notation). Finally, there was no formal link (such as we get by using an Information Object Set as a constraint) between use of this notation and holes in the ROSE protocol. 

Nonetheless, when the Information Object Class material was introduced into ASN.1 (and the use of macro notation withdrawn) in 1994, it was felt important to allow a more human-friendly (but still fully machine-friendly, and with full semantics) notation for the definition of objects of a given class. 

The aim was to allow definers of a class to be able to specify the notation for defining objects of that class which would let them get as close as possible (without sacrificing machineprocessability) to the notation that had hitherto been provided as ad-hoc notation. The "variable syntax" of ASN.1 supports (fulfills) this aim. 

Variable syntax requires that a class definition is immediately followed by the key words "WITH SYNTAX" followed by a definition of the syntax for defining objects of that class. If those keywords are not present following the class definition, then the only available syntax for defining objects is the object-definition-notation. (The latter can still be used by users defining objects even if there is a "WITH SYNTAX" clause.) 

Figure II-22 adds WITH SYNTAX to the OPERATION class definition. (Again we must emphasise that the real ROSE specification is a little more complex than this - we are not producing a full tutorial on ROSE!) 

```txt
OPERATION ::= CLASS
    { &operationCode CHOICE {local INTEGER,
    global OBJECT IDENTIFIER}
    UNIQUE,
    &ArgumentType,
    &ResultType,
    &Errors ERROR OPTIONAL }
WITH SYNTAX
    { ARGUMENT &ArgumentType
    RESULT &ResultType
    [ERRORS &Errors]
    CODE &operationCode } 
```

What is this saying/doing? It allows an object of class operation to be defined with the syntax: 

```txt
my-op OPERATION ::=
{ ARGUMENT Type-for-my-op-arg
RESULT Type-for-my-op-result
ERRORS {error1 | error4}
CODE local:1 } 
```

The reader will notice the disappearance of the unsightly "&", the strong similarity between this and the ad-hoc-notation, but also the presence of curly brackets around the definition, needed to maintain machine-processability. 

What can you write following "WITH SYNTAX"? Roughly you have the power normally used in defining command-line syntax - a series of words, interspersed with references to fields of the class. In defining an object, the definer must repeat these words, in order, and give the necessary syntax to define any field that is referenced. Where a sequence of words and/or field references are enclosed in square brackets (as with "[ERRORS &Errors]" above), then that part of the syntax can be omitted. (Of course, the inclusion of the square brackets was only legal in the definition of the "WITH SYNTAX" clause because "&Errors" was flagged as "OPTIONAL" in the main class definition.) 

A "word" for the purpose of the WITH SYNTAX clause is defined as a sequence of upper-case (not lower-case) letters (no digits allowed), possibly with (single) hyphens in the middle. 

It is also possible to include a comma (but no other punctuation) in the WITH SYNTAX clause, in which case the comma has to appear at the corresponding point in the definition of an object of that class. 

Square brackets can be nested to produce optional sections within optional sections. However, there are some quite severe restrictions on the use of "WITH SYNTAX" which are designed both to prevent the apparent acquisition of information with no effect on the actual object definition, and also to ensure easy machine-processability. Writers of a WITH SYNTAX clause should read the Standard carefully. Figure II-23 would, for example, be illegal. 

```txt
OPERATION ::= CLASS
    { &operationCode CHOICE {local INTEGER,
    global OBJECT IDENTIFER}
    UNIQUE,
    &ArgumentType,
    &ResultType,
    &Errors ERROR OPTIONAL }
WITH SYNTAX
    { ARGUMENT &ArgumentType
    RESULT &ResultType [REQUIRED]
    [ERRORS &Errors]
    CODE &operationCode }

Figure II-23: Illegal specification of WITH SYNTAX 
```

```txt
OPERATION ::= CLASS
    { &operationCode CHOICE {local INTEGER,
    global OBJECT IDENTIFIER}
    UNIQUE,
    &ArgumentType,
    &ResultType,
    &ReturnsResult ENUMERATED
    {does, does-not},
    &Errors ERROR OPTIONAL }
WITH SYNTAX
    { ARGUMENT &ArgumentType
    RESULT &ResultType
    &ReturnsResult RETURN-RESULT
    [ERRORS &Errors]
    CODE &operationCode } 
```

This is because it allows the definer of an object to provide information by inclusion or not of the word "REQUIRED" which is nowhere recorded in a field of the object. If it is desired to let the definer of an object specify whether the return of a result is required or not, the definition of figure II-24 could be used, allowing: 

```makefile
my-op OPERATION ::=
{ ARGUMENT Type-for-my-op-arg
RESULT Type-for-my-op-result
does-not RETURN-RESULT
ERRORS {error1 | error4}
CODE local:1 } 
```

Finally, we try to provide a tabular notation for the compact definition of a an object of class OPERATION similar to the table defined originally in Figure II-14. This is shown in figure II-25. 

```txt
OPERATION ::= CLASS
    { &operationCode CHOICE {local INTEGER,
    global OBJECT IDENTIFER}
    UNIQUE,
    &ArgumentType,
    &ResultType,
    &Errors ERROR OPTIONAL }
WITH SYNTAX
    { &operationCode
    &ArgumentType
    &ResultType
    [&Errors]
    } 
```

With the definition in figure II-24 we would be allowed to write (compare figures II-14 and II-17): 

```txt
My-ops OPERATION ::=
{ {asn-val-order Order-for-stock Order-confirmed
    {security-failure
    | unknown-branch} }
| {asn-val-sales Return-of-sales NULL {security-failure
    | unknown-branch} }
| {asn-val-query Query-availability Availability-response
    {security-failure
    | unknown-branch
    | unavailable } }
| {asn-val-state Request-order-state Order-state {security-failure
    | unknown-branch
    | unknown-order } } 
```

So we have now come full circle! The informal tabular presentation we used in figure II-14 was replaced with the formal but more verbose definition of figure II-17, which (using WITH SYNTAX) can be replaced with syntax very like that of figure II-14. 

It should by now be clear to the reader that WITH SYNTAX clauses should be carefully considered. Not only must the rules of what is legal be understood, but what is a good compromise between verbosity and intelligibility in the final notation has to be determined. As with all human interface matters, there is no one right decision, but a little thought will avoid bad decisions! 

## 3 Constraints re-visited - the user-defined constraint

There is not a lot to add on constraints. We have covered earlier all the simple sub-type constraints, and in the last chapter the table and relational constraints. There is just one other form of constraint to discuss, the so-called user-defined constraint. 

```txt
User-defined constraints - little more than a comment! Why bother? 
```

We discussed above the earlier availability of a notation (the macro notation) that allowed people to define new ad-hoc-notation (with no real semantics) for inclusion in an ASN.1 module. When this "facility" was removed in 1994, it turned out that the Information Object concept did not quite cover all the requirements that had been met by use of this macro notation, and the user-defined constraint concept was introduced to meet the remaining requirements. This form of constraint would probably not have been introduced otherwise, as it is little more than a comment, and tools can make little use of it. It is almost always used in connection with a parameterised type, introduced in clause 9 of II-6. 

One piece of ad-hoc-notation that was defined using the macro notation was the ability to write: 

$$
\text { ENCRYPTED   My - type }
$$

as an element of a SET or SEQUENCE. 

Although not implied by the ASN.1 formal text, this actually meant that the element was a BITSTRING, whose contents were an encryption (according to an encryption algorithm specified in English text) of the encoding of the type My-type. 

We can get slightly more clarity if we define a parameterised type "ENCRYPTED" as : 

and then use 

```txt
ENCRYPTED {My-type} 
```

as the SEQUENCE or SET element. 

(Note that we violate convention, but not the rules of ASN.1 by using all capitals for the ENCRYPTED type. This is for reasons of historical compatibility with the original ad-hocnotation "ENCRYPTED My-type". Note also that the new formal notation includes a new pair of curly brackets, as we saw - for a slightly different reason - with the move from ad-hoc-notation to object-definition-notation.) 

The above avoided the use of an ad-hoc-notation, but it is curious for the dummy parameter of "ENCRYPTED" not to be used at all on the right-hand side of the assignment. It is clear that the actual value of the BITSTRING will depend on the "Type-to-be-encrypted" type (and also on the encryption algorithm and keys, which we cannot define using ASN.1). 

So we introduce the user-defined constraint. In its basic form, we would write: 

```txt
ENCRYPTED {Type-to-be-encrypted} ::= BITSTRING
(CONSTRAINED BY {Type-to-be-encrypted}) 
```

which shows that the dummy parameter is used to constrain the value of BITSTRING. (If there were multiple parameters used in the constraint, these would be in a comma-separated list within the curly braces after CONSTRAINED BY.) 

The constraint is called a "user-defined" constraint because the precise nature of the constraint is not specified with formal ASN.1 notation. This construction almost invariably contains comment that details the precise nature of the constraint. So the above would more commonly be written as: 

```txt
ENCRYPTED {Type-to-be-encrypted} ::= BITSTRING
(CONSTRAINED BY {Type-to-be-encrypted}
-- The BITSTRING is the results of
-- encrypting Type-to-be-encrypted
-- using the algorithm specified
-- in the field security-algorithm,
-- and with the encryption parameters
-- specified in Security-data -- ) 
```

The reader should know enough by now (assuming earlier text has been read and not skipped!) to realise that "security-algorithm" will turn out to be a (UNIQUE) fixed type value field (probably of type object identifier) of some SECURITY-INFORMATION class, with "Security-data" being a corresponding type field of this class that, for any given object of SECURITY-INFORMATION is defined with an ASN.1 type that can carry all necessary parameters for the algorithm that is being defined by that object. There might be other fields of SECURITY-INFORMATION that statically define choices of procedures in the application of the algorithm, filling in procedural "holes" in this process. 

<table><tr><td>It is obvious, powerful, and simple! How unusual for ASN.1!</td></tr></table>

## 4 The full story on parameterization

There is not a lot more to add on parameterization, and it is all pretty obvious stuff. But here it is. © OS, 31 May 1999 22 

## 4.1 What can be parameterized and be a parameter?

The box says it all. Any form of reference name - a type reference, a value reference, a class reference, Answer: Anything and everything! an object reference, an object set reference can be parameterised by adding a dummy parameter list after the reference name and before the "::=" when the "thing" the name references is being defined. 

Here is an example of a reference name with a complete range of parameters: 

```autohotkey
Example-reference {INTEGER:intval,
My-type,
THIS-CLASS,
OPERATION:My-ops,
ILLUSTRATION:illustration-object} ::= 
```

As we would expect, the initial letter of dummy parameters is upper-case for types, classes, and object sets, and lower case for objects and values. Note that for values, object sets, and objects, the dummy parameter list includes the type or class of these parameters followed by a ":" (colon). (The only one of the above examples that I have not seen in an actual specification is a dummy parameter which is a class (THIS-CLASS above). 

Normally, the dummy parameter is used somewhere on the right-hand side of the assignment, but it can also be used within the parameter list itself (before or after its own appearance). So we could, for example, write: 

$$
\text {   Example1   } \left\{\text {   My - type:default - value,   My - type   } \right\}:: =
$$

This notation is extremely general and powerful, and has many applications. We have seen the ROSE examples where an Information Object Set is declared as a dummy parameter. This is probably the most common thing that is used as a dummy parameter, but next to that is a value of type INTEGER that is used on the right-hand side as the upper-bound of INTEGER values, or as an upper-bound on the length of strings. 

There is also an important use in the Manufacturing Messaging Formats (MMF) specification. Here the bulk of the protocol specification occurs in a "generic" module, and is common to all cells on a production line. However, specific cells on the production line require some additional information to be passed to them. In the generic module we use a dummy parameter (a type) and include it in our protocol specification as an element of our SEQUENCE and export this parameterised type. Modules for specific cells define a type containing the additional information for that cell, import the generic type, and declare the protocol to be used for that type of cell as the generic type, supplied with the type containing the additional information as the actual parameter. This is similar to the ROSE example, but using a type rather than an information object set. 

Let us explore the question of bounds a little further. Few protocols "hard-wire" upper bounds into the specification, but it is always a good idea to specify such bounds, as designers rarely intend to require implementors to handle arbitrarily large integers, iterations of sequences, or arbitrarily long strings. Where such bounds are fixed for the entire protocol, then it is common practice to assign the various bounds that are needed to an integer reference name in some module, then to use EXPORTS and IMPORTS to get those names into the modules where they are used as bounds. 

Where, however, there are generic types (such as a CHOICE of a number of different character string types) that are used in many places but with different bounds for each use, then using an INTEGER dummy parameter for the bounds is a very effective and common practice. 

It is actually quite rare to see long dummy parameter lists. This is because any collection of information (apart from a class) can easily be turned into a Information Object Set. So with the earlier example (taking MY-CLASS out) of: 

```txt
Example-reference {INTEGER:intval,
My-type,
OPERATION:My-ops,
ILLUSTRATION:illustration-object} ::= 
```

We could instead define: 

```txt
PARAMETERS-CLASS ::= CLASS
    {&intval INTEGER,
    &My-type,
    &My-ops OPERATION,
    &illustration-object ILLUSTRATION} 
```

and then our parameter list just becomes: 

```txt
Example-reference {PARAMETERS-CLASS:parameters} ::= 
```

and on the right-hand side we use (for example) "parameters.&My-type" instead of "My-type". This may seem more cumbersome than using several dummy parameters, but if the same parameter list is appearing in several places, particularly if dummy parameters are being passed down as actual parameters through several levels of type definition, it can be useful to bundle up the dummy parameters in this way. 

A particular case of this would be where a protocol designer has identified twelve situations (iterations of sequences, lengths of strings, sizes of integers) where bounds are appropriate, with potentially twelve different integer values for each of these situations, probably with each of the twelve values being used in several places in the protocol. This is again a good case for "bundling". We can define a class: 

```txt
BOUNDS ::= CLASS
    { &short-strings INTEGER,
    &long-strings INTEGER,
    &normal-ints INTEGER,
    &very-long-ints INTEGER,
    &number-of-orders INTEGER}
WITH SYNTAX
{STRG &short-strings, LONG-STRG &long-strings,
    INT &normal-ints, LONG-INT &very-long-ints,
    ORDERS &number-of-orders} 
```

and routinely and simply make an object set of this class a dummy parameter of every type that we define, passing it down as an actual parameter of any types in SEQUENCE, SET, or CHOICE constructions. We can then use whichever of the fields we need in the various places in our protocol. In some type definitions, we might use none of them, and the dummy parameter for that type would be redundant (but still legal), or we might use one or two of the fields, or (probably rarely) all of them. 

At the point where we define our top-level type (usually a CHOICE type, as we discussed in the early parts of this book), we can set our bounds and supply them as an actual parameter. So if "Wineco-protocol" is our top-level type, we could have: 

```txt
bounds BOUNDS ::= {STRG 32, LONG-STRG 128,
    etc }
Wineco-protocol {BOUNDS:bounds} ::= CHOICE
{ordering [APPLICATION 1] Order-for-stock
{BOUNDS: bounds},
sales [APPLICATION 2] Return-of-sales
{BOUNDS: bounds}
etc. } 
```

No doubt there are some readers that will be saying "What is the point of passing this stuff down as parameters, when (provided "bounds" is exported and imported everywhere), it can be directly used?" The answer in this case is "Not much!". If, for any given type, any set of bounds is always going to be fixed, then there is no point in making it a parameter, a global reference name can be used instead, with a simpler and more obvious specification. But read on to the next section! 

## 4.2 Parameters of the abstract syntax

Protocol designers are often hesitant about fixing bounds in the body of a protocol definition, even if they are defined in just one place and passed around either by simple import/export or by additionally using dummy parameters. The reason for the hesitation is that bounds can very much "date" a protocol for two reasons: First, what seems adequate initially (for example, for the number of iterations of the "details" SEQUENCE in our "Order-for-stock" type in 

So you want to leave some things implementation-dependent? Coward! But at least make it explicit (and define exceptionhandling to help interworking between different implementations) Parameters of the abstract syntax let you do that, but they are a rarely-used feature. 

Figure 13 of Section I) can well prove inadequate ten years later when the business has expanded and mergers have occurred! Second, bounds are usually applied to ease the implementation effort when implementing on machines with limited memory capacity, or without support for calculations with very long integer values. Such technological limitations do, however, have a habit of disappearing over time. So whilst fifteen years ago, many designers felt that it was unreasonable to have messages that exceeded 64K octets, today implementors on most machines would have no problem handling messages that are a megabyte long. (An exception here would be specifications of data formats for smart cards, where memory is still very limited. This is an area where ASN.1 has been used.) 

So ..., if we don't want to put our bounds into the main specification, what to do? Just leave them out? This will undoubtedly cause interworking problems, with some systems not being able to handle things of the size that some other systems generate, and we are not even flagging this up as a potential problem in our ASN.1 specification. 

Providing a "bounds" parameter, but never setting values for it, can help with this problem. We have already seen in figure 21 in Section I Chapter 3 that we can specify our top-level type using the "ABSTRACT- SYNTAX" notation. Let us repeat that now with our parameterised Winecoprotocol developed above: 

$$
\begin{array}{l} \text {wineco - abstract - syntax   \{BOUNDS:bounds\} ABSTRACT - SYNTAX   :: =} \\ \quad \{\text {Wineco - protocol   \{BOUNDS: bounds\} IDENTIFIED BY etc} \} \end{array}
$$

We are now defining our abstract syntax with a parameter list. We have parameters of the abstract syntax. ASN.1 permits this, provided such parameters are used only in constraints. These constraints are then called variable constraints, because the actual bound is implementationdependent. The important gain that we have now got, however, is that this implementationdependence has been made very clear and specific. Where we have a variable constraint, we would normally provide an exception marker to indicate the intended error handling if material is received that exceeds the local bounds. 

In the OSI work, there is the concept of International Standardized Profiles (ISPs) and of Protocol Implementation Conformance Statements (PICS). The purpose of ISPs is to provide a profile of options and parameter values to tailor a protocol to the needs of specific communities, or to define different classes (small, medium, large say) of implementation. The purpose of the PICS is to provide a format for implementors to specify the choices they have made in implementationdependent parts of the protocol. Clearly, the use of parameters of the abstract syntax aids in both these tasks, with values for those parameters either being specified in some profile (which an implementation would then claim conformance to) or directly in the PICS for an implementation. 

Parameters of the abstract syntax (with exception markers on all variable parameters) provide a very powerful tool for identifying areas of potential interworking problems, but it is (for this author at least) sad that to-date these features are not yet widely used. 

## 4.3 Making your requirements explicit

## 4.3.1 The TYPE-IDENTIFIER class

A very common Information Object Class is one which has just two fields, one holding an object identifier to identify an object of the class, and the other holding a type associated with that object. This class is in fact pre-defined (built-in) in ASN.1 as the TYPE-IDENTIFIER class. It is defined as: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/f12ec0bf62d08541f83d1c50d88a4bca70976606f7b72a692028c5c688f51b70.jpg)


One of only two built-in classes (the other is ABSTRACT-SYNTAX) in ASN.1, and quite well-used. 

TYPE-IDENTIFIER ::= CLASS {&id OBJECT IDENTIFIER UNIQUE, &Type } WITH SYNTAX {&Type IDENTIFIED BY &id} 

There are many protocols that make use of this class. It is the foundation stone for a very flexible approach to extensibility of protocols. 

## 4.3.2 An example - X.400 headers

(As with ROSE, the following is not an exact copy of X.400). 

In X.400 (an e-mail standard), there is the concept of "headers" for a message. A wide range of headers are defined. In the earliest version of X.400, these were hard-wired as types within a SEQUENCE, but it rapidly became clear that new headers would be added in subsequent versions. Of course, the SEQUENCE could just have had the extensibility ellipsis added, with defined exception handling on the ellipsis, ensuring interworking between versions 1 and 2, but an alternative approach is to define the headers as: 

$$
\text { HEADER - CLASS }:: := \text { TYPE - IDENTIFIER }
$$

and the actual headers as: 

```autohotkey
Headers-type {HEADER-CLASS:Supported-headers} ::=
SEQUENCE OF SEQUENCE
{id HEADER-CLASS.&id ( {Supported-headers} !100),
info HEADER-CLASS.&Type ( {Supported-headers}{@id}!101) } 
```

Exception handling 100 and 101 will be specified in the text of the protocol definition. Handling of 100 is likely to be "silently ignore" and of 101 (a bad type) "send an error return and otherwise ignore". 

The question is, when we eventually supply an actual parameter for Header-type, what do we provide? Let us examine some options. 

There will certainly be some headers defined in this version of the protocol, and we will undoubtedly expect to add more in subsequent versions, so we would first define an extensible information object set something like: 

$$
\begin{array}{l} \text {Defined - Headers HEADER - CLASS : : =} \\ \{\text {header1 | header2 | header3 , ..., header4} \} \end{array}
$$

where header4 was added in version 2. 

But what do we supply as the actual parameter for our protocol? Let us take the most general case first. We consider providing two parameters of the abstract syntax, both object sets of class HEADER-CLASS. One is called "Not-implemented" and the other "Additional-headers". We might want to provide one or both of these or neither, depending on the decisions below. I think you are probably getting the idea! 

Let us now look at various possible views we might take on the requirements of implementations to support headers. 

## 4.3.3 Use of a simple SEQUENCE

We decide we want to define a fixed set of headers, all to be implemented, no additions, and we will never make later changes. Some headers will be required, others optional. 

We got it right first time! 

This case is easy, and we don't need Information Object Sets, we simply use: 

```txt
Headers ::= SEQUENCE
{header1 Header1-type --must be included--, header2 Header2-type OPTIONAL, etc } 
```

This is simple and straight-forward, but very inflexible. Where the decisions on what headers to provide (as in the case of e-mail headers) is rather ad hoc and likely to need to be changed in the future, this is NOT a good way to go! 

Note that in this case the identification of what header is being encoded in a group of OPTIONAL headers is essentially done (in BER) using the tag value. (In PER it is slightly different - a bitmap identifies which header has been encoded in a particular position). 

## 4.3.4 Use of an extensible SEQUENCE

In the case of e-mail headers, it is highly likely that we will want to add more types of header later, so making the SEQUENCE extensible would be a better approach. And we should specify exception handling so that we know how 

We are in control. You do what we say. We won't remove anything, but we might add more later. 

version 1 systems will behave when they are sent headers from a version 2 system (and how version 2 systems should behave if headers that are mandatory in version 2 are missing because it is a version 1 system that is generating the headers). 

## 4.3.5 Moving to an information object set definition

Now we make a quite big jump in apparent complexity, and use the "Headers" type we introduced above, namely: 

Giving ourselves more options, but still keeping control. 

```autohotkey
Headers-type {HEADER-CLASS:Headers} ::= SEQUENCE OF SEQUENCE
{identifier HEADER-CLASS.&id({Headers} !100),
data HEADER-CLASS.&Type({Headers}{@identifier} !101)} 
```

We have now moved to use of an object identifier to identify the type of any particular header, and potentially we now allow any given header type to be supplied multiple times with different values. But we have lost the ability to say whether a header is optional or not, and we have no easy way of saying which headers can appear multiple times. 

We can address these problems by adding fields to our HEADER-CLASS. So instead of defining it as TYPE-IDENTIFIER, we can define it as: 

```sql
HEADER-CLASS ::= CLASS
    {&id OBJECT IDENTIFIER UNIQUE,
    &Type,
    &Required BOOLEAN DEFAULT TRUE,
    &Multiples BOOLEAN DEFAULT TRUE}
WITH SYNTAX {&Type IDENTIFIED BY &id,
    [REQUIRED IS &Required],
    [MULTIPLES ALLOWED IS &Multiples]} 
```

We can now specify (when each header object is defined) whether it is optional or not, and whether multiple occurrences of it are permitted or not. Of course, when we used a SEQUENCE, we could flag optionality, and we could have indicated that multiples were allowed by putting SEQUENCE OF around certain elements. But the approach using information objects is probably simpler if we want all of that, and paves the way for more options. 

Of course, when we define the information object set "Defined-Headers", we will make it extensible, indicating the possibility of additions in version 2, and will put an exception specification on the ellipsis to tell version 1 systems what to do if they get headers they don't understand. 

We could actually go further than this, as X.500 does in a similar circumstance: we could put another field into HEADER-CLASS defining the "criticality" of a header, and we could provide a field in "Headers-type" to carry that value. Our exception specification could then define different exception handling for unknown headers, depending on the value of the "criticality" field associated with it in the message. 

We have advanced some way from the rather restricted functionality we had with SEQUENCE. 

## 4.3.6 The object set "Headers"

An extensible "Defined-Headers" merely gives us control over what version 1 does when we add new material in version 2. It in no way says that implementations (probably on some user-group or vendor-specific basis) can agree and add new headers. It also says that to conform to version x, you must support all the headers listed in the "Defined- Headers" for version x. 

Now we give flexibility to the implementors. We use the parameters of the abstract syntax. 

But, suppose we define: 

```txt
Supported-Headers
{HEADER-CLASS:Additional-Headers,
HEADER-CLASS:Excluded-Headers} HEADER-CLASS::=
{ (Defined-Headers | Additional-Headers)
EXCEPT Excluded-Headers) } 
```

where "Additional-Headers" and "Excluded-Headers" are parameters of the abstract syntax as described above, and where "Supported-Headers" is supplied as the actual parameter for our dummy parameter "Headers" in an instantiation of "Header-type".when we define our top-level PDU (and then passed down for eventual use in the constraints on "Header-type"). 

As usual, we could, if we wish, bundle the two object sets together as an object set of a new object class, making just one parameter of the abstract syntax covering both specifications. 

With the above definition, we are clearly saying that we have some defined headers, implementors may support others, and indeed may choose not to support some of the defined headers. Total freedom! Possibly total anarchy! But most implementations will probably choose to implement most of the defined headers, and the exception handling should cope with interworking problems with those that miss a few out (for whatever reason). 

It is left as a (simple!) exercise for the reader to write an appropriate definition of Supported-Headers where we 

a) decide to allow additional headers, but require support for all defined headers; or 

b) decide to allow some defined headers not to be supported, but disallow implementation-dependent or vendor-specific additions. 

Of course, at the end of the day, you can never ENFORCE a requirement to implement everything, nor can you prevent people from extending a standardised protocol. But you CAN make it very clear that they are then not conforming to the Standard. ASN.1 provides the tools for doing this. 

## 4.4 The (empty) extensible information object set

It makes little sense in most protocols to have an information object set with no members, even if it is extensible: 

$$
\{\dots \}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/9a6f23c88de756158da2a8b4e74094a2e289c7bac746578c35355370af1cf5e5.jpg)


It has become a fairly common practice (now supported by text in the Standard) to use this notation as a short-hand for "a parameter of the abstract syntax". When this is used as a constraint, it quite simply says that the specification is incomplete, and that you must look elsewhere for the specification of what is or is not supported. 

This is called a "dynamically extensible object set", the idea being that implementations will determine in an instance of communication what objects they deem it to contain, and may indeed (depending on whether it is raining or not!) accept or reject some objects at different times. 

If you get the impression that this author disapproves of the use of this construct, you will not be very wrong! 

It provides no functionality beyond that provided (far more clearly) by parameters of the abstract syntax. It does, however, have one advantage. Parameters of the abstract syntax appear at the top-level, and need to be passed down as parameters to succeeding nested types until they reach the point at which they are to be used. This adds to the size of a specification, and can sometimes make it less easily readable. (Work was once proposed to add the concept of "global parameters" to ASN.1. This would effectively have enabled a top-level parameter to become a normal reference name, usable anywhere, without being passed from type to type as a sequence of actualdummy parameters. This work was, however, never progressed). 

The use of the "{...}" notation in a constraint provides a direct statement at the bottom level that this constraint is implementation-dependent. But on the opposite side again - you cannot tell by looking at the top-level definition that there are (effectively) parameters of the abstract syntax, that is, that the specification is incomplete. You have to look through perhaps a hundred pages of ASN.1 definitions trying to spot occurrences of "{...}. 

The advice of this author is DON'T USE THIS CONSTRUCT. But you do need to know what it is supposed to mean if you encounter it, and there are many specifications that use it (more than use parameters of the abstract syntax). 

There is an informative annex (not part of the Standard) in X.681 that says that ANY object set that is made extensible implies that random additions and removals of objects can be made when considering constraints imposed by that object set. It is not often that this author criticises the ASN.1 Standards - I wrote a lot of the text in them! But this annex gives bad advice, and is not really supported by normative text in the body of the Standard. 

So ... how do you decide what a particular specification means when it uses an extensible nonempty set? Read the specification carefully, and it will usually be clear. If it uses {...} it is probably saying that all extensible object sets can have implementation-dependent additions or exceptions (but then has no way of countering that in specific cases except by comment). If (like X.400), it has explicit parameters of the abstract syntax, it surely will NOT be implying that, and you should use the interpretation given in the previous clause for "Headers". 

<table><tr><td>You and me both - we must be getting tired! There is not much more to say, but there is still some. We&#x27;ll try to keep it brief. This is not difficult stuff, but it IS used, and IS important.</td></tr></table>

## 5 Other provision for "holes"

There are some other mechanisms, mainly pre-dating the information object concept, that support holes in ASN.1 specifications. We need to have a brief discussion of these. 

## 5.1 ANY

This has two important claims to fame. First, it was the only support for black-holes in the original 1984 ASN.1 Specifications! And second, it was withdrawn in 1994, causing a fairly major uproar among some ASN.1 users. 

A (bad?) first attempt? 'Twas the best we could do in 1984. Holes were not really understood then. 

If you wrote type "ANY" in a SEQUENCE or SET, it literally meant that any ASN.1 type could be slotted in there to replace the ANY. It was frequently accompanied in early CCITT specifications with the comment: 

$$
- - \text {   For   further   study   } - -
$$

This comment clearly indicated that it was merely a place-holder in an incomplete specification. Usually in such cases, the SEQUENCE element read: 

## ANY OPTIONAL

so you basically knew that that element was not implementable - YET! 

Used in this way, it did no harm, but was probably not really useful. It provided part of the functionality we get today by using the extensibility ellipsis. It said "there is more to come in a later version, but we don't really know what yet". 

There were, however, other uses. One was in X.500 until recent times, where an element of a SEQUENCE read: 

## bi-lateral-information ANY OPTIONAL

The intent here was to allow implementation-dependent additional information to be passed, where the ASN.1 type for this information would be determined elsewhere (community of interest, or vendor-specific). If several vendors or communities produced different specifications for the type to fill this field, then you would typically look at the calling address to determine what the field was saying. (Yet another - non-standard - way of providing an identifier for the content of a hole!) 

In practice, this field was never implemented by X.500 implementors. 

Another option for determining the type (and its semantics) that filled the field would be to see if it was raining or not, but I don't think anyone ever used this particular mechanism for "holeidentification"! 

## 5.2 ANY DEFINED BY

This was an attempt in 1986/88 to shore up the ANY. There was by now a recognition that a black-hole absolutely had to have somewhere close to it in the protocol some value that would point to the definition of the actual type (and - more importantly - the semantics associated with that type) that was filling the hole. Suddenly the hole became a bit less black! 

Dawn breaks (but just a bit!). It was recognised that any hole really MUST have associated with it a mechanism for determining what (and with what semantics) fills the hole. 

(The light in the coal-cellar really got switched on when information objects appeared in the 1994 specification. I am grateful to Bancroft Scott for the analogy between the introduction of the information object concepts and switching on a light in a coal-cellar. When he first made the remark, someone - forgotten who - replied "That sounds rather dramatic. Things that dramatic can cause tidal waves." The reply was a good one! Information objects did not replace ANY and ANY DEFINED BY easily. Eventually they did, but it took close to seven years before the waves subsided!) 

With ANY DEFINED BY a typical SEQUENCE might now contain: 

$$
\begin{array}{l l} \text {identifier} & \text {OBJECT IDENTIFIER,} \\ \text {hole} & \text {ANY DEFINED BY identifier} \end{array}
$$

The reader will recognise that this provides the same sort of link between the two fields that is now provided by use of a relational constraint (the @ notation) between "information from object class" constructs, but that it lacks any information object set reference to define the precise linkage, the types that can fill the "ANY" field, and the semantics associated with those types.. 

There were also (too severe) restrictions on the linkages that could be specified using the ANY DEFINED BY notation which made it impossible for some existing specifications to move from ANY to ANY DEFINED BY, even 'tho' they DID have a field (somewhere) in their protocol that defined the content of the ANY hole. 

## 5.3 EXTERNAL

EXTERNAL was introduced in 1986/88, and is still with us. The name is in recognition of the fact that people want to embed material that is external to ASN.1, that is, material that is not defined using ASN.1 (for example, a GIF image). It was, however, also intended as a better version of ANY and ANY DEFINED BY, because it encapsulated identification of what was in the hole with the hole itself. 

But you want to include material that is not defined using ASN.1. And you want to identify the type of material and the encoding of it. Roll your own using OCTET STRING or BIT STRING and a separate identifier field. That would work. But EXTERNAL tried to provide a ready-made solution. 

EXTERNAL was defined when ASN.1 was very much part of the OSI family, and recognised (amongst other possibilities) identification of the hole contents using a "presentation context" 

negotiated using the Presentation Layer facilities of OSI. This mechanism was probably never used by any actual implementation. 

EXTERNAL can also make a claim to fame: its definition is almost certainly the only place in any ASN.1 specification where the type "ObjectDescriptor" is used! (But it is OPTIONAL - and I will wager that no implementation has ever transmitted an "ObjectDescriptor" value within an EXTERNAL.) 

Finally, EXTERNAL was borne in the early days of understanding about abstract and transfer syntaxes, and (if you exclude the option of using the OSI Presentation Layer) used only a single object identifier value to identify the combination of abstract and transfer syntax for the material that filled the hole. Today, we generally believe that it is appropriate to identify the set of abstract values in the hole (for example, that it is a still picture) with one object identifier, and the encoding of those values (the encoding of the picture) with a separate object identifier. So whilst EXTERNAL remains (unchanged from its original introduction in 1986/88) in the 1988 specification, it has serious flaws, and new specifications should instead use "EMBEDDED PDV" (described below) if they wish to carry non-ASN.1-defined material. 

## 5.4 EMBEDDED PDV

EMBEDDED PDV was introduced in 1994. It was, quite simply, an attempt to "improve" EXTERNAL. It has all the functionality of EXTERNAL that anyone cares about. It got rid of the Object Descriptor that no-one ever used, and it allowed (but did not require) separate object identifiers for the identification of the abstract syntax and the transfer syntax (encoding) of the material that filled the hole. 

Why is it so difficult to get it right first time? EMBEDDED PDV is really just mending the deficiencies of EXTERNAL. EXTERNAL looked pretty good in 1986/88, but by 1994, it needed a re-fit. 

Perhaps more importantly, it included the ability for a protocol designer to specify (statically) either or both of the abstract and transfer syntaxes for the "hole" (using constraint notation). 

One important use for this is in security work, where EMBEDDED PDV is used to carry the encryption of a type, the type (abstract syntax of hole contents) being statically specified, and the encryption mechanism (transfer syntax) being transferred at communication time. 

In appropriate circumstances, a designer can specify statically both the abstract (type of material) and transfer syntax (encoding) of what fills the hole. If this is done, then EMBEDDED PDV produces no overheads other than a length wrapper around the embedded material. 

A brief word about the name. (Figure 999 again). It is certainly a bad name for the type. "EMBEDDED" is fine. It represents a hole that can take embedded material. But "PDV"? Most readers will never have met the term "PDV". It actually standard for "Presentation Data Value", and is the term used by the OSI Presentation Layer Standard to describe the unit of information passed between the Application Layer and the Presentation Layer, or (in terms more related to the description given here of ASN.1) an abstract value from some abstract syntax (not necessarily defined using ASN.1). 

So don't worry about the name! For embedded material which is defined as an ASN.1 type you probably want to use the information object-related concepts to handle your holes. But if the material you want to embed is not defined using ASN.1, use EMBEDDED PDV. 

## 5.5 CHARACTER STRING

CHARACTER STRING is actually just a special case of EMBEDDED PDV, and there is a lot of shared text in the specification of these types in the ASN.1 Standard. 

CHARACTER STRING was an (unsuccessful!) attempt to produce a character string type that would satisfy all possible needs FOREVER. It was intended to make it possible for the maintainers of the ASN.1 Standard to say (as new character sets and encodings emerged in the world), "We don't need to change ASN.1, use CHARACTER STRING". 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/8a87220a7125939494262707937b0ea4f8a29ba294678aca25ab014e6e91e448.jpg)


The CHARACTER STRING type extends the concept of abstract and transfer syntax. It introduces the term "character abstract syntax" (an abstract syntax all of whose values are strings of characters from some defined character set), and "character transfer syntax" (a transfer syntax that provides encodings for all possible strings in a given character abstract syntax). 

Put in slightly less technical terms, a character abstract syntax object identifier identifies a character repertoire, and a character transfer syntax OBJECT IDENTIFIER identifies an encoding for strings of those characters. 

Unconstrained, an encoding of the CHARACTER STRING type includes the two object identifiers that identify its character abstract syntax (repertoire) and its character transfer syntax (encoding) with each string that is transmitted. This is an unfortunate(!) overhead, as constructs like 

## SEQUENCE OF CHARACTER STRING

(where the repertoire and encoding are the same for each element of the SEQUENCE OF) are quite common. As with EMBEDDED PDV, however, it is possible to statically constrain the CHARACTER STRING type so that only the actual encodings of characters are transmitted. 

Object identifier values have been assigned for many character repertoires and sub-repertoires, and for many encoding schemes, but unfortunately not for all. UTF8String was added to ASN.1 after CHARACTER STRING. It could have been defined as a constrained CHARACTER STRING, but in fact it was "hard-wired" into ASN.1 as a new type defined using English text, just like PrintableString and IA5String etc! That is why "unsuccessful!" appeared in the second paragraph of this clause. 

## 5.6 OCTET STRING and BIT STRING

Of course, the ultimate blackest of black holes is to use OCTET STRING or BIT STRING to carry embedded material. It happens. You are really "rolling your own". ASN.1 will provide the delimitation (the length wrapper), but you must sort out the problems of identifying to a receiver the semantics of what fills the octet string or bit string hole. 

Those who believe in using a very cut-down ASN.1 use these types for their holes. I guess you can't complain. They make it work. But there are more powerful specification tools available in the ASN.1 armoury, and I hope that anyone that has read this far in this text will not be tempted into use of OCTET STRING or BIT STRING when they need to introduce a hole! 

## 6 Remarks to conclude Section II

I wonder if there is a single reader (even my reviewers!) that can say they read from the start through to here? E-mail me at j.larmouth@iti.salford.ac.uk if you did. (But don't bother if you just jumped around and got here from the index!) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/9d6105f53a7fde328b216adbe3f363451dff946a34c6181a4a2c296b0fec3032.jpg)


This text has tried to cover the whole of the ASN.1 concepts, mechanisms, notation. It is believed to be complete ("ASN.1 Complete" is the title!). There are further sections concerned with encoding rules and history and applications, but the description of the notation itself is now complete. 

Well ... it is complete as of 1999! If you are reading this book in 2010, there might be a later version available which you should get, 'cos there is probably a lot missing in this text! But I can't give you a reference to a later version - try a Web search, and in particular try the URL given in Appendix 5 (which might or might not still work in 2010!). 

At the time of writing, there are quite a lot of suggestions bubbling up in the ASN.1 standardization group that could give rise to additions to the ASN.1 notation. Recent (post-1994) history, however, has been of only introducing changes that clarify existing text or add very minor (from a technical view-point) and simple new functionality (such as UTF8String), not of earthshaking additions. Indeed, possibly earth-shaking additions that have been proposed in the last decade have a history of being abandoned - examples include light-weight encoding rules, global parameters, and dynamic constraints. 

Good luck in reading, writing, or implementing ASN.1 specifications! 

## THE END.

Well ... of this section! 

SECTION III 

Encodings 

# Chapter 1 Introduction to encoding rules

## (Or: What no-one needs to know!)

Summary: This first chapter of Section 3: 

• Discusses the concept of encoding rules. 

• Describes the TLV principle underlying the Basic Encoding Rules (BER). 

• Discusses the question of "extensibility", or "future proofing". 

• Describes the principles underlying the more recent Packed Encoding Rules (PER). 

• Discusses the need for "canonical" encoding rules. 

• Briefly mentions the existence of other encoding rules. 

There has already been some discussion of encoding rules in earlier chapters which can provide a useful introduction to this concept, but this section has been designed to be complete and to be readable without reference to other sections. 

The next two chapters of Section III describe in detail the Basic Encoding Rules and the Packed Encoding Rules, but assume an understanding of the principles and concepts given here. 

## 1 What are encoding rules, and why the chapter sub-title?

"What no-one needs to know!". At the end-of-the-day, computer communication is all about "bits-on-the-line" - what has in the past been called "concrete transfer syntax", but today is just called "transfer syntax". (But if you think about it, a "bit" or "binary digit" is itself a pretty abstract concept - what is "concrete" is the electrical or optical signals used to represent the bits.) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/9844feb9c199bf490625271c9c90f0d00b42d468148271ca9de317c5eacadc87.jpg)


ASN.1 has taken on-board some concepts which originated with the so-called "Presentation Layer" of the ISO/ITU-T specifications for Open Systems Interconnection (OSI). (Note that the term "Presentation Layer" is a bad and misleading one - "Representation Layer" might be better). 

The concepts are of a set of "abstract values" that are sent over a communications line, and which have associated with them bit patterns that represent these abstract values in an instance of communication. 

The set of abstract values to be used, and their associated semantics, is at the heart of any application specification. The "encoding rules" are concerns of the (Re)Presentation Layer, and define the bit patterns used to represent the abstract values. The rules are a complete specification in their own right (actually, there are a number of variants of two main sets of rules - these are described later). The encoding rules say how to represent with a bit-pattern the abstract values in each basic ASN.1 type, and those in any possible constructed type that can be defined using the ASN.1 notation. 

ASN.1 provides its users with notation for defining the "abstract values" which carry user semantics and which are to be conveyed over a communications line. (This was fully described in Sections I and II). Just as a user does not care (and frequently does not know) what electrical or optical signal is used to represent zero and one bits, so in ASN.1, the user should not care (or bother to learn about) what bit patterns are used to represent his abstract values. 

So details of the ASN.1 "encoding rules", which define the precise bit-patterns to be used to represent ASN.1 values, while frightfully important, are "What no-one needs to know". 

It is the case today that there are good ASN.1 tools (called "ASN.1 compilers") available that will map an ASN.1 type definition into a type definition in (for example), the C, C++, or Java programming languages (see Section I Chapter 6), and will provide run-time support to encode values of these data structures in accordance with the ASN.1 Encoding Rules. Similarly, an incoming bit-stream is decoded by these tools into values of the programming language datastructure. This means that application programmers using such tools need have no knowledge of, or even interest in, the encoded bit-patterns. All that they need to worry about is providing the right application semantics for values of the programming language data structures. The reader will find some further discussion of these issues in the Introduction to this book, and in Chapter 1 of Section 1. A detailed discussion of ASN.1 compilers is provided in Chapter 6 of Section 1. 

There are, however, a few groups of people that will want to know all about the ASN.1 Encoding Rules. These are: 

• The intellectually curious! 

• Students being examined on them! 

• Standards writers who wish to be reassured about the quality of the ASN.1 Encoding Rules. 

Implementors who, for whatever reason, are unable to use an ASN.1 compiler (perhaps they are working with an obscure programming language or hardware platform, or perhaps they have no funding to purchase tools), and have to "hand-code" values for transmission and "hand-decode" incoming bit-patterns. 

Testers and trouble-shooters that need to determine whether the actual bit-patterns being transmitted by some implementation are in accordance with the ASN.1 Encoding Rules specification. 

If you fall into any of these categories, read on! Otherwise this section of the book is not for you! 

## 2 What are the advantages of the encoding rules approach?

Section 1 Chapter 1 discussed a number of approaches to specifying protocols. The ASN.1 approach (borrowed from the Presentation Layer of OSI) of completely separating off and "hiding" the details of the bit-patterns used to represent values has a number of advantages which are discussed in the next few paragraphs. 

The first point to note is that a clear separation of the concept of transmitting abstract values from the bitpatterns representing those values enables a variety of different encodings to be used to suit the needs of particular environments. One often-quoted example (but I am not sure you will find it in the real-world!) is of a communication over a high-bandwidth leased line with hardware encryption devices at each end. The main concern here is to have representations of values that impose the least CPU-cycle cost at the two ends. But a 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/0a7afe179e34eeae083d3f3e300250e54851a7856095e5d3f8ae3d4379b9ca3c.jpg)


bull-dozer goes through the leased line! And the back-up provision is a modem on a telephone line with no security device. The concern is now with maximum compression, and some selective field encryption. The same abstract values have to be communicated, but what is the "best" representation of these values has now changed. 

The second example is similar. There are some protocols where a large bulk of information has to be transferred from the disk of one computer system to the disk of another computer system. If those systems are different, then some work will be needed by one or both systems to map the local representations of the information into an agreed (standard) representation for transfer of the values over a communication line. But if, in some instance of communication, the two systems are the same type of system, CPU-cycles can probably be saved by using a representation that is close to that used for their common local representation of the information. 

Both the above examples are used to justify the OSI concept of negotiating in an instance of communication the representation (encoding) to be used, from a set of possible representations. However, today, ASN.1 is more commonly used in non-OSI applications, where the encoding is fixed in advance, and is not negotiable at communications-time (there is no OSI Presentation Layer present). 

There are, however, a few other advantages of this clear separation of encodings from abstract values that are important in the real-world of today for the users of ASN.1. 

We have seen over the last twenty years considerable progress in human knowledge about how to produce "good" encodings for abstract values. This is reflected in the difference between the ASN.1 Basic Encoding Rules developed in the early 1980s and the Packed Encoding Rules developed in the early 1990s. But application specifications defined using ASN.1 in the 1980s require little or no change to the specification to take advantage of the new encoding rules - the application specification is unaffected, and will continue to be unaffected if even better encoding rules are devised in the next century. 

There is a similar but perhaps more far-reaching issue concerned with tools. The separation of encoding issues from the application specification of abstract values and semantics is fundamental to the ability to provide ASN.1 compilers, relieving application implementors from the task of writing (and more importantly, debugging) code to map between the values of their programming language data-structures and "bits-on-the-line". Moreover, where such tools are in use, changing to a new set of encoding rules, such as PER, requires nothing more than the installation of a new version of the ASN.1 compiler, and perhaps the changing of a flag in a run-time call to invoke the code for the new encoding rules rather than the old. 

## 3 Defining encodings - the TLV approach

Chapter 1 of Section 1 discussed briefly the approach of using character strings to represent values, giving rise to a variety of mechanisms to precisely specify the strings to be used, and to "parsing" tools to recognise the patterns in incoming strings of characters. These approaches tend to produce quite verbose protocols, and generally do not give rise to as complete tool support as is possible with ASN.1. They are not discussed further, and we here concentrate on approaches which more directly specify the bit-patterns to be employed in communication. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/021e9a1cb30d6908ea4269ddc56c14d7b8d6f427d60c3e657d1cf303b40d0dff.jpg)


As the complexity of application specifications developed over the years, one important and early technique to introduce some "order" to the task of defining representations was the so-called "TLV" approach. 

With this approach, information to be sent in a message was regarded as a set of "parameter values". Each parameter value was encoded with a parameter identification (usually of fixed length, commonly a single octet, but perhaps overflowing to further octets), followed by some encoding that gave the length (octet count) of the parameter value (again as a single octet with occasionally the need for two or more octets of length encoding), and then an encoding for the value itself as a sequence of octets. 

The parameter id was often said to identify the type of the parameter, so we have a Type field, a Length field, and a Value field, or a TLV encoding. 

In these approaches, all fields were an integral number of octets, with all length counts counting octets, although some of the earliest approaches (not followed by ASN.1) had sixteen bit words as the fundamental unit, not octets. 

Once the way of encoding types and lengths is determined, the rest of the specification merely needs to determine what parameters are to appear on each message, what their exact id is, and how the values are to be encoded. 

This structure has a number of important advantages: 

• It makes it possible to give freedom to a sender to transmit the parameters in any order, perhaps making for simpler (sender) implementation. (Note that this is today seen as actually a bad thing to allow, not a good one!) 

• It makes it possible to declare that some parameters are optional - to be included only when needed in a message. 

• It handles items of variable length. 

• It enables a basic "parsing" into a set of parameter values without needing any knowledge about the actual parameters themselves. 

And importantly - it enables a version 1 system to identify, to find the end of, and to ignore (if that is the desired behaviour), or perhaps to relay onwards, parameters that were added in a version 2 of the protocol. 

The reader should recognise the relationship of these features to ASN.1 - the existence of "SET" (elements transmitted in any order), the "OPTIONAL" notation which can be applied to elements of a SET or SEQUENCE, and the variable length nature of many ASN.1 basic types. The version 1/version 2 issue is what is usually called "extensibility" in ASN.1. 

The major extension beyond this "parameter" concept developed in the late 1970s with the idea of "parameter groups", used to keep close together related parameters. Here we encode a "group identifier", a group length encoding, then a series of TLV encodings for the parameters within the group. As before, the groups can appear in any order, and a complete group may be optional or mandatory, with parameters within that group in any order and either optional or mandatory for that group. Thus we have effectively two levels of TLV - the group level and the parameter level. 

It is a natural extension to allow arbitrarily many levels of TLV, with the V part of all except the innermost TLVs being a series of embedded TLVs. This clearly maps well to the ASN.1 concept of being able to define a new type as a SEQUENCE or SET of basic types, then to use that new type as if it were a basic type in further SEQUENCEs or SETs, and so on to any depth. 

Thus this nested TLV approach emerged as the natural one to take for the ASN.1 Basic Encoding Rules, and reigned supreme for over a decade. 

To completely understand the Basic Encoding Rules we need: 

• To understand the encoding of the "T" part, and how the identifier in the "T" part is allocated. 

• To understand the encoding of the "L" part, for both short "V" parts and for long "V" parts. 

• For each basic type such as INTEGER, BOOLEAN, BIT STRING, how the "V" is encoded to represent the abstract values of that type. 

• For each construction mechanism such as SEQUENCE or SET, how the encodings of types defined with that mechanism map to nested TLV structures. 

This is the agenda for the next chapter. 

## 4 Extensibility or "future proofing"

The TLV approach is very powerful at enabling the specification of a version 1 system to require specified action on TLV elements where the "T" part is not recognised. This allows new elements (with a distinct "T" part) to be added in version 2 of a specification, with a known pattern of behaviour from version 1 systems that receive such material. 

This interworking between version 1 and version 2 systems without the need for version 2 implementations to implement both the version 1 and the version 2 protocol is a powerful and important feature of ASN.1. 

It is a natural outcome of the TLV approach to encoding in the Basic Encoding Rules, but if one seeks encodings where there is a minimal transfer of information down the line, it is important to investigate how to get some degree of "future-proofing" to allow interworking of version 1 and version 2 systems without the verbosity of the TLV approach. 

Early discussions in this area seemed to indicate that future-proofing was only possible if a TLV style of encoding was used, but later work showed that provided the places in the protocol where version 2 additions might be needed were identified by a new notational construct (the ASN.1 "extensibility" ellipsis - three dots), then future-proofing becomes possible with very little overhead even in an encoding structure that is not in any way a TLV type of structure. 

It was this recognition that enabled the so-called Packed Encoding Rules (PER) to be developed. 

## 5 First attempts at PER - start with BER and remove redundant octets

This was a blind-alley! 

NOTE — Those with no knowledge of BER may wish to at lest skim the next chapter before returning to the following text, as some examples show BER encodings. 

The first approach to producing more compact (packed) encodings for ASN.1 was based on a BER TLV-style encoding, but with recognition that in a BER encoding there were frequently octets sent down the line where this was the only possible octet value allowed in this position (at least in this version of the specification). This 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/938407f05197da57daa2b8225483ecf566abb7269a6f32912231a7f5f63bf182.jpg)


applied particularly to the "T" values, but also frequently to the length field if the value part of the item (such as a BOOLEAN value) was fixed length. 

By allowing the Packed Encoding Rules to take account of constraints (on, for example, the length of strings or the sizes of INTEGERs), we can find many more cases where explicit transmission of length fields is not needed, because both ends know the value of the "L" field. 

A final "improvement" is to consider the "L" field for a SEQUENCE type. Here each element of the SEQUENCE is encoded as a TLV, and there is an outer level "TL" "wrapper" for the SEQUENCE as a whole. If we modify BER so that the "L" part of this wrapper is a count not of octets, but of the number of TLVs in the value part of the SEQUENCE, this count is again fixed (unless the SEQUENCE has OPTIONAL elements), and therefore often need not be transmitted, even if there are inner elements whose length might vary. 

Consider the ASN.1 type shown in figure III-1. The BER encoding (modified to count TLVs rather than octets for non-inner length fields) is shown in figure III-2. 

```txt
Example ::= SEQUENCE
{first INTEGER (0..127),
second SEQUENCE
{string OCTET STRING (SIZE(2)),
name PrintableString (SIZE(1..8)) },
third BIT STRING (SIZE (8)) }

Figure III-1: An example for encoding 
```

You will see from Figure III-2 that there are a total of 23 octets sent down the line, but a receiver can predict in advance the value of all but 11 of them - those marked as {????} (and knows precisely where these 11 occur). Thus we need not transmit the remaining 12 octets, giving a 50% reduction in communications traffic. Attractive! 

The approach, then, was to take a BER encoding as the starting point, determine rules for what 

```txt
{U 16} -- Universal class 16 ("T" value for SEQUENCE)
{3} -- 3 items ("L" value for SEQUENCE)
{U 2} -- Universal class 2 ("T" value for "first")
{1} -- 1 octet ("L" value for "first")
{?????} -- Value of "first"
{U 16} -- Universal class 16 ("T" value for "second")
{2} -- 2 items ("L" value for "second")
{U 3} -- Universal class 3 ("T" value for "string")
{2} -- 2 octets ("L" value for "string")
{?????}{?????} -- Value of "string"
{U 24} -- Universal class 24 ("T" value for "name")
{?????} -- 1 to 8 ("L" value for "name" - 5 say)
{?????}{?????}{?????}{?????}{?????} -- Value of "name"
{U 4} -- Universal class 4 "T" value for "third"
{3} -- 3 octets ("L" value for "third")
{0} -- 0 unused bits in last octet of "third" "V"
{?????}{?????} -- Value of "third"

Figure III-2: Modified BER encoding of figure III-1 
```

octets need not be transmitted, and to delete those octets from the BER encoding before transmission, re-inserting them (from knowledge of the type definition) on reception before performing a standard BER decode. 

Work was done on this approach over a period of some three years, but it fell apart. A document was produced, getting gradually more and more complex as additional (pretty ad hoc) rules were added on what could and could not be deleted from a BER encoding, and went for international ballot. An editing meeting was convened just outside New York (around 1990), and the comments from National Bodies were only faxed to participants at the start of the meeting. 

Imagine the consternation when the dozen or so participants realised that EVERY National Body had voted "NO", and, moreover, with NO constructive comments! The approach was seen as too complex, too ad hoc, and (because it still left everything requiring an integral number of octets) insufficient to produce efficient encodings of things like "SEQUENCE OF BOOLEAN". It was quite clearly dead in the water. 

Many people had pre-booked flights which could not be changed without considerable expense, but it was clear that what had been planned as a week-long meeting was over. The meeting broke early at about 11am for lunch (and eventually reconvened late at about 4pm). Over the lunch-break much beer was consumed, and the proverbial back-of-a-cigarette-packet recorded the discussions (actually, I think it was a paper napkin – long since lost!). PER as we know it today was born! The rest of the week put some flesh on the bones, and the next two years produced the final text for what was eventually accepted as the PER specification. Implementations of tools supporting it came a year or so later. 

## 6 Some of the principles of PER

## 6.1 Breaking out of the BER straight-jacket

Probably the most important decisions in that initial lunch-time design of PER were: 

To start with a clean piece of paper (or rather napkin!) and ignore BER and any concept of TLV. This was quite radical at the time, and the beer probably helped people to think the unthinkable! 

## Initial "principles"

• Forget about TLV. 

• Forget about octets - use bits. 

• Recognise constraints (subtypes). 

• Produce "intelligent" encodings. 

• Forget "extensibility" (initially). 

• Not to be constrained to using an integral number of octets - another quite radical idea. 

To take as full account of constraints (subtyping) in the type definition as could sensibly be done. (BER ignored constraints, perhaps largely because it was produced before the constraint/subtype notation was introduced into ASN.1, and was not modified when that notation came in around 1986). 

• To produce the sort of encoding that a (by now slightly drunk!) intelligent human being would produce - this was quite a challenge! 

• Not to consider "extensibility" issues. This was a pragmatic decision that made the whole thing possible over a (long) lunch-time discussion, but of course provision for "futureproofing" had to be (and was) added later. 

So how would you the reader encode things? Whatever you think is the obvious way is probably what PER does! In all the following cases, the "obvious" solution is what PER does. 

What about the encoding of BOOLEAN? Clearly a single bit set to zero or one is the "obvious" solution. 

What about 

INTEGER (0..7) 

and 

INTEGER (8..11) 

Clearly a three-bit encoding is appropriate for the former and a two-bit encoding for the latter. 

© OS, 31 May 1999 

An INTEGER value restricted to a 16-bit range could go into two octets with no length field. 

But what about an unconstrained INTEGER? (Meaning, in theory, integer values up to infinity, and with BER capable of encoding integer values that take millions of years to transmit (even over super- fast lines)? Clearly an "L" will be needed here to encode the length of the integer value (and here you probably want to go for a length count in octets). 

If you have read about the details of BER encodings of "L", you will know that for length counts up to 127 octets, "L" is encoded in a single octet, but that BER requires three octets for "L" once the count is more than 255. In PER, the count is a count of bits, items, or octets, but only goes beyond two octets for counts of 64K or more - a fifty per cent reduction on the size of "L" in many cases compared with BER. 

For virtually all values of an unconstrained INTEGER, we will get a one octet "L" field, followed by the minimum number of octets needed to hold the actual value being sent. This is the same as BER. 

## 6.2 How to cope with other problems that a "T" solves?

So far, no mention has been made of a "T" field for PER. Do we ever need one? There are three main areas in BER where the "T" field is rather important. These are: 

```txt
- Use a "choice-index".
- SET in a fixed order.
- Bit-map for OPTIONAL elements. 
```

• To identify which actual alternative has been encoded as the value of a CHOICE type (remember that all alternatives of a CHOICE are required to have distinct tags, and hence have distinct "T" values). 

• To identify the presence or absence of OPTIONAL elements in a SEQUENCE (or SET). 

• To identify which element of a SET has been encoded where (remember that elements of a SET can be encoded and sent in any order chosen by the sender). 

How to do these things without a "T" encoding for each element? 

To cope with alternatives in a CHOICE, PER encodes a "choice-index" in the minimum bits necessary: up to two alternatives, one bit; three or four alternatives, two bits; five to seven alternatives, three bits; etc. 

At this point we can observe one important discipline in the design of PER. The fieldwidth (in bits) for any particular part of the encoding (in this case the field-width of the choice-index) does not (must not) depend on the abstract value being 

The important field-length principle or rule: Encode into fields of an arbitrary number of bits, but the length of fields must be statically determinable from the type definition, for all values. 

transmitted, but can be statically determined by examining the type definition. Hence it is known unambiguously by both ends of the communication - assuming they are using the same type definition. But there is the rub! If one is using a version 1 type definition and the other a version 2 type definition .... but we agreed not to consider this just yet! 

What about OPTIONAL elements in a SET or SEQUENCE? Again, the idea is pretty obvious. We use one bit to identify whether an OPTIONAL element is present or absent in the value of the 

SET or SEQUENCE. In fact, these bits are all collected together and encoded at the start of the SET or SEQUENCE encoding rather than in the position of the optional element, for reasons to do with "alignment" discussed below. 

And so to the third item that might require a "T". What about the encoding of SET - surely we need the "T" encodings here? Start of big debate about the importance of SET (where elements are transmitted in an order determined by the sender) over SEQUENCE (where the order of encodings is the order of elements in the type definition), and of the problems that SET causes. In addition to the verbosity of introducing some form of "T" encoding, we can also observe that: 

Allowing sender's options produces a combinatoric explosion in any form of exhaustive test sequence (and hence in the cost of conformance checking) to check that (receiving) implementations behave correctly in all cases. 

The existence of multiple ways of sending the same information produces what in the security world is called a "side-channel" - a means of transmitting additional information from a trojan horse by systematically varying the senders options. For example, if there are eight elements in a SET, then 256 bits of additional information can be transmitted with each value of that SET by systematically varying the order of elements. 

This discussion led to the development of a further principle for PER: there shall be NO sender's options in the encoding unless there was an excellent reason 

The sender's options principle/rule: Don't have any! 

for introducing them. PER effectively has no sender's options. A canonical order is needed for transmitting elements of a SET, and after much discussion, this was taken to be the tag order of the elements (see the next chapter for more detail), rather than the textually printed order. (In allocating choice-index values to alternatives of a choice, the same tag-order, rather than textual order is also used, for consistency). 

It should, however, be noted that the term "PER" strictly refers to a family of four closely related encoding rules. The most important is "BASIC-PER" (with an ALIGNED and an UNALIGNED variant discussed later). Although BASIC-PER has no senders options, it is not regarded as truly a canonical encoding rule because values of the elements of a SET OF are not required to be sorted into a fixed order, and no restrictions are placed on the way escape sequences are used in encodings of GeneralString. (If neither of these two types are used in an application specification, then BASIC-PER is almost canonical (there are some other unimportant complex cases that never arise in practice where it is not fully canonical. There is a separate CANONICAL-PER (also with an ALIGNED and an UNALIGNED version) that is truly canonical even when these types are present. 

## 6.3 Do we still need T and L for SEQUENCE and SET headers?

Clearly we do not! We need no header encodings for these types, provided we can identify the presence or absence of optional elements (which is done by the bit-map described earlier). 

"Wrappers" are no longer needed. Well ... that is sort of true - but see the discussion of extensibility below, that re-introduces wrappers for elements added in version 2! 

## 6.4 Aligned and Unaligned PER

But here we look at another feature of PER. Basically, PER produces encodings into fields that are a certain number of bits long and which are simply concatenated end-to-end for transmission. But there was recognition from the start that for some ASN.1 types (for example, a sequence of two-byte integers), it is silly to start every component value at, say, bit 6. Insertion of two padding bits at the start of the sequence-of value 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/99cf5af4eaf50b4889c4973c4c6732e5f3d368823905c2a328c76facc36f0a78.jpg)


would probably be a good compromise between CPU costs and line costs. 

This led to the concept of encoding items into bit-fields (which were simply added to the end of the bits in earlier parts of the encoding) or into octet-aligned-bit-fields where padding bits were introduced to ensure that the octet-aligned-bit-fields started on an octet boundary. 

The intelligent reader (aren't you all?) will note that whilst the length of fields is (has to be) statically determined from the type, the number of padding bits to be inserted before an octetaligned-bit-field is not fixed. The number of bits in the earlier part of the encoding can depend on whether optional elements of SET and SEQUENCE are present or not, and on the actual alternative chosen in a CHOICE. But of course, the encoding always contains information about this, and hence a receiving implementation can always determine the number of padding bits that are present and that have to be ignored. Notice that whether a field is a bit-field or an octetaligned-bit-field again has to be (and is) statically determined from the type definition - it must not depend on the actul value being transmitted, or PER would be bust! 

The concept of "octet-aligned-bit-fields" and "padding bits" was in the original design, but later people in air traffic control wanted the padding bits removed, and we now have two variants of PER. Both formally encode into a sequence of "bit-fields" and "octet-aligned-bit-fields", depending on the type definition, but for "unaligned PER", there is no difference in the two - padding bits are never inserted at the start of "octet-aligned-bit-fields". With aligned PER, they are. 

There are actually a couple of other differences between aligned and unaligned PER, but these are left to the later chapter on PER for details. 

As a final comment - if you want to try to keep octet alignment for as long as possible after insertion of padding bits, then using a single bit to denote the presence or absence of an OPTIONAL element in a SEQUENCE or SET is probably not a good idea - better to collect all such bits together as a "bit-map" at the start of the encoding of the SEQUENCE or SET. This was part of the original back-of-cigarette-packet design and was briefly referred to earlier. That feature is present in PER. 

## 7 Extensibility - you have to have it!

## Third attempt!

One bit says it all - it is a version 1 value, or it contains wrapped-up version 2 material. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/3d6b16fc2ed327099aecaadc051730f4a50279d15e1f88e463f5b2c8a1dbef26.jpg)


When the second approach to better encodings (described above) was balloted internationally, it almost failed again. 

It is clear from the above discussion that unless both ends have exactly the same type definition for their implementation, all hell will break loose - pardon the term. They will have different views on the fields and the field lengths that are present, and will produce almost random abstract values from the encodings. 

But do we really want to throw in the towel and admit that a very verbose TLV style of encoding is all that is possible if we are to be "future-proof"? NO! 

How to allow version 2 to add things? How about notation to indicate the end of the "root" (version 1) specification, and the start of added version 2 (or 3 etc) material? Will this help? 

The most common case for requiring "extensibility" is the ability to add elements to the end of SETs and SEQUENCEs in version 2. 

Later, people argued - successfully - for the need to add elements in the middle of SETs and SEQUENCEs, and we got the "insertion point" concept described in an earlier Section. 

But let's stick to adding at the end for now. Suppose we have added elements (most of which are probably going to be OPTIONAL) at the end of a SEQUENCE, or added alternatives in a CHOICE, or added enumerations in an ENUMERATED, or relaxed constraints on an INTEGER (that list will do for now!). 

How to handle that? We first require that a type be marked "extensible" if we want "futureproofing" (this is the ellipsis that can appear in many ASN.1 types). This warns the version 1 implementation that it may be hit with abstract values going beyond the version 1 type, but more importantly, it introduces one "extended" bit at the head of the version 1 encodings of all values of that type. 

The concept is that any of these "extensible" types has a "root" set of abstract values - version 1 abstract values. If the abstract value being sent (by a version 1, version 2, or version 3, etc implementation) is within the root, the "extended" bit is set to zero, and the encoding is purely the encoding of the version 1 type. But if it is set to 1, then abstract values introduced in version 2 or later are present, and version 1 systems have a number of options, but importantly, extra length (and sometimes identification) fields are included to "wrap-up" parts or all of these new abstract values to enable good interworking with version 1 systems. The "exception marker" enables specifiers to say how early version systems are to deal with material that was added in later versions, and (in the views of this author) should always be included if the extensibility marker is introduced. 

The exact form of encodings for "extensible" types is discussed in more detail in the PER chapter following. later in this section. 

## 8 What more do you need to know about PER?

It is interesting to note that whilst PER is now defined without any reference to BER (except for encoding the value part of things like object identifiers and generalizedtime and real types), a PER encoding of a value of the type shown in Figure III-1 actually produces exactly the same 11 octets (shown in Figure III-2) that would have been produced in the earlier (abandonned) approach! 

This chapter has introduced most of the concepts of PER, but there are rather more things to learn about PER than about BER. These are all covered in the next chapter-but-one. 

You need to know (well, you probably don't, unless you are writing an ASN.1 compiler tool! See the first part of this chapter!): 

• What constraints (subtyping) affect the PER encoding of various types (these are called "PER-visible constraints"). 

• What is the general structure of the encoding ("bit-fields" and "octet-aligned-bit-fields", and how is a "complete encoding" produced. 

• When are length fields included, and when are "lengths of lengths" needed, and how are they encoded. 

• How PER encodes SEQUENCEs, SETs, and CHOICEs. (You already have a good idea from the above text). 

• How PER encodes all the other ASN.1 types. (Actually, it references the BER "V" part encoding a lot of the time.) 

• How does the presence of the "extensibility marker" affect PER encodings. (Again, the above has given some outline of the effect - a one-bit overhead if the abstract value is in the root, and generally an additional length field if it is not. 

These are all issues that have been touched on above, but which are treated more fully later. 

## 9 Experience with PER

There is now a lot of experience with PER applied to existing protocol specifications, and there is a growing willingness among specifiers to produce PER-friendly specifications (that is, specifications where constraints are consistently applied to integer fields and lengths of strings where appropriate). 

Bandwidth reductions (even with added general-purpose compression - surprise?). CPU-cycle reductions (real surprise). Complexity - only at analysis time! Relation to use of tools - increases the advantages of tools. 

There were some surprises when PER implementations started to become available. 

First of all, it became possible to apply general-purpose compression algorithms to both the BER and the PER encodings of existing protocols, and it turned out that such compression algorithms produced about a 50% reduction in BER encodings (known for a long-time), but also produced a 50% reduction in PER encodings, which (uncompressed) turned out to be about a 50% reduction of the uncompressed BER encodings. Interesting! 

If you apply Shannon's information theory, it is perhaps not quite so surprising. A BER encoding more or less transmits complete details of the ASN.1 type as well as the value of that type. PER transmits information about only the value, assuming that full details of the type are already known at both ends. So an uncompressed PER encoding carries less information, and can be expected to be smaller than, an uncompressed BER encoding, but the same statement applies to compressed versions of these encodings. This is borne out in practice. 

<table><tr><td colspan="2">SEQUENCE</td></tr><tr><td>{ firstfield</td><td>INTEGER (0..7),</td></tr><tr><td>secondfield</td><td>BOOLEAN,</td></tr><tr><td>thirdfield</td><td>INTEGER (8..11),</td></tr><tr><td>fourthfield</td><td>SEQUENCE</td></tr><tr><td>{fourA</td><td>BOOLEAN,</td></tr><tr><td>fourB</td><td>BOOLEAN}</td></tr></table>

Secondly - and this WAS a surprise to most ASN.1 workers - the number of CPU cycles needed to produce an ASN.1 PER encoding proved to be a lot LESS than those required to produce an ASN.1 BER encoding (and similarly for encoding). Why? Surely PER is more complex? 

It is true that to determine the encoding to produce (what constraints apply, the field-widths to use, whether a length field is needed or not) is much more complex for PER than for BER. But that determination is static. It is part of generating (by hand or by an ASN.1 "compiler") the code to do an encoding. 

At encode time, it is far less orders to take an integer from memory, mask off the bottom three bits, and add them to the encoding buffer (that is what PER needs to do to encode a value of "INTEGER (0..7)") than to generate (and add to the encoding buffer) a BER "T" value, a BER "L" value (which for most old BER implementations means testing the actual size of the integer value, as most old BER implementations ignored constraints), and then an octet or two of actual value encoding. Similarly for decoding. 

There is a further CPU-cycle gain in the code handling the lower layers of the protocol stack, simply from the reduced volume of the material to be handled when PER is in use. 

So PER seems to produce good gains in both bandwidth and CPU cycles, even for "old" protocols. Where a specification tries to introduce bounds on integers and lengths, where they are sensible for the application, the gains can be much greater. Also protocols that have a lot of boolean "flags" benefit heavily. Figure III-3 shows a (slightly artificial!) SEQUENCE type for which the BER encoding is 19 octets and the PER encoding a single octet! 

There is a view in the implementor community that use of PER requires the use of a tool to analyze the type definition, determine what constraints affect the encoding (and follow possibly long chains of parameterization of these constraints if necessary), in order to generate correct code for use in an instance of communication to encode\decode values. 

There is no doubt that it is easier to make mistakes in PER encoding/decoding by hand than with BER. The PER specification is more complex, and is probably less easy to understand. (If you want my honest opinion, it is actually less well-written than the BER specification! Mea Culpa!) 

All these points increase the importance of using a well-debugged tool to generate encodings rather than trying to do it by hand. But hand-encodings of PER do exist, and are perfectly possible - but be prepared to put a wet-towel over your head and drink lot's of coffee! And importantly to test against encodings/decodings produced using a tool. These points also apply to hand-encoding of BER, but to a much lesser extent. 

## 10 Distinguished and Canonical Encoding Rules

We have observed earlier that encoding rules in which there are no options for the encoder are a good thing. 

Encodings produced by such encoding rules are usually called "distinguished" or "canonical" encodings. At this level (no capitals!) the two terms are synonymous! 

<table><tr><td>Your job is to produce Standards. If you can&#x27;t agree, make it optional, or better still another Standard. After all, if one Standard is good, many Standards must be better!</td></tr></table>

However, if options are introduced (such as the indefinite and definite length encodings in BER - see the next chapter) because you cannot agree, how do you agree on encoding rules with all options removed? The answer is two Standards! The Basic Encoding Rules come in three variants: 

• BER - which allows options for the encoder. 

• DER (Distinguished Encoding Rules) - which resolves all options in a particular direction. 

• CER (Canonical Encoding Rules) - which resolves all options in the other direction! 

It is arguably the case that CER is technically superior, but there is no doubt that DER has become the de facto distinguished/canonical encoding for BER. 

When we come to PER, the term "distinguished" is not used, but there is defined a BASIC-PER and a CANONICAL-PER with both aligned and unaligned versions as described ealier. 

We mentioned earlier the problem with encodings of the "SET OF xyz" type. (There are also problems with the encoding of GraphicString and GeneralString that are discussed in the later chapters). In a formal sense, the order of the series of "xyz" encodings that are being sent has no significance at the abstract level (it is a SET, not a SEQUENCE), so the order of encodings is clearly a senders option. To determine a single "canonical" encoding for the values of this type requires that the series of "xyz" encodings be SORTED (based on the binary value of each of these encodings) into some defined order. This can put a very significant load on CPU cycles, and also on "disk-churning", and is not something to be lightly entered into! 

So "normal PER" is not strictly-speaking canonical if a specification contains uses of "SET OF" (although there are those that would argue that we get into "how many angels can sit on the end of a pin" issues here). 

"Canonical PER" specifies sorting of the "xyz" encodings to produce a truly one-to-one mapping of an (unordered) set of values into bitstrings, each bitstring representing one possible set of (unordered) values of the type "xyz". 

Author's opinion: I know of no applications where this degree of formality or precision matters. CANONICAL-PER is basically not a good idea, but neither is the use of "SET OF" in specifications! Try to avoid both. (Others may not agree!) 

## 11 Conclusion

This chapter has provided an introduction to the ASN.1 Basic Encoding Rules and the ASN.1 Packed Encoding Rules, showing their approach to encodings and their relative advantages and disadvantages. 

It has also discussed issues of extensibility or "future-proofing", and mentioned canonical/distinguished encoding rules. 

The chapter has formed a basic introduction to the detailed, factual (and dry!) description of BER and of PER in the next two chapters. 

Readers may also have heard of ASN.1 Encoding Rules with names like "Minimum Bit Encoding Rules" (MBER), "Lightweight Encoding Rules" (LWER), "Clear text encoding rules", "BACNet Encoding Rules", "Session Layer Encoding Rules" and perhaps others. These represented attempts (sometimes outside the standards community, sometimes within it) to develop other Encoding Rules for ASN.1 that might be superior to both BER and PER in some circumstances (or which were partial early attempts to move towards PER). None of these is regarded as important today for general use with ASN.1, but these are discussed a little further in the fourth (short) chapter of this section. 

# Chapter 2 The Basic Encoding Rules

## (Or: Encodings for the 80s - simple, robust, but inefficient!)

Summary: This chapter provides details of the Basic Encoding Rules. It describes: 

• The form of the T part of a TLV encoding (the identifier octets), including the primitive/constructed bit. 

The short, definite, and indefinite forms of encoding for the L part of the TLV (the length octets). 

• The V part of the TLV encoding (the contents octets) for each of the primitive types, taken roughly in order of increasing complexity. 

• The encoding of the constructed types (such as SET and SEQUENCE) 

The encoding of remaining types, such as the character string and time types and types that represent "holes" of various sorts. 

## 1 Introduction

The TLV principles underlying BER encodings have been extensively introduced in earlier chapters, and the reader should have little difficulty in going to the actual Standard/Recommendation for authoritative details. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/e0dd100192e597fa60c073bdfbd69bc36fac8b1bc5977b80a130cadf056e40ef.jpg)


For completeness, however, this chapter provides examples of all the encodings, and gives some further explanation in a few cases. 

## 2 General issues

## 2.1 Notation for bit numbers and diagrams

One of the problems with encoding specifications in the late 1970s was that the bits of an octet were sometimes numbered from left to right in diagrams, sometimes the other way, and sometimes the most significant bit was shown at the right, and sometimes at the left. The order of octet transmission from diagrams could also be right to left in some specifications and left to right in others. Naturally there was often confusion! 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/24a1406f6817a65a44e83d3c35a86e4935de902fbbb344ed82659f4e63a90d7b.jpg)


In the case of ASN.1 (and this book), we show the first transmitted octet to the left (or above) later transmitted octets, and we show each octet with the most significant bit on the left, with bit numbers running from 8 (most significant) to 1 (least significant) as shown in Figure III-4. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/fa9d6e223841698f52d2ead9321da83934a74e341bf821744cb77903a064555a.jpg)


Whether within an octet the most or least significant bit is transmitted first (or the bits are transmitted in parallel) is not prescribed in ASN.1. This is determined by the carrier protocols. On a serial line, most significant first is the most common. It is the terms "most significant bit" and "least significant bit" that link the ASN.1 specifications to the lower layer carrier specifications for the determination of the order of bits on the line. 

The order of octets on the line is entirely determined by ASN.1. When encoding a multi-octet integer value, ASN.1 specifies that the most significant octet of the value is transmitted first, and hence is shown in diagrams in the standard (and in this book) as the left-most octet of the value (see the encoding of the integer type later in this chapter). 

## 2.2 The identifier octets

Every ASN.1 type has a tag of one of four classes, with a number for the tag, as discussed earlier. In the simplest case these values are encoded in a single octet as shown in Figure III-5. 

<table><tr><td>First the T part, encoding the tag value.</td></tr></table>

We see that the first two bits encode the class as follows: 

<table><tr><td>Class</td><td>Bit 8</td><td>Bit 7</td></tr><tr><td>Universal</td><td>0</td><td>0</td></tr><tr><td>Application</td><td>0</td><td>1</td></tr><tr><td>Context-specific</td><td>1</td><td>0</td></tr><tr><td>Private</td><td>1</td><td>1</td></tr></table>

<table><tr><td>Class</td><td>P/C</td><td>Number</td></tr></table>


Figure III-5: Encoding of the identifier octet (number less than 31)


The next bit (bit six) is called the primitive/constructed (P/C) bit, and we will return to that in a moment. 

The last five bits (bits 5 to 1) encode the number of the tag. Clearly this will only cope with numbers that are less than 32. In fact, the value 31 is used as an escape marker, so only tag numbers up to 30 encode in a single octet. 

For larger tag values, the first octet has all ones in bits 5 to 1, and the tag value is then encoded in as many following octets as are needed, using only the least significant seven bits of each octet, and using the minimum number of octets for the encoding. The most significant bit (the "more" bit) is set to 1 in the first following octet, and to zero in the last. This is illustrated in Figure III-6. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/b3106c91de051193a4a462381e280177a69b450a48f03688488bfd7a910b644f.jpg)



Figure III-6: Encoding of the identifier octets (numbers greater than 30)


Thus tag numbers between 31 and 127 (inclusive) will produce two identifier octets, tag numbers between 128 and 16383 will produce three identifier octets. (Most ASN.1 specifications keep tag numbers below 128, so either 1 identifier octet - most common - or two identifier octets is what you will normally see, but I have seen a tag number of 999!. 

What about the primitive/constructed bit? This is required to be set to 1 (constructed) if the V part of the encoding is itself a series of TLV encodings, and is required to be set to 0 (primitive) otherwise. Thus for the encoding of an integer type or boolean type (provided any tagging was implicit), it is always set to 0. For the encoding of a SET or SET-OF etc, it is always set to 1. In these cases it is clearly redundant, provided the decoder has the type definition available. 

But having this bit present permits a style of decoding architecture in which the incoming octetstream is first parsed into a tree-structure of TLV encodings (with no knowledge of the type definition), so that the leaves of the tree are all primitive encodings. The tree is then passed to code that does know about the type definition, for further processing. 

There is, however, a rather more important role for this bit. As we will see later, when transmitting a very long octet string value (and the same applies to bit string and character string values), ASN.1 permits the encoder to either transmit as the entire V part the octets of the octet string value (preceded by a length count), or to fragment the octet string into a series of fragments which are each turned into TLV encodings which then go into the V part of the main outer-level encoding of the octet string value. Clearly a decoder needs to know which option was taken, and the primitive/constructed bit tells it precisely that. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/2fc52f8237440683c5c30a222660246fefcc0e3e6d23dc6f3176e708bf9b65aa.jpg)


Why is fragmentation in this way useful? This will become clearer in the next Clause, when we consider the form of the "L" encoding, but the problem is roughly as follows. 

If our V part is primitive, clearly all possible octet values can appear within it, and the only mechanism that ASN.1 provides for determining its length is to have an explicit count of octets in the "L" part. For extremely long octet values, this could mean a lot of disk churning to determine the exact length (and transmit it) before any of the actual octets can be sent. If however, the V part is made up of a series of TLVs, we can find ways of terminating that series of TLVs without an up-front count, so we can transmit octets from the value as they become available, without having to count them all first. 

## 2.3 The length octets

There are three forms of length encoding used in BER, called the short form, the long form, and the indefinite form. It is not always possible to use all three forms, but where it is, it is an encoder's option which to use. This is one of the main sources of optionality in BER, and the main area that canonical/distinguished encoding rules have to address. 

## 2.3.1 The short form

Now the L part - three forms are available in general, sometimes only two, and occasionally only one. The encoder chooses the one to use. 

This is illustrated in Figure III-7. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/f4cfb5d8662b3b5660db71ab31e0bc2c4a9f7521a32cf836a3aead5529acb77c.jpg)


The short form can be used if the number of octets in the V part is less than or equal to 127, and can be used whether the V part is primitive or constructed. This form is identified by encoding bit 8 as zero, with the length count in bits 7 to 1 (as usual, with bit 7 the most significant bit of the length). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/f0602d0c4f4636f3b6c16069c1444375f65a49db4cd78553bf4256c6c4cd1e32.jpg)


## 2.3.2 The long form

If bit 8 of the first length octet is set to 1, then we have the long form of length. This form can be used for all types of V part, no matter how long or short, no matter whether primitive or constructed. In this long form, the first octet encodes in its remaining seven bits a value N which is the length of a series of octets that themselves encode the length of the V part. This is shown in Figure III-8. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/4eee760be8638cdd607c45a3190970899dae892c9d90c2ff59c79c1b3b417064.jpg)


There is no requirement that the minimum number of octets be used to encode the actual length, so all the length encodings shown in Figure III-9 are permitted if the actual length of the V part is 5. 

This was actually introduced into ASN.1 in the early 1980s just before the first specification was finalised (early drafts required length encodings to be as small as possible). It was introduced because there were a number of implementors that wanted N to have a fixed value (typically 2), then the N (2) octets that would hold the actual length value, then the V part. There are probably still BER implementations around today that always have three length octets (using the long form encoding), even where one octet (using the short form encoding) would do. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/40c7ac8b33e789580fc9c48d0e8b14b6097b22af0b42ee979144020c7895fec9.jpg)



Figure III-9: Options for encoding a length of 5


There is a restriction on the first length octet in the long form. N is not allowed to have the value 127. This is "reserved for future extensions", but such extensions are now highly unlikely. If you consider how long the V part can be when N has the maximum value of 126, and how large an integer value such a V part can hold, you will find that the number is greater than the number of stars in our galaxy. It was also calculated that if you transmit down a line running at one tera-bit per second the longest possible V part, it would take one hundred million years to transmit all the octets! So there is no practical limit imposed by BER on the size of the V part, or on the value of integers. 

## 2.3.3 The indefinite form

The indefinite form of length can only be used (but does not have to be) if the V part is constructed, that is to say, consists of a series of TLVs. (The length octets of each of these TLVs in this contained series can independently be chosen as short, definite, or indefinite where such choices are available - the form used at the outer level does not affect the inner encoding.) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/e2ad1a0b0bca9d08fbbe1d79711756dec8077610f64880925012a2aef3875d0a.jpg)


In the indefinite form of length the first bit of the first octet is set to 1, as for the long form, but the value N is set to zero. Clearly a value of zero for N would not be useful in the long form, so this serves as a flag that the indefinite form is in use. Following this single octet, we get the series of TLVs forming the V part, followed by a special delimiter that is a pair of zero octets. 

This is shown in Figure III-10. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/7bab9cc570e56ea51cfb1a7cebca15785b4396923be116508d4ad85a877712ef.jpg)



Figure III-10: An indefinite length encoding


How does this work? The most important thing to note is that a decoder is processing the series of TLVs, and when it hits the pair of zero octets it will interpret them as the start of another TLV. So let us do just that. The zero T looks like a primitive encoding (bit six is zero) with a tag of UNIVERSAL class ZERO, and a definite form length encoding of zero length (zero octets in the V part). 

If you now refer back to the assignment of UNIVERSAL class tags given in Figure II-7, you will see that UNIVERSAL class zero is "Reserved for use by Encoding Rules" (and remember that users are not allowed to assign UNIVERSAL class tags). So a pair of zero octets can never appear as a TLV in any real encoding, and this "special" TLV can safely be defined by BER as the delimiter for the series of TLVs in the V part of an indefinite form encoding. 

We have said earlier that, within an indefinite form TLV we may have inner TLVs that themselves are constructed and have an indefinite form of length. There is no confusion: a pair of zero octets (when a TLV is expected) terminates the innermost "open" indefinite form. 

## 2.3.4 Discussion of length variants

Why do we need so many different variants of length? Clearly they all have some advantages and disadvantages. The short form is the briefest when it can be used, the long form is the only one that can handle very large primitive encodings, and seems to many to be intuitively simpler than the indefinite form. The indefinite is the only one which allows very large OCTET STRING values or SEQUENCE OF values to be transmitted without counting the number of octets in the value before starting. 

The disadvantage of having three options is the extra implementation complexity in decoders, and the presence of encoding options creating side-channels and extra debugging effort. If we want to remove these options, then we have to either say "use indefinite length form whenever possible" (and make statements about the size of fragment to use when fragmenting an octet string), or to say "use short form where possible, otherwise use long form with the minimum value of N needed for the count". Both of these approaches are standardised! The distinguished/canonical encoding rules that take the former approach are called the Canonical Encoding Rules (CER), and those that take the latter approach are called the Distinguished Encoding Rules (DER). Applications with requirements for canonical/distinguished encoding rules will mandate use of one of these in the application specification. 

## 3 Encodings of the V part of the main types

In the examples for this clause we use the ASN.1 value notation to specify a value of a type, and then show the complete encoding of that value using hexadecimal notation for the value of each octet. 

The primary focus here is to illustrate the encoding of the V part for each type, but it must be remembered that there will be other permissible length encodings in addition to the one illustrated (as discussed earlier), and that if implicit tagging were to be applied, the T part would differ. 

<table><tr><td>Encoding the V part is specific to each type. In many cases it is obvious, but the majority of types throw up problems which produce a little complexity in the encoding.</td></tr></table>

The encoding of each of the following types is always primitive unless stated otherwise. The types are taken roughly in ascending order of complexity! 

## 3.1 Encoding a NULL value

Utterly simple! 

The value of 

$$
\text { null   NULL }: := \text { NULL }
$$

(the only value of the NULL type) is encoded as 

<table><tr><td></td><td>T</td><td>L</td><td>V</td></tr><tr><td>null:</td><td>05</td><td>00</td><td>empty</td></tr></table>

Note that whilst we have described our structure as TLV, it is (as in this case) possible for there to be zero octets in the V part if the length is zero. This can arise in cases other than NULL. So for example, a SEQUENCE OF value with an iteration count of zero would encode with an L of zero. Similarly a SEQUENCE, all of whose elements were optional, and which in an instance of communication were all missing, would again encode with an L of zero. 

## 3.2 Encoding a BOOLEAN value

The values of 

<table><tr><td>boolean1</td><td>BOOLEAN ::= TRUE</td></tr><tr><td>boolean2</td><td>BOOLEAN ::= FALSE</td></tr></table>

<table><tr><td>Still pretty obvious, but we now have encoders options!</td></tr></table>

are encoded as 

<table><tr><td></td><td>T</td><td>L</td><td>V</td></tr><tr><td>boolean1:</td><td>01</td><td>01</td><td>FF</td></tr><tr><td>boolean2:</td><td>01</td><td>01</td><td>00</td></tr></table>

For the value TRUE, an encoding of hex FF is shown. This is the only permissible encoding in DER and CER, but in BER any non-zero value for the V part is permitted. 

## 3.3 Encoding an INTEGER value

A two's complement encoding of the integer values into the smallest possible V part is specified. When two's complement is used "smallest possible" means that the first (most significant) nine bits of the V part cannot be all zeros or all ones, but there will be values that will encode with the first eight bits all zeros or ones. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/33b375164fb43da3eec7e3613c8bdf06e9cb0c08d5a209618aac4a49444a43e1.jpg)


Note that it would in theory have been possible to use an L value of zero and no V part to represent the integer value zero, but this is expressly forbidden by BER - there is always at least one octet in the V part. 

Thus the values of 

<table><tr><td>integer1</td><td>INTEGER ::= 72</td></tr><tr><td>integer2</td><td>INTEGER ::= 127</td></tr><tr><td>integer3</td><td>INTEGER ::= -128</td></tr><tr><td>integer4</td><td>INTEGER ::= 128</td></tr></table>

are encoded as 

<table><tr><td></td><td>T</td><td>L</td><td>V</td></tr><tr><td>integer1</td><td>02</td><td>01</td><td>48</td></tr><tr><td>integer2</td><td>02</td><td>01</td><td>7F</td></tr><tr><td>integer3</td><td>02</td><td>01</td><td>80</td></tr><tr><td>integer4</td><td>02</td><td>02</td><td>0080</td></tr></table>

If the integer type was defined with a distinguished value list, this does not in any way affect the encoding. 

## 3.4 Encoding an ENUMERATED value

The definition of an enumerated type may include integer values to be used to represent each enumeration during transfer, or (post 1994) may allow those values to be automatically assigned in order from zero. In the latter case all such values will be positive, but in the general case a user is allowed to assign negative values for 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/d3083e03bbd7a1e050a8ab11ad71d9c94ab0ed6920359aa8aa65fa2b7b781a1e.jpg)


enumerations (nobody ever does). BER takes no account of the (common) case where all associated values are positive: the encoding of an enumerated value is exactly the same as the (two's complement) encoding of the associated integer value (except that the tag value is different of course). 

In practice, this only makes an efficiency difference if there are more than 127 enumerations, which is rare. 

## 3.5 Encoding a REAL value

The encoding of a real value is quite complex. First of all, recall that the type is formally defined as the set of all values that can be expressed base 10, together with the set of all possible values that can be expressed base 2, even if these are the same numerical value. This means that different 

Forget about floating point format standards. What matters is how easily you can encode/decode with real hardware. 

encodings are applied to these two sets of values, and the application may apply different semantics. (There is one exception to this - the value zero has just one encoding, zero octets in the V part.) For base 10 values, the encoding is character-based, for base 2 values, it is binary floating point. 

There are also two further values of type REAL - PLUS-INFINITY and MINUS-INFINITY, with their own special encodings. 

Note that it is possible to subtype type REAL to contain only base 10 or base 2 values, effectively giving the application designer control over whether the character-based encoding or the binarybased encoding of values of the type are to be used. 

## 3.5.1 Encoding base 10 values

If the (non-zero) value is base 10, then the contents octets (the V part) start with one octet whose first two bits are 00 (other values are used for the base 2 values and the special values PLUS-INFINITY and MINUS-INFINITY). Octets after this initial octet are a series of ASCII characters (8 bits 

A character encoding base 10 is available. (But not much used!) 

per character) representing digits 0 to 9, space, plus sign, minus sign, comma or full-stop (for "decimal mark"), and capital E and small e (for exponents), in a format defined in the ISO Standard 6093. This standard has a lot of options, and in particular defines "Numerical Representation 1" (NR1), NR2, and NR3. Which of these is used is coded as values 1, 2, or 3 respectively into the bottom six bits of the first contents octet. Even within these representations, there are many options. In particular, arbitrary many leading spaces can be included, plus signs are optional, and so on. 

When used with DER and CER (and all versions of PER), options are restricted to NR3, spaces and leading zeros are in general forbidden, the full-stop has to be used for any "decimal mark", and the plus sign is required for positive values. The mantissa is required to be normalised so that there are no digits after the "decimal mark". In each case below, the second column shows the way the same real value would be encoded in DER/CER/PER. 

We will not attempt here a detailed description of ISO 6093, but give below some examples of the resulting strings. Note that whilst there may be leading spaces, there are never trailing spaces. There may also be leading zeros and trailing zeros. 

NR1 encodes only simple whole numbers (no decimal point, no exponent). Here are some examples of NR1 encodings, where # is used to denote the space character: 

<table><tr><td>4902</td><td>4902.E+0</td></tr><tr><td>#4902</td><td>4902.E+0</td></tr><tr><td>###0004902</td><td>4902.E+0</td></tr><tr><td>###+4902</td><td>4902.E+0</td></tr><tr><td>-004902</td><td>-4902.E+0</td></tr></table>

NR2 requires the presence of a "decimal mark" (full-stop or comma as an encoders option). Here are some examples of NR2 encodings: 

<table><tr><td>4902.00</td><td>4902.E+0</td></tr><tr><td>###4902,00</td><td>4902.E+0</td></tr><tr><td>000.4</td><td>4.E-1</td></tr><tr><td>#.4</td><td>4.E-1</td></tr><tr><td>4.</td><td>4.E+0</td></tr></table>

NR3 extends NR2 by the use of a base 10 exponent represented by a capital E or lower case e. Examples of NR3 are: 

## 3.5.2 Encoding base 2 values

NOTE — For a full understanding of this material the reader will need some familiarity with the form of computer floating point units - something assembler language programmers of the 1960s were very familiar with, but something today's programmers can usually forget about! You may want to skim this material very quickly, or even totally ignore it. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/c9a47fe5fef77e24f4015a1ed604bd5ff04bc09295cfa833e3811bff3d1ff07a.jpg)


Base 2 values are encoded in a form that is similar to the floating point formats used when a computer system dumps the contents of a floating point unit into main memory. We talk about the mantissa (M), the base (B) and the exponent (E) of the number. 

However, in real floating point units, the base may be either 2, 8 or 16 (but is fixed for that hardware). In an ASN.1 encoding, the value of B has to be sent. This is done in the first contents octet. We then need the value of the exponent for this numerical value, and of the mantissa. 

Let us look at the first contents octet in the case of base 2 values (recall that the first contents octet for base 10 values started 00 and then encoded NR1, NR2, or NR3). This first content octet is illustrated in Figure III-11. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/ec66448663891fc77681e68455b96759a571162d7820aea3779c56cd5e78851a.jpg)



Figure III-11: Encoding of the first contents octet of a base 2 real value


The first bit (bit 8, most significant) is set to 1 to identify this as a base 2 value. The next bit (S) is the sign of the number, with the mantissa represented (later) as a positive integer value. The next two bits (B) encode the base (2, 8, or 16, with the fourth value reserved for future use). The next two bits encode a "scaling factor" value called F, restricted to values 0 to 3, and the final two bits encode the length (LE) of the exponent encoding (the exponent is encoded as a two's complement integer value immediately following this initial octet). The four values of LE allow for a one octet, two octet, or three octet exponent, with the fourth value indicating that the exponent field starts with a one octet length field, then the exponent value. Following the encoding of the exponent field we get the mantissa (M) as a positive integer encoding, terminated by the end of the contents octets (V part) in the usual way. 

The actual value of the real number encoded in this way is: 

$$
\texttt {S x M x (2 * *} \texttt {F) x (B * *} \texttt {E)}
$$

where ** above denotes exponentiation and x denotes multiplication. 

This is a fairly familiar way to represent floating point numbers, apart from the presence of F. We also need to discuss a little more the use of sign and magnitude instead of a 2's complement (or even 1's complement) mantissa. 

In the early 1980s, there was very considerable variation in the form of floating point units, even within a single computer manufacturer, and although there are now de jure standards for floating point representation, there is in practice still a wide de facto variation. 

What has to be achieved (and was achieved) in the ASN.1 encoding of real is a representation that makes it (fairly) easy and quick for any floating point architecture to encode or decode values. 

Consider the choice between sign and magnitude or two's complement for the mantissa. If your actual hardware is two's complement, you can easily test the number and set the S bit, then negate the number, and you have a sign and magnitude format. If, however, your hardware was sign and magnitude and you are asked to generate a two's complement representation for transfer, the task is much more difficult. It is clear then that sign and magnitude is right for transfer, no matter which type of machine is most common. 

The scaling factor F is included for a similar reason. All mantissa's have an implied decimal point position when the floating point value is dumped into main memory, but this is frequently not at the end of the mantissa field, that is, the mantissa is not naturally considered as an integer value. However, it is an integer value we wish to transfer in the ASN.1 encoding, and rather than try to encode the position of the implied decimal point, instead we recognise that the implied point can be moved one place to the right if we subtract one off the exponent value (for base 2). If the base is 8, one off the exponent value moves the implied decimal point three places right, and base 16 four places. Thus with a fixed (for this hardware) decrement to the exponent, we can get the implied decimal point close to the end of the mantissa. In particular, to within three positions of the end for a base 16 machine. By encoding an F value (which again is fixed for any given hardware), we can move the implied decimal point the remaining zero to three bits to get it exactly at the end. Of course a decoder has to multiply the resulting number by 2 to the power F, but this is quick and easy to do in a floating point unit. 

When this encoding was developed in the mid-1980s, there was a lot of discussion of these issues, and there was agreement over a range of vendors that the format provided a very good "neutral" format that they could all encode into and decode out of from a range of actual floating point hardware. Recommendation X.690/ISO 8825 Part 1 has a substantial tutorial annex about both the rationale for including F and also describing in some detail the algorithm needed to statically determine the encodings for a given floating point unit, and for encoding and decoding values. The interested reader is referred to this tutorial for further detail. 

Once again, in producing a canonical/distinguished encoding, we have to look at what options are being permitted, and eliminate them. We also have to concern ourselves with "normalization" of the representation. (This was illustrated in the character case above, where we required 4.E-1 rather than 0.4. A similar concern arises with the binary encoding.) For DER/CER/PER (all forms) we require that B be 2, that the mantissa be odd, that F be zero, and that the exponent and mantissa be encoded in the minimum number of octets possible. This is sufficient to remove all options. 

## 3.5.3 Encoding the special real values

There were early discussions about allowing special encodings for real values of the form "underflow" and "overflow", and for pi and other "interesting" values, but the only special values standardised so far (and there are unlikely to be any others now) are PLUS-INFINITY and MINUS-INFINITY. 

And finally there are "special" real values that cannot easily be represented by normal character or floating point formats. 

Recall that for a base 2 encoding the first (most significant) bit of the first contents octet is 1, and that for a base 10 encoding, the first two bits are zero. A special value encoding has the first two bits set to zero and one, with the remaining six bits of the first (and only) content octet identifying the value (two encodings only used). 

## 3.6 Encoding an OCTET STRING value

As was pointed out earlier, there are two ways of encoding an octet string - either as a primitive encoding, or as a series of TLV encodings, which we illustrate using the indefinite form for the outer-level TLV. 

Thus: 

<table><tr><td>Pretty simple again - except that if you have a very long octet string you may want to fragment it to avoid counting it before transmission. Again, an encoder&#x27;s option.</td></tr></table>

## octetstring OCTET STRING ::= '00112233445566778899AABBCCDDEEFF'H

encodes as either 

<table><tr><td></td><td>T</td><td>L</td><td>V</td><td></td><td></td></tr><tr><td>octetstring:</td><td>04</td><td>10</td><td colspan="3">00112233445566778899AABBCCDDEEFF</td></tr><tr><td>or as octetstring:</td><td>24</td><td>80</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>T</td><td>L</td><td>V</td></tr><tr><td></td><td></td><td></td><td>04</td><td>08</td><td>0011223344556677</td></tr><tr><td></td><td></td><td></td><td>04</td><td>08</td><td>8899AABBCCDDEEFF</td></tr><tr><td></td><td></td><td>0000</td><td></td><td></td><td></td></tr></table>

There are a number of points to note here. Of course fragmentation makes little sense for such a short string, but it illustrates the form. We chose here to fragment into two equal halves, but in general we can fragment at any point. We chose not to fragment our fragments, but we are actually permitted to do so! In DER fragmentation is forbidden. In CER the fragment size is fixed at 1000 octets (no fragmentation if 1000 octets or under), and additional fragmentation of fragments is forbidden. 

Finally, note that if the OCTET STRING had been implicitly tagged, the outer most T value (24 - universal class 4, constructed), would reflect the replacement tag, but the tag on each fragment would remain 04 (universal class 4, primitive). 

## 3.7 Encoding a BIT STRING value

For a BIT STRING value, we talk about the leading bit of the bitstring and the trailing bit, with the leading bit numbered as bit zero if we list named bits. The leading bit goes into the most significant bit of the first octet of the contents octets. Thus using the diagram conventions detailed earlier, the bits are transmitted with the left-most on the paper as the leading bit, proceeding to the right-most. When specifying a BIT STRING value, the value 

<table><tr><td>BER length counts are always in octets. So how to determine the exact length of a bit string encoding? And what bit-value to pad with to reach an octet boundary? (Answer to the latter - encoder&#x27;s option!)</td></tr></table>

notation declares the left-most bit in the notation as the leading bit, so there is general consistency, except that the numbering of bits in a BIT STRING type goes in the opposite direction to the numbering of bits in an octet. 

As with an OCTET STRING value, BIT STRING value encodings can be primitive or broken into fragments. There is only one additional complication - the length count in BER is always a count of octets, so we need some way of determining how many unused bits there are in the last octet. This is handled by adding an extra contents octet at the start of the contents octets saying how many unused bits there are in the last octet. (In CER/DER these unused bits are required to be set to zero. BER has their values as a sender's option.) 

If fragmentation of the bitstring into separate TLVs is performed, the fragments are required to be on an octet boundary, and the extra octet described above is placed (only) at the start of the last fragment in the fragmented encoding. 

Thus: 

## bitstring BIT STRING ::= '1111000011110000111101'B

encodes as either 

<table><tr><td></td><td>T</td><td>L</td><td>V</td><td></td><td></td></tr><tr><td>bitstring:</td><td>03</td><td>0F</td><td>02F0F0F4</td><td></td><td></td></tr><tr><td>or as bitstring:</td><td>23</td><td>80</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>T</td><td>L</td><td>V</td></tr><tr><td></td><td></td><td></td><td>03</td><td>02</td><td>F0F0</td></tr><tr><td></td><td></td><td></td><td>03</td><td>02</td><td>02F4</td></tr><tr><td></td><td></td><td>0000</td><td></td><td></td><td></td></tr></table>

Again, fragmentation makes little sense for such a short string, and again in DER fragmentation is forbidden. In CER the fragment size is again fixed at 1000 octets (no fragmentation if 1000 octets or under), and additional fragmentation of fragments is forbidden. 

Apart from the extra octet detailing the number of unused bits, the situation is in all respects the same as for OCTET STRING. 

## 3.8 Encoding values of tagged types

If an implicit tag is applied (either by use of the word IMPLICIT, or because we are in an environment of automatic or implicit tagging), then as described in Section II, the class and number of the new tag replaces that of the old tag in all the above encodings. 

<table><tr><td>The final discussion of tagging!If its not clear by the end of thisclause, throw the book in theriver!</td></tr></table>

If however, an explicit tag is applied, we get the original encoding with the old tag, placed as a (single) TLV as the contents octets of a constructed encoding whose T part encodes the new (explicit) tag. 

For example: 

integer1 INTEGER ::= 72 

integer2 [1] IMPLICIT INTEGER ::= 72 

integer3 [APPLICATION 27] EXPLICIT INTEGER ::= 72 

are encoded as 

<table><tr><td></td><td>T</td><td>L</td><td>V</td><td></td><td></td></tr><tr><td>integer1</td><td>02</td><td>01</td><td>48</td><td></td><td></td></tr><tr><td>integer2</td><td>C1</td><td>01</td><td>48</td><td></td><td></td></tr><tr><td>integer3</td><td>7B</td><td>03</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>T</td><td>L</td><td>V</td></tr><tr><td></td><td></td><td></td><td>02</td><td>01</td><td>48</td></tr></table>

where the 7B is made up, in binary, as follows: 

<table><tr><td>Class</td><td>P/C</td><td>Number</td></tr><tr><td>APPLICATION</td><td>Constructed</td><td>27</td></tr><tr><td>01</td><td>1</td><td>11011 = 01111011 = 7B</td></tr></table>

## 3.9 Encoding values of CHOICE types

In all variants of BER, there are no additional TL wrappers for choices. The encoding is just that of the chosen item. The decoder knows which was encoded, because the tags of all alternatives in a choice are required to be distinct. 

<table><tr><td>This is either obvious or curious! There is no TLV associated with the CHOICE construct itself - you just encode the TLV for a value of the chosen alternative.</td></tr></table>

So (compare with the encodings for the INTEGER and BOOLEAN types given above) 

and 

```txt
value1 CHOICE
{ flag BOOLEAN,
    value INTEGER} ::= flag:TRUE
value2 CHOICE
{flag BOOLEAN,
    value INTEGER} ::= value:72 
```

we get the encodings: 

<table><tr><td></td><td>T</td><td>L</td><td>V</td></tr><tr><td>value1</td><td>01</td><td>01</td><td>FF</td></tr><tr><td>value2</td><td>02</td><td>01</td><td>48</td></tr></table>

## 3.10 Encoding SEQUENCE OF values

This is quite straight-forward - an outer (constructed) TL as the wrapper, with a TLV for each element (if any) in the SEQUENCE OF value. 

So 

<table><tr><td>You should know this already from the general discussion of the TLV approach. Nothing new here.</td></tr></table>

$$
\begin{array}{r l} \text { temperature - each - day   SEQUENCE(7)OF   INTEGER } \\ & : := \{2 1, 1 5, 5, - 2, 5, 1 0, 5 \} \end{array}
$$

could be encoded as: 

<table><tr><td rowspan="2">temperature-each-day:</td><td>T</td><td>L</td><td>V</td><td></td><td></td></tr><tr><td>30</td><td>80</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>T</td><td>L</td><td>V</td></tr><tr><td></td><td></td><td></td><td>02</td><td>01</td><td>15</td></tr><tr><td></td><td></td><td></td><td>02</td><td>01</td><td>0F</td></tr><tr><td></td><td></td><td></td><td>02</td><td>01</td><td>05</td></tr><tr><td></td><td></td><td></td><td>02</td><td>01</td><td>FE</td></tr><tr><td></td><td></td><td></td><td>02</td><td>01</td><td>05</td></tr><tr><td></td><td></td><td></td><td>02</td><td>01</td><td>10</td></tr><tr><td></td><td></td><td></td><td>02</td><td>01</td><td>05</td></tr><tr><td></td><td></td><td>0000</td><td></td><td></td><td></td></tr></table>

Of course, we could have employed definite length encoding at the outer level, which in this case would have saved two octets if the short form had been employed. 

## 3.11 Encoding SET OF values

What are the actual set of abstract values? Is {3, 2} the same value as {2, 3}? It should be! So we must have just one encoding in distinguished/canonical encoding rules for this single value. This produces a significant cost at encode time. Best not to use set-of if you want to have distinguished/canonical encodings. 

The encoding of set-of is just the same as for sequence-of except that the outer T field is 31. If, however, this were a CER or DER encoding then the seven TLVs would be sorted into ascending order and we would get: 

$$
\begin{array}{c c c c c} \text {unordered - weeks - temps SET (7) OF INTEGER} \\ : := \{2 1, 1 5, 5, - 2, 5, 1 0, 5 \} \\ \text {weekstemperatures:} & T & L & V \\ & 3 1 & 8 0 \\ & & & T & L & V \\ & & & 0 2 & 0 1 & F E \\ & & & 0 2 & 0 1 & 1 5 \\ & & & 0 2 & 0 1 & 1 0 \\ & & & 0 2 & 0 1 & O F \\ & & & 0 2 & 0 1 & 0 5 \\ & & & 0 2 & 0 1 & 0 5 \\ & & & 0 2 & 0 1 & 0 5 \\ & & & 0 0 0 0 \end{array}
$$

Notice that the sort is on the final encodings of each element, so the temperature -2 sorts ahead of the temperature 21. 

## 3.12 Encoding SEQUENCE and SET values

These are exactly similar, except that now the inner TLVs (one for each element of the sequence or set) will be of varying size and have varying tags. In some cases these elements may themselves be sequences or sets, so we may get deeper nesting of TLVs (to any depth). 

<table><tr><td>Back to simplicity again. Nested TLVs, to any depth.</td></tr></table>

If there are optional elements, and the abstract value of the sequence or set does not contain a value for these elements, then the corresponding TLV is simply omitted. 

In the case of SET, BER allows the nested TLVs to be appear in any order chosen by the encoder. In DER, the elements are sorted by the tag of each element (which again are required to be distinct). However, if we have 

```txt
My-type ::= SET OF
{ field1 INTEGER,
    field2 CHOICE
    { flag BOOLEAN,
    dummy NULL } } 
```

then each set-of value contains an integer value plus either a boolean or a null value. But in the sort into ascending order of tag, a boolean value would come before an integer value but a null value after it. Thus depending on which value of field2 is chosen, it may appear before or after the value of field1! In CER, a slightly more complicated algorithm applies which says that the maximum tag that appears in any value of field2 is the NULL tag, and that that determines the position of field 2 no matter what value is actually being sent. This is marginally more difficult to explain and perhaps understand, but avoids having to do a sort at encode time. 

## 3.13 Handling of OPTIONAL and DEFAULT elements in sequence and set

There are no problems caused by OPTIONAL (the use of tags makes it unambiguous what has been included and what has not). However, in the case of DEFAULT, BER leaves it as a sender's option whether to omit 

a default value (implying possibly complex checking that it is the default value), or whether to encode it anyway! 

Again, this gives DER and CER problems to remove this encoder's option. In this case they both require that an element whose value equals the default value be omitted, no matter how complicated the check might be. (However, in practice, DEFAULT is normally applied only to elements that are very simple types, rarely to elements that are complex structured sequences and sets). 

When we discuss PER more fully in the next chapter, however, we find that PER specifies mandatory omission for "simple types" (which it lists) and a sender's option otherwise, avoiding verbosity in and options incommon cases, but avoiding implementation complexity in the other cases. 

## 3.14 Encoding OBJECT IDENTIFIER values

The value is basically a sequence of integers, but we need a more compact encoding than using "SEQUENCE OF INTEGER". The "more bit" concept comes in again here, but with a curious (and nasty) optimization for the top two arcs. 

Figure III-12 is a repeat of Figure II-1, and shows a part of the object identifier tree. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/8eb5b15270b1140cff5eb2b8d49c06d17c780b047474c4aebd4678532c875505.jpg)


Object identifier values are paths down this tree from the root to a leaf, and one such path is defined by 

$$
\{\text { iso(1)   standard(0)   8571   abstract - syntax(2) } \}
$$

but the only information that is encoded is a value of 

$$
\left\{ \begin{array}{c c c c} 1 & 0 & 8 5 7 1 & 2 \end{array} \right\}
$$

This could in theory be carried by an encoding of "SEQUENCE OF INTEGER", but the presence of T and L fields for each integer value makes this rather verbose, and a different (ad hoc) encoding is specified. 

The "more bit" concept (also used in the encoding of tags – see Figure III-6 in 2.2) is used. For each object identifier component (the values 1, 0, 8571 and 2 above), we encode it as a positive integer value into the minimum necessary number of bits (the standard requires that the minimum multiple of seven bits is used), then place those bits into octets using only the least significant seven bits of each octet (most significant octet first). Bit 8 (most significant) of the last octet is set to 0, earlier bit 8 values (the "more" bit) are set to 1. 

The result of encoding 

$$
\text { ftam - oid   OBJECT   IDENTIFER }: := \{1 0 8 5 7 1 2 \}
$$

would be (in hex): 

<table><tr><td></td><td>T</td><td>L</td><td>V</td><td></td><td></td><td></td></tr><tr><td>ftam-oid:</td><td>06</td><td>05</td><td>01</td><td>00</td><td>C27B</td><td>02</td></tr></table>

However, the actual encoding of this object identifier value is 

<table><tr><td>T</td><td>L</td><td>V</td></tr><tr><td>06</td><td>04</td><td>28 C27B 02</td></tr></table>

How come? 

A dirty trick was played! (And like most dirty tricks, it caused problems later). 

The octets encoding the first two arcs were (in 1986) thought to be unlikely to ever have large values, and that using two octets for these two arcs was "a bad thing". So an "optimization" (mandatory) was introduced. 

We can take the top two arcs of Figure III-12 and "overlay" them with the dotted arcs shown in Figure III-13, producing a single (pseudo) arc from the root to each second level node. How to number these pseudo-arcs? 

Well, there are three top-level arcs, and we can accommodate encodings for up to 128 arcs (0 to 127) in a single octet with the "more bit" concept described above. 128 divided by 3 is about 40! Let's assume the first two top-level arcs will never have more than 40 sub-arcs, and allocate the first 40 pseudo-arcs to top-level arc 0, the next 40 to top-level arc 1, and the remainder to top-level arc 2. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/2aea3e26801372abe6a42602994299592adf6633fb77063f15b1d3d7c0f3e6b3.jpg)



Figure III-13: Making the top two arcs into a single arc


So for any second level arc beneath top-level arc 0, we use the second level arc number as the number for the pseudo-arc. For any second-level arc beneath top-level arc 1, we use the second level arc number plus 40 as the number for the pseudo-arc, and for any second-level arc beneath top-level arc 2, we use the second level arc number plus 80 as the number for the pseudo-arc. 

We then get the encoding of {1 0 8571 2} as 

$$
\begin{array}{c c c c c} \mathbf {T} & \mathbf {L} & \mathbf {V} \\ 0 6 & 0 4 & 2 8 \text {C27B} 0 2 \end{array}
$$

as described earlier. 

As was pointed out earlier, where you are "hung" on the object identifier tree is unimportant, except that your object identifiers will be longer the lower down you are. In mid-1995 this surfaced as an issue, with other major international players wanting top-level arcs. The above "fudge" with the top two arcs makes it difficult (not impossible, but difficult) to add new top-level arcs, and to alleviate this problem the RELATIVE OID constructor was proposed for addition to ASN.1. 

If an organization has the need to allocate object identifiers beneath a root such as: 

$$
\left\{\text { joint - iso - itu - t(2) } \quad \text { internationalRA(2)set(42) } \right\}
$$

and has a protocol that is specifically designed to carry (always or commonly) object identifier values beneath this root, then it can define 

$$
\begin{array}{r l} \text {SET - OIDs} & : := \text {RELATIVE OID} \\ & \quad \text {- - Relative to\{2 2 42\}} \end{array}
$$

and use that type in its protocol, either alone or as a CHOICE of that and a normal OBJECT IDENTIFIER. 

A relative object identifier type is only capable of carrying object identifier values that hang below a known node (in this case {2 2 42}), but the encoding of the value encodes only the object identifier components after {2 2 42}, saving in this case two octets. 

The saving can be more significant in PER, where encodings are generally smaller anyway. In the case of Secure Electronic Transactions (SET), getting ASN.1 encodings of certificates down to a size that will fit easily on a smart card posed some challenges, and the use of PER and the relative object identifier technique was important. 

At the time of going to press, the RELATIVE OID work was not finalised, so do check details with the latest standard! (And/or look for errata sheets for this book on the Web site in Appendix 5). 

## 3.15 Encoding character string values

The character string types (as with the time types described below) are encoded by reference to other standards. A more detailed description of these character set standards is included in Section IV, but the basic characteristics of each encoding is described here. 

<table><tr><td>Here&#x27;s where you have to go out and buy additional specifications - almost all the character string encodings are by reference to other specifications.</td></tr></table>

There is probably more text in this book than in the ASN.1 Standard itself! 

Starting with the simplest character string types - NumericString, PrintableString, VisibleString, and GraphicString - the contents octets of these are just the ASCII encoding of the characters. 

The next group is TeletexString, VideotexString, GraphicString and GeneralString. These have encodings whose structure is specified in ISO 2022, using "escape sequences" specified for each Register Entry in the International Register to "designate and invoke" that register entry. After the appropriate escape sequence, subsequent eight bit encodings reference characters from that register entry until the next escape sequence occurs. It is important to note that there are many characters that appear in multiple register entries, so there are frequently many encodings for a given character string. It is also theoretically possible to have a succession of escape sequences each one over-riding the last, with no intervening character encoding. In the distinguished/canonical encoding rules, all these options are eliminated. 

The next two character set types to consider are UniversalString and BMPString. UniversalString supports all the characters of ISO 10646 (the most recent character code standard, using 32 bits per character in the encoding. BMPString supports only those characters in the "Basic Multilingual Plane" (sufficient for all normal earthly activity!) which also corresponds to the "Unicode" character set, using 16 bits per character. 

Finally, UTF8String uses a variable number of octets per character (from one for the ASCII characters to a maximum of six octets). None of the octets in a UTF8String encoding have the top bit set to zero unless they are the (single octet) encoding of an ASCII character. The encoding of octets that form a single character always start with "10" unless they are the first octet of the encoding of a character, so even if you start at a random point in the middle of an encoding, you can easily identify the start of the next character encoding. 

A UTF8 encoding of a character has an "initial octet" that either starts with a "0" bit (in which case we have a single octet ASCII encoding), or starts with two to six one bits followed by a zero bit. Remaining bits in this first octet are available to identify the character. The number of one bits gives the number of octets being used to encode the character. Each subsequent octet has the top two bits set to "10", and the remaining six bits are available to identify the character. The character is identified by its number in the ISO 10646 32-bit coding scheme, which is encoded into the available bits (right justified), using the minimum number of octets necessary. Thus characters with values less than two to the power 11 (which is all "European" characters) will encode into two octets, and characters with values less than two to the power 16 will encode into three characters, and so on. 

Some examples of UTF8 encodings of characters are given in Figure III-14 as hex representations. 

<table><tr><td>Name of character</td><td>Unicode/10646 number</td><td>Encoding in binary</td></tr><tr><td>LATIN CAPITAL LETTER H</td><td>72</td><td>01001000</td></tr><tr><td>LATIN DIGIT ZERO</td><td>48</td><td>00110000</td></tr><tr><td>LATIN CAPITAL LETTER C WITH CEDILLA</td><td>199</td><td>11000011 10000111</td></tr><tr><td>GREEK CAPITAL LETTER BETA</td><td>914</td><td>11001110 10010010</td></tr><tr><td>CYRILLIC CAPITAL LETTER EN</td><td>1053</td><td>11010000 10011101</td></tr><tr><td>ARABIC LETTER BEHEH</td><td>1664</td><td>11011010 10000000</td></tr><tr><td>KATAKANA LETTER KA</td><td>12459</td><td>11100001 10100001 10101011</td></tr></table>


Figure III-14: Some examples of UTF8 Encodings


## 3.16 Encoding values of the time types

The time types are specified as strings of characters, and their encoding is simply the ASCII encoding of those characters. 

There were problems with the precision of GeneralizedTime. The actual referenced standard is 

Simply an ASCII encoding of the characters. But watch out for issues of precision in the distinguished/canonical rules. 

ISO 3307, which from its first edition in 1975 permitted seconds to have any number of decimal places. But somehow some parts of the ASN.1 implementor community had got the impression that the precision was limited to milliseconds, and would not accept values to a greater precision. 

There are also issues with what is the precise set of abstract values. The ASN.1 specification states that GeneralizedTime allows the representation of times to a variety of precisions. So, for example, is a time of: 

## "199205201221.00Z"

the same abstract value as 

## "199205201221.0Z"

If so, then the canonical and distinguished encoding rules should forbid one or the other encoding (or even both!). But if it is regarded that different precisions are different abstract values (and may carry different semantics), then all such encodings need to be allowed in the canonical and distinguished encoding rules. 

The eventual ruling was that the implied precision by the inclusion of trailing zeros was not a primary part of the abstract value, and that in the distinguished and canonical encoding rules trailing zeros should be forbidden - a time to an implied precision of one hundredth of a second is the same time (abstract value) as one to an implied precision of one tenth of a second, and should not carry different semantics, and should have the same encoding in the distinguished and canonical encoding rules. 

## 4 Encodings for more complex constructions

## 4.1 Open types

ASN.1 has had the concept of "holes" from its inception, originally described as a type called "ANY", and later as a so-called "open type" specified with syntax looking like: 

Most of the more complex types are defined as ASN.1 SEQUENCE types, and their values encode by encoding values of those sequence types. 

## OPERATOR.&Type

stating that the type that will fill this field is the value of some ASN.1 type that is assigned to the &Type field of an information object of the OPERATOR class (see Section II Chapter 6). 

BER handles open types very simply: What eventually fills this field has to be an ASN.1 type, and the encoding of the field is simply the encoding of a value of that type. 

Remember that in BER there is a strict TLV structure, so it is always possible to find the end of a BER TLV encoding without any knowledge of the actual type being encoded. In the case of an open type, the identification of that type may appear later in the encoding than the occurrence of the encoding of a value of the type. That gives no problem in BER, because the TLV structure is independent of the type. 

## 4.2 The embedded pdv type and the external type

As described in Section II, these are slightly obscure names for ASN.1 types, but the "embedded" means that here we have foreign (non-ASN.1-defined) material embedded in an ASN.1 type, and the "external" means more or less the same thing - material external to ASN.1 is being embedded. 

Historically, EXTERNAL came first, and EMBEDDED PDV was added in 1994 with slightly greater functionality (new specifications should always use EMBEDDED PDV, not EXTERNAL). 

Both these types have "associated types" which are sequence types, and which have fields capable of carrying all the semantics of the type. Broadly, this is the encoding of some material (carried as a bitstring in the most general case) and identification (using one object identifier in the case of EXTERNAL and zero to two in the case of EMBEDDED PDV) of the abstract and transfer syntax for the encoding in the bitstring. (There is some slight additional complexity by the inclusion of options that apply when the encodings are transferred over an OSI Presentation Layer protocol, but this does not affect the encoding in the non-OSI case.) The BER encoding is simply defined as the encoding of these "associated types". 

## 4.3 The INSTANCE OF type

The INSTANCE OF type provides a very simplified version of EXTERNAL or EMBEDDED PDV, designed specifically for the case where what we want to put into our "hole" is a (single) object identifier to identify the (ASN.1) type whose value is encoded into the "hole", followed by a value of that ASN.1 type. This type relates to the built-in very simple information object class TYPE-IDENTIFIER described in section II. 

It is encoded as a SEQUENCE type with just two fields - an object identifier and the value of an ASN.1 type (as an open type). 

## 4.4 The CHARACTER STRING type

The CHARACTER STRING type was introduced in 1994, and is almost identical to EMBEDDED PDV in its encoding. The idea here is that we have the value of a character string (from some repertoire identified by a character abstract syntax object identifier) is encoded according to a character transfer syntax object identifier. Thus we have essentially an encoding of a sequence comprising zero to two object identifiers (as with EMBEDDED PDV, there are options where either or both object identifiers take fixed values determined by the protocol specification and which therefore do not need to be encoded), followed by the encoding of the actual characters in the string. 

## 5 Conclusion

The ASN.1 specification of BER is just 17 pages long - less than this chapter! (Ignoring the Annexes and details of DER and CER). The interested reader should now have no problems in understanding that specification. Go away and read it! 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/87b5c16d558dec77afcdc069928e79327f29dcf35af1f1c014bb30d70e002b13.jpg)


# Chapter 3 The Packed Encoding Rules

(Or: Encodings for the next millennium - as good as you'll get – for now!) 

Summary: This chapter provides details of the Packed Encoding Rules. It has broadly two main parts. In the first part further details are given of some of the global features of PER and the terminology employed in the actual specification. In this first part we cover: 

• The overall structure of a PER encoding and the terminology used (preamble, length determinant, contents), with discussion of the four variants of PER. 

• The general nature of encodings for extensible types. 

• PER-visible constraints. 

• Effective size and alphabet constraints. 

• Canonical order of tags, and the use of this ordering. 

• The form of a general length field, when needed. 

• The OPTIONAL bit-map and the CHOICE index (for extensible and non-extensible choices) 

The second part gives details of the encodings of each ASN.1 type in much the same way as was done for BER in the previous chapter. The order is again chosen in a way that moves from the simpler to the slightly more complex encodings. We cover the encodings of: 

• NULL and BOOLEAN values. 

• INTEGER values. 

• ENUMERATED values. 

• Length determinants of strings. 

• Character string values. 

• Encoding of SEQUENCE and SET. 

• Encoding of SEQUENCE OF and SET OF. 

• Encoding of REAL and OBJECT IDENTIFIER. 

• Encoding of the remaining types (GeneralizedTime, UTCTime, ObjectDescriptor, and types defined using the "ValueSet" notation). 

Most of these later topics are covered by simply giving examples, as they follow the general approaches that are fully covered in the first part of this chapter. 

## 1 Introduction

The principles underlying PER encodings (no encoding of tags, use of a bit-map for OPTIONAL, use of a CHOICE index, and the sorting of SET elements and CHOICE alternatives into tag order have already been introduced in Chapter 1 of this section. In this chapter we complete the detail. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/ee8b1a4d5529c0803c7975913faf64f1722b11c5d0fe8fc5deb12bc40b98ca01.jpg)


The latter part of this chapter provides examples of all the encodings, and gives some further explanation where needed. 

This chapter is not totally free-standing. It is assumed that the reader will have read the relevant parts of Section III, Chapter 1 before starting on this chapter, but there are also a number of cases where PER codings are the same as BER (or more usually CER/DER) encodings, and in such cases reference is made to Section III, Chapter 2. 

The bit-numbering and diagram convention (first octet of the encoding shown on the left, bits numbered with 8 as the most significant and shown on the left) that was used for BER is used here also. 

However, with PER there are sometimes padding bits inserted to produce octet alignment at the start of some field. Where padding bits may have to be inserted (depending on the current bit position within an octet, there may be anything from zero to seven padding bits), a capital "P" is used at the start of the field in the examples given in this chapter. 

## 2 Structure of a PER encoding

## 2.1 General form

You will already know that PER does not necessarily encode into fields that are a multiple of eight bits, but the BER concept of encodings of (for example) SEQUENCE, being some up-front header followed by the complete encodings of each element also applies to PER. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/ae9d36befc90d603329da1ffa43632eaeb47e8ce401d24640dff5510e7738552.jpg)


In the case of PER, the "header" is called the preamble, but is present for SEQUENCE only if there are optional elements, otherwise it is null and we have simply the encoding of each element. 

There is also a difference in the "L" part of an encoding from BER. Once again, it can frequently be missing (whenever the length is known in advance in fact), but also the terminology changes to "length determinant". This change was made because whilst the length octets of BER are always a count of octets (apart from the indefinite form), in PER the length determinant encodes a value that may be: 

• a count of octets (as in BER); or 

• a count of bits (used for the length of an unconstrained BIT STRING value); or 

• a count of iterations (used to determine the length of a SEQUENCE OF or SET OF value). 

It is also the case that in PER the length determinant is not necessarily an integral multiple of eight bits. 

The precise form and encoding of a length determinant is described later. 

Each of the three pieces of encoding encode into what is called a bit-field. The length of this bitfield is either statically determinable from the type definition, or that part of the encoding will be preceded by a length determinant encoding. The term "bit-field" is used to imply that the field is not necessarily an integral multiple of eight bits, nor in general is the field required to start on an octet boundary. 

As we proceed through the encoding of a value of a large and complex structured type, we generate a succession of bit-fields. At the end of the encoding, these are simply placed end-to-end (in order), ignoring octet boundaries, to produce the complete encoding of the value. 

## 2.2 Partial octet alignment and PER variants

There are a couple of further wrinkles on the overall structure, of which this is the first! 

There are some fields where the designers of PER felt that it would be more sensible to ensure that the field started on an octet boundary (for simplicity of implementation and minimisation of CPU cycles). Fields to which this applies can be identified from the type definition (and do not depend on the particular value being transmitted). Such cases are said to encode into octet-aligned bitfields. In the final concatenation of bit-fields, padding bits are inserted as necessary before any octet-aligned bit-fields to ensure that they start at a multiple of eight bits from the start of the entire encoding of the outer-level type - the message, or "protocol data unit" (PDU). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/465ebab73fa8046aab0ecbfbb8c52cf01a4dada2ea08b796f58258ee32df4109.jpg)


There are some applications (air traffic control is one), where the padding bits are not wanted - minimising bandwidth is considered the primary need. There are therefore formally two variants of PER: 

• the ALIGNED variant (with padding bits); and 

• the UNALIGNED variant (with no padding bits, and with some other bandwidth reduction features that will be described later). 

## 2.3 Canonical encodings

BASIC-PER is largely canonical, but there are some types (SET OF, some character string types, time types, and some occurrences of DEFAULT) where being 100% canonical is "expensive". So BASIC-PER (being pragmatic!) has non-canonical encodings for these types. CANONICAL-PER is fully canonical. 

This is another area that gives rise to further encoding rules within the general PER family. 

Notice that whilst BER has many encoder's options, leading to the production of specifications for CER and DER, PER avoids options in the basic encoding, and looks at first sight to be canonical. (It is certainly far more canonical than BER!) 

However, to produce truly canonical encodings (as with BER) requires a sort of SET OF elements, and adds complexity to encoding character string types like GeneralString and GraphicString. Socalled BASIC-PER (with both ALIGNED and UNALIGNED variants) does not do this, and produces canonical encodings ONLY if these types are not involved. CANONICAL-PER (with an ALIGNED and an UNALIGNED variant) is fully canonical, and introduces sorting of SET-OF and special rules for GeneralString etc. The actual rules are exactly the same (and are specified by reference) as those used to turn BER into CER. 

## 2.4 The outer level complete encoding

Another slight complication arises at the outer level of a complete encoding (the total message being sent down the line). (This is a pretty detailed point, and unless you are heavily involved in producing encodings you can skip to the next clause). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/80ea7e64fd8f84c231ad6676c8730af3ec302d2b010e60a8924338f316fe5b65.jpg)


There are a few theoretical cases where a message may encode into zero bits with PER. This would occur, for example, with an outer-level type of NULL, or of a SET OF constrained to have zero iterations (both are highly unlikely to occur in practice, but ...!). 

The problem here is that if the way a carrier protocol is used allows multiple values of that type to be placed into the carrier, a multiple of zero bits is still zero bits, and the receiver would not know how many values had been sent, even with complete knowledge of the type definition! 

So PER requires that if the complete encoding of the outer-level type is zero bits (which would mean that the outer-level type contains only one abstract value), then a single one-bit is used for that encoding instead. 

And finally, recognising that carrier protocols often provide "buckets" that are only able to contain multiples of eight bits, PER specifies that the complete encoding should always be padded at the end with zero bits to produce an integral multiple of eight bits. (Again, this is to ensure that there is no doubt at the decoding end about the number of values that have been encoded into the octet bucket that the carrier uses to convey the PER encoding from encoder to decoder). 

So the minimum size of a complete outer-level PER encoding is one octet, and it is always a multiple of eight bits, but individual component parts are generally not a multiple of eight bits, and may be zero bits. 

## 3 Encoding values of extensible types

PER has a uniform approach to extensibility. Refer in what follows to Figure III-15 for an illustration of the encoding of extensible INTEGER and string values, to Figure III-16 for an illustration of the encoding of extensible SET and SEQUENCE values, to Figure III-17 for an illustration of the encoding of extensible CHOICE values, and to Figure III-18 for an illustration of the encoding of extensible ENUMERATED values. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/cd0337690a49f4bd1cc6dc2c001de1c24ad78970da5c07aa313a6d5c76a7ef88.jpg)


```txt
Either:
0
followed by:
An encoding of a value of the type, which is the same as that for the type without an extensibility marker or extensions.
Or:
1
followed by:
An encoding for a value of the extensible type which is outside the root, which is the same as that for values of the unconstrained type.
Figure III-15: Extensible constrained INTEGER or string encodings 
```

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/9a8cb650bed81ccd615c7b70264aad07b83d7c97eb33a161a62e722483fe18d9.jpg)


Any type (a constrained INTEGER, a constrained string, a SEQUENCE, a SET, a CHOICE, or an ENUMERATED) that has an extensibility marker (the ellipsis) in its type definition or in a PERvisible constraint has a value of that type encoded as follows: 

```txt
Either:
0
followed by:
An encoding of the choice index (identifying an alternative which is present in the root), which is the same as that for the type without an extensibility marker.
followed by:
The encoding of a value of the chosen alternative within the root.
Or:
1
followed by:
A different encoding for the choice index, (identifying an alternative outside the root).
followed by:
The encoding of a value of the chosen alternative that is outside the root.
Figure III-17: Extensible CHOICE encodings 
```

• There is a one-bit-long bit-field encoded up-front - the extensions bit. 

The extensions bit is set to zero if the value being encoded is in the root (one of the original INTEGER or ENUMERATED values, or a SET or SEQUENCE value in which all extension additions - if any - are absent). 

• The extensions bit is set to one otherwise (values outside the root). 

NOTE — Only implementations of versions greater than 1 will set the bit to one, but all implementations may encode a root value, and hence set the extensions bit to zero. 

```txt
Either:
0
followed by:
An encoding of a value of the type, which is the same as that for the type without an extensibility marker or extensions.
Or:
1
followed by:
An encoding for a value of the extensible type which is outside the root.
Figure III-18: Extensible ENUMERATED type encodings 
```

• If the "extensions bit" is set to zero, what follows is exactly the same encoding (for all types that can be marked extensible) as if the extension marker (and all extensions) was absent. 

If the "extensions bit" is set to one, the following encoding is sometimes the same as for the unconstrained type, but sometimes different, as follows: 

If the "extensions bit" is set to one when encoding an extensible INTEGER or extensible string, what follows is an encoding which is the same as for a value of the unconstrained type. 

If the "extensions bit" is set to one when encoding a SEQUENCE or SET value, what follows is the encoding of the elements that are in the root, with a special encoding (see 15.2) inserted at the insertion point to carry the values of elements outside the root (and to identify their presence). 

If the "extensions bit" is set to one when encoding a CHOICE value, what follows is a special encoding of the choice index (recognising that although theoretically unbounded, the value will usually be small), followed by an encoding of the chosen alternative. (See 8.2 for the encoding of a "normally small whole number"). 

• If the "extensions bit" is set to one when encoding an ENUMERATED value, the same encoding is used as for the choice index, for again the value is theoretically unbounded, but in practice will usually be small. 

It will be seen from the above that the only cost in version 1 of including an extensibility marker is 1 bit (possibly causing the insertion of up to seven padding bits after it). We will see later that if the type actually has extensions, and values outside the root are encoded, we generally get an additional overhead of a length field for such values. 

The encoding for values of extensible types that lie outside the root is described below after the description of the encoding for types that were not defined to be extensible (and for values of extensible types that are within the root). 

It will be clear from the above description that encoders and decoders must agree on whether a type is extensible or not, and if so on precisely which abstract values are in the root. Where a type has an ellipsis as a direct part of the type definition - SET, SEQUENCE, CHOICE, ENUMERATED, there is little problem. But where a type such as integer or a character string is constrained with a constraint that contains an ellipsis, the situation is (perhaps surprisingly!) not so clear cut, and the type may well be declared to be not extensible for PER-encodings, despite the clear presence of an ellipsis! This area is discussed at the end of the discussion on PER-visible constraints. 

## 4 PER-visible constraints

## 4.1 The concept

Crucial to understanding PER encodings is the concept of PER-visible constraints. These are (subtype) constraints which, if present, affect the encoding of the parent type. 

The most important PER-visible constraints are those placed on the INTEGER type and on the lengths of strings (or on iteration counts for SET OF and SEQUENCE OF). There are also constraints on the alphabet of some character string types that are PERvisible (see Clause 6), and can reduce the number of bits per character for these character strings. 

Constraints that are PER-visible in the above cases are quite widely-defined. They may be applied "a bit at a time", through repeated use of type references, or they may be 

PER-visible constraints are constraints that PER uses to produce less verbose encodings - for example - INTEGER (0..7) encodes into just three bits because the (0..7) constraint is PER-visible. BER ignores all constraints, and hence always needs a length field. PER takes a pragmatic view and uses constraints that are "easily" used and produce important bandwidth gains, but ignores other more complex constraints. 

applied through the use of parameterisation. Or they may be extremely complicated subtype specifications involving included subtype constraints, intersections and unions. 

There are two comments to make on this: first, most specifications are pretty simple, so handcoders don't have to do too much work to calculate the actual constraint in the real world; second, an ASN.1 compiler has no problems in resolving such expressions of arbitrary generality down to a precise record of the permitted values for the integer type, the length of the string, etc. 

## 4.2 The effect of variable parameters

One major exception to PER-visibility is if, in trying to determine the actual constraint, a variable parameter (a parameter that still does not have a value when the abstract syntax is defined) is textually referenced in the resolution of the actual constraint, then the constraint ceases to be PER-

Presence of a variable parameter in a constraint means that PER totally ignores that entire constraint. 

visible, and would encode as if that constraint were not present. 

This is the first of several cases where a type which is formally extensible encodes as if it was not extensible. In this case, it contains an ellipsis in a constraint that is not PER-visible, so (assuming no other constraints have been applied) it will encode as not extensible and not constrained. 

Variable parameters are still not heavily used, so this is not too big an issue, but the term textually above refers to the possibility of constructing union and intersection expressions which appear to use the value of such a parameter, but where the actual result of the expression evaluation proves to be the same no matter what value the variable parameter might have. Even if the parameter does not affect the result, its textual presence kicks the constraint out of court. This was done to ease implementation efforts for compilers, and to avoid possible errors in hand-encoding. 

## 4.3 Character strings with variable length encodings

Another major exception to PER-visibility that should be noted is that a constraint on the length of a character string applies to the number of (abstract) characters that can appear in the string. If the encoding is something like UTF8 (or GeneralString), where the number of octets needed to encode each character is different for different characters (and in the case of GeneralString can depend on encoder options), the length constraint is not much help at the encoding level - a length field is still needed in order to find the end of the encoding. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/72b9cab3815afca5bb11939fe92c371169ee0d4493e7365806e6d11ff9daf052.jpg)


(The above statement is not strictly true. If the itty-gritty details of an encoding scheme such as UTF8 are fully understood then knowledge of the number of abstract characters being encoded is in fact sufficient to find the end of the encoding, but PER wants a decoder to be able to find the end of the encoding without resorting to such detailed analysis.) 

So character set types that have a fixed number of octets for each abstract character are called known multiplier types, and length constraints on such types are PER-visible (and will give rise to reduced or eliminated length encodings), but for character string types that are not "known multiplier types", the constraints are not PER-visible (do not affect the encoding of values of the type), and any extension markers in these constraints are ignored for the purpose of PER encodings. 

## 4.4 Now let's get complicated!

This book is called "ASN.1 Complete", so we had better explore a bit more about PER-visibility and about extensibility. 

First, we note that there are a number of different sorts of subtype constraint which may be used alone, but which in the general case combine together using EXCEPT, INTERSECTION, and UNION. We call the basic building blocks component constraints, and the complete constraint the outer-level constraint. Both component constraints and outer-level constraints may contain an ellipsis! 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/d191c2a7a95bb9b5db1d8cfcc4a9f3e733384b51e2ce1534244569a68f6d671a.jpg)


Whether a component constraint is PER-visible will depend in general on the sort of component constraint it is, and on the type being constrained. Figure III-19 gives a list. 

<table><tr><td>Variable constraint</td><td>Never visible</td></tr><tr><td>Single value constraint</td><td>Visible for INTEGER only</td></tr><tr><td>Contained subtype constraint</td><td>Always visible</td></tr><tr><td>Value range</td><td>Visible for INTEGER only and in an alphabet constraint on a known-multiplier character string type</td></tr><tr><td>Size constraint</td><td>Visible for OCTET STRING, SET and SEQUENCE OF, and known-multiplier character string types</td></tr><tr><td>Permitted alphabet</td><td>Visible for known-multiplier character string types</td></tr><tr><td>Inner subtyping</td><td>Never visible</td></tr><tr><td colspan="2">Figure III-19: PER-visibility of constraints</td></tr></table>


Two important points to note from Figure III-19 are that a single value constraint is only visible if applied to INTEGER, and a contained subtype constraint is always visible. This can give rise to some distinctly non-obvious effects in relation to known-multiplier character string types such as IA5String! Suppose we have: 



Subtype ::= IA5String ("abcd" UNION "abc" UNION SIZE(2)) MyString ::= IA5String (Subtype INTERSECTION SIZE(3)) 


In Mystring, all the component constraints are PER-visible, and we expect to be able to work out the outer-level constraint. In Subtype, the first two component constraints are not PER-visible but the third is. What is the effect on Subtype and on MyString? This question, and a number of related ones, produced some lengthy discussion within the ASN.1 group with "keep it simple" colliding to some extent with "keep it general and intuitive". 

The first important rule is that if any component constraint is not PER-visible, then the entire outerlevel constraint is declared to be not PER-visible, and will not affect the encoding. Notice here that if there is an ellipsis in either a component or in the outerlevel constraint, because we are ignoring the entire constraint, the type is NOT encoded as an extensible type. So Subtype above is treated by PER as unconstrained, and contributes all abstract values of an unconstrained IA5String in the set arithmetic for MyString. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/31aca601be57ebe68e52a4e7a124cac876173f9170d5a73a93a51a0f2e9bad36.jpg)


For MyString, all component constraints are PER-visible, so the SIZE(3) applies, and values of the string encode as if it contained all possible abstract values of length 3. 

There is one additional rule, related to the use of the ellipsis. When performing set arithmetic to determine whether a PER-encoding is extensible and what values are in the root, all ellipsis marks (and any actual additions) in a component constraint (or any of the component constraints of that component - such as Subtype above) are ignored. A constrained type is extensible for PERencodings if and only if an ellipsis appears at the outer-level of a constraint, all of whose © OS, 31 May 1999 287 component constraints are PER-visible. This is simple, but perhaps not quite what you might have expected. 

Now consider a Version 2 specification, where the constraint in Version 1 was PER-visible, but in Version 2 things (such as a single value constraint) are added that would normally wreck PER-visibility. This does not (and cannot be allowed to) affect PERvisibility of the original Version 1 constraint, otherwise interworking would be prejudiced. So it is only those parts of a constraint that appear in the root that affect PER-visibility (and that affect the way a value is encoded). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/94f939b2285d22840eaefb6990ace134cbd1150f942eb68da2bc2929108ff02c.jpg)


But as someone once said "Such contorted constraint specifications only ever appear in discussions within the ASN.1 group, never in real user specifications." And they are right! 

## 5 Encoding INTEGERs - preparatory discussion

What matters for a PER-encoding of the INTEGER type (and of the lengths of known-multiplier 

character strings) is not the actual values, but the range of values permitted by PER-visible constraints. It is the largest and smallest value that matter. An integer constrained to have only the two values 0 and 7 will still encode in three bits, not two. What matters is the range, not the number of values. 

<table><tr><td>It&#x27;s the largest and smallest values that matter. Gaps in between do not affect the encoding.</td></tr></table>

Figure III-20 illustrates some simple constraints that are PER-visible, and the values that PER assumes need encoding. 

For any integer that has a lower bound (and similarly for the lengths of strings), what is encoded in the PER encoding is the offset from the lower bound. So the encoding of values of SET3 in Figure III-20 would use just 2 bits. 

<table><tr><td>Type definition</td><td>Values assumed to need encoding</td></tr><tr><td>INTEGER (0..7)</td><td>0 to 7</td></tr><tr><td>INTEGER (0 UNION 7)</td><td>0 to 7</td></tr><tr><td>SET1 ::= INTEGER (15..31)</td><td>15 to 31</td></tr><tr><td>SET2 ::= INTEGER (0..18)</td><td>0 to 18</td></tr><tr><td>SET3 ::= INTEGER (SET1 INTERSECTION SET2)</td><td>15 to 18</td></tr><tr><td>SET (SIZE (0..3)) OF INTEGER</td><td>Iteration count: 0 to 3</td></tr><tr><td>INTEGER (1 UNION 3 UNION 5 UNION 7)</td><td>1 to 7</td></tr><tr><td colspan="2">Figure III-20: Values assumed to need encoding</td></tr></table>

When we look at the encoding of integers (and of the lengths of strings) we will see that there are three distinct cases: 

• We have a finite upper and lower bound (called a constrained value); 

• We have a finite lower bound, but no upper bound (called a semi-constrained value); 

• We do not have a lower bound (this cannot occur for the length of strings, as zero is always a lower bound); this is called an unconstrained value; (even if there is a defined upper bound! - the upper bound gets ignored in this case). 

We describe below the encoding of constrained, semi-constrained, and unconstrained integers, and of constrained and semi-constrained lengths of strings in subsequent text, also addressing any special encodings that arise in the case of an extensible type. In the case of a constrained integer (or length), there are several different encodings depending on the range permitted by the constraint. (Remember that the absolute values permitted do not matter). 

The reader may wonder whether it is worth bothering with using "range" (and offset from the lower bound), rather than just determining the coding based on whether negative values are allowed or not, and then using enough bits to handle the largest value permitted by the constraint. Certainly INTEGER (10..13) and INTEGER (-3..0) are not likely to occur in the real world! But INTEGER (1..4) may be more common, and will use just two bits with the "offset from lower bound" rule, rather than three if we encoded the actual values. 

Working with "offset from lower bound" may appear to be an additional complexity, but is actually simpler than a specification saying "First see if all allowed values are positive or not, then etc etc", and amounts to just a couple of orders in a couple of places in actual implementations. 

## 6 Effective size and alphabet constraints.

## 6.1 Statement of the problem

We mentioned above (but did not emphasise) that constraints such as: 

```autohotkey
MyString ::= PrintableString (FROM (("0" .."9")  
UNION ("#")  
UNION ("*")) 
```

are PER-visible, and would result in just four bits per character for the encoding of values of "MyString" (which consists of all strings that contain only zero to nine and hash and star - twelve characters). 

This is described more fully in the discussion of the encoding of character string values in clause 14, but note here that for alphabet constraints, what matters is the actual number of characters permitted, not the range of characters. This is different from the treatment of constrained integers, as the need to define a character string type with an almost random selection of characters being permitted is far more likely to arise than the need to define an integer type with a random selection of integer values. 

There is, however, a slightly difficult interaction between alphabet constraints such as that above and length (size) constraints which can also be applied. 

For example, consider 

```txt
MyString1 ::= IA5String (FROM ("01") INTERSECTION SIZE (4))
MyString2 ::= IA5String (FROM ("TF") INTERSECTION SIZE (6))
MyString3 ::= IA5String (Mystring1 UNION Mystring2) 
```

All constraints are PER-visible, and it is clear that MyString 1 has a fixed length of 4 characters so should encode without a length field, and contains only two characters "0" and "1", and should encode with just one bit per character. Similarly MyString2 has an alphabet constraint restricting its character set to "T" and "F" (again giving one bit per character), and a size constraint of 6. 

But what is the alphabet and size constraint on MyString3? Does it have them? This is where the concept of an effective size constraint and an effective alphabet constraint comes in. 

## 6.2 Effective size constraint

An "effective size constraint" is defined to be a single size constraint such that a length is permitted by that size constraint if and only if there is at least one abstract value in the constrained type that has that length. 

So in the earlier example, MyString3 has abstract values of length 4 and 6 only. But what matters is the range of a size constraint, which is 4 to 6. This is equivalent to 0 to 2 when we remove the lower bound, so the length field of MyString3 would encode with 2 bits. 

## 6.3 Effective alphabet constraint

In an exactly equivalent fashion, an "effective alphabet constraint" is defined to be a single permitted alphabet constraint such that a character is permitted by that alphabet constraint if and only if there is at least one abstract value in the constrained type that contains somewhere within it that character. 

So in the earlier example, all the characters "0", "1", "T" and "F" are used by at least one abstract value, and the effective alphabet constraint allows these (and only these) characters, so two bits will be used per character. 

It is normally a simple matter for both a human and a computer to work out the effective alphabet and effective size constraints in every case, provided the rules on what is PER-visible are understood and applied. 

This is particularly true for a human because constraints are in practice quite simple. For a computer (which in an ASN.1 tool needs to be programmed to handle all possible constraints, no matter how complex or way-out), a program can be written which can take any arbitrarily complex set arithmetic expression (using only size and alphabet constraints) and resolve it down to an effective alphabet and an effective size constraint. It does this using equalities like: 

```txt
A EXCEPT B equals A INTERSECTION (NOT B)
and
NOT (A UNION B) equals (NOT A) INTERSECTION (NOT B)
etc 
```

If single value constraints had been allowed on character string types, this would have been a much more difficult task. 

## 7 Canonical order of tags

The reader will recall that PER requires a choice index, which means numbering the alternatives in a CHOICE in some order. Similarly, it avoids the need to encode a tag with elements of a SET by determining a fixed order for transmission of values of those elements. 

It would have been possible to have used the textual order of the alternatives and elements for this purpose, but this was felt to be inappropriate, as any change in the textual order (perhaps in going from version 1 to version 2, for purely editorial reasons) would change the encoding on the line. Essentially, such a change of order would have to be forbidden, which was felt to be counter-intuitive. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/8322cef91d76bce238aa89f366f59fa39d31d1bcb5c7cc2f46f70aa78b05cf52.jpg)


As all alternatives in a CHOICE and all elements in a SET are already required to have distinct (outer-level) tags, there is an obvious alternative available to that of using textual order: define an order for tag values, and then effectively re-order CHOICE and SET into tag order before determining the choice index or the order of transmission for SET elements. This is what is done. 

The so-called canonical tag order is defined to be: 

```txt
Universal Class (first)
Application Class
Context-specific Class
Private Class (last) 
```

with lower tag numbers coming before higher ones within each class. 

There is just one small complication - there always is! Recall that most types have the same outerlevel tag for all their abstract values, and we can validly talk about the "tag of the type". The only case where this is not true is for an untagged choice type. In this case different abstractvalues may have different outer level tags, and we cannot talk about "the tag of the type" so easily. (But remember that all these tags are required to be distinct from any of the tags of any other type in a SET or CHOICE). PER defines the tag of an untagged choice type as the smallest tag of any of its values, for the purpose of putting types into a canonical order, and the problem is solved. 

## 8 Encoding an unbounded count

If constraints are placed on lengths, iteration counts, or sizes of integers, PER will often omit the length field completely, or will use a highly optimised encoding for the length (described later), otherwise it will use length encodings similar to (but different from) those of BER. It is these encodings that are described in this clause. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/c1ffc65dfd2059ca2438fe3377006a891e2fa8818e6c503fc6dd4e7de209f78f.jpg)


## 8.1 The three forms of length encoding

PER has an equivalent of the BER short and long definite length and indefinite length forms, but there are a number of important differences, and apart from the short definite form the encodings are not the same as BER. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/eaf0388646b3398d97e51f3c3c53c8d0aad70523ef1eaf976ccf85dc5f488d8c.jpg)


This clause describes the form used for length determinants in cases where a count is needed which is potentially unbounded. This is generally the case only when there are no PER-visible constraints on the length of strings, iteration counts of SEQUENCE OF and SET OF, or on the size of integers. 

Where there are such constraints, PER will have a much more optimised length field (described later), or no length field at all. 

The first important difference from BER is in what PER counts. (BER always counts the number of octets in the contents). PER counts the number of bits in a BIT STRING value, abstract characters in a known-multiplier character string values, the iteration count in a SEQUENCE OF or SET OF, and octets in all other cases. We talk about the count in the length determinant. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/d9de893ca7ab05ab0de1992ed9ac17249880e49b35a59c179402922e2206cfb1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/80e26e68cb788a2b90e5dbf1678b2981ab36f014f83b3a9e582eb0a98d65fe67.jpg)



Figure III-21 to III-23 illustrate the three forms of encoding for the length determinant.


In the first form (corresponding to the BER short form, although PER does not use this term), we have the same encoding as BER, with the encoding placed in an octet-aligned-bit-field (in other words, there will be padding bits in the ALIGNED variants). The top bit of the octet is set to zero, and the remainder of the octet encodes count values from zero to 127. 

In the second form (corresponding roughly to the BER long definite form), there are always exactly two octets of length determinant. The first octet has the first bit set to 1 and the second bit set to zero, and the remaining 14 bits of those two octets encode count values from 128 to 16K-1. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/12e29a53499794351d8d4b4ca6b068cfddc4b09d09282222c6c00d58d89c5740.jpg)



Figure III-23: The encoding for large counts


The third form (corresponding roughly to the BER indefinite form, but with a very different mechanism) has an initial octet with both the top two bits set to 1. The remaining six bits encode (right justified) the values 1 to 4 - call this value "m". This octet says two things: 

• It says that "m" times 16K bits, iterations, abstract characters, or octets of the contents follow. 

• It says that after this fragment of the contents, there will be a further length field (of either of the three forms) for the rest of the contents, or for another fragment. 

PER requires that each fragment should be as large as possible, so there are no encoder's options in the choice of "m". Notice that in principle the largest permitted "m" could have been made much greater (there are six bits available to encode it), but the designers of PER chose to enforce fragmentation into fragments of at most 64K (4 times 16K) items for long octet strings etc. 

Figure III-24 illustrates the encoding (in binary) for count values (for example for a SEQUENCE OF) of 5, 130, 16000, 32768, and 99000. The insertion of one or more padding bits is shown with a "P", the length determinant is prefixed with "L:", and fragments of content with "C:" (a convention used throughout this chapter). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/87c7471fc5b9e533b0986329d5fa1eb711840acf77737b2d350ed898d6df6bde.jpg)


Note that where we get fragmentation in Figure III-24, although the fragments will be encoding multiples of 16K values of the same type, the encodings for each value are not necessarily the same length if the type being iterated has extensions, so padding bits may again be required before the length determinant after a fragment, as all these length determinants are specified as octetaligned. 

## 8.2 Encoding "normally small" values

PER has one further encoding for counts that are potentially unbounded. This encoding is used in cases where, although there is no upper-bound on the values which may need to be encoded, the values are expected to be "normally small" (and are all zero or positive), so this is described as "encoding a normally small non-negative whole number". 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/f77abbe65e10ff278b1be3a5160b584bebed527835d206e0174060e8662297d0.jpg)


This case is applied to encode a choice index for a choice alternative that is not in the root - there could be millions of additional choices in Version 2, and a Version 1 system has no idea how many, but actually, there are unlikely to be more than a few. 

A second application is to encode values of an enumerated type that are outside the root, where again the possible values are unbounded but are usually going to be small. 

In both these cases, encoding the value as an unbounded integer value (which would require an octet-aligned length field - usually set to 1 - as above and an integer encoding of one octet) is not optimal. The specified encoding in this case is instead to use just seven bits (not octet-aligned), with the top bit set to zero and the other six encoding values up to 63. Thus we avoid the octet alignment, and use only seven bits, not sixteen. Why use seven bits and not eight? Remember that this encoding will frequently appear following an extensions bit, so the two together give us exactly eight bits and if we had alignment at the start, we still have it. 

Of course, there is a penalty in optimising for small values! If the normally small non-negative whole number actually turns out to be more than 63, then we add a one-bit bit-field set to one, followed by a positive integer encoding into minimum octets preceded by a general length field as described above. 

Figure III-25 illustrates the encoding of a count as a normally small non-negative whole number for values of 5, 60, 254, and 99000. (There is no way the latter will occur in any real specification, and a tool that failed to provide code for this case - simply saying "not supported" - would be very unlikely to be caught out! The specification is, however, complete, and will encode any value no matter how large.) Note the absence of padding bits in the first two cases. 

```txt
5 L:0000101 C:(5 items of content)
60 L:0111100 C:(60 items of content)
254 L:1 P00000001 11111110 C:(254 items of content)
99000: L:1 P11000100
C:(64K items of content)
L:P11000010
C:(32K items of content)
L:P10000010 10111000
C:(696 items of content)

Figure III-25: Encoding normally-small non-negative whole numbers 
```

## 8.3 Comments on encodings of unbounded counts

The fragmentation mechanism in PER is not reliant on nested TLV structures, and can be applied to any contents encoding, and in particular to encodings of unbounded integers. Because the number of 64K fragments is unlimited, PER can truly encode indefinitely large integers, but we have already seen that the actual limit BER imposes is for all practical purposes irrelevant. The fragmentation mechanism of PER, particularly the lack of encoder's options, is, irrelevant. The fragmentation mechanism of PER, particularly however, probably simpler than that of BER. however, probably simpler than that of BER. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/517e198ab3afac50846ed1673f29daae7d95504139d64e3c5d7c2a2b98016cc7.jpg)


The main advantage of the PER encoding over BER is that length fields will generally be two octets, and counts of less than 128 are required to be done using the short form. With BER, length fields of three octets (long definite form) are permitted (and some implementations use them always), even for a contents length of - say - five octets. This is a big verbosity overhead for such implementations. 

The main advantage of the encoding of normally small non-negative whole numbers is that they (usually) encode into a bit-field without padding bits. If the value gets too big (unlikely to occur in practice), there is still only an additional penalty of one bit over a general length encoding. 

## 9 Encoding the OPTIONAL bit-map and the CHOICE index.

## 9.1 The OPTIONAL bit-map

We already know that when encoding a sequence or set value, PER encodes a preamble into a bit-field, with one bit for each OPTIONAL or DEFAULT element (zero bits if there are no OPTIONAL or DEFAULT elements). The bit is set to one if a value of the element is present in the encoding, set to zero otherwise. The encoding of each element then follows. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/45bc52391de8e6dc935ece9e45267ceb3853afc5012be11a715e7c6ae46ddf39.jpg)


This applies to elements in the root. A similar bit-map is used at the insertion point for elements which are extension additions, but this is described later. 

Under normal circumstances, there is no length determinant for this bit-map (as both sender and receiver know its length from the type definition), but if (and it will never occur, so a "not supported" response from a tool would be OK!) the length of the bit-map (the number of optional or default elements) exceeds 64K, then a length determinant is included and the bit-map fragments into 64K fragments. 

## 9.2 The CHOICE index

For a CHOICE value, there is again a preamble. If the type is not extensible, or the value is in the root, we have an upper bound on this choice index (and a lower bound of zero - the choice index starts at zero with the alternative that has the lowest tag value, as described earlier). This value is encoded as a constrained integer value - one that has both an upper and a lower bound. We will see below that integer values that are constrained to a range of, say, 0 to 15 (up to 16 alternatives in the CHOICE type) encode into a bit-field of four bits. 

If the chosen alternative is outside of the root, then we get our "extensions bit" set to one in a bitfield (as described earlier), followed by (usually) seven bits in a bit-field encoding the normally small non-negative whole number which is the index of the alternative within the extension additions (taking the first addition alternative as value zero). Note that whilst version brackets are allowed in a CHOICE, their presence makes no difference to the encoding, it is only for SEQUENCE and SET that the encoding is affected. 

Notice that if we started on an octet boundary, we have added exactly eight bits and will remain on an octet boundary, and we have not forced any octet alignment in these encodings. Illustrations of these encodings are given in Clause 16 describing the complete encoding of choice values. 

## 10 Encoding NULL and BOOLEAN values.

These are easy. No PER-visible constraints can apply, and optionality is sorted by the bit-map. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/5f4e17134524597f8b7980c89af41ef4e23a48209041f3c7be5d933119743a5e.jpg)


Zero bits for NULL. That's all you need. One bit for BOOLEAN - set to 1 for TRUE and set to zero for FALSE. And of course there are no padding bits in the ALIGNED version. 

## 11 Encoding INTEGER values.

Remember - when we talk about constraints below, we are only concerned with PER-visible constraints as discussed earlier. 

The only interesting parts of this discussion are to do with encoding constrained integers, when "minimum bits" tend to be used. For unconstrained integers, we get the standard length determinant and an encoding in the mum octets. There are, however, differences between the ALIGNED and UNALIGNED variants (apart from adding or not adding padding bits). 

## 11.1 Unconstrained integer types

The most important thing with the encoding of INTEGER types is whether a lower bound on the value exists or not. If it doesn't, we encode into the minimum octets as a signed number, with a general length determinant (as described earlier) containing a count of the number of octets. So: 

If there is no lower bound, we get a 2's-complement encoding into minimum octets with a general length determinant (all variants). 

```txt
integer1 INTEGER ::= 4096
integer2 INTEGER (MIN .. 65535) ::= 127
integer3 INTEGER (MIN .. 65535) ::= -128
integer4 INTEGER (MIN .. 65535) ::= 128 
```

are all described as "unconstrained" and encode as (with "L:" preceding the length determinant - if any - and "C:" preceding the contents encoding - if any): 

```yaml
integer1: L:P00000010 C:00010000 00000000
integer2: L:P00000001 C:01111111
integer3: L:P00000001 C:10000000
integer4: L:P00000010 C:00000000 10000000 
```

This is the same as BER (for values up to 127 octets), but without the identifier octets. Remember that in the UNALIGNED variant P bits are never inserted. 

## 11.2 Semi-constrained integer types

Once we have a lower bound (which will typically be zero or one, but could be anything) then we only need to encode a positive value, using the offset from the base as the value to be encoded. 

Encode the (positive) offset from the lower bound. 

As for unconstrained integer types, the encoding is into the minimum necessary multiple of eight bits preceded by a length determinant counting the number of octets. So: 

```txt
integer5 INTEGER (-1.. MAX) ::= 4096
integer6 INTEGER (1 .. MAX) ::= 127
integer7 INTEGER (0 .. MAX) ::= 128 
```

encode as: 

```yaml
Integer5: L:P00000010 C:00010000 00000001
Integer6: L:P00000001 C:01111110
Integer7: L:P00000001 C:10000000 
```

(Compare the encoding of integer7 with that of integer4.) 

## 11.3 Constrained integer types

It is in the encoding of integers with both a lower and an upper bound that PER tries hardest to "do the sensible thing". However, "the sensible thing" as determined by the proponents of the UNALIGNED variant turned out to be different from "the sensible thing" as determined by the proponents of the ALIGNED version, so the approaches are not quite the same. Which is the most sensible, you must judge! 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/8005424648fbe349266b1ecd5c6751a3825a98954104fa3279482655a97f55eb.jpg)


The standard talks about the "range" of the values, defining the "range" as the upper-bound minus the lower-bound plus 1. So a constraint of (0..3) has a "range" of four. Thus "range" is essentially defined as the total number of values between (and including) the upper and lower bounds. 

If the "range" is one, then only one value is possible. This is not likely to occur in practice, but the encoding follows naturally from the treatment of larger ranges and is similar to the handling of NULL: there are no bits in the encoding! 

We first describe all the cases that can arise, then we give examples. 

For larger ranges, the UNALIGNED case is the easiest to describe. It encodes the offset from the lower bound into the minimum number of bits needed to support all values in the range. So a constraint of (1..3) - or (6..8) or (11..13) or (-2..0) - has a range of three, and values will encode into a bit-field of 2 bits (as would a range of 4). A constraint of (0..65535) will produce encodings of all values into exactly 16 bits, and so on. Remember that with the UNALIGNED variants, there are never any padding bits, so in this last case successive integers in the encoding of SEQUENCE OF INTEGER (0..65535) will all be 16 bits long, but may all be starting at bit 3 (say) of an octet. 

## The ALIGNED case is a bit more varied!

If the range is less than or equal to 255 (note: 255, not 256), then the encoding is into a bit-field which is the minimum necessary to encode the range, and there will be no padding bits. If, however, the range is 256 - for example, the constraint might be (0..255) or (1..256) - then the value encodes into eight bits, but they go into an octet-aligned field - we get padding bits if necessary. 

If the range is greater than 256 but no greater than 64K, we get two octets (octet-aligned). 

If we need to go over two octets (the range is more than 64K), we encode each value (as a positive integer offset from the lower bound) into the minimum number of octets necessary (except that zero always encodes into an octet of all zeros, not into zero bits, so we always have a minimum of one octet), and prefix a length determinant giving the number of octets used. In this case, however, the general length determinant described earlier is not used! Instead, we look at the range of values that this octet count can take (lower bound one, remember, because zero encodes into one octet), and encode the value of the length in the minimum number of bits needed to encode a positive number with that range, offset from one. 

Let's have some examples. What follows is not correct value notation - for compactness of the examples, we give a value, then a comma, then another value, etc, and use commas to separate the encodings in the same way. 

```txt
integer8 INTEGER (3..6) ::= 3, 4, 5, 6
integer9 INTEGER (4000..4254) ::= 4002, 4006
integer10 INTEGER (4000..4255) ::= 4002, 4006
integer11 INTEGER (0..32000) ::= 0, 31000
integer12 INTEGER (1..65538) ::= 1, 257, 65538 
```

will encode as follows: 

```txt
integer8 C:00, C:01, C:10, C:11
integer9 C:00000010, C:00000110
integer10 C:P00000010, C:P00000110
integer11 C:P00000000 00000000, C:P01111001 00011000
integer12 (UNALIGNED) C:0 00000000 00000000,
    C:0 00000001 00000000,
    C:1 00000000 00000001
(ALIGNED) L:00 C:P00000000,
    L:01 C:P00000001 00000000,
    L:10 C:P00000001 00000000 00000001 
```

You will see that where there is no length determinant, the field is the same size for all values of the type, and can be deduced from the type notation. (If this were not true, PER would be a bust specification!) Where the field size varies, a length determinant is encoded so that the decoder knows the size of the field, with the length of the length determinant the same for all values, and again derivable from the type definition. As stated earlier, these are necessary conditions for an encoder and decoder to be able to interwork. Study these examples! 

There is one further (and final) case for encoding the ALIGNED variant of a constrained integer: If the number of octets needed to encode the range of the integer value exceeds 64K ..... Need I go on? This will never ever arise in practice! But if it did, then a general length encoding is used, and the fragmentation procedures discussed earlier come into place. 

## 11.4 And if the constraint on the integer is extensible?

There is nothing new or unexpected here. The principles of encoding extensible types have been discussed already. 

But let's have some examples: 

It's just the usual one bit up-front, a constrained encoding if in the root, and an unconstrained encoding otherwise. 

```txt
integer13 INTEGER (MIN .. 65535, ..., 65536 .. 4294967296) ::= 127, 65536
integer14 INTEGER (-1..MAX, ..., -20..0) ::= 4096, -8
integer15 INTEGER (3..6, ..., 7, 8) ::= 3, 4, 5, 6, 7, 8
integer16 INTEGER (1..65538, ..., 65539) ::= 1, 257, 65538, 65539 
```

will encode as (the "extensions bit" has "E:" placed before it for clarity): 

```txt
integer13: E:0 L:P00000001 C:0111111,
E:1 L:P00000011 C:00000001 00000000 00000000
integer14: E:0 L:P00000010 C:00010000 00000001,
E:1 L:P00000001 C:11111000
integer15: E:0 C:00, E:0 C:01, E:0 C:10, E:0 C:11,
E:1 L:P00000001 C:00000101,
E:1 L:P00000001 C:00001000
integer16: (UNALIGNED) E:0 0 00000000 00000000,
E:0 0 00000001 00000001,
E:0 1 00000000 00000001,
E:1 L:00000011 C:00000001 00000000 0000010
(ALIGNED) E:0 L:00 C:P0000000,
E:0 L:01 C:P0000001 0000000,
E:1 L:12 C:P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2P2 
```

OK - Now you know it all! It is not difficult, but there are a lot of cases to remember. Come back BER! All the other types are much more straightforward! No doubt you will want to write notes on this lot, and hope that your examination is an Open Book examination! But by now (if you got this far!) you should certainly have a very good understanding of the principles involved in the PER encodings. 

## 12 Encoding ENUMERATED values.

First we consider the encoding of an enumerated type that is not marked extensible (and remember, the encoding of an extensible type for a value that is in the root is just the same except that it is preceded by an extensions bit set to zero). Encoding of enumerations outside of the root are covered later. 

The numerical value associated with an enumeration is always bounded above and below. Moreover, it is possible to order the enumerations into ascending order (even if some have negative associated values), and then to re-number each enumeration from zero upwards. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/0162e80d544493a88338e4c69663891f03283a7cc5d2fbaab118b4ede1015f52.jpg)


This gives us a compact set of integer values (called the enumeration index) with a lower and an upper bound. Any value of the enumerated type now encodes like the corresponding constrained integer. 

In principle, all possible constrained integer encodings are possible, but in practice, definitions of enumerated types never have more than a few tens of enumerations - usually much less, so we are essentially encoding the enumeration index into a bit-field of size equal to the minimum necessary to cope with the range of the index. 

If the enumeration is extensible, then enumerations outside the root are again sorted by their associated numerical value, and are given their own enumeration index starting at zero again. (Remember, the extensions bit identifies whether an encoded value is a root one or not, so there is no ambiguity, and starting again at zero keeps the index values as small as possible). For a value outside the root, the encoding is the encoding of the enumeration index as a "normally small nonnegative whole number" described earlier. 

No doubt you want some examples! Here goes (with a way-out example first!) - and again we use commas to separate lists of values and of encodings, for brevity: 

```txt
enum1 ENUMERATED {red(-6), blue(20), green(-8)}
    ::= red, blue, green
enum2 ENUMERATED {red, blue, green, ..., yellow, purple}
    ::= red, yellow, purple

These encode as:

enum1: C:01, C:10, C:00
enum2: E:0 C:00,
E:1 C:0000000, (These are the "normally small"
E:1 C:0000001 encodings of zero and one.
Note the absence of a "P")

If we had more than 63 extension additions .... No! I am not going to give an example for that. It won't happen! Produce your own example! (You have been told enough to be able do it). 
```

## 13 Encoding length determinants of strings etc

The "etc" in the heading of this clause refers to iteration counts in SEQUENCE OF and SET OF. 

Remember that for iteration counts, the length determinant encodes the number of iterations, for the length of bitstrings it encodes the number of bits, for the length of knownmultiplier character strings it encodes the number of abstract characters, and for everything else it encodes the number of octets. 

<table><tr><td>A length determinant which is constrained by an effective size constraint encodes in exactly the same way that an integer with an equivalent constraint would encode (well, almost - read the details below if you wish!).</td></tr></table>

A length determinant can, however, have values which are constrained by an effective size constraint, and in many ways we can view this as similar to the situation when an integer value (a count) is constrained by a direct constraint on the integer. 

Note that we are here talking only about lengths of strings or iteration counts - the form of the length determinant for integer values has been fully dealt with (and illustrated) earlier. We have also discussed earlier the general case of a length determinant where there are no PER-visible size constraints. So in this clause we are talking only about the case where there is an effective size constraint, and as in earlier clauses, we consider first the case of a constraint without an extension marker (which also applies to encoding counts within the root if there is an extension marker). 

The discussion of length encodings for strings etc has been deliberately delayed until after the description of integer encodings was given, and the reader may like to review that description before reading on. 

A length or iteration count is basically an integer value, except that it is always bounded below (by zero if no other lower bound is specified), so if we need to encode the lengths of strings, we can draw on the concepts (and the text!) used to describe the encoding of values of the integer type. For a semi-constrained count (no upper bound), it would be pointless to encode a semi-constrained integer value (with its "length of length" encoding), and instead a general length determinant as described in Clause 8 is encoded. 

For a constrained count, where the count is restricted to a single value (a fixed length string, for example, or a fixed number of iterations in a sequence-of), then there is no length determinant - we simply encode the contents. Otherwise, we need a length determinant. 

For a constrained count, the count is encoded (in both the ALIGNED and UNALIGNED versions) exactly like the encoding of a corresponding constrained integer, except where the maximum allowed count exceeds 64K. In this latter case the constraint is ignored for purposes of encoding, and a general length determinant is used, with fragmentation into 64K hunks (as described in Clause 8) if the actual value has more than 64K bits, octets, iterations, or abstract characters. 

Finally, we need to consider an extensible constraint. If the effective size constraint makes the type extensible, then the general provisions for encoding extensible types discussed earlier apply to the type as a whole - we don't encode an extensible integer for the length determinant. So we get the extensions bit up-front saying whether the count (and any other aspect of the value, such as the alphabet used) is in the root, and if so we encode the count according to the size constraint on the root. If not, then the extensions bit is set to one and a general length determinant is used. 

So to summarise: 

• With no PER-visible size constraint, or a constraint that allows counts in excess of 64K, we encode a general length determinant. 

• For abstract values outside the root, a general length determinant is again used. 

With a size constraint that gives a fixed value for the count, there is no length determinant encoding. 

• Otherwise, we encode the count exactly like an integer with the equivalent constraint. 

We illustrate this with some IA5String examples, but remember that the same length determinant encodings also apply to iteration counts etc. In the examples you will see "P" for padding bits in the contents. These are a consequence of the main type being IA5String with more than two characters, and would not be present if we had used BIT STRING for the examples (or if we had an IA5String whose length was restricted to at most two characters - see later). Where padding bits are shown in the length determinant, these would be present for all types. We give the E: and L: fields in binary, but the C: fields in hexadecimal, for brevity. 

If the reader wants some exercise, then try writing down the encodings of each value before reading the answers that follow! (For very long strings, we indicate the contents with the count in characters in brackets, and do the same when giving the encoding). 

With the following value definitions: 

```txt
string1 IA5String (SIZE (6)) ::= "012345"
string2 IA5String (SIZE (5..20)) ::= "0123456"
string3 IA5String (SIZE (MIN..7)) ::= "abc"
string4 IA5String ::= "ABCDEFGH"
string5 IA5String (SIZE (0..7, ..., 8)) ::= "abc", "abcdefgh"
string6 IA5String (SIZE (65534..65535)) ::= "(65534 chars)"
string7 IA5String (SIZE (65537)) ::= "(65537 chars)" 
```

we get the following encodings (using hex or binary as appropriate): 

```yaml
string1: C:P303132333435
string2: L:0001 C:P30313233343536
string3: L:011 C:P616263
string4: L:P00001000 C:4142434445464748
string5: L:011 C:P616263,
    L:P00001000 C:6162636465666768
string6: L:0 C:(65534 octets)
string7: L:P11000100 C:(65536 octets) L:P00000001 C:(1 octet) 
```

## 14 Encoding character string values.

## 14.1 Bits per character

We have discussed above the encoding of the lengths of strings. To recap, the length determinant gives the count of the number of abstract characters for the "known multiplier" character string types, and of octets for the other character string types. 

In the case of the known multiplier character string types, the number of bits used in the encoding of the UNALIGNED variants of PER is the minimum needed to represent each character unambiguously. For the ALIGNED versions, the number of bits for each character is rounded up to a power of two (one, two, four, eight, sixteen, etc), to ensure that octet alignment is not lost between characters. 

<table><tr><td>Encoding of known multiplier character strings uses the minimum number of bits for each character, except that in the ALIGNED variants this number is rounded up to a power of two, to avoid losing alignment.</td></tr></table>

The known multiplier types, with the number of characters that the unconstrained type is defined to contain (and the number you need to exclude to improve the encoding in the UNALIGNED variants) are: 

<table><tr><td>Type name</td><td>Number of chars</td><td>Number of reductions needed for better encoding</td></tr><tr><td>IA5String</td><td>128 characters</td><td>64</td></tr><tr><td>PrintableString</td><td>74 characters</td><td>10</td></tr><tr><td>VisibleString</td><td>95 characters</td><td>31</td></tr><tr><td>NumericString</td><td>11 characters</td><td>3</td></tr><tr><td>UniversalString</td><td>2**32 characters</td><td>2**31</td></tr><tr><td>BMPString</td><td>2**16 characters</td><td>2**15</td></tr></table>

For all other character string types, the length determinant gives the count in octets, because the number of octets used to represent each character can vary for different characters. In this latter case, constraints are not PER-visible, and the encoding of each character is that specified by the base specification, is outside the scope of this chapter, and is the same as for BER. 

All that remains is to discuss the encoding of each character in the known multiplier character string types, as the encoding of these characters is affected by the effective alphabet constraint (see Clause 6), and to see when octet-aligned fields are or are not used for character string encodings. Again we see differences between the ALIGNED and the UNALIGNED variants, but the encodings are what you would probably expect, or have invented yourself! 

Each of the known multiplier characters string types has a canonical order defined for the characters, based on the numerical value in the BER encoding (the ASCII value for IA5String, 

PrintableString, VisibleString, and NumericString, the UNICODE value for BMPString, and the ISO 10646 32-bit value for characters outside the Basic Multi-lingual Plane for UniversalString). These values are used to provide a canonical order of characters. The values used to encode each character are determined by assigning the value zero to the first abstract character permitted by the effective alphabet constraint, one to the second, etc. The last value used is n-1 if there are n abstract characters permitted for the type (using only PER-visible constraints in this determination). There are a minimum number of bits needed to encode the value n-1 as a positive integer, and in the UNALIGNED variants, this is exactly the number of bits used to encode each character. For example: 

$$
\begin{array}{l l} \text {Type definition} & \text {No of bits per char} \\ \text {My - chars1}: := \text {IA5String (FROM ("T"))} & \text {Zero} \\ \text {My - chars2}: := \text {IA5String (FROM ("TF"))} & \text {One} \\ \text {My - chars2}: := \text {UniversalString (FROM ("01"))} & \text {One} \\ \text {My - chars2}: := \text {NumericString (FROM ("01234567")} & \text {Three} \end{array}
$$

Note that in the above, the actual base type being constrained could be any of the known-multiplier character string types, and the result would actually be just the same encoding! You effectively design your own character set, and PER then assigns an efficient encoding for each character. 

For the ALIGNED variants, the number of bits used is always rounded up to a power of two - zero, one, two, four, eight, sixteen, thirty-two, to ensure that octet alignment is not lost within the string. 

There is one small exception to this mapping of values to new values for encoding. The original set of characters have associated values with some "holes" in the middle (in general). If remapping the original values to a compact range from zero to n-1 does not produce a reduction in the number of bits per character in the PER encoding (for whichever variant is in use), then the remapping is not done, and the original associated value is used in the encoding. In practice, this means that remapping is more likely for UNALIGNED PER than for ALIGNED PER (where the number of bits per character is always a power of two), except in the case of NumericString, where the presence of "space" means that for both variants (even with no constraints), remapping takes place, reducing the encoding to a maximum of four bits per character. 

So with: 

$$
\text { My - Boolean   }:: := \text { IA5STRING   (FROM  ("TF"))(SIZE(1))}
$$

The encoding would be a single bit in a bit-field (with no length encoding) - in other words, it would be identical to the encoding of a BOOLEAN! 

## 14.2 Padding bits

When do we get padding bits in the ALIGNED case? Here we need to look at the combination of the effective size constraint (which restricts the number of abstract characters in every value) and the effective alphabet constraint (which determines the number of bits used to encode each character). If the combination of these is 

<table><tr><td>No padding if the size is constrained so that an encoded string value never exceeds 16 bits.</td></tr></table>

such that the total encoding size for a value of this constrained type can never exceed sixteen bits, then there are no padding bits. The character string value is encoded into a bit-field. If, however, there are some values which might require more than 16 bits, then the encoding is into an octetaligned bit-field, and no character will cross an octet boundary (in the ALIGNED case). 

Some examples of character strings whose encodings do not produce padding bits: 

```autohotkey
String1 ::= NumericString (SIZE (0..4))
String2 ::= IA5String (FROM ("TF")) (SIZE (0..16))
String3 ::= IA5String (SIZE (0..2))
String4 ::= BMPString (SIZE (0..1)) 
```

Again, this rule of "16 bits" maximum is another example of PER being pragmatic. The limit could just as well have been set at 32, or 64 bits. The philosophy is that for short strings we do not want to force alignment, but that for long strings doing alignment at the start of the string (and then maintaining it) is on balance the best decision. 

## 14.3 Extensible character string types

The encoding of an extensible (by PER-visible constraints) known-multiplier character string type follows the normal pattern - an extensions bit set to zero if in the root, one otherwise, then the optimised encoding described above for root values, and an encoding of the unconstrained type (with a general length determinant) if we are not in the root. (Note, however, That mapping of associated values to produce a 4-bit encoding still occurs for an unconstrained NumericString). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/036face1d9860911dd5c4c8ac01b23548d783d02d4c9e661e274195a7cdc4441.jpg)


All the above applies only to the known-multiplier types. For the other character string types, there is never an extensions bit, the general encoding always applies for all values. 

Finally, note that there is no concern in determining encodings of whether a known-multiplier type is extensible for alphabet or for size constraints. All that matters is whether or not PER-visible constraints make it extensible, and what the effective alphabet and effective size constraints for the root then are. The encoding is totally determined by that. 

## 15 Encoding SEQUENCE and SET values.

For a SEQUENCE without an extension marker, earlier text (Clause 9) has described the encoding. There is up-front a preamble (encoded as a bit-field, not octet-aligned), with one bit for each element that is OPTIONAL or DEFAULT, set to one if there is an encoding present for a value of that element, to zero otherwise. Then there is simply the encoding for each element. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/5b1a4731eebf31875fcd51aada444fd1533380bd73bfc414709aba0e882c8a80.jpg)


We have also discussed earlier the use of tags to provide a canonical order for the elements of a SET, which then encodes in exactly the same way as a SEQUENCE. 

We are left in this clause to discuss when/whether values equal to a DEFAULT value are required to be present, or required to be absent, or whether we have an encoder's option. We also need to discuss the way extension additions are encoded. 

But first, let's have an example of encoding a value of a simple sequence type. The example is shown in Figure III-26 and the encoding in Figure III-27. The OPTIONAL/DEFAULT bit-map is preceded by "B:", contents by "C:", length determinant by "L:", and one or more padding bits by "P", as in earlier examples. 

```txt
my-sequence-val
SEQUENCE
{item-code INTEGER (0..254),
item-name IA5String (SIZE (3..10))OPTIONAL,
urgency ENUMERATED
{normal, high} DEFAULT normal }
::= {item-code 29, item-name "SHERRY"} 
```

```txt
B:10 (item-name present, urgency missing)
C:00011011 (value of item-code)
L:011 C:P534845525259 (length and value of item-name)

Figure III-27 Encoding of the sequence value 
```

It is worth noting that the total length of this PER encoding is seven octets. In BER (assuming the encoder takes the option of encoding default values and always using a 3-octet definite length field, both on the grounds of simplicity), we get a total of 24 octets. If the encoder is more bandwidth conscious and omits the encoding of the default value and uses short definite lengths (which suffice in this case), BER will produce 13 octets. 

## 15.1 Encoding DEFAULT values

Here we find some differences between CANONICAL-PER (which is fully canonical), and BASIC-PER (which has encoder's options in complex cases that rarely arise). 

For both encoding rules, if the actual value to be encoded equals the default value for "simple types" (defined as anything that is not a SET, SEQUENCE, SET OF, SEQUENCE OF, CHOICE, EMBEDDED PDV, EXTERNAL or unrestricted character string type, then the encoder is required to omit the encoding in both CANONICAL-PER and in BASIC-PER (both are canonical). 

However, for the types listed above, CANONICAL-PER again requires omission if the value equals the default value, but BASIC-PER leave it as an encoder's option, making it unnecessary to do a possibly complex run-time check for equality of a value with the DEFAULT value. 

## 15.2 Encoding extension additions

The general principles of encoding extensible types applies: we have an extensions bit up front (before the bit-map of OPTIONAL or DEFAULT elements) which is set to zero if the abstract value is in the root, one otherwise. 

Extension additions tend in practice to be marked OPTIONAL (or DEFAULT), but this is not a requirement. If in Version 2, one addition was not so marked, then Version 2 systems would always have to encode additions, and would always have the extensions bit set to one. Only version 1 systems would set it to zero. 

Values for extension additions are always encoded at the position of the insertion point, and a decoder expects such encodings if the extensions bit is set to 1, not otherwise. 

First, we must recap about extension additions in a SEQUENCE. These may be either a single element (called an extension addition type), or a group of elements contained in version brackets (called an extension addition group). 

The easiest way to describe the handling of an extensions addition group (and the way it is described in the specification), is for the reader to mentally replace the entire group of elements and the version brackets with a single OPTIONAL SEQUENCE, whose elements are the elements of the addition group. There is just one rider: if all elements of the group are to be omitted in the encoding (they are all marked OPTIONAL or DEFAULT), then there is no encoding for the entire SEQUENCE, and the outer-most OPTIONAL bit-map would record its absence. (An example of this is given later). 

We have now reduced the problem to a simple list of extension addition types, some or all of which may be marked OPTIONAL, and hence may be missing in an encoding. As with elements in the root, a decoder needs to know which elements are present in the encoding, and which are not, and once again a bit-map is used. The problem in this case, however, is that Version 1 systems will not know how many extension addition types there are in the specification, and hence will not know the length of the bit-map. Moreover, such systems will not know whether an extension addition type was marked optional or not. This produces two differences from the bit-map used for the root elements: 

• The bit-map contains one bit for every extension addition type, whether it is marked optional or not, recording its presence or absence in the encoding. 

• The bit-map is preceded by a count giving the number of bits in the bit-map. 

The count for the bit-map length is encoded as a normally small whole number. 

The effect of encoding the count as a normally small whole number is that there is again provision for fragmenting the extension additions bit-map into 64K fragments if the number of extension additions exceeds 64K. With the presence of version brackets, where additions are unlikely to occur at less than about one year intervals, a "not supported" response from a tool would be wholly appropriate! 

Following the bit-map, we encode the value of the extension addition types, but in this case a Version 1 system does not know the actual types involved, and would not be able to find the end of the encoding of an extension addition, so each of the extension addition types is "wrapped up" with a preceding length determinant. The situation is slightly worse than this, however. What should the length determinant count, given that the decoder does not know the type that is wrapped up? Clearly the only possibility is bits or octets, and octets was chosen. 

So each extension addition type is treated as if it were an outer- level type being encoded. If it is present, but has zero bits (not likely to arise - a NULL, for example), then it encodes to a one-bit. It then has zero padding bits added at the end to make it up to an integral number of octets and is then added to the encoding preceded by a general length determinant (which, remember, is octet aligned). 

This "wrapping up" then can be quite expensive on bandwidth, and it was for this reason (mainly) that "version brackets" were introduced. Because all the elements in a version bracket encode (optimally) as the elements of an OPTIONAL SEQUENCE which is treated as a single extension addition, we get only one "wrapper" instead of one for each element. 

```txt
my-sequence-val
SEQUENCE
{item-code INTEGER (0..254),
item-name IA5String (SIZE (3..10))OPTIONAL,
... !1 -- see para 14.6 for exception handling --,
urgency ENUMERATED {normal, high} DEFAULT normal,
[[ alternate-item-code INTEGER (0..254),
alternate-item-name IA5String (SIZE (3..10))OPTIONAL ]] }
::= {item-code 29, item-name "SHERRY",
urgency high, alternate-item-code 45,
alternate-item-name "PORT" }
Figure III:28: An extended sequence value for encoding 
```

The "wrapping up" also has a significant implementation cost, in that it requires the complete encoding (or at least the first 64K octets thereof) of the extension addition to be produced and any necessary padding bits inserted, before the length wrapper count is known and can be encoded. (This is similar to the problem of the use of the long definite form in BER to encode the length of a SEQUENCE, rather than the indefinite form). There is, however, no alternative to this wrapping up if we want interworking between Version 2 and Version 1 systems (unless we go back to a TLV approach for everything). 

```txt
E:1 (extensions bit SET)
B:1 (item-name present)
C:00011011 (value of item-code)
L:011 C:P534845525259 (length and value of item-name)
L:000010 B:11 (length - normally small whole number and value of extensions bit-map)
L:P0000001 C:10000000 (general length and padded value of urgency)
L:P00000011 (general length of version bracket addition)
C:00101101 (alternate-item-code)
L:001 C:P504F5254 (length and value of alternate-item-name) 
```

Figure III-29: The encoding of the extended sequence value 

Now for an example of encoding an extensible SEQUENCE with one extension addition type and one extension addition group added. (We base this on the earlier sequence type example.) Figure III-28 shows the value to be encoded, and Figure III-29 shows the encoding (the notation used is the same as in earlier examples of encodings). 

This gives a total of 18 octets. Again, if we take the worst case BER encoding as described earlier, this gives 37 octets, and the best case gives 25. 

## 16 Encoding CHOICE values.

The encoding of choice indexes for both root alternatives and for those outside the root has been fully described earlier. The only remaining point to note is that here, as for sequence, if the chosen alternative is outside the root a Version 1 system will not be able to find the end of it, so we again have a "wrapper", encoded in exactly the same way as extension additions in a SEQUENCE or SET. 

Here we give one example of each of these cases. 

Note that version brackets are permitted in choice type extensions, but they do not affect the encoding, and serve purely as a documentation aid for humans. What matters is simply the list of added alternatives, each of which must have distinct outer-level tags, even if they are in different version brackets. 

The values to be encoded are shown in Figure III-30 (assume an environment of automatic tags) and the encodings are shown in Figure III-31, where "I:" is used to introduce the choice index encoding. 

```txt
Choice-example ::= CHOICE
{normal NULL,
high NULL,
... !2 -- see para 14.6 for exception handling --
medium NULL }

first-choice Choice-example ::= normal:NULL
second-choice Choice-example ::= medium:NULL

Figure III-30: Two choice values for encoding 
```

```txt
first-choice: E:0 I:0 C: (a total of two bits)
second-choice: E:1 (extensions bit set)
C:000000 (index as a normally small
whole number)
L:P00000001 (general length "wrapper")
C:00000000 (padded encoding of NULL)

Figure III-31: The encodings of the choice values 
```

In this example, worst case BER encodes with four octets in both cases, and best-case BER with two octets. PER took three octets in the second. This is just one of a small number of cases where PER can actually produce worse encodings than BER, but this is not often the case! 

## 17 Encoding SEQUENCE OF and SET OF values.

There is nothing more to add here. There is a length determinant upfront giving the iteration count. The form of this (depending on any SIZE constraint on the SEQUENCE OF or SET OF) has been fully discussed earlier. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/a49acbd3f7ab7df30215c675dfe690ed1ecdec71d1809905760ab0a825962d83.jpg)


Note that these types may have a SIZE constraint in which there is an extension marker. As usual, values outside the root encode as if there were no size constraint. 

Two examples are shown in Figures III-32 and III-33. The numbers have been kept deliberately small for ease of illustration. Note that in the example both the iteration count and the type being iterated are extensible. For a value of the SEQUENCE OF to be in its root only requires the iteration count to be within the root. The fact that the integer value 4 is outside the root of the INTEGER in the third iteration is flagged in the encoding of the INTEGER, and does not affect the extensions bit for the SEQUENCE OF. 

My-sequence-of SEQUENCE (SIZE(1..4), ..., 4) OF INTEGER (0..3, ..., 4) 

My-value-1 My-sequence-of ::= {1, 3, 4} 

My-value-2 My-sequence-of ::= {1, 2, 3, 4} 

Figure III-32: Two SEQUENCE OF values for encoding 

```lisp
My-value-1:
E:0 (extensions bit)
L:10 (iteration count of 3)
E:0 C:01 (value 1)
E:0 C:11 (value 3)
E:1 L:P0000001 C:00000100 (value 4)
My-value-2:
E:1 (extensions bit)
L:P00000011 (iteration count of 4)
E:0 C:01 (value 1)
E:0 C:10 (value 2)
E:0 C:11 (value 3)
E:1 L:P00000001 C:00000100 (value 4) 
```

Figure III-33: The encodings of the two SEQUENCE OF values 

## 18 Encoding REAL and OBJECT IDENTIFIER values.

The box says it all! We have a general length determinant giving a count in octets, then for REAL (for both BASIC-PER and CANONICAL-PER) the contents octets of the CER/DER encoding of REAL (they are the same). For OBJECT IDENTIFIER encodings, the specification actually references the BER encoding, but the CER/DER encodings are exactly the same. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/da5ed63c22643aebe78dba69c293ba1f5b0703e97187376d539cf0313eb768d6.jpg)


## 19 Encoding an Open Type

We have discussed the form of an outer-level encoding, and of a general length determinant to provide a "wrapper" for extensions in sequence and set and choice types. Exactly the same mechanism is used to wrap up an Open Type (a "hole" that can contain any ASN.1 type). In general, the field of the protocol which tells a decoder what type has been encoded 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/7972b18a98ccce91d4c3806b63e47767d268e588eddd3cd41930d4303ed457fb.jpg)


into the "hole" - into the Open Type field, may appear later in the encoding than that field, but with PER a decoder will be unable to find the end of the encoding in the "hole" without knowing the type. (Contrast BER, where there is a standard TLV wrapper at the outer level of all types, and where no additional wrapper is needed nor used). So in PER the wrapper is essential in the general case, and is always encoded. 

The inclusion of a wrapper in PER Open Types has been exploited by some applications to "wrap-up" parts of an encoding, even tho' it is not strictly necessary to do so. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/f85c1dc0b626565b62d37b4ad8ae076378de45b34c32a256462e15bb304f4ad4.jpg)


Consider an element of a large SEQUENCE consisting of: 

## security-data SECURITY-TYPES.&Type (Type1)

This is an example of a "type constraint" on an Open Type, and the reader was referred to this clause for an explanation of its usefulness. 

From the point of view of abstract values, this is exactly equivalent to: 

## security-data Type1

The PER encoding, however, will have a wrapper round Type1 in the first case, not in the second (type constraints are not PER-visible). 

This can be useful in an implementation, because it enables the main body of the protocol to be dealt with in an application-specific way, leaving the security data unwrapped and unprocessed, passing it as a complete package to some common "security kernel" in the implementation. 

It is generally only in the security field that specifiers use these sorts of construct. 

## 20 Encoding of the remaining types

GeneralizedTime, UTCTime, ObjectDescriptor, all encode with a general length determinant giving an octet count, and contents the same as BER or CER (for BASIC-PER and CANONICAL-PER respectively). Notice that this is the fourth occurrence where BASIC-PER is not canonical, in the interests of simplicity - the other three are: 

```txt
At last! The final clause describing PER encodings. I wish this book was a Web site, so that I could see how many people had read all the way to here! Well done those of you that made it! 
```

• Encoding values of a set-of type. 

• Encoding GeneralString and related character string types. 

• Encoding a DEFAULT element (which is not a simple type) in a sequence or set type. 

Canonical PER is, of course, always canonical. 

That just leaves types which are defined using the "ValueSetTypeAssignment" notation, that is, notation such as: 

```txt
MyInt1 INTEGER ::= { 3 | 4 | 7}
MyReal1 REAL ::= {0 | PLUS-INFINITY | MINUS-INFINITY} 
```

These are equivalent to: 

```txt
MyInt2 ::= INTEGER (3 | 4 | 7)
MyReal2 ::= REAL (0 | PLUS-INFINITY | MINUS-INFINITY) 
```

Initially the PER standard overlooked the specification of these types, but a Corrigendum was issued saying that they encode using this transformation. 

## 21 Conclusion

In a chapter like this, it seems important to emphasise that neither the author nor any of those involved in publishing this material can in any way be held liable for errors within the text. 

Caveat Emptor! 

The only authoritative definition of PER encodings is that specified in the Standards/Recommendations themselves, and anyone undertaking implementations should base their work on those primary documents, not on this tutorial text. 

Nonetheless, it is hoped that this text will have been useful, and will help implementors to more readily read and to understand the actual specifications. 

The reader should now have a good grasp of the principles used in PER to provide optimum encodings, but tempered by pragmatic decisions to avoid unnecessary implementation complexity. 

Some things may appear to be unnecessarily complex, such as fragmenting bit-maps if they are more than 64K, or encoding zero bits if an INTEGER is restricted to a single value, as such things will never occur in the real world. These specifications, however, result from applying a general principle (and general code in an implementation) to a wider range of circumstances, and are not extra implementation complexity. 

We have also seen in the examples how PER encodings achieve significant gains over BER in verbosity, and even greater gains if sensible use of constraints has been made in the base specification. 

There is just one more chapter to come in this section (very much shorter than this one!). That discusses some other encoding rules that never quite made it (or have not yet made it!) to becoming International standards, and the advantages and (mainly) disadvantages of "rolling your own" encoding rules. 

# Chapter 4 Other ASN.1-related encoding rules

(Or: So you have special requirements?) 

## Summary:

This chapter briefly describes other proposals for ASN.1 encoding rules that have been made from time to time. None of these are currently on a path for International Standardization as part of the ASN.1 specifications, and this chapter can safely be omitted by all but the intellectually curious. It is of no interest to most readers concerned with "What is ASN.1, how do I write it, and how do I implement protocols defined using it." But it does give an (incomplete) picture of other attempts to enhance the ASN.1 notation with different encoding rules. 

The order of coverage is not time order (saying when the germ of an idea first appeared within a sometimes closed community is not easy), but is basically random! The following are briefly mentioned: 

• LWER - Light-Weight Encoding Rules 

• MBER - Minimum Bit Encoding Rules 

• OER - Octet Encoding Rules 

• XER - XML (Extended Mark-up Language) Encoding Rules 

• BACnetER - BAC (Building Automation Committee) net Encoding Rules 

• Encoding Control Specifications (ECS) 

No doubt there are others lurking out there! 

## 1 Why do people suggest new encoding rules?

As a basic work-horse, it is doubtful if BER can be bettered. It is simple, straight-forward, and robust. If you keep its basic "TLV" approach, there are few improvements that can be made. 

But it was clear in 1984 that it should be possible to encode more efficiently 

In the beginning there was chaos. And the greater Gods descended and each begat a new Standard, and the people worshipped the Standards and said "Give us more, give us more!" So the greater Gods begat more Standards and more and more, and lo, there was chaos once more! 

than BER, and several attempts were made prior to or around the time of the introduction of PER to produce essentially PER-like encodings. To avoid a proliferation of encoding rules, PER should have been developed and standardised in the late 1980s, not the early 1990s, but it wasn't! So several "industry-specific" encoding rules emerged to fill the vacuum. 

Currently, major tool vendors support only BER and PER. Support for other encoding rules for particular industry-specific protocols (supporting only the types used in those protocols, rather than all ASN.1 types) by a library of routines to perform specific parts of the encoding (not by an ASN.1 compiler, as defined and described in Section I Chapter 6) does however exist. 

Producers of new encoding rules often claim either less verbosity on the line than BER, or greater simplicity than PER (or both!). 

But to-date, the standardizers of ASN.1 have not considered any of the alternative encoding rule drafts that have been submitted to have sufficient merit to progress them as standards within the ASN.1 suite. 

That is not to say that they are (for example), necessarily on balance inferior to PER - everyone accepts that if you started again with what you know now, PER could be improved - but providing another standard for encoding rules that was very similar to PER and only a marginal improvement on it would not make any sort of sense. Tool vendors would not want to support it, and of course existing implementations of protocols would have to be considered. The ASN.1 encoding rules have a high degree of inertia (the notation can be changed much more easily) because of the "bitson-the-line" that are flowing around the world every minute of every day. 

Nonetheless, there continue to be attempts to provide slightly different encoding rules to support a particular protocol for a particular industry, usually proposed by some consultancy or software house associated with that industry, in the hope that those encoding rules will become the de facto standard for that industry. Such encoding rules rarely, however, achieve the market demand that leads to their incorporation in the main ASN.1 compiler tools, or ratification as international standards for ASN.1 encoding rules for use across all industries. 

It is, perhaps, a sign of the success of the ASN.1 notation that many industries new to protocol design are choosing to use ASN.1 to define their messages, but perhaps it is the NIH (Not Invented Here) factor that so often leads to desires to cut down the notation, or to produce different encodings for it. Who knows? 

## 2 LWER - Light-Weight Encoding Rules

Light-Weight Encoding Rules were first proposed in the late 1980s when ASN.1 compilers started to emerge, and were from the beginning the subject of much controversy, with the Deutsches Institut für Normung (DIN) strenuously opposing their development as international standards. 

Standards work was approved, but was eventually abandoned - too many problems! 

Suggestions for LWER pre-dated work on PER, and the concern was not with the verbosity of BER, but with the number of CPU cycles required to do a BER encoding. They were approved as a Work Item within ISO, and were being progressed up to the mid-1990s, when they were abandoned (for reasons, see below). 

## 2.1 The LWER approach

The basic idea was simple, and was based on the observation that: 

An ASN.1 compiler generates the pattern for an in-core data structure to hold values of an ASN.1 type (it is usually a whole series of linked lists and pointers to similar structures), defining that in-core data structure using a high-level programming language. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/3d216ed7905ffd119dc76585153bb9a4701d2de3042028c52d724198d9f7865f.jpg)


• Run-time support tree-walks that structure to generate encodings (at some cost in CPU cycles) that are then transmitted down the line. 

• A decoder reproduces a (very similar) in-core structure at the other end of the line. 

Why not simply ship the contents of the in-core data structure directly? That was in essence the LWER proposal. 

## 2.2 The way to proceed was agreed

Early work agreed several key points: 

<table><tr><td>Agree a standard in-core representation of ASN.1 values, and agree how to ship it to another machine. Easy.</td></tr></table>

• The first step was to agree a model of computer memory on which to base the definition of in-core data structures. 

• The second step was to standardise a memory-based in-core structure for holding the values of any ASN.1 type. 

• The third step was to standardise how such a structure was to be transmitted to a remote system. 

## 2.3 Problems, problems, problems

Serious problems were encountered related to all these areas. 

As far as a model of computer memory was concerned, at assembler language level (which noone uses today anyway), memory is made up of addressable units capable of containing integers or pointers to other addressable units or strings of characters (a simplification, but it will do). But the size of those addressable units - bytes, 16-bit words, 32-bit words - hard-ware varies very much. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/8755fa79eaa19aea40f0b25f400376ff62a0642cf0425aa66898979974fa414b.jpg)


And if a structure is defined using such a model, how easy will it be to replicate that structure using the features available in particular high level languages such as Java? 

More significant was the little-endian/big-endian problem. (Named after the characters in Jonathon Swift's Gulliver's travels who fought a war over whether eggs should be broken at their "little-end" or their "big-end"). But in computer parlance, you look at basic hardware architecture and proceed as follows: 

• Assume byte addressing, and draw a picture of your memory with two-byte integers in it. 

• Put an arrow on your picture from low addresses to high addresses. (Some people will have drawn the picture so that the arrow goes left-to right, others the reverse. This is not important, that only affects the depiction on paper.) 

Now write down whether, for each integer, the first byte that you encounter in the direction of the arrow is the least significant octet of the integer (a little-endian machine) or the most significant octet of the integer (a big-endian machine). 

Little-endians will probably have drawn the arrow going left-to-right, and big-endians will probably have drawn it going right-to-left, but as said above, that is not important (both could have drawn a mirror image of their picture). What matters is whether the high-order octet of an integer is at a higher or lower address position than the low-order octet. And remember, what applies to integers also (invariably) applies to fields holding addresses (pointers). 

Unfortunately, both big-endian and little-endian machines exist in the world! 

And if you have an in-core data structure representing an ASN.1 value on a little-endian machine, and you copy that to a big-endian machine, decoding it into a usable from will certainly not be light-weight! 

So we need a big-endian and a little-endian variant of LWER, and you will only be able to use LWER if you are transferring between similar (endian-wise) machines, otherwise you go back to BER or PER. 

But that was all assuming machines with byte addressing, and 16-bit integers and pointers. Now consider the possible permutations of 32-bit integers, or machines that can only (easily) address (point to) 16-bit or 32-bit words ..... 

Suddenly we seem to need rather a lot of variants of LWER! 

This was the basic reason for the DIN opposition to the work - even if standards were produced, they would be useful only for transfers between very restricted families of machine architecture. And add the problems of mirroring those low-level memory-based architectures in high-level languages. Throw in the fact that tool-vendors can, if they wish, define an LWER (separate ones for each machine range that they support) to be used when their own tool is communicating with itself on the same machine range, and what do you get? Probably as much interworking as you would get with LWER! 

What LWER demonstrated was the importance of defining encoding rules (be they character-based or binary-based) that were independent of any given machine architecture - the idea of having something like BER or PER was vindicated. (And of course character-based encodings are also architecture independent.) 

## 2.4 The demise of LWER

Even if the above problems were sorted, there were still issues about what to ship down the line. If the total memory the linked list structures occupied was shipped, empty memory within that total hunk would need to be zeroed 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/1b549f2399019d16c7d94ef47979b5ac3a79794f5db9fa58e8c22caf0b1096e8.jpg)


to prevent security leaks. If empty memory was not shipped, then some form of garbage collection or of tree-walking for transmission would be needed, none of which seemed very light-weight. 

But what eventually killed the LWER work is something that nobody had expected. Implementations of PER began to emerge. Whilst it was expected that PER would produce about a factor of two reduction in the length of an encoding (it did), it was wholly unexpected that it would encode and decode twice as fast! It did the job that LWER was trying to do! 

Once you know, it seems obvious. All the complexity and CPU cycles in PER relates to analyzing the type definition and deciding what the encoding should be. This is either a hand-implementors brain-cycles, or is the compiler phase of a tool. It does not affect run-time CPU cycles. 

At run-time, it is a lot quicker (assuming code has been generated) to pick-up an integer value from a known location, and add the bottom three bits (say) of that integer value to a bit-position in a buffer than it is to generate the T and the L and the V for BER (probably using subroutine calls). 

There were also gains because if you reduce the size of the encoding you reduce the CPU cycles spent in the code of the lower layers of the protocol stack. 

And finally, LWER was conceived in the mid to late 1980s, but machines got faster year-by-year. Gradually the CPU cycles spent in encoding/decoding became insignificant and irrelevant (the application processing for actual protocols also became more complex and time-consuming by comparison). 

LWER was dead. Too many problems with developing it, and what it was trying to achieve seemed no longer necessary. It was finally abandoned in 1997. 

## 3 MBER - Minimum Bit Encoding Rules

MBER was proposed in about the mid-1980s, but was never approved for the Standards path. Many of its principles were, however, adopted when PER was produced. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/2a5107d07616545bdc566a1bc43650a6eafa94ac014936e9d7d1adc51bfc9af5.jpg)


The idea behind MBER was to make full use of bounds information, and to produce encodings that were "what you would expect". 

So a BOOLEAN would encode into one bit, and the type INTEGER (0..7) would encode into three bits. 

MBER never addressed the encoding of all possible ASN.1 types (and in particular did not address the problems solved in PER by a choice index and a bit-map for OPTIONAL elements). 

The main thrust of the MBER work was to make it possible to produce an ASN.1 definition of a type which, if MBER was applied to values of that type, would produce exactly and precisely the same bits on the line as some existing hand-crafted protocol was producing. 

Typically, the aim was to move from protocol definitions using the techniques described in Section I Chapter 1 Clause 5.1 (pictures of octets) to ASN.1 specifications with no change to the bits on the line. 

(The reader may well ask "Why?", but this was a rather flattering recognition that use of the ASN.1 notation was quite a good (clear) way to describe the fields in a protocol message.) 

MBER was never progressed internationally, but (as stated above), the idea of "minimum bit encodings" had a long-term influence and was included in PER. 

## 4 OER - Octet Encoding Rules

At the time of writing this text, the future of OER is unclear, nor is its final form fully-determined. This text merely gives an outline of what this specification appears to the author to look like in the (very) late 1990s. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/009bacf74b54cd89910bb4abb2349eaabfac19d9fe95274d4f8cb8263f196efd.jpg)


It has been proposed as the encoding rules for a particular industry sector in the USA, and perhaps for international standardization for use with protocols in that sector. The industry sector is concerned with "intelligent highways". The sector is using ASN.1 to define protocols for communication between devices on the road-side and between them and control centres. In some cases the devices are large general-purpose computers (where BER or PER could certainly be easily handled). Some devices, however, will be more limited, and may not be able to handle the (alleged) complexity of PER, but where much of the efficiency of PER is required. 

(In relation to “alleged”, remember that all the complexity in PER is in the compile phase to analyze what the encoding should be. Once that is done, the actual encoding in PER is less code and simpler than in BER. Given a good cross-compiler system, even the simplest devices should be able to handle PER.) 

OER was originally developed around the same time as PER, but in ignorance of the PER work (which was later folded into it). At the time of writing, it is a mix of BER (using BER length encodings) and PER. 

The name Octet-aligned Encoding Rules stems from the fact that all elements of an OER encoding have padding bits that make them an integral of eight bits. So INTEGER (0..7) will encode into eight bits (no tag, no length field), and BOOLEAN will encode into eight bits (no tag, no length field). 

Apart from the use of BER-style length encodings, OER is very much like PER, but omits some of the optimisations of PER, producing a specification that is (arguably) simpler. 

These encoding rules were considered by a joint meeting of the ISO/IEC and ITU-T ASN.1 groups in 1999, and the idea of providing a "FULLY-ALIGNED" version of PER received some support. This would in some ways complete the PER family, going along-side the existing UNALIGNED (no padding bits) and ALIGNED (padding bits where sensible) variants. 

In discussion, it was felt that there was as yet insufficient customer demand to justify a "FULLY-ALIGNED" version of PER, and that in any case such a version of PER would not in fact be OER-compatible because of the multitude of differences (less optimization and use of BER features) between OER and PER. 

At the time of writing, international standardization of OER is not being progressed within ASN.1 standardization. 

## 5 XER - XML (Extended Mark-up Language) Encoding Rules

XER is a relative new-comer (in 1999) to ASN.1 standardization. Work on it is proceeding with great rapidity through electronic mailing groups, and serious consideration of it will occur within ISO/IEC and ITU-T about a month after the text of this book is put to bed! The outcome of that discussion cannot be predicted with any accuracy, but I 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/703e3c4eee00be3486a1405795b282c6066f10fa2418e70ec7689b102ae9c210.jpg)


have a sneaming feeling that any second edition of this book may contain a substantial section on XER! 

Many readers will be aware that XML has a strong head of steam, and a lot of supporting tools. A marriage of XML with ASN.1 will undoubtedly be a good thing for both. But XER is VERY verbose! 

XER is character-based, and carries XML start and end mark-up (tags which are usually the names of the elements of ASN.1 SEQUENCES or SETS or CHOICES, which are frequently very long) around ASN.1 items. 

XER appears to hold out the promise of being able to send an XER encoding to a data-base system that has only been configured with a schema corresponding to the fields of an ASN.1 SEQUENCE, and to use code which is independent of the actual ASN.1 SEQUENCE definition (and which is part of the database vendor's software) to automatically insert the received values into the database. This may prove to be worth the price of the verbosity of XER (perhaps!). 

## 6 BACnetER - BAC (Building Automation Committee) net Encoding Rules

These encoding rules are quite old, and were a very honest attempt to produce PER before PER ever existed! They were never submitted to the ASN.1 group for international standardization, and have largely been over-taken by PER (but are still in use). 

Perhaps one of the first industry sectors to decide to use ASN.1, but to also decide to "roll their own" encoding rules. 

They are again an industry sector de facto standard in the USA for messages used in "intelligent buildings" (compare the discussion of "intelligent highways" above). 

BACnet encodings are used to control elevators, lights, central heating systems, and so on. 

From a technical point of view, there are some ASN.1 constructs for which BACnetER does not provide unambiguous encodings, and they have no real advantage over the now standard PER, so it is unlikely (in the opinion of this author) that they will have further impact on the international scene. 

## 7 Encoding Control Specifications

A very recent (1999) development in the work on ASN.1, largely resulting from consideration of requirements for variations of encoding rules such as OER, was the production of text for extensions to the ASN.1 notation called "Encoding Control Specifications". 

<table><tr><td>If everyone is changing BER and PER, let&#x27;s have a meta-language to formally specify the changes they want. Good idea?</td></tr></table>

The idea is that the definition of an Encoding Control Specification (using a notation very distinct from ASN.1) could be associated with an ASN.1 module in much the same way as a style-sheet can be associated with a page of HTML or XML. The Encoding Control Specification could vary the way certain types were encoded, selecting (for specified types or all types) PER or BER styles of length, including or omitting tags and/or padding bits, etc, etc. 

This work (1999) is very much in its infancy. Could the result be a meta-language (that a tool can be built to use) which is powerful enough that a suitable Encoding Control Specification could be applied to an ASN.1 module with the effect that types in that module are encoded with BACnetER or OER (or perhaps even XER) encodings? 

This is broadly the aim of the work. But five years from now you may never have heard of it, and it may be as dead as LWER, or it may be supported by lots of tools and give important added flexibility to ASN.1. Don’t know! Get the second edition (if there is one!) of this book! (But it is not yet even a formally approved Work Item in ISO, so this stuff is just glints in the eye at present.) 

## SECTION IV

## History and Applications

# Chapter 1 The development of ASN.1

# (Or: The ramblings of an old man!)

## Summary:

This chapter is somewhat different in style from the rest of the book. (This summary is not a list of bullets, for a start!) Whilst it does contain some facts, it is not so much a formal record of the stages and dates in the development of ASN.1 (Olivier Dubuisson's book is better for that – see the link via Appendix 5) as my own personal recollections of the various events that occurred along the way. 

Unusually for an academic text, in this chapter I blatantly use the "I" personal pronoun in several sections. It seemed appropriate. 

I was involved in ASN.1 almost from its earliest days (I think that only Jim White – I talk about Jim in the first clause of this chapter - can claim to have seen it through from its start, but he "retired" from Standards work in the late-1980s) through to the present day. I have been active in a number of areas of Standardization within ISO, but ASN.1 has probably taken up the largest part of my time because of its time-span (at the time of writing this text) of close on 20 years. 

There were many other people who gave a great deal of their time to the development of ASN.1, and if you list of some of them, you are in very great danger of being unfair to (and offending) those who just drop off the end of the list, but who nevertheless made important contributions to the work. There is no easy criterion on who to mention, and there are some of my past fellowworkers whose names I can no longer spell with accuracy, and have lost the attendance records! 

And, of course, there are the current participants in the ASN.1 work that seem larger than life simply because they are the current drivers. But I am ignoring most of them! I hope nobody takes offence at being left out. 

The structure of this chapter is not a simple time-line. Rather, certain themes have been selected for the major sub-headings, but within those sub-headings the material is largely presented on a time-line basis. I hope that this will ensure rather more continuity in the text and easier reading than a pure time-line treatment, but the reader is advised that the major sub-headings are largely self-contained, and can be read (or skipped, or omitted) in a more or less random order depending on your interests. 

One major part of this chapter contains the history of the development of character encodings, that was promised in Section II Chapter 2. 

## 1 People

Jim White played an active part (perhaps a leading part - I am not sure) in the development of the Xerox Courier specification, on which ASN.1 was eventually based. 

## Let's get this one out of the way first!

Courier was part of the "XNS" protocol stack. It represented, I think, the first recognition in protocol architecture of the value of providing a notation for the definition of protocol messages that was supported by well-defined encoding rules and tools within high-level language systems to enable users (not just computer vendors) to define their own protocols and to have an easy implementation path for those protocols. 

Jim (as Rapporteur in CCITT responsible for developing notational support for the X.400 work) was largely responsible for bringing the Courier principles into international standardization and in due course for the production of X.409. 

Doug Steedman was also very active within both CCITT and ISO in these early days, and was (I think) the first person to author a full-length tutorial text on ASN.1. This is still read today, but unfortunately was never updated to cover the work beyond 1990, as Doug also "retired" from Standards work in the late 1980s. 

I was ISO Editor for the early ISO texts (and after X.409, CCITT texts were copies of the ISO texts). Bancroft Scott came onto the seen in the late 1980s, when (due to other "retirements"), I became Rapporteur for the ASN.1 work in ISO, and Bancroft, having volunteered to be Editor for one part of ASN.1, found himself Editor for all the different parts (now six parts in ISO and six corresponding ITU-T Recommendations), a role that he continues to occupy at the date of publication of this text (1999). 

In more recent years, Olivier Dubuisson has played a very active role in the development of ASN.1, and is the author of the second/third/fourth major book on ASN.1. (He can claim prior publication to this text with a French version of his book - making his the second text, but at the time of typing this I hope his English version will be later than this publication, making him also the fourth - but he could make third as well! Friendly rivalry!) 

There are many, many, others that I could and perhaps should list, particularly colleagues in BSI that have provided much support for ASN.1 over the years, but then I should also mention colleagues operating within AFNOR and from Sweden, and colleagues in the USA that produced course material for ASN.1 that is still used throughout the world today, and ... 

Stop! Enough of this clause! 

## 2 Going round in circles?

There are so many areas of notational and encoding support for computer communications where understanding has emerged only slowly. (Support for "holes", described earlier, is one of these, as are mechanisms to ensure interworking between implementations of "version 1" and "version 2" of protocol specifications). Sometimes developments are clear steps forward (as was the case when ASN.1 was introduced in the early 1980s), sometimes we make backward steps in some areas to make progress in others. 

We see through a glass darkly. What is the "right" notational support for people trying to define messages for computer communication? ASN.1 has a lot to offer, and has recognised many of the problems (and provided some good solutions) but the world has a way to go yet. 

When ASN.1 was born in the early 1980s, Open System's Interconnection (OSI) Standards were "the best thing since sliced bread", and meetings to develop these Standards within ISO and CCITT often involved several hundred people. But in all the ISO groups defining OSI Standards for applications, there was at that time a doubt, a debate, about what notation to use to clearly specify the messages (including their semantics, and their bit-patterns) to be used to support the application. Every group was doing its own thing, with different approaches and different notations. 

Use of a BNF (Bacchus-Naur Form) style of specification was common in most early OSI drafts, often with an encoding based on strings of characters (much as many Internet protocols are today). 

When the first ASN.1 text (and it was not called ASN.1 in those days - that is another story - see below) was sent as a liaison from CCITT to ISO, it was almost immediately welcomed by every single application layer standardization group in ISO as: 

• Great to have a common and standard notation for all to use in specifying protocols. 

• Great to get away from verbose text-based exchanges. 

(Note the latter point. Despite later strong criticism of the verbosity of BER, and the eventual emergence of PER, both are far less verbose than text-based encodings.) 

ASN.1 became the notation of choice (and BER the encoding) for all the application layer OSI Standards (and for the Presentation Layer as well). 

But it was in the mid-1980s when ASN.1 started to become widely used outside of the OSI stack. There was even some take-up (usually in a cut-down - some would say bastardised! - form) within the Internet community, but the real expansion of ASN.1 was amongst the telecommunications standards specifiers. 

It is the case today that a great many telecommunications standards (for mobile phones, for intelligent networks, for signalling systems, for control of electric power distribution, for air traffic control) use ASN.1. (See the next chapter.) 

But today we still see a battle between those who prefer text-based protocols and the supporters of ASN.1. The emergence of XER (Extended Mark-up Language - XML - Encoding Rules) for ASN.1 has in some ways married the two camps. XER is based on ASN.1 notation for defining types, but is totally character-based (and verbose!) for the transfer of values of those types. However, you will hear people today (with some justification) saying: 

HTML (with Netscape and Microsoft) made provision for write-it-once, read-it-anywhere Web pages. 

• JAVA made provision for write-it-once, run-it-anywhere programs. 

• XML makes provision for write-it-once, process-it-anywhere data. 

And, of course, there is still CORBA (with its IDL notation and IOP protocol as an encoding) as a communications-specification-language contender! 

And we still have a lot of Internet Engineering Task Force (IETF) specifications choosing to use BNF and character-based exchanges as the preferred definition mechanism for messages. 

It may be some time yet before the world homes-in-on, understands, or recognises the "right" way to define and to encode computer communications (and that may or may not be ASN.1 in the form we know it today). We have progressed a lot (in terms of understanding the issues and problems to be solved) from the early 1980s, but we have progressed rather less far in political (lower-case "p") agreements, with a still (alarmingly large) number of contenders for notation to be used in defining protocols. And still people continue to suggest more! (I guess it is no worse than the programming language scene.) 

So ... I look forward to the next decade with interest! What notation will we be using in 2020 to specify protocol standards? I regret that I may not be around to find out! Some readers will! 

## 3 Who produces Standards?

There have over the years and into today been five main sets of actors in the production of Standards related to computer communication, and in the adoption of various forms of notation to support those Standards. 

Who are the five? 

I would suggest: 

There has always been a difficulty over de jure and de facto standards for computer communication around the world. National Standards Institutes often think/hope they wield the power. But the real power over deciding how the world's computers communicate is largely not in their hands, but has shifted over time between many actors. 

• Main-frame computer vendors in the 1970s, but largely now unimportant. 

• CCITT (renamed ITU-T at the start of the 1990s) in the 1980s and 1990s, and still the dominant force in the specification of telecommunications standards today. 

• ISO, working largely in collaboration with CCITT/ITU-T, but with its major influence limited to the OSI developments of the 1980s, and perhaps not being a dominant force today except in isolated areas. 

The IETF, its task forces and working groups, now responsible for the development of Internet standards, which have (for many applications) become the de facto standards for computer communication between telecommunications users (whilst ITU-T remains dominant for standardising the protocols that make telecommunications possible). 

• And with increasing influence today, various consortia of manufacturers and other groups, including the SET consortium and the World-Wide Web Consortium (W3C), and the CORBA grouping. 

The importance of computer vendors in protocol definition had largely declined before ASN.1 entered the scene, with the notable exception of XEROX which (as stated earlier) gave birth to the original ASN.1 concepts. 

ASN.1 as an international specification started life within CCITT as X.409, entitled "Presentation Transfer Syntax and Notation". (Note that the "transfer syntax" was placed first in the - English - title, not the "notation"! Today we would probably see the notation as the more important part of ASN.1). The work leading to ASN.1 was originally intended only to provide notational support for the definition of the X.400-series e-mail protocols. However, it very rapidly moved into ISO, and during the early 1980s, although the work was collaborative, it was largely ISO National Bodies (they were then called "Member Bodies") through which most of the input was provided. 

In the late 1990s the pendulum swung back (partly due to the decline of OSI, and partly due to reorganizations within ISO), with what had by then become ITU-T making most of the running in progressing new work on ASN.1. 

Within IETF, take-up of ASN.1 was always very patchy. This was probably at least in part due to the fact that most of the movers in IETF wanted a specification language that had support from publicly available (for-free) tools. BNF-based text-encodings satisfied this requirement. ASN.1 did not, and does not to this day (1999). So most use of ASN.1 in the IETF world was (and is) using a cut-down version of ASN.1 that was (is) easily capable of being encoded without the use of any tools. 

By contrast, ITU-T telecommunications specifications use the full power of ASN.1, and the telecomms and switch vendors implementing those specifications make full use of available tool products for easy, rapid, and (largely) bug-free implementation of protocols that are highly efficient in terms of band-width requirements. 

## 4 The numbers game

The ASN.1 specifications have gone through a variety of designations. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/66ae97c8ce9eb8cc27aacb3c6d659957c50aa0f7b4b9da910555e37b438dcede.jpg)


The first published specification was X.409 (1984). X.409 pre-dated the use of the term "Abstract Syntax Notation One (ASN.1)", and was part of the X.400 series. It was seen, quite simply, as a notation (and encoding rules) to aid the specification of protocols in the X.400 (OSI e-mail) suite. 

Later it was completely re-written (with no technical changes - see later!) and published (with some additions) by ISO as ISO 8824 and ISO 8825 in 1986, and the same text (again with some additions) was then published by CCITT as X.208 and X.209 in 1988. There was a later version of this text (with minor corrections) published jointly by ISO and IEC in 1990 as ISO/IEC 8824 and ISO/IEC 8825. This became known as the infamous "1990 version of ASN.1". 

The "1994 version of ASN.1" (with very major extensions to the 1990 version) was jointly published by ISO/IEC and CCITT as a whole raft of new documents, with identical text shown in parallel columns below: 

ITU-T X.680 ISO/IEC 8824-1 ITU-T X.681 ISO/IEC 8824-2 ITU-T X.682 ISO/IEC 8824-3 ITU-T X.683 ISO/IEC 8824-4 ITU-T X.690 ISO/IEC 8825-1 ITU-T X.691 ISO/IEC 8825-2 

Still later, there was a joint ISO/IEC and ITU-T "1997 version" (with only relatively minor changes and additions to the 1994 version). However, whilst the "final" text was approved in 1997, neither ITU-T nor ISO have yet produced a published copy that people can purchase (current date early 1999)! But watch this space, it is imminent! (Later correctoin – you can now buy it from ITU-T!) 

Readers should note that in 1994 (and in 1997) X.680 was roughly the old X.208 with some extensions, mainly in the character set area. X.681 was the extensions related to the Information Object concept. X.682 was the table and relational and user-defined constraints, and X.683 was parameterization. X.690 was the old X.209 with CER and DER added, and X.691 was the PER specification. 

Phew! I hate numbers! 'Nuff said. 

## 5 The early years - X.409 and all that

## 5.1 Drafts are exchanged and the name ASN.1 is assigned

The first drafts of X.409 were produced in CCITT. In those days both ISO and CCITT had a "7-layer model" for OSI, and they were totally different texts (technically very similar, but largely developed independently). The era of strong collaboration between the two groups was yet to come, and most communication was by written "liaison statements", usually accompanied by a draft of some specification. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/1db2f4bdecc5b6922d8d1b92ab569a1975467d821c42658fa2bcc704a112600f.jpg)


This is how (during 1982) X.409 first reached ISO TC97 SC16 (Technical Committee 97 - responsible for the whole of computer-related standards, Sub-Committee 16 - responsible for the OSI model and for all work on OSI standards above the Network Layer). At first, it was unclear how these X.409 concepts fitted into the OSI model, and an ad hoc group (chaired, I think, by Lloyd Hollis) was set up to consider the draft. It rapidly became apparent that this work should be slotted into the Presentation Layer of OSI, and a liaison statement was despatched welcoming the work. 

This X.409 draft came into an ISO vacuum - or perhaps I mean a primeval plasma! There was anarchy, with all the various application layer standards wondering what notational mechanisms to use to define their protocols, and all having different approaches. The new notation was extremely rapidly accepted by every single Application Layer standards group as the means to define their protocols. 

It was at this time that a name was considered for the notation, and the ISO group suggested Abstract Syntax Notation One, or "ASN1". The CCITT group replied "OK, but never talk to us about ASN2". ASN2 was never proposed, although there are those that have argued that ASN.1 (1994) should have been named ASN.2 (see later text). 

Notice that in the last paragraph there was no dot after "ASN". This was not a typo! The original proposed name was indeed "ASN1". However, within six months it became apparent that people were frequently mistyping it as "ANS1", and/or misreading it as "ANSI" - the American National Standards Institute. Considerable confusion was being caused! I remember the day when the head of the USA delegation (also Chairman of SC16!) came to the ASN.1 group and said "Look, I know it isn't "ANSI", but it is so close that it is causing problems, can't you change the name?". Uproar! Explosion! But when the dust settled, the "dot" had been inserted and we had "ASN.1". Thereafter no-one ever mistyped it or confused it with ANSI! 

The "dot" is not without precedent - all CCITT Recommendations are written with a dot - X.400, X.25, V.24, so ASN.1 was readily accepted. 

It was at this time that the term "BER" (Basic Encoding Rules) was coined, but in this case there was recognition in both ISO and CCITT that other and perhaps better encoding rules could be produced, but it took ten years before PER (Packed Encoding Rules) eventually emerged. 

## 5.2 Splitting BER from the notation

There were some difficult moments in these early years. It was ISO and not CCITT that had a very strong view on the importance of separating abstract specification (Application Layer) from encoding issues (the first published X.400 specifications were a monolithic protocol directly on the Session Layer, with no Presentation Layer). The X.409 draft (and the eventually published X.409 (1984)) contained, interleaved paragraph by paragraph, a description of a piece of ASN.1 notation and the specification of the corresponding BER encoding. 

ISO was serious about the Presentation Layer. Encoding details should be kept clearly separate (in separate documents) from application semantics. A great idea, but CCITT were not quite as evangelical about it. But without ASN.1 the concept would probably never have reached reality. 

The first thing that ISO decided to do was to rip these pieces apart, and completely re-write them (in theory with no technical change) as two separate documents, one describing the notation (this eventually became ISO 8824) and one describing BER (this eventually became ISO 8825). 

As closer and closer collaboration occurred between ISO and CCITT in the following years (and on the ASN.1 work in particular), the question of course arose - would CCITT adopt the ISO text for ASN.1 and drop X.409? After some agonising, it did, and in 1988 X.409 was withdrawn and there were two new CCITT recommendations in the X.200 series, X.208 and X.209. Recommendation X.200 itself was (and is) the CCITT/ITU-T publication of the OSI Reference Model - eventually aligned with that of ISO but leaning technically far more towards the original CCITT draft than to the OSI one - but that is a separate story! (See my book "Understanding OSI", available on the Web.) Putting the ASN.1 specifications into the X.200 series was a recognition that ASN.1 had become a general tool for the whole of OSI, having outgrown X.400. I like to think that its move to the X.680 and the X.690 range in 1994 represented its outgrowing of OSI, but I think it was more due to the fact that it now needed six Recommendations, and there was no suitable space left in the X.200 range! (ISO does not have similar problems - a single part Standard like ISO 8824 can grow into ISO 8824 Part 1 (ISO 8824-1), Part 2, etc, without changing its number.) 

X.409 was written in a fairly informal style, but when it was re-written within the ISO community, the rather stilted "standardese" language required for ISO Standards was used. For example, "must" must never be used - use "shall" instead (this was due to claimed translation difficulties into French), don't give examples or reasons, just state clearly and exactly what the requirements are - you are writing a specification of what people must do to conform to the Standard, not a piece of descriptive text. 

I often advise those who want a gentle introduction to ASN.1 to try to find an old copy of X.409 (1984) and read that - it is written in more informal language, and because the encodings are specified along-side the notation, I believe that it is easier for a beginner to grasp. But I was interested to see that in Olivier's book he claimed that 8824/8825 were more readable and better specifications than X.409! I guess we all have our own views on what makes a good specification! 

## 5.3 When are changes technical changes?

Genuinely, ISO attempted to re-write X.409 without making technical changes, but two crept in. The first was to do with the type "GeneralizedTime". These were in the days when people had human secretaries to do their 

Correct a spelling, remove an example, trivial things. No problem. Don't you believe it! 

typing and not word processors. X.409 had been authored in the USA. The ISO text for 8824/8825 had a UK Editor (mea culpa), and the secretary (another name - Barbara Cheadle!), unknown to the Editor, corrected the spelling to "GeneralisedTime". This went unnoticed through all the formal balloting, but was eventually corrected before 8824 was actually published! Irrespective about arguments over what is "correct" English, the term "GeneralizedTime" had to stand, because this was a formal part of the notation, and any change to its spelling represented a technical change! 

The second change was only noticed in the early 1990s! Far too late to do anything about it! There was a point of detail about the character string type TeletexString that was only indicated in X.409 in an example. The example was lost in 8824, and the point of detail lost with it - I am afraid I have forgotten the precise details of the point of detail! 

## 5.4 The near-demise of ASN.1 - OPERATION and ERROR

The final incident I want to describe, in this clause about the early days, is one which almost completely de-railed ASN.1. 

At that time, CCITT was locked into a fouryear time-frame called a Study Period where at the start of the four years "Questions" 

Easy wars are based on misunderstanding or lack of understanding (difficult ones are base on real clashes of self-interest). This was an easy war, but the short time-scales for achieving peace amplified the conflict. 

(capital Q!) were formulated. (Each Question generally gave rise to a new Recommendation or to an update of an existing one.) At the end of the Study Period, a complete new set of CCITT Recommendations were published (with a different colour cover in each period). In 1980 the colour was Yellow, Red in 1984, and Blue in 1988. 

(1988 was the last year this complete re-publication occurred, so if you have a set of the Bluebooks in mint condition, keep them - they will be valuable fifty years from now!) 

It took time for the administration to prepare these new texts for publication, and in those days CCITT went into a "big sleep" about twelve months before the end of the Study Period, with the new or amended Recommendations finalised, and with only "rubber-stamping" meetings during the following year. It was in mid-1993, with the "big sleep" about to start - we were at five minutes to midnight - when the CCITT ASN.1 group sent their latest draft of X.409 to the ISO group. 

Mostly it was only minor tidies, but a whole new section had been added that "hard-wired" into the ASN.1 syntax the ability to write constructions such as: 

and 

```txt
lookup OPERATION
    ARGUMENTS name Some-type
    RESULT name Result-type
    ERRORS {invalidName, nameNotFound}
::= 1

nameNotFound ERROR ::= 1

invalidName ERROR
    PARAMETER reason BITSTRING
    {nameTooLong(1),
    illegalCharacter(2),
    unspecified(3)}
::= 2 
```

Well ... if the reader has read the earlier parts of this book, and in particular Section II Chapters 6 and 7, that syntax will look rather familiar, and the meaning will be perhaps fairly obvious. But to those in the ISO group faced with a simple liaison statement defining the revised ASN.1 (and with absolutely no understanding or knowledge about even the existence of the ROSE work), there was utter incomprehension. 

What had this to do with defining datatypes for an abstract syntax (and corresponding encoding rules)? How were ERROR and OPERATION encoded (there was no specification of any encoding in the draft)? What on earth was an "operation" or an "error"? Rip it all out! Had there been more time .... But the ISO group decided that no-way was this stuff going into the ISO Standards that were planned. Agonies within CCITT. Keep it in and risk different Recommendations and Standards for ASN.1? 

It was one minute to midnight when the next draft of X.409 reached ISO. The offending OPERATION and ERROR syntax had been removed - deep sigh of relief - but a new Annex had been added defining a "macro notation". This Annex was very, very obscure! But many programming languages had a "macro notation" to support the language. (These usually took the form of some template text with dummy parameters that could be instantiated in various places with actual parameters - what was eventually introduced with the parameterization features of ASN.1). And it was one minute to midnight. And the CCITT group had agreed to withdraw the OPERATION and ERROR syntax, and deserved a favour in return. The ISO group agreed to accept the macro notation Annex. Peace had been achieved and ASN.1 had been saved! 

In retrospect, this whole incident was probably a good thing, although it had reverberations into the late-1990s. If OPERATION and ERROR had remained hard-wired, and there had been no macro-notation, it would have been very much harder for ASN.1 to develop the concepts related to Information Objects (and it was quite hard anyway!). More on this subject below. 

## 6 Organization and re-organization!

When the idea of Open Systems Interconnection was first considered in ISO, it came from the work in TC97 SC6 on HDLC (High Level Data Link Control) from the question "Who is going to define - and how - the formats of what fills the HDLC frames?" At a meeting in Sydney of TC97 it was decided to create a new sub-committee, SC16, to be charged with the task of developing a model for OSI, and at its first meeting about six different proposed models were submitted from each of the major countries, but the 

Organizational structures matter a bit, but the technical work can often go on despite re-organization above. But sometimes too much turbulence can make it difficult to progress the work formally (and hence to reach publication status). Fortunately, with a joint project between ITU-T/CCITT and ISO/IEC, if you can't progress it in one forum, you can probably progress it in the other! 

submission that most nearly resembled the eventual shape of OSI was that from the European Computer Manufacturers Association (ECMA). The USA voted against the establishment of a new sub-committee, but by some rather interesting political manoeuvres (again beyond the scope of this text!) became the Secretariat and provided the Chair for SC16. 

SC16 became one of the largest sub-committees in the whole of ISO, and in its hey-day could only meet by taking over a complete large University campus. ASN.1 became a relatively selfcontained group within the Presentation Layer Rapporteur Group of SC16. 

On the CCITT front, ASN.1 became a part of Study Group VII, and has had a relatively calm (organizationally) life. When CCITT changed its name to ITU-T, it had little organizational impact at the bottom levels, the main change being that SG VII became SG 7! This is the home of ASN.1 to this day (within Working Party 5 of SG 7). 

On the ISO front, there was a top-level re-organization when ISO agreed that standardization of computer matters was a joint responsibility with the International Electro-Technical Commission (IEC), and formed, with the IEC, a new "Joint Technical Committee 1" to replace TC97. (There has never been, and probably never will be, a JTC2). This had zero impact on the ASN.1 work, save that the cover-page of the Standards now included the IEC logo alongside that of ISO, and the formal number became ISO/IEC 8824 instead of ISO 8824. JTC1 inherited exactly the same SC structure and the same officers and members as were originally in TC97. It was at this time that the name of contributors to the ISO work changed from "Member Body" to "National Body", but they were still the same organizations - BSI, ANSI, AFNOR, DIN, JISC, to name just a few. 

A slightly more disruptive reorganization was when SC5 (programming languages and databases) and SC16 (OSI) were re-shaped into a new SC21 and SC22, but the transition was smooth and the ASN.1 work was not really affected. 

In the late 1990s, however, the Secretariat of SC21 decided it could no longer resource the subcommittee, and it was split into an SC32 and SC33. ASN.1 was placed in SC33 as a fully-fledged Working Group (it had had the lower-status of a Rapporteur Group within a Working Group for all its previous history), but it never met under this group as there was no National Body prepared to provide the Secretariat for it, and SC33 was disbanded almost before it ever existed. ASN.1 (together with other remnants of the original OSI work, including the continuing X.400 standardization) was assigned to SC6 (a very old sub-committee, responsible for the lower layer protocol standards, and with a very long history of a close working relationship with CCITT/ITU-T SG VII/SG 7). This is likely to prove a good home for ASN.1 within ISO. 

This last transition was less smooth than earlier re-organizations, and the formal progression of ASN.1 work within ISO was disrupted, but at the technical level the work non-the-less continued, and formal progression of documents was undertaken within the ITU-T structures. 

## 7 The tool vendors

Of course, when ASN.1 was "invented" in the 1980 to 1984 CCITT Study Period, there were no tools to support the notation. Whilst it drew on Xerox Courier for many of its concepts, it was sufficiently different that none of the Xerox tools were remotely useful for ASN.1. 

The tool vendors. The Traders of ASIMOV's "Foundation". A law unto themselves, but vital to the success of the enterprise and contributing immensely to its development in the middle years. 

It was the mid-1980s before tools began to appear, and these were generally just syntax-checkers and pretty-print programs. It was in the late 1980s that tools as we now know them started to emerge, and the ASN.1 tool vendor industry was borne. (See Chapter 6 in Section I for more about ASN.1 tools). 

Of course, in the early days, all those working on ASN.1 were essentially "users" - employees of computer manufacturers or telecommunications companies, (sometimes Universities), and usually with strong interests in some protocol that was using ASN.1 as its notation for protocol definition. But at the last meeting (1999) of the ASN.1 group, the majority of those around the table had strong links one way or another with the vendor of some ASN.1 tool - ASN.1 had come of age! 

There was an interesting transition point in the late 1980s when tool vendors were beginning to appear at Standards meetings, and were complaining that there were some features of the ASN.1 syntax that made it hard for computers to read (the main problem was the lack of a semi-colon as a separator between assignment statements - eventually resolved by introducing a colon into the value notation for CHOICE and ANY values). At that time, there were strong arguments that ASN.1 was not, and was never intended to be, a computer-processable language. Rather it was a medium for communication between one set of humans (those writing protocol standards) and another set of humans (those producing implementations of those protocols). That view was rapidly demolished, and today ASN.1 is seen as very much a computer language, and many of the changes made in the early 1990s were driven by the need to make it fully computer-friendly. 

## 8 Object identifiers

## 8.1 Long or short, human or computer friendly, that is the question

Object identifiers (I'll use the informal abbreviation OID below) pre-dated the "Information Object" concept by at least five years, although today they are closely associated with that concept. 

Again, what's in a name? Well the length might matter if you are carrying it in your protocol! 

It was in the mid-1980s that it became apparent that many different groups within OSI had a requirement for unambiguous names to identify things that their protocol was dealing with, and which could be assigned in a distributed fashion by many groups around the world. 

A similar problem had been tackled a few years earlier in SC6, but with the narrower focus of providing a name-space for so-called "Network Service Access Point Addresses" - NSAP addresses, the OSI equivalent of IP addresses on the Internet. If the reader studies the NSAP addressing scheme, some similarities will be seen to the Object Identifier system, but with the very important difference that the length of NSAP addresses had always to be kept relatively short, whilst for application layer protocols long(ish) object identifiers were considered OK. 

In around 1986 a lot of blood was spilt over the OBJECT IDENTIFIER type, and it could easily have gone in a totally opposite direction (but I think the right decision was eventually taken). This was not a CCITT v ISO fight - by this time the two groups were meeting jointly, and divisions between them were rarely apparent. (That situation continues to this day, where at any given meeting, the various attendees can often claim representation of both camps, but where if they are delegates from one camp or the other, discussion almost never polarises around the two camps.) 

To return to OIDs! The argument was over whether an OID should be as short as possible, using only numbers, or whether it should be much more human-friendly and be character-based, with encouragement to use quite long names as components within it. 

The eventual compromise was what we have today - an object identifier tree with unique numbers on each arc, but with a rather loose provision for providing names as well on each arc. In the value notation for object identifiers, the numbers always appear (apart from the top-level arcs, where the names are essentially well-known synonyms for the numbers), but the names can be added as well to aid human-beings. In encodings, however, only the numbers are conveyed. 

A further part of the compromise was the introduction of the "ObjectDescriptor" type to carry long human-friendly text, but text that was not guaranteed to be world-wide unambiguous, and hence which was not much use to computers. As stated earlier, the "ObjectDescriptor" type was the biggest damp squib in the whole of the ASN.1 armoury! 

A very similar battle raged - but with pretty-well the opposite outcome - within the X.500 group a year or so later. X.500 names (called "Distinguished Names") are an ASN.1 data type that is (simplifying slightly again) essentially: 

$$
\begin{array}{l} \text {SEQUENCE OF} \\ \text {SEQUENCE} \\ \left\{\text {attribute - id} \quad \text {TYPE - IDENTIFIER.} \& \text {id}, \right. \\ \left. \text {attribute - value TYPE - IDENTIFIER.} \& \text {Type} \right\} \end{array}
$$

Remember that "TYPE-IDENTIFIER.&id" is essentially a synonym for "OBJECT IDENTIFIER", so it is clear that X.500 names are very much longer than ASN.1 names. 

There was pressure in the late 1980s (from groups outside of X.500) for X.500 to support use of a simple single OBJECT IDENTIFER (a so-called "short-form" name) along-side its Distinguished Names (so-called "long-form" names), and I believe it was formally agreed within SC21 that this should happen, but I think it never did happen! 

## 8.2 Where should the object identifier tree be defined?

Another problem with the definition of the OBJECT IDENTIFIER type is that it is not just defining a data type, it is implicitly establishing a whole registration authority structure. 

Demarcation disputes. Ugh! 

This went beyond the remit of the ASN.1 group (a separate group in OSI was charged with sorting out registration authority issues, and produced its own standard). This was a source of continuing wrangling over almost a decade. Initially (mid-1980), it was within ISO that people were saying "The description of the object identifier tree should be moved from ASN.1 to the Registration Authority Standard", but the CCITT people were saying "No-way - ASN.1 users want to be able to read that text as part of the ASN.1 Standard, and control of it should remain with the ASN.1 group." 

It stayed in the ASN.1 Standard until (and including) the 1990 publication. But in the early 1990s, the roles were reversed, and there was pressure from ITU-T (largely from outside the ASN.1 work) to move the text from X.680 (ISO/IEC 8824-1) to X.660 (ISO/IEC 9834-1). There was some opposition within the ASN.1 group itself, but the move happened, and relevant text was deleted from X.680/8824 and replaced by a reference to X.660/9834. Ever since then, there have been various liaisons between the keepers of the respective standards to try to ensure continued consistency! Fortunately, however, the work on the object identifier tree itself was completed long ago and is very stable. (But see the next clause!) 

## 8.3 The battle for top-level arcs and the introduction of RELATIVE OIDs

The change of name from CCITT to ITU-T was a simple top-level name change, yes? But remember that two of the top arcs of the object identifier tree were "ccitt" and "joint-iso-ccitt". 

Everyone wants to be at the top of the tree, but in this case for good reasons - it reduces the verbosity of their protocols. 

ITU-T proposed two new arcs (with new numbers) for "itu-t" and "joint-iso-itu-t". Those who have read the text associated with figure III-13 will realise that whilst it was not wholly impossible to accede to this request, it would be very difficult! Eventually, the new names were accepted as synonyms for the existing arcs (keeping the same numbers). 

It was shortly after this that there became an increased demand by international organizations for object identifier name space using a top arc. Organizations realised that object identifier values they allocated (and used in their protocols) would be shorter if they could get "hung" nearer the top of the tree. ITU-R, the International Postal Union, and the IETF were among organizations expressing (with various degrees of strength) the wish to wrest some top-level arcs from ISO and ITU-T (who were surely never going to use all the ones allocated to them). 

This issue looks today (1999) as if it is being defused by the addition of a new type called RELATIVE OID. (Yes, at the time of writing it is OID, not OBJECT IDENTIFIER.) A RELATIVE OID value identifies parts of the object identifier tree that sits below some (statically determined) root node, and the encodings of these values only contain the numbers of the nodes beneath that root node, omitting the common prefix. 

This rather simple proposal was a very much cut-down version of an earlier proposal that would have allowed the common prefix to be transmitted in an instance of communication, and then be automatically associated with particular relative oid values that were transmitted later in that instance of communication. 

(It is always very difficult when writing books to avoid them becoming rapidly out of date - you either don't talk about things like RELATIVE OID, or you do, with the danger that a few weeks after publication you find it has either been withdrawn or has been dramatically changed. But in this case, I am fairly confident that it will be added to ASN.1 much as described above.) 

## 9 The REAL type

The REAL type might seem innocuous enough, but was also the source of controversy around 1986. 

Probably just an academic exercise - nobody uses REAL in actual protocols! But it produced its own heated moments. 

Everyone agreed we had to have it, but how 

to encode it? (The actual encoding eventually agreed is fully described in Section II Chapter 2 clause 3.5, and the interested reader should refer to that.) 

There were several issues, of which binary versus character encodings was one. As usual, the easy compromise was to allow both, but that produced problems later when canonical encodings were needed, and the rather dirty fudge had to be taken of saying that base 2 and base 10 values that are mathematically equal are regarded as distinct abstract values, and hence encode differently, even in the canonical encoding rules. 

But the main problem was with the binary encoding format. There was a (fairly new) standard at that time for floating point formats for computer systems, and it was generally used by people handling floating point in software, but not by existing hardware (later it got implemented in chips). Naturally, there were those that advocated use of this format for ASN.1 encodings. 

The counter-argument, however, eventually prevailed (and again I think this was the right decision). The counter-argument was that we were some time away from a de facto standard for floating point formats, and that what mattered was to find a format that could be easily encoded and decoded with whatever floating point unit your hardware possessed. 

This principle dictated, for example, the use of a "sign and magnitude" (rather than "two's complement" or "one's complement") mantissa, because "sign and magnitude" can be easily generated or processed by hardware of the other two forms, but the converse is not true. It was also this principle that gave rise to the rather curious format (not present in any real floating point hardware or package) involving the "F" scaling factor described in 3.5.2. 

Finally, there was a lot of pressure at the time to support specific encodings that would identify "common and important" numbers that otherwise would have no finite representation, such as "3.14159..." and "2.7183...", and also values such as "overflow", and "not-a-number", but in the end all that was added was encodings to identify PLUS-INFINITY and MINUS-INFINITY, with plenty of encoding space for identification of other things related to type REAL later. The pressure to provide these additional encodings evaporated, and no extensions have been made, nor do any seem likely now. 

## 10 Character string types - let's try to keep it short!

The history of the development of encodings for "characters" (and discussion on just what a "character" is) is much broader than ASN.1. ASN.1 has not really contributed to this work, but rather has done its best to enable ASN.1 users to have available notation that can let them reference 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/43ed84c2bbf11bb1e2e3922d86dee2afa43772df2c5c809e2364a29fac7c9cd2.jpg)


in their protocols, clearly and simply, these various character encoding standards. 

The result, however, has been a steady growth in the number of character types in ASN.1 over the years, with a lot of fairly obsolete baggage being carried around now. 

Section II Chapter 2 promised that we would here provide a description of the history of the development of character encoding schemes, and the impact this had on ASN.1 over the years. What follows is the main parts of that history (but detail is sometimes lacking, and it is not a complete history - that is left to other texts), with the impact on ASN.1. 

## 10.1 From the beginning to ASCII

The earliest character coding standards were used for the telegraph system, and on punched paper tape and cards. The earliest formats used 5 bits to represent each character (32 possible encodings), with an encoding for "alpha-shift" and "numeric-shift" to allow upper-case letters, digits, and a few additional characters. 

Five-bit codes, seven-bit codes. And to come later, 16 bit codes and 32 bit codes! I doubt anyone will EVER suggest 64 bit codes ... but on second thoughts, how many bits does Microsoft Word take to indicate fonts etc? (OK, that is usually per paragraph not per character, but in the future ... ?) 

Later the use of 7 bits with an eighth parity bit 

became the de facto standard, and this eventually became enshrined in the 8-bit bytes of current computers. The ASCII code-set is the best-known 7-bit encoding, with essentially 32 so-called "control characters" (many of whose functions related to the framing of early protocol packets) and 94 so-called "graphics characters" (printing characters), plus SPACE and DEL (delete). (DEL, of course, is in the all-ones position - 127 decimal - because on punched paper tape the only thing you could do if you had made a mistake was to punch out all the rest of the holes - you could not remove a hole!). 

ASCII has formed the basis of our character coding schemes for close on forty years, and is only now being replaced. ASCII is in fact the American variant of the international standard ISO 646, which defines a number of "national options" in certain character positions, and many other countries defined similar (but different) national variants. The UK variant was often called (incorrectly!) "UK ASCII". 

## 10.2 The emergence of the international register of character sets

Early computer protocols used 7 bit encodings, and retained the use of the eighth bit as a parity bit. That is why we find today that if you wish to send arbitrary binary over e-mail, it gets converted into a seven-bit format, and more or 

Providing encodings for all the characters in the world - first attempt, and not a bad one. 

less doubles in size! More modern protocols (such as those used to access Web pages) provide what is called "full eight-bit transparency" and the eighth bit is a perfectly ordinary bit which can carry user information. 

As protocols developed, the use of a parity bit was very quickly dropped in favour of a Cyclic Redundancy Code (CRC) as an error detecting code on a complete packet of information, and character coding schemes were free to move to an 8-bit encoding capable of representing 256 characters. 

There were two developments related to this: The first of these was developed as early as 1973. This was ISO 2022, which established a framework (based on ISO 646) for the representation of all the characters in the world. (I am afraid the following description is of necessity somewhat simplified - the so-called multiple-byte formats and the dynamically redefinable character sets of 2022 are not mentioned in what follows.) 

The way ISO 2022 worked was to identify the first two columns (32 cells holding control characters) of the ASCII structure as cells that could contain (represent, define) any so-called Cset of characters, and the remaining 94 positions (keeping the SPACE and DEL positions fixed as SPACE and DEL) as cells that could contain (represent, define) any so-called G-set. Moreover, within the C-set positions, the ASCII ESC character would always be kept at that precise position, so a C-set of characters was in fact only allowed to be 31 control functions. 

The old parity bit could be used to identify one of two meanings (one of two character sets) for encodings of C-sets, called the C0 and the C1 set. If one of the C-sets in use included control characters for "shift-outer" and "shift-inner" (which affected the interpretation of G-set but not Cset codes), then the combination of using these together with the old parity bit enabled reference to (encodings of) up to four G-sets, called G0, G1, G2, and G3. 

Finally, there was the concept of a register of C-sets and G-sets that, for each register entry, would assign characters to each position in the ASCII structure. At any point in time, up to two C-sets and up to four G-sets could be "designated and invoked" into the C0, C1, G0, G1, G2, and G3 positions. The ESC character (required to be present in the same position in all C-sets, remember) was given a special meaning. Each register entry contained the specification of binary codes that could follow the ESC character to "designate and invoke" any register entry into either a C0 or C1 position (for C entries) or into one of the G0 to G3 positions (for G-entries). 

All that remained was to produce the register entries! This became the "International Register of Coded Character Sets to be used with Escape Sequences", commonly referred to as "the international register of character sets". 

The register was originally maintained by the European Computer Manufacturer's Association (ECMA), and grew to well over 200 entries covering virtually the entire world's character sets. Today it is maintained by the Japanese Industrial Standards Committee (JISC), the Japanese equivalent of BSI and ANSI and AFNOR and DIN. Both ECMA and JISC provide free copies and free up-dates to interested parties, but JISC now maintains a web-site with every register entry on it. (See Appendix 5 if you want to access this site). 

ASN.1 provides full support for ISO 2022, with GraphicString and GeneralString, and relies on the International Register for the definition of many of its other character string types. 

## 10.3 The development if ISO 8859

ISO 8859 came much later (in 1987), and came in a number of "parts". 

The problem with the 2022 scheme was that because of the inclusion of ESC sequences to make new designations and invocations, encodings for characters were not fixed length. 

Giving European languages full coverage with an efficient encoding - a standard ignored by ASN.1! Who cares about Europe in International Standardization? (President of the European Commission, please do not read this!) 

ISO 8859 was designed to meet the needs of European languages with a fixed (eight bits per character) encoding. Each part of 8859 specified ASCII as its so-called "left half" - the encoding you got with the old parity bit set to zero, and a further 94 printing characters in its "right-half" designed to meet the needs of various European languages. So 8859-1 is called "Latin alphabet No.1", and in addition to ASCII provides characters with grave, circumflex, acute accents, cedillas, tildas and umlauts, together with a number of other characters. 8859-6 is called "Latin/Arabic", and contains arabic characters in its right-half. 

ASN.1 never provided any direct support for 8859, although 8859 encodings were quite often used in computer systems in Europe. 

## 10.4 The emergence of ISO 10646 and Unicode

## 10.4.1 The four-dimensional architecture

A very major development in the early 1990s (still, almost a decade later, to work its way completely into computer systems and protocols) was the development of a completely new frame-work for encoding characters, wholly unrelated to the ASCII structure. (But of course capable of encoding ASCII characters!) 

Probably the most important development in character set encoding work EVER. It is hard to see a likely change from this architecture at any time in the future. Wow! At ANY time in the future? Yup. 

Here you must look at figure IV-1 (yes, the first figure in this chapter - you must be feeling deprived!). This shows a four-dimensional structure (compared with the ASCII 2-dimensional code table). 

Figure IV-1 shows a street of 256 houses. Each house has 256 "planes" in it (positioned vertically, and running left to right within the house on the street). Each plane has 256 rows in it (running top to bottom within each plane of each house). And each row has 256 cells in it (running from left to right within each row). Each cell can contain (define, represent) a different character. (Actually, the correct technical term for a house is a "group" - "house" is not used, but I prefer to call them houses!) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/96ab0308e7b2832f374d449e732f3769ad597255c57b28efc18901d9d39e21f0.jpg)



Figure IV-1: 256 houses each with 256 planes each with 256 rows each with 256 cells


The very first plane (number zero) of the first house (number zero) is called the Basic Multilingual Plane or "BMP". The first row of that plane contains Latin Alphabet No 1 (8859-1), and hence contains ASCII in its left half. 

(In the early drafts of ISO 10646, the other parts of 8859 occupied successive rows, and hence ASCII appeared multiple times, but this was removed in the "fight" with Unicode (see below), and the other parts of 8859 only have their right-hand halves present.) 

Notice that any cell of any row of any plane of any house can be identified by four values of 0 to 255, that is to say, by 32 bits. So in its basic form ISO 10646 is a 32-bits per character encoding scheme. 

Notice also that the numerical value of these 32 bits for ASCII characters is just the numerical value of those characters in 7-bit ASCII - the top 25 bits are all zero! 

Now, it is a sad fact of life that if 

• You take all the characters there are in the world (defining things like "a-grave" and "acircumflex" and even more complicated combinations of scribbles used in the Thai language as separate and distinct characters requiring a fixed length encoding); and 

You admit that glyphs (scribbles) in the Chinese and Japanese and Korean scripts that look to a Western eye to be extremely similar are actually distinct characters that need separate encodings; and 

You include all the scribbles carved into Egyptian tomb-stones and on bark long-preserved in deepest Africa; and 

• You include ASCII multiple times by putting the whole of each part of 8859 into successive rows of the BMP; then 

you find that there are nowhere near 2 to the power 32 "characters" you would want to encode, but that there are very significantly more than 2 to the power 16. 

The ISO 10646 structure permits all such characters to be represented with a fixed 32 bits per character, but is this over-kill? Can we manage with just 16 bits per character if we do some judicious pruning? 

## 10.4.2 Enter Unicode

(For a pointer to Unicode material on the Web, see Appendix 5). 

Whilst the ISO group JTC1 SC2 was beavering away trying to develop ISO 10646, computer manufacturers were independently getting together to recognise 

The manufacturers flex their muscle. 32 bits per character is not necessary or sensible for commercially important character sets! 16 bits can be made to work. 

that neither the ISO 2022 nor the ISO 8859 schemes were adequate for the increasingly global communications infrastructure and text processing requirements of the world, but they jibbed at going to a full 32 bits per character. Can't we make 16 bits suffice? 

Well, we can reverse some of the decisions taken above. Let's ignore Egyptian hierogplyphs and anything of interest only to librarians. Let's also introduce the concept of combining characters with which we can build scribbles like a-grave etc (this does not save much for European languages, but saves a lot for Eastern languages such as Thai). Of course, from one point of view, use of combining characters means we no longer have a fixed length encoding for each character, but that depends on your definition of what is a character! 

Finally, let us perform "Han unification" or "CJK Unification" to produce a "unified code" or "Unicode". CJK Unification means that we look at the scribbles in the Chinese (C), Japanese (J), and Korean (K) scripts with a western eye, and decide that they are sufficiently similar that we can assign all three similar scribbles to a single cell in our street of houses. 

Now we have cracked it! There are less than two to the power sixteen (important) characters in the world, and we can fit them all into the Basic Multi-lingual Plane and use just 16 bits per character to represent them. 

Of course, when the final balloting to approve the ISO 10646 draft ocurred, there were massive "NO" votes, saying "replace it with Unicode"! 

## 10.4.3 The final compromise

ISO 10646 was published as an International Standard in 1993 (about 750 pages long!), and the Unicode specification was published in 1992 by Addison Wesley on behalf of the Unicode Consortium, with Version 2 appearing in 1996. 

And the amazing thing about international standardization is that compromises ARE often reached, and standards agreed. 

Unicode and ISO 10646 were aligned: the CJK unification and the inclusion of combining characters was agreed, and the Basic Multi-lingual Plane of ISO 10646 was populated with exactly the same characters as appeared in the Unicode specification, and close collaboration has continued since. 

However, important differences remained in the two texts. The ISO text describes three "levels of implementation" of ISO 10646. In level 1, combining characters are forbidden. Everything is encoded with the same number of bits, 32 (UCS-4) bits if you want the whole street, or 16 (UCS-2) bits if you just want the characters in the Basic Multi-lingual Plane. In level 2, you can use combining characters, but only if the character you want is not present in a populated cell (this forbids the use of "a" with the combining character "grave" to get "a-grave"). In level 3, anything goes. Unicode does not describe these levels, but it is in the spirit of Unicode to use combining characters wherever possible. 

There are also other differences between the texts that do not relate to character encoding (and hence are irrelevant to ASN.1): the Unicode specification contains some excellent classificatory material that says what characters should be regarded as numbers, upper/lower-case mappings, and so on; such text is missing from ISO 10646. 

After the initial publication of Version 1 of Unicode and of ISO 10646, work continued. There are now characters in cells outside of the BMP, but both groups have agreed a mechanism for referencing them within a 16-bit encoding scheme (called UTF-16 - Universal Transformation Function 16) by using reserved characters in the BMP as escape characters to effectively designate and invoke other planes into the BMP position (although that is not the terminology used). 

Another extremely important development was the definition of UTF-8, briefly described in clause 12 of Section II Chapter 2. This provides a variable number of octets per character, but with all ASCII characters represented with just one octet, with their normal ASCII encoding (with the top bit - the old parity bit - set to zero). 

For in-core handling of characters in programming languages (and operating system interfaces), computer vendors are supporting 16 bits (usually) or 32 bits (some) or both representations of characters. But for storage on disk or for transfer, UTF-8 is proving a very popular format. 

## 10.5 And the impact of all this on ASN.1?

Current ASN.1 support for character sets has been described in Section II, and it should now be possible for the reader to relate that text to the development of character set standards. The history of character set work in ASN.1 

On the character set front, ASN.1 has just rolled with the punches. It has not seriously contributed to either repertoire definitions or to encodings. What it HAS tried to do is to provide simple notational support for referencing character set standards. 

has, however, been a long up-hill struggle to try to meet the demands of its users. It has not always succeeded in keeping everybody happy! 

X.409 made no use of any of the ISO character set standards apart from ISO 646 (equal to CCITT International Alphabet #5), which it used in the definition of ISO646String (no control characters) and IA5String (control characters included). "ISO646String" is still a permitted type, but the synonym "VisibleString" is preferred. NumericString and PrintableString were also present in X.409, but with the character repertoires and the encodings hard-wired into ASN.1 (as they still are today). 

The only other two character string types in X.409 were T61String (with the preferred synonym today of TeletexString) and VideotexString, which were defined by reference to what was then Recommendation T.61 and T.100 and T.101. 

In the early 1980s, writers of ISO standards had to get special permission to reference any specification that was not an ISO standard, so TeletexString and VideotexString posed some problems. The decision was taken (when the re-write that produced ISO 8824 and ISO 8825 was done) to re-cast the definitions (with no technical change!) in terms of references to the international register of character sets described earlier, and this was successfully accomplished (by adding some new register entries!). 

At the same time, GraphicString and GeneralString were added to provide full support for the International Register. 

There were two problems with this: first, new entries were being continually made to the register, so it was very unclear what implementation of GraphicString and GeneralString really meant - these were open-ended specifications. Second, and perhaps more importantly, recasting TeletexString as a reference to particular register entries effectively "froze" it at the 1984 T.61 definition, but many countries made (successful) attempts to get their scripts added to the teletex Recommendations and were (perhaps not surprisingly!) annoyed that they were still not part of the formal definition of TeletexString in ASN.1! 

Eventually the political pressure to change TeletexString in ASN.1 became just too great, and in 1994 a whole raft of new register entries was added as permissible entries to designate and invoke within a TeletexString encoding. What about existing implementations of existing protocols? Political pressure is no respecter of minor technical matters like that! The formal definition of TeletexString changed! 

There was another change that also caused some upsets. Formally, VisibleString and IA5String referred to register entry #2, which was the so-called "International Reference Version" of ISO 646 (but virtually everyone - incorrectly - interpreted that as "ASCII"). But ISO 646 was changed in the late 1980s to introduce the "dollar" character - present in ASCII, but not in the International Reference Version of ISO 646. So ASN.1 changed the reference to register entry #6 (ASCII). At the same time it changed the default G0 set at the start of all GraphicString and GeneralString encodings from #2 to #6. This caused great anger from the X.400 group, who now recommend that in these encodings the G-sets should be specifically designated and invoked by escape sequences, and a default should not be assumed. 

Then ISO 10646 came along, and the ASN.1 group watched the discussions between the ISO workers and the Unicode workers with interest, but from the side-lines. When a compromise was reached and ISO 10646 was published, it looked easy: ASN.1 provided two new types, UniversalString (UCS-4 32-bit encoding), and BMPString (UCS-2 16-bit encoding) for characters in the multi-lingual plane. UCS-2 and UCS-4 provided escapes into encodings using the International Register - effectively the ability to embed GeneralString encodings in UniversalString or BMPString. In the interests of simplicity ASN.1 locked these escape mechanisms out in ASN.1 encodings, again giving some complaints today from sophisticated users! 

A more serious problem was that just after the ink was dry on the 1994 ASN.1 publication, UTF-8 (and UTF-16), described earlier, arrived as amendments to ISO 10646 and to Unicode. UTF8String was added to ASN.1 in the 1997 version, but at the time of writing there is no support for UTF-16 - but some pressure to provide it! 

In an attempt to "get out from under" in this character set and encoding debate, ASN.1 introduced "CHARACTER STRING" in 1994, supported by JTC1 SC2, who included an annex (but only an informative one!) in ISO 10646 that specified object identifier values to be used to identify character repertoires (including restrictions to level 1 or level 2 described above) and encoding schemes (UCS-2 and UCS-4). 

The type "CHARACTER STRING" was originally intended to be very efficient, with the object identifiers used to identify the character abstract and transfer syntaxes of character strings within a "SEQUENCE OF CHARACTER STRING" being transmitted only once. Unfortunately, the mechanism used to provide this turned out to have some fatal bugs in it, and was with-drawn. A later mechanism of "dynamic constraints", or "run-time parameters" attempted to provide equivalent support, but foundered because the power to complexity ratio was found to be too low. (This is discussed further in the final clause of this chapter.) 

ASN.1 also provided mappings from the names of "collections" of characters in ISO 10646 into ASN.1 (sub)type names, and provided (sub)type names corresponding to the different "levels of implementation" of ISO 10646, and value references for each of the characters in 10646. (See Section II Chapter 2.). 

That is the history to-date, but watch this space! I think the saga of character sets and encodings is probably not yet over! 

## 11 ANY, macros, and Information Objects - hard to keep that short (even the heading has gone to two lines)!

Well, maybe we can keep it short - the information object concept has been well and fully discussed earlier, and ANY and macros were withdrawn from ASN.1 in 1994, so perhaps there is not really much more to say! 

<table><tr><td>Much of this (if you are reading from front to back!) you already know. Let&#x27;s pull the historical threads together.</td></tr></table>

The story starts with the attempted introduction of the OPERATION and ERROR syntax into ASN.1 in 1982/83 as described above. 

This attempt failed, and macros were introduced. It turned out that what the macro notation really provided (forget about what it appeared to provide!) was the ability to define arbitrary syntactic extensions (but with no semantics to relate those extensions to other ASN.1 constructs) to ASN.1. Until 1986, there were only two macros defined. These were defined in ROSE, and (surprise, surprise!) were called OPERATION and ERROR, and provided for any ASN.1 module that imported these macros to write precisely the OPERATION and ERROR syntax described earlier. 

Of course, what was really happening (but this was only realised about five years later) was that the syntax was being provided to give ROSE users a reasonably friendly syntax with which to provide the information needed to complete the ROSE protocol - ASN.1 types and values associated with the definition of operations and errors which would be carried in ROSE messages. Information objects, in other words. But whilst the macro notation gave ROSE the ability to define the syntax it wanted, the underlying information object concepts were missing, and the use of that syntax (to define information associated with an operation or error) had no formal link with the ROSE messages. 

Around 1986 there was a sudden explosion in the writing of new macros. It seemed that almost every group using ASN.1 found the need to add new syntax to the ASN.1 notation. What were they all doing? 

Well ... nobody really knew, in terms of a global picture. The uses of that new syntax were many and varied, and had nothing to do with operations or errors. Moreover, tool providers were beginning to complain about the macro notation. 

It became clear that (at least formally) it was possible to write new notation which claimed to define an ASN.1 type, but which totally failed to define the type unless accompanied by value notation (such as value notation in a value reference assignment, or use of DEFAULT in an element of a SET or SEQUENCE). 

There were two other major problems. 

The first was that ASN.1 users were given (via the macro notation) the power to define arbitrarily complex syntactic extensions to ASN.1 using the Bacchus-Naur Form (BNF) notation. BNF is an extremely powerful notation that is often used to define the syntax of programming languages (and is indeed used to formally define the syntax of the ASN.1 notation itself). However, it is well known to definers of programming languages and other users of BNF that if the resulting syntax is to be computer-friendly (easily parsed by computers), then some moderately sophisticated and complex restrictions have to be adhered to in the BNF definition. No such restrictions were applied to its use in ASN.1. 

The second problem was that it was generally not possible to find the end of a new piece of syntax introduced by a macro without knowing the details of that macro. But the definition of the macro could well follow the first use of the macro name and hence of the new syntax. 

Whoops! Tool vendors did not like it! Some of the better tools hard-wired into their tool knowledge of the syntax defined by macros in most known international standards, and then simply ignored the actual syntax definition (macro definition) supplied to the tool. It worked, but .... 

Around 1988, the USA campaigned strongly within SC21 for an embargo on the writing of new macros, and succeeded in getting a resolution passed forbidding such new macros until "either the macro notation was replaced, or the problems with it were resolved". It took around five years for this demand to be satisfied, with, in fact, replacement. 

Most of that time was spent trying to determine just exactly what the different groups were using macros for, and eventually light dawned, and it became apparent that in almost all cases the definition of extensions to the ASN.1 syntax was (as with ROSE) in order to provide users of a protocol full of holes with a human-friendly but formal notation to specify the contents of those holes. Use of the macro notation was (almost) always associated with use of "ANY" (and later "ANY DEFINED BY") in ASN.1-defined messages. (There were important exceptions, such as the ENCRYPTED macro in X.500, where the new syntax was being used to provide a real extension to ASN.1 which was later satisfied using the user-defined constraint and parameterization, described earlier in this text.) 

Around this time (late 1980s early 1900s) the problems with "ANY" became more widely recognised (although they had been flagged as early as 1985, with attempts to shore up "ANY" with "ANY DEFINED BY".) 

The attempt to understand what macros were being used for and to define an appropriate replacement for macros and ANY went through many iterations and false starts over several years. "Non-encodable types" and "table types" were terms that were invented and discarded. 

Eventually something was almost ready, but it was complicated, and the terminology was not clear. There was a critical meeting (I think in Seoul, Korea, and I am pretty sure it was Bancroft Scott's first international ASN.1 meeting) in which it looked as tho' we could not find a replacement for macros - the earlier work was just too complex. But after a night of no sleep, solutions began to appear. The next day we started to discuss the Information Object Class concept, and to keep things simple, we agreed to allow just (eg): 

## OPERATION.&Type

without any constraint applied to it. (Something I still regret!) 

But the Seoul meeting was a good one. What looked (at the start) like the abandoning of several years of work, ended with the Information Object Class terminology and associated concepts pretty-well as we know them today. 

Slightly later, another crucial meeting (at which probably nobody really understood the magnitude of the decision taken) occurred around 1991 - Washington I think (I remember the room, but can't remember the location!). This meeting decided to withdraw from ASN.1: 

• The entire macro notation. 

• The ANY and ANY DEFINED BY syntax. 

These were to be replaced by the notation for defining information object classes, objects, and sets, and the associated "information from object class" notation and the application of table and relational constraints. 

There was around this time a popular UK television series about UK Government in which a civil servant would often say to a Cabinet Minister, "Minister, that is very brave of you." The Minister would wince, and almost instantly attempt to withdraw what he had been proposing. 

Nobody told the ASN.1 group that they were being "very brave" in withdrawing the macro and ANY and ANY DEFINED BY notation, but somebody should have! I don't know whether they (we) would have backed-off even if told, but I am sure that the extent of the adverse reaction was not anticipated. 

This was the first (and only) non-backwards-compatible change to ASN.1 in its twenty year (todate) history, and gave rise to the "ASN.1 1990 problem" - see below - which lingered on for almost a decade. 

## 12 The ASN.1(1990) controversy

When the 1994 version of ASN.1 was published, there was an accompanying campaign to get people to change their specifications from use of ANY and ANY DEFINED BY and macros to use of the information object concepts. I think the ASN.1 group felt that as this would not 

Never, never, never produce a specification that makes illegal what was previously legal. If you do, you will regret it! But maybe sometimes it is the only way to get rid of a bad feature? 

change any "bits on the line", it was not a big deal! But of course any change to a specification (even to add a single comma) that is "stable" and not immediately about to be re-issued in a new version is actually a costly exercise. The gains must be apparent. 

The ASN.1 group had no doubt: there were so many flaws with the macro notation and the use of ANY, and the information object concepts and associated notation were so much better. Everyone should make the transition. A transition plan was agreed. A lot of the use of macro notation was in the original ROSE OPERATION and ERROR macros. So it was agreed that ROSE would change in 1994 (it did - keeping the old macro definition as an informative annex) and that users of ROSE would change no later than 1998. 

New specifications (like SET - Secure Electronic Transactions) did, of course, like the readers of this book(!), have no problems in adopting the new concepts - they gave important clarity in the specification of protocols with holes in them. 

Specifications such as X.400 and X.500, which defined their own macros and were still in the process of being extended also bettered the agreed time-frame. They recognised the greater clarity of the new notation, and switched to it early in the 1990s. 

However, there were some groups that found the change more difficult, and resisted it for longer. Interestingly, the embargo that the USA placed on writing new macros lead one group whose protocol was almost 50% "ANY" (of course I exaggerate!) to define (in English) their own notation for specifying the information objects (as we now call them) that would complete their protocol. This notation is called "Generic Definition of Managed Objects" (GDMO), and is today supported by its own set of tools specific to that application and that notation. This group had the least incentive, and took longest, to make the transition to the 1994 version of ASN.1. (Removal of uses of "ANY" from their protocol.) 

It is normal in ISO for a revised Standard to automatically replace an earlier version. It replaces it in the sense that the older version can no longer be purchased, and is no longer recorded in the catalogue of available ISO Standards, and new Standards are not allowed to refer to the old version. 

Because the definition of the ASN.1 notation in ASN.1 (1994) was not fully backwards compatible with the ASN.1 (1990) definition (and because everyone knew that time was needed for standards referencing ASN.1 to up-date their specifications to conform to the 1994 versions), there was strong pressure to "retain" ASN.1 (1990). ISO Central Secretariat agreed to this, provided a resolution to that effect was passed by SC21 at each of its annual plenary meetings. 

Of course, these resolutions became the focus of a battle-ground, with each year the ASN.1 group increasingly strongly proposing withdrawal of ASN.1 1990, and each year some group or other saying "we are not ready yet". It was actually 1999 before ASN.1 (1990) was finally laid to rest! 

This has been a salutary lesson, and if in an ASN.1 meeting anyone dares to propose a change that would make illegal anything that could reasonably be interpreted as legal under the current wording, there are howls of "1990, 1990", and the proposal fails! Even if changes do not affect the bits on the line, the notation is now sacrosanct - too many people use it, and existing specifications can not be made retrospectively illegal. 

## 13 The emergence of PER

## 13.1 The first attempt - PER-2

Pronounce that "PER minus 2"! 

It took three attempts to get PER to where it is today - PER-2, PER-1, and finally real-PER. 

Work on producing better encoding rules started at about the same time as work on understanding how macros were being used, and on mending or replacing macros, and was for a long time overshadowed by that work, with only a small number of people really contributing to work on new encoding rules. 

The original work (let me call this "PER-2", pronounced "PER minus 2"!) was based on using BER and "improving" it. The recognition was that BER often transmitted octets down the line that a decoder (provided they had knowledge of the identical type definition to that being used by an encoder) could totally predict. This was what had to be sent at that point. Therefore it did not need to be sent. 

```txt
Example-for-encoding ::= SEQUENCE
{first-element INTEGER (0..127),
second-element SEQUENCE
{string OCTET STRING (SIZE (2)),
name PrintableString (SIZE (1..8)) }
third-element BIT STRING (SIZE (8)) }

Figure IV-2: An example sequence to be encoded 
```

It was also recognised that if the length field of a constructed encoding was changed to provide a count of the number of TLVs in the encoding of the contents rather than a count of the octets in the contents, then further octets could be removed. And finally, it was recognised that if there were constraints on the length of a character string field or on the size of an integer, then length fields could be omitted. 

Accept these changes to BER, and examine figure IV-2, a (slightly contrived) example of a type to be encoded, and figure IV-3, the BER encoding of that type. 

```ini
1 T=[Universal 16]
2 L=3 (TLV count)
3 T=[Universal 2]
4 L=1
5 V=what-ever
6 T=[Universal 16]
7 L=2 (TLV count)
8 T=[Universal 4]
9 L=2
10-11 V=what-ever
12 T=[Universal 19]
13 L=5 (say)
14-18 V=what-ever
19 T=[Universal 3]
20 L=2
21 V1=0 (no unused bits in last octet)
22 V2=what-ever

Figure IV-3: The 22 octet BER encoding of figure IV-2 
```

Looking at figure IV-3, we have 22 octets in the BER encoding. But all except octets 5, 10-11, 13-18, and 22 (a total of 10 octets) are completely known by a decoder, and need never be transmitted! PER-2 said "delete them!". 

(Interestingly, whilst the final real-PER specification was totally different from this early approach, it is just these 10 octets that the current real-PER will transmit!) 

The PER-2 draft said essentially: 

• Do a standard BER encoding (slightly modified to provide counts of TLVs rather than octets for constructed encodings). 

• Apply the following rules to delete octets from the encoding. 

• At the receiving end, apply the rules in reverse to reconstruct the original BER encoding. 

• Do a standard BER decoding (again modified to use TLV counts). 

Some of the rules for when you could delete octets were obvious and straight-forward, some got quite complicated. The reader might like to try to formulate precisely the rules that enabled us to delete (not transmit) 12 of the 22 octets in the encoding of figure IV-3. 

PER-2 was really a sort of "expert system" approach to encoding. There were a whole raft of rules to be applied to determine when you could or could not delete octets (with re-insertion on receipt), and these were very ad hoc and some-how looked as if they were not complete and not founded on any good general principles. (They were ad hoc, and were not founded on any general principles!) 

But the text was eventually deemed complete, and sent for ballot. The editing meeting to consider ballot comments was in New Jersey, and was scheduled to last for one week (this being the only business under consideration). Something went wrong with the administration, and the copies of the formal National Body responses to the ballot only became available by fax at 9am on the first day of the meeting. 

Faces dropped. Everyone knew their own country's response, but until then they did not know what others had said. Every, yes every, National Body had voted "DISAPPROVE". And none of the comments were in any way helpful for further progress. They more or less all said "This is just too complicated, too ad hoc, it will never work". None of them suggested anything that could be done to change the PER-2 draft to make it acceptable. 

The meeting broke up for lunch that day at about 11am, with many delegates (there were about a dozen present representing five or six countries) ringing their air-lines to find out how much more it would cost to fly back that day rather than on their scheduled flight at the end of the week. Other delegates (myself included) retired to the bar to drown their sorrows. 

After enough beer had been consumed, people started to think the unthinkable. Why don't we just abandon the TLV principle and start from scratch? Forget interworking between different versions of a standard (PER-2 didn't really provide that anyway) - how would we encode stuff, using maximum human intelligence, to produce minimum octets on the line? The "back of a cigarette packet" (actually, it was a paper table napkin) design started to take shape. (I wish now that I had kept the napkin, but I think it was consigned to the WPB. So much for important historical documents!) Come 2pm, the chairman (Bancroft, the Editor, I think) said, "Shall we convene and get this meeting wrapped up?". "No," was the response from the then mildly intoxicated bar group (drunk - never!), "we might be getting somewhere." I think the meeting eventually resumed that day at around 4pm. PER-1 (PER minus 1), almost PER as we now know it (but not quite) had been borne. 

The principles were in place: 

Forget about tags - abandon them! (You had to be pretty drunk to make that statement - TLV was a sort of mind-set it was hard to break out of.) 

Make full use of knowledge about constraints on integers and on lengths to remove length fields whenever possible. 

How to solve the problem of SET elements being in a random order? Fix the order! (You had to be a little drunk to say that too!) 

• How to identify a chosen element of a CHOICE? Encode a choice index. 

• How to identify missing OPTIONAL elements in a SEQUENCE or SET? Use a bit-map at the head of the SEQUENCE or SET. 

• How to encode a BOOLEAN - well of course, use just one bit! 

But .... octet-alignment? Recognise it is good to have padding bits at times so that later material which is a sequence of elements that are an integral number of octets will lie on an octet boundary, but use the minimum number of bits without worrying about octet alignment where that looks sensible. 

There were still some elements of the "expert system" approach to this design (as there are with current PER). It is a fairly ad hoc decision on which fields should encode into bit-fields (no padding bits) and which into octet-aligned-bit-fields (with padding bits). 

A lot of details remained to be solved, but the meeting continued for the rest of the week, drafts were produced and considered, and PER-1 became a reality, with later editorial work being done to produce good text over the next few months. 

## 13.2 The second attempt - PER-1

When PER-1 was balloted, it got a much more favorable response than PER-2, but there was still a very strong "DISAPPROVE" vote from the USA which said "Regrettably, after much discussion, we have to disapprove of PER-1. With PER-1 there is no way a version 1 system can interwork with a version 2 system (you can't even find the end of an encoding unless you are both working with an identical type definition). This stuff just isn't going to work for International Standards. Kill it." 

Nope - you must go back to TLV. Only TLV can provide interworking between version 1 and version 2 systems. It is a tried and true technique. Well, the last sentence is true, but is the second? We know now that it is not. In 1992 we were less sure! 

This meeting was less traumatic than the last, but this "interworking" (or "extensibility" problem as it became known) delayed the production of the final real-PER for just over twelve months. 

## 13.3 And eventually we get real-PER

A lot of trees were cut down to provide paper for people to describe what sorts of additions or changes they would want to make between version 1 and version 2 of a protocol. The consensus that emerged was essentially "We only need to add things at the end." 

The ellipsis goes into the notation (and the exception marker with it), and the extension bit goes into PER. We have got there! 

The ellipsis was provided for people to indicate this, and the extension bit in PER provided the encoding support. 

The real-PER approach is to say essentially: 

• If parts of the specification are not flagged as extensible, then encode them in an efficient manner. 

• If parts are marked extensible, but the values are values of the version 1 specification (in the root), provide one bit to say so, but still encode them efficiently. 

• If extensible parts have values outside of the root (version 2 additions), set the extensions bit to one, and provide a length wrapper. 

It is unlikely that this approach would have been developed if we had not been starting from a design (PER-1) that did efficient encodings, with no concern for interworking. The various traumas on the path to PER were probably necessary to break the in-built tradition of TLV encodings as the only way to provide version 1 to version 2 interworking. 

This is not quite the end of the story! Later, there was strong pressure to be able to add things in the middle of sequences and sets, and version brackets were added. 

There was also pressure from the air traffic control people to get rid of the padding bits and to forget about octet alignment, which produced the UNALIGNED version of PER. 

But these were minor problems. The path from PER-1 to the final PER has left us with text which is not always as precise as it should be, and in particular the integration of the extensibility and extensions bit concept into the PER-1 text still poses some problems today (1999), with arguments (and probably eventually corrigenda) related to obscure uses of the extensibility notation (which fortunately no-one has yet written, and perhaps never will!). Many of these problems were uncovered by Olivier and myself when we started writing our books! Fortunately, we both agreed on what the answer should be, and I think our books both tell the same story! 

## 14 DER and CER

(Sounds familiar? Yup, I've used that box before - sorry!) 

The major "option" in a BER encoding is the use of definite or indefinite lengths for constructed encodings. There was never agreement on which was best, and both are allowed in the BER specification. There have been all sorts of rows over the years when some profiling groups attempted to mandate one form or the other. 

Engraven on the hearts of standardizers: Your job is to produce Standards. If you can't agree, make it optional, or better still, another Standard. After all, if one Standard is good, many standards must be better! 

Roughly speaking, for short messages, the definite length form is probably the most sensible, but for long ones the indefinite form is to be preferred. Leaving the option to an implementor seems like a good idea, but of course it means that decoders have to handle both forms. 

If, however, you want encoding rules with no options for the encoder (to minimise the testing problem and to help with security-related problems, as discussed in clause 10 of Section III Chapter 1) then you have to bite the bullet! 

X.500 first produced (as about a twenty-line specification) the rules for producing a canonical encoding of BER, and they called it a "distinguished" encoding. It did enough of the job to cover the types that they wanted to apply it to, but was not complete. It also (arguably) did not make some choices in an optimal manner. 

The ASN.1 group decided to produce a standard for a canonical version of BER which it decided to call "Distinguished Encoding Rules", taking the name from X.500. 

The major difference between the ASN.1 specification and the X.500 specification was that X.500 mandated use of definite length encodings, and the ASN.1 group went for indefinite length wherever they were possible! 

Major liaison statements, etc etc. Meanwhile, workers on another standard - ODA (Office Document Architecture) - who had very large messages to ship but who also needed canonical encodings, liked the ASN.1 groups draft! 

So the eventual up-shot was effectively two separate standards, one for DER (totally aligned with the early X.500 text, and using definite length encodings), and one for CER ("improving" on the © OS, 31 May 1999 353 original X.500 work, and using indefinite length encodings whenever possible). Both "standards" are, of course, published alongside BER in X.690 (ISO/IEC 8825-1). 

The X.500 use of DER is mainly for certificates, becoming now heavily used in the development of e-commerce. (Most e-commerce activity is based on X.509 certificates, which use DER encoding.) By contrast, the ODA work has not been widely implemented. So whatever their relative technical merits, DER has become the de facto standard for canonical encodings of BER, and CER is probably dead! 

## 15 Semantic models and all that - ASN.1 in the late 1990s

There have always been questions about the legality of certain ASN.1 constructs where things were syntactically permissible, but might or might not really be something you should allow. The main area of these problems is in "type matching" rules between a value reference and its governor. For example, with: 

Humans only write simple and obvious ASN.1. But stupid dumb computers want to know about the legality of the most abstruse expressions that the syntax allows. And the computers have an important voice in the tool vendors! They have to be listened to! 

## intval INTEGER ::= 7

You might ask whether you can legally write as an element of a sequence: 

## [27] INTEGER DEFAULT intval

or 

## INTEGER (0..127) DEFAULT intval

Of course you would expect these to be legal, yes? But "[27] INTEGER" and "INTEGER (0..27)" are certainly not exactly the same type as "INTEGER". All three types do not contain exactly the same values, and the encoding of their common values differs in either or both of BER and PER. 

Again, if a value reference is defined using a certain (fairly complex) type definition, and that value reference is then used when governed by an identical (but textually distinct) type reference, is that legal? And if the second textual occurrence is not quite identical to the first, by how much can it deviate before the text becomes illegal ASN.1? 

Add to these examples use of the extension marker .... 

These are the problems that are being grappled with in the late 1990s, and which will probably lead to the inclusion in the standard of models (pictures) of types as buckets containing values, and of "value mappings" between types which are defined by textually separate pieces of notation. Similar models/pictures are needed to cover types that have an ellipsis, and/or extensions. 

The guiding principle in all this work is to make things legal if they make any sort of sense (rather than a tight specification that makes only the most obviously correct things legal), but to end up with a very complete specification of what is legal ASN.1. 

Of course, the reader will guess that the pressure for this work comes from tool vendors. They have to write code which is required to make judgments on the legality or otherwise of stuff that no protocol specifier in their right mind would ever write! 

## 16 What got away?

There have been a few features of ASN.1 development that have not made it into the current standard. They may get resurrected, but probably won't! 

<table><tr><td>Could ASN.1 be even better? There are certainly further improvements that have been discussed. But is the added complexity worth the gains? The consensus is &quot;NO&quot;.</td></tr></table>

The Light Weight Encoding Rules (LWER) were fully discussed in Section III Chapter 4, and will not be referred to again here. 

Probably the major loss was in not providing an efficient encoding for SEQUENCE OF CHARACTER STRING, and for the encoding of a table where each column can be the choice of a number of possible types. 

In the case of CHARACTER STRING (which, if you remember, carries two object identifier values with each encoding of this type), the original concept was to permit chains of encodings of type CHARACTER STRING, where each encoding in any given chain had the same object identifier values. These values would be transmitted at the start of each chain, and then, rather like virtual circuits in network protocol, there would be an abbreviated identification to link each encoding into its chain. Unfortunately, serious bugs were found in this chaining concept (because of interaction with extensions), and it was very rapidly withdrawn within days of its initial publication. 

At the time, it was felt that another feature "run-time parameters" (also called "dynamic constraints", because the run-time parameters could only be used in constraints) could support the same efficiency requirement, but run-time parameters (dynamic constraints) were eventually abandoned. 

The approach was abandoned not because of any inherent problems, but simply that the marketplace (ASN.1 users) did not really seem to be demanding it, and adding a further fairly complex feature to ASN.1 did not seem worthwhile. 

What were these run-time parameters? The idea was that a type could be a parameterised type, but the actual parameters would be transmitted in an instance of communication rather than being specified when the type was referenced. This would enable any information that was common to a SEQUENCE OF (for example the object identifiers of SEQUENCE OF CHARACTER STRING, or the identification of the types for each column of a table) to be transmitted just once, rather than with each element of the SEQUENCE OF. 

Another abandoned feature was "global parameters". If you have a parameterised type, it is quite common for parameters to be passed down from the abstract syntax definition through many levels of type definition to the point where they are eventually used. 

The global parameters work was intended to improve clarity and reduce the verbosity of specifications by providing essentially a direct path from a parameter of the abstract syntax to the point where it would be used. 

If you rather like some of these ideas, get into the standardization game and see if you can bring them back! If you don't want to get into the standardization game, then just agree that ASN.1 is great as it is, and we can end this chapter! 

END OF CHAPTER. 

# Chapter 2 Applications of ASN.1

## (Or: Are you using software that does ASN.1 encodings?)

## Summary:

This chapter: 

• Tries to provide an indication of the application areas in which ASN.1 has been used. 

• Tries to identify some of the organizations that have used ASN.1 as their chosen specification-language. 

• Uses a partial historical framework for the discussion of applications and organizations. 

## 1 Introduction

This brief chapter outlines some of the areas in which ASN.1 has been applied. It in no way claims to be exhaustive, and if some groups feel offended that they have not been mentioned, I apologise! 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/6bf2cdb75daf70c884363fbabdd16c90ab1a02e5d71e7727d09b2686eb66c423.jpg)


Equally, I have seen Web pages that say they will include their ASN.1 definitions, only to be assured by people I trust that use of ASN.1 for that particular application was abandoned! I hope there are not too many errors in what follows, but I am sure there are serious omissions. 

Whilst the emphasis is on different applications, the treatment is partly historical, showing the gradual extension of the use of ASN.1 from a single application (X.400) to a wide range of applications today. 

Thus this chapter complements the previous historical chapter. 

The chapter does not contain a detailed list of ISO Standard numbers and ITU-T Recommendations and Internet RFCs, but rather gives a broad outline of application areas with the occasional mention of an actual specification as an illustration. 

For anyone interested, a more complete set of detailed references to specifications using ASN.1 can be found via the URL in Appendix 5, or in the companion text by Olivier Dubuisson (also referenced via Appendix 5). 

Most of the acronyms in this chapter can be used as input to Web search engines, and will usually result in hits on home-pages for the relevant organizations or specifications. This is the best way to obtain more information if Appendix 5 does not work for you! (Web URLs have a habit of changing!) 

There are also Web sites (access via Appendix 5 or a search) for ITU-T and ETSI and ECMA that will give you much more information about their specifications, and in the case of ITU-T a list of the Recommendations that use ASN.1. (If you get interested in any of the ITU-T Recommendations, beware - they can all be purchased and delivered on-line, but it will cost you serious money!) 

This chapter inevitably contains a lot of acronyms - every protocol and every organization has its own acronym. I try to spell out the acronym if it has not been used in earlier text, but sometimes it it seems hardly worth the effort, because the acronym is often far better known than the full title! 

In many cases you will find that a document you locate via a search uses the acronym without giving the full name. Many, many people know these acronyms, but would have to think hard to give you the full name, and would probably then get it wrong! (In some cases, different Web and other documents give different full names for the same acronyms - but clearly intend to identify the same thing!) 

So, we do our best. But if you want a challenge, see what you can find out about the following acronyms (in the ASN.1 context). They are given in no particular order. Some are mentioned in this chapter, most are not. It is believed that they all relate to protocols or organizations that are using ASN.1 as a specification language. Test yourself on the following: 

SET, SNMP, TCAP, CMIP, PKCS, MHS, ACSE, CSTA, NSDP, DPA, TDP, ETSI, DMH, ICAO, IMTC, DAVIC, DSS1, PKIX, IIF, LSM, MHEG, NSP, ROS(E), FTAM, JTMP, VT, RPI, RR, SCAI, TME, WMtp, GDMO, SMTP. 

If you don't get 100% (although some could of course be mistyping!), you are not a network guru, and can't charge $$££££$$ per hour for your advice on network matters! 

If you commute between Europe and the US and are active in both communities, you stand a better chance of meeting the challenge than those operating on only one side of the Atlantic pond. Of course, ASN.1 tool providers CERTAINLY know what all these acronyms mean, 'cos they are selling their tools to support them. But will they tell? 

Well, I honestly admit that after a fair bit of research I can cover about 95% of the above list (I have described a lot less than 95% in this chapter), but certainly not all! 

If any reader can cover the lot (and preferably give a URL for further info) then an e-mail to the my address via the link in Appendix 5 would be welcomed - but too late for this book, maybe the second edition? 

## 2 The origins in X.400

X.400 was originally a related set of CCITT Recommendations covering (with gaps) X.400 to X.430. The X.400 specifications were intended to become the (OSI) de facto e-mail system for the world. 

Everything has a beginning! 

X.400 started off with many advantages over the Internet mail protocol (at that time it was Simple Mail Transfer Protocol (SMTP), with no frills - frills like Multipurpose Internet Mail Extensions (MIME) were added later). 

X.400 from the start supported a variety of different types of "body part", permitting multi-media attachments to mail, and in its 1998 version incorporated virtually all the security features of the Military Message Handling Systems (MMHS) specifications (security features in SMTP are still very much poorer). 

SMTP was, however, enhanced with the MIME extensions to provide for the transfer of arbitrary attachments (albeit at about twice the band-width of X.400) and Internet mail implementations today generally do not accept mail from outside their own domain, reducing (but not eliminating) the risks of masquerade. (None of this work is ASN.1-based.) But whatever the technical merits or otherwise, we all know that SMTP-based e-mail is now the world's de facto standard, although X.400 still plays a roll in gateways between different mail systems, and in military communications, and has other minority followings. 

ASN.1 was originally produced to support just this one X.400 specification, and is, of course, still used in all the ongoing X.400 work. 

Another important specification which was originally produced to support just X.400 was the Remote Operations Service Element (ROSE) specification - originally just called "ROS". Like ASN.1, this became recognised as of more general utility, and moved into the X.200 series of Recommendations. (ROSE is discussed further in Section II Chapter 6). ROSE was (and is) totally ASN.1-based and is the foundation of many many applications in the telecommunications area. Its requirements were very influential in the development of the Information Object concept and in the recognition of the need to handle "holes". (See the previous chapter on the history of ASN.1.) 

## 3 The move into Open Systems Interconnection (OSI) and ISO

In the early 1980s, papers at conferences would have titles like "OSI versus SNA" (SNA was IBM's "Systems Network Architecture"), with most people believing that the OSI work would eventually become the de facto standard for world-wide networking, but would have a battle 

Rapid expansion to take over the world through OSI - supposedly! But also take-up by several other ISO Technical Committees. 

to unseat SNA. Again, historically, OSI as a whole never really made it, but it was the introduction of ASN.1 into main-stream OSI that moved ASN.1 from being a single-application language into a tool used by many protocol specifiers. 

Very soon after it was introduced from CCITT (as it then was) into ISO, ASN.1 was adopted as the specification language of choice by every single group producing specifications for the Application Layer of OSI and for many other OSI-related standards. Implementations of most of these standards are still in use today, but it is fair to say that in most cases they are in a minority use. 

Most of the OSI applications of ASN.1 were for standards in the so-called "Application Layer" of OSI, developed by ISO/JTC1/SC16, and then (following a reorganization) by ISO/JTC1/SC21. These covered, inter alia, standards for remote database access, for transaction processing, for file transfer, for virtual terminals, and so on. 

The ASN.1 concepts of a separation of abstract and transfer syntax fitted very well with the socalled "Presentation Layer" of OSI for protocols running over the OSI stack and using the Presentation Layer to negotiate the transfer syntax to be used for any given abstract syntax. 

Interestingly, however, ASN.1 was also used to define the Presentation Layer protocol itself - probably the first use of ASN.1 for a protocol which did not run over the OSI Presentation Layer (many others were to follow). 

There was even a draft circulated showing how the OSI Session Layer (the layer below the Presentation Layer) could be defined (more clearly, and in a machine-readable format) using ASN.1. This was accompanied by a draft of a "Session-Layer-BER" which was a minor change to BER and which if applied to the ASN.1 definition would produce exactly the bits on the line that the Session Protocol Standard currently specified. But the Session Layer specifications were complete and stable by then, so the draft was never progressed. 

A similar situation arose with the Generic Definition of Managed Objects (GDMO) - see Clause 8 below, where an equivalent notation using Information Object Classes and "WITH SYNTAX" was identified in a circulated draft - from Japan - but was never progressed because the GDMO work was by then stable and quite mature. 

ASN.1 has been used in many other ISO Technical Committees, in areas such as banking, security, protocols for control of automated production lines, and most recently in the development of protocols in the transportation domain for "intelligent highways". These protocols are often (usually) not carried over the OSI stack, and have served to show the independence of ASN.1 from OSI, despite its early roots in the OSI work. 

A recent example of such use is for the definition (by ISO/TC68) of messages passing between an Integrated Circuit credit card and the card accepting device. 

## 4 Use within the protocol testing community

As well as protocol specifications, the OSI world started the idea of standardized tests of protocol implementations. These test sequences are, of course, protocols in their own right, where a testing system sends messages to an implementation under test, and assesses the responses it gets. The Tree and Tabular Combined Notation (TTCN) is the most commonly used notation for this purpose, and ASN.1 is embedded within this notation for the definition of data structures. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/999d030e1a163a1e941ec951ff0c23ea0a605752ea724d6bee1fa3a1b1acb219.jpg)


Closely related to the TTCN application is the use of ASN.1 within another ITU-T formal description technique, System Description Language (SDL). 

The European Telecommunications Standards Institute (ETSI) has been a major actor in the development of testing specifications using these notations. 

## 5 Use within the Integrated Services Digital Network (ISDN)

In the 80's, Integrated Services Digital Network (ISDN) was the great talking point. It grew out of the digitisation of the telephone network. 

<table><tr><td>Probably the first application of ASN.1 outside of the main OSI work.</td></tr></table>

The telephone network in most advanced countries is now entirely digital apart from the so-called "local loop" between homes and the local telephone exchange, which in the majority of cases remains analogue. 

ISDN provided, using the existing local loops between homes and a local telephone exchange, two so-called "B-channels" each capable of carrying a telephone call or a 64 Kbps data connection, and a "D-channel" (used for signalling between the subscriber and the exchange). ISDN became widely available to telephone subscribers, but its main application was (and still is today - 1999) the use of the two B-channels together to provide a 128 Kbps data channel for video-conferencing over the telephone network. 

Within ISDN, many so-called "supplementary services" (for example, Call Back to Busy Subscriber) were implemented using the D-channel, and ASN.1 (with BER encodings) was chosen to define the protocol for these services. 

## 6 Use in ITU-T and multimedia standards

ASN.1 was, of course, first introduced to ITU-T through X.400 and OSI, but was rapidly taken up by many other standardization groups within ITU-T (then CCITT). 

<table><tr><td>Widespread use of ASN.1 throughout many parts of ITU-T continues to this day.</td></tr></table>

Uses of ASN.1 within ITU-T can be found in: 

• The G-series recommendations for speech encoding and silence compression. 

• The H-series for multimedia (audio-visual) communications, including moving video coding for low bit rate communication, and specifications being implemented by the Interactive Multimedia Teleconferencing Consortium (IMTC). 

• The M-series for test management in ATM. 

• The Q-series for a host of specifications related to ISDN and Intelligent Networks (IN). 

• The T-series for group 3 facsimile and for MHEG communications. 

• The V-series for audio-visual terminal communication. 

• The Z-series for use within SDL (described above) and within GDMO (described in Clause 8 below). 

• And of course, in the X-series for Recommendations that originated in the OSI work. 

Regarding the H-series, the most important of these Recommendations is perhaps the H.323 series for audio, video, and data communication across the Internet (including video-conferencing, interactive shopping, network gaming, and many other multi-media applications - check out the H.323 Web site for further details). Other specifications in the H.320 series address multimedia communication over both narrow-band and broad-band (ATM) ISDN and PSTN communications. These Recommendations seem set to become de facto standards for multi-media communication that will operate over a wide range of network infrastructures. 

It is these Recommendations that cause many familiar products to have ASN.1 (PER in this case) encoders embedded wtihin them, so if you use any of these products, you are using ASN.1 (encodings)! Examples of such products are Microsoft NetMeeting, Intel VideoPhone, PictureTel software, and so on and so on. 

## 7 Use in European and American standardization groups

There are three European standardization groups worth mentioning where ASN.1 has been quite heavily used (no doubt there are others). The first two carry the name "European" in their title, but they all contribute standards to the world-wide community. These are the European Computer Manufacturers Association (ECMA), the 

Many sub-international (to coin a phrase) groups that are really international actors have used ASN.1. 

European Telecommunications Standards Institute (ETSI), and the rather more recent Digital Audio Visual Council (DAVIC). (DAVIC is Europe-based, but would justifiably claim to be a world-wide consortium.) 

ECMA has long worked on OSI-related standards for input into OSI (but also in broader areas - for example, it had significant input into the initial IEEE 802 Standard). It has also produced the ASN.1-based Computer Supported Telecommunications Applications (CSTA) specification for communication between telephone switches and end-user computers. Initial deployment of CSTA has been in support of large Call Centres - an important development in communications in the late 1990s. As is normal with ECMA specifications, the work has been input to ISO for international standardization. 

ETSI is primarily concerned with European variants of ITU-T Recommendations and with the development of telecommunications specifications for input into ITU-T. It has also been active in the development of specifications based on TTCN (which has ASN.1 embedded within it). There is close liaison between ECMA and ETSI on telecommunications standards, and with ITU-T. 

DAVIC is a consortium of 157 companies and government agencies from 25 countries promoting video-conferencing. Its specifications are input to ISO for international standardization. 

There are also a number of standards groups and consortia in the USA that have used ASN.1 in their specifications. Frequently, but not always, such work feeds into international standardization. 

Worth mentioning (but this list is very incomplete and a bit random - it is the ones I have heard about) are: 

The ANSI X9 committees concerned with Financial Industry Standardization (Funds Transfer and EDI, for example), feeding into ISO/TC68. 

The American Chemical Society for the exchange of chemical information and DNA sequences (for the Web site, see links via Appendix 5 to the National Centre for Biological Information (NCBI)). 

Many Federal Information Processing Standards (FIPS) concerned with security matters, for example, FIPS PUB 188 on Standard Security Labels for Information Transfer - the Standard Security Label is defined as an ASN.1 type: "SET OF NamedTagSet" where "NamedTagSet" is .... etc. 

• The SET consortium (see Clause 9 below). 

## 8 Use for managing computer-controlled systems

Another major "invention" from the OSI work was the concept of "managed objects" (devices that are interrogated, tested, configured, reset, etc by remote communications). This came out of the work on Common Management Information Services/Protocol (CMIS/CMIP), which produced a model of such objects (identified by ASN.1 object identifiers) having attributes (which were ASN.1 types identified by further ASN.1 object identifiers). "Management" was essentially performed by reading from or writing to these "attributes" (using CMIP) which were, as it were, on the surface of the managed objects, and provided external visibility and contro of the object. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/8162efd0291dcaa79bfae15064b24fc2495ad12a9afae0bf4613f0ee5b6e04ee.jpg)


When the CMIP standard was first published, it was a protocol full of "holes" - not a single managed object and its attributes had been defined at that stage! A notation was clearly needed to allow people to define (preferably in a machine-readable way) managed objects. An ASN.1 macro might well have been used to define that notation, but by then there was an embargo on writing new macros, and the replacement Information Object Class work was still in its infancy. So Generic Definition of Managed Objects (GDMO) was defined (in English) as a notation for specifying the necessary details about managed objects, with ASN.1 as an embedded notation within GDMO. 

In the Internet world, the concepts of CMIS/CMIP were adopted, and while work was still continuing on the development of CMIS/CMIP, an RFC was produced for Simple Network Management Protocol (SNMP). Initially, this was stated to be a temporary solution until CMIS/CMIP matured, but like most temporary solutions, it became rather permanent, and has today a greater market share of management of remote devices than does CMIS/CMIP. 

Like CMIS/CMIP, SNMP also uses ASN.1, but in a very cut-down form, and with considerable restrictions on the form of ASN.1 types that can be used to define the values to be set or read on managed objects. This did, however, represent the first real penetration of ASN.1 into the Internet standardization community. 

CMIS/CMIP was originally designed to control implementations of the OSI stack in network switches and remote hosts, but (like SNMP) it is increasingly used today to manage remotely anything that is computer controlled. So applications of management protocols can include the steering of telescopes or radar dishes, or even the switching on and off of washing machines or ovens! (But I am not sure the latter are yet a reality.) 

## 9 Use in PKCS and PKIX and SET and other security-related protocols

Let's just get the acronyms in the title out of the way! PKCS is Public Key Cryptographic Standards, PKIX is Public Key Infrastructure (X.509), and SET is Secure Electronic Transactions (a little more detail on these follows below). 

The wide-spread adoption of X.509 (ASN.1-based) certificates has made ASN.1 the dominant specification technique in security work. 

X.500 is one of the OSI Standards that still has significant support, and its use of ASN.1 in the OSI work has led to adoption of ASN.1 in almost all security-related protocols. 

X.500 was (and is) an ISO and ITU-T Standard and Recommendation, but the Light-Weight Directory Access Protocol (LDAP), which is a functional subset of X.500 is an Internet RFC, and is rapidly becoming the de facto standard for access to Directory services, leaving X.500 proper for use "behind the scenes" to link local LDAP servers to provide a world-wide Directory service. LDAP uses the ASN.1 notation to define its messages, but specifies a text encoding for values of the (limited) subset of ASN.1 that it uses (see later discussion in Clause 10 on preferences for textbased protocols among Internet specifiers). 

Whilst X.500 was primarily designed to provide a world-wide Directory service, allowing look-up of a very wide variety of information with a world-wide search, it also provided the first standard (X.509) for certificates (which were - and are, of course, an ASN.1 type). 

The basic certificate concept is that a Certification Authority (CA) will provide a public and private key pair (usually for some commercial fee) to an applicant, and will also provide an electronic bit-pattern (a certificate) that is encrypted using the public key of the CA. The certificate is an ASN.1 type that provides an association between the public key issued to the applicant and some property of the applicant (name, company registration number, etc). Certificates cannot be forged provided the CA keeps its own private key secure. However, anyone knowing (for absolutely sure) the public key of the CA, can decrypt the certificates it issues and hence "believe" the public key of the organization or person that the certificate contains - and hence apply some degree of "trust" to that organization or person (and to messages or signatures that decrypt to produce valid hash values using that public key). Of course, the public key of the CA is usually obtained from another certificate issued by a "higher" CA, whose public key is obtained from another certificate issued by .... and so on, until, .... well, .... the Netscape public key is usually built into your Web browser software! (Which of course you obtained from a trustworthy source!). 

This process of obtaining a public key from one certificate to unlock another certificate to get a public key which unlocks another certificate etc is called certificate chaining, and originally people expected just one or two top-level CAs in the entire world, with their public keys really public - perhaps advertised daily in the newspapers! 

But then just about every national government decided it wanted one of its agencies to be a toplevel CA, and many companies also decided to be their own CA for internal use. And suddenly the problem of distribution of public keys and of degrees of trust got a lot more complicated. 

PKIX stands for Public Key Infrastructure (X.509), and is a set of Internet RFCs and Draft RFCs which specify how CAs should operate. For example, PKIX 4 specifies the form of a Certification Policy Statement (CPS) which all conforming CAs should make available to the public. The CPS says, for example, that (before issuing a certificate) the CA should verify individual names by requiring a photo-copy of a passport, or an actual passport, or a birth certificate, or (for a company in the UK) has checked that the Registered Office exists, as registered with Companies House, or ... You get the idea. The certificate they issue asserts that there is some association between the public key it contains and some further information about an individual or company. How much trust can you place in that assertion? The CPS helps you to determine that. 

Several parts of PKIX use ASN.1, fully and straight-forwardly. 

PKCS stands for Public-Key Cryptographic Standards. These are standards produced by a consortium of RSA Data Security and its major licensees, including Microsoft, Apple, Lotus, Sun, Novell, and MIT. PKCS uses ASN.1 as its notation for defining data-structures and their encoding. 

Another important security-related protocol is Secure Electronic Transactions (SET), produced by a consortium of MasterCard, Visa, and other parts of the computer and banking industries. SET is designed to support electronic commerce in a fully secure manner, and hence uses X.509 certificates, and is itself about 60 pages of ASN.1 (with many more pages of supporting text). 

When SET certificates are stored on smart-cards (because of the limited memory available on smart-cards) PER encoding is likely to be used with an ASN.1 datatype called a compressed certificate. 

In general, the use of ASN.1 in X.509 has led most security-related protocols to use ASN.1. 

## 10 Use in other Internet specifications

We have already discussed PKCS and PKIX and SNMP. ASN.1 (with PER) was considered for use in the latest version of HTTP, but instead an ASN.1-like notation called "pseudo-C was invented. 

Yes, even here we see some use of ASN.1! 

In general, Internet specifiers try to keep protocol specifications as simple as possible and to make it easy for implementors to operate without specialised tools, or using only tools that are in the public domain. 

This tends to lead to protocols that in the end are simply lines of ASCII text (usually defined using BNF), or, if ASN.1 is used, to use of a subset of the ASN.1 notation. 

The Web is very much part of the Internet, but the World-Wide Web Consortium (W3C) now has very much a life of its own. 

It is within the W3C forum that work is on-going to marry XML and ASN.1 through the definition of XML Encoding Rules (XER). This work is recent, and was mentioned also in Section III Chapter 3. 

## 11 Use in major corporate enterprises and agencies

It is known that a number of house-hold name corporations and national and international agencies have made use of (and are still using) ASN.1 and its encoding rules to support communications activities within their corporations and agencies. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/1f002efacb6ddc15f55f3985205bae08c87a6a50da6a21ea284a64a0f3b6ccb1.jpg)


However, attempts to obtain more details for publication in this book met with an almost universal rejection, due to concerns about commercial confidentiality of the applications. With regret, therefore, I have decided to make no mention of any specific name of a commercial organization unless the information about their use of ASN.1 appears on the Web. 

I will, however, mention one agency, and this is the International Civil Aviation Organization (ICAO). 

The ICAO is worth mentioning because it was the first organization to take-up (and to help in the development of) the Packed Encoding Rules. PER encodings were described in ICAO specifications long before the actual ASN.1 specifications were finally ratified, and use of ASN.1 and PER is fundamental to their Aeronautical Telecommunication Network (ATN). 

## 12 Conclusion

ASN.1 has come a long way from the days when it provided support for just one application (X.400). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/54379e17-c034-430b-894c-f77661f731e5/c60ff5478eec3b041ea80a8d0974a652a5a63f7bc8be05be2f87a80ce304f77f.jpg)


It is now used to a significant extent by all the main specifiers of protocols, and in some (but not all) cases is the dominant specification language. Usually use of the notation is associated with use of the ASN.1-defined encodings, with a few exceptions. 

If you were to wave a magic wand and eliminate from the world all messages that are encodings of ASN.1-defined values, disaster would certainly strike on a scale far beyond any that the most pessimistic have described for possible effects of the Y2K (year 2000) computer bugs. (Or any that actually occurred if you are reading this book post-2000!) 

Aircraft would collide, mobile phones would cease to work, virtually all telecoms and network switches would be unmanageable and unmaintainable and would gradually die, electric power distribution systems would cease to work, and to look a little further ahead before we wave our magic wand, smart-card-based electronic transactions would fail to complete and your washing machine might fail to work! But worst of all, your NetMeeting with your newly betrothed would suddenly collapse and your life would become a misery! 

It is on that happy note that we will conclude this book! 

## APPENDICES

# 1 The Wineco protocol scenario

Many of the examples in this book are based on the development of the "Wineco protocol". This is a fictitious protocol, used simply to illustrate various parts of ASN.1. The first parts of it appear in Figure 13 of Section 1 Chapter 2, and a full copy of the final protocol is given in Appendix 2 below. 

Wineco is a company selling wine from a variety of outlets, and owning two warehouses, one northern and one southern. Initially all outlets were in the UK only (where the name of an outlet could be supported by the ASCII character set), but later Wineco extended to overseas territories, where a larger character set was needed. 

In Figure 13 we see one of the messages we use in the protocol, "Order-for-stock", to request a number of cases of particular types of wine with a specified urgency. We also see the form of a "Branch-identification" type. 

In Section 1 Chapter 3 we add the necessary module headers, and some extensibility markers with an insertion point not at the end. Later we turn it into a multi-module specification with "common types" in one module, the top-level type in another, and the ordering protocol message "Order-forstock" in a third. We also introduced a second top-level message in Figure 21, "Return-of-sales", which provides for a report on the sales that have been made within the last period. 

In Chapter 4 of Section 1 we populated the "Return-of-sales" message in a hopefully plausible way, but really solely in order to illustrate the remaining ASN.1 basic data types! Exception markers and exception handling are introduced in this Chapter. "Return-of-sales" and the "Reportitem" type it uses are used as the main example for illustration of the output from an ASN.1- compiler-tool, given in Appendix 3 for C and in Appendix 4 for Java. 

"Return-of-sales" is also used to illustrate the ASN.1 value notation in at the Section I Chapter 4 (Figure 23). 

The next use of our example is in Chapter 3 of Section II, when we decide to define a "basic class" protocol as a strict subset of our "full class" protocol, both for ordering and for return of sales. Here we have also added a third top-level message as we enter the digital-cash age! We are up-loading the contents of our electronic till using an enhanced protocol. 

The final major extension is when we decide (in Section II Chapter 6 to change over to use of a Remote Operations metaphor, with four defined operations. This leads to two further modules - one to define the Remote Operations PDU (which in the real world would have been imported from the Remote Operations Service (ROSE) Standard, and one to define the Wineco operation Information Objects. 

# 2 The full protocol for Wineco

This appendix gives the final version of the specification of the Wineco protocol in a form that is syntactically correct and complete. 

```txt
Wineco-common-top-level
{joint-iso-itu-t international-organization(23) set(42)
set-vendors(9) wineco(43) modules(2) top(0)}
DEFINITIONS
AUTOMATIC TAGS ::= BEGIN

EXPORTS;
IMPORTS Order-for-stock FROM
Wineco-ordering-protocol
{wineco-OID modules(2) ordering(1)}
Return-of-sales FROM
Wineco-returns-protocol
{wineco-OID modules(2) returns(2)};
wineco-OID OBJECT IDENTIFIER ::= 
{joint-iso-itu-t international-organization(23) set(42)
set-vendors(9) wineco(43)}

wineco-abstract-syntax ABSTRACT-SYNTAX ::= 
{Wineco-protocol IDENTIFIED BY
{wineco-OID abstract-syntax(1)}
HAS PROPERTY
{handles-invalid-encodings}
--See clause 45.6 --
}

Wineco-protocol ::= CHOICE
{ordering [APPLICATION 1] Order-for-stock,
sales [APPLICATION 2] Return-of-sales,
... ! PrintableString : "See clause 45.7"
}

END
--New page in published spec.
Wineco-ordering-protocol
{joint-iso-itu-t international-organization(23) set(42)
set-vendors(9) wineco(43)modules(2) ordering(1)}
DEFINITIONS
AUTOMATIC TAGS ::= BEGIN

EXPORTS Order-for-stock;

IMPORTS OutletType, Address, Security-Type FROM
Wineco-common-types
{wineco-OID modules(2) common (3)};
wineco-OID OBJECT IDENTIFIER ::= 
{joint-iso-itu-t international-organization(23) set(42)
set-vendors(9) wineco(43)}

Order-for-stock ::= SEQUENCE
{order-no INTEGER,
name-address BranchIdentification,
details SEQUENCE OF

© OS, 31 May 1999 
```

```txt
SEQUENCE
{item OBJECT IDENTIFIER,
cases INTEGER},
urgency ENUMERATED
{tomorrow(0),
three-day(1),
week(2)} DEFAULT week,
authenticator Security-Type}

BranchIdentification ::= SET
{unique-id OBJECT IDENTIFIER,
details CHOICE
{uk [0] SEQUENCE
{name VisibleString,
type OutletType,
location Address},
overseas [1] SEQUENCE
{name UTF8String,
type OutletType,
location Address},
warehouse [2] CHOICE
{northern [0] NULL,
southern [1] NULL} }
}
END
New page in published spec.
Wineco-returns-protocol
{joint-iso-itu-t international-organization(23) set(42)
set-vendors(9) wineco(43) modules(2) returns(2)}
DEFINITIONS
AUTOMATIC TAGS ::=
BEGIN

EXPORTS Return-of-sales;

IMPORTS OutletType, Address, Security-Type FROM
Wineco-common-types
{wineco-OID modules(2) common (3)};
wineco-OID OBJECT IDENTIFIER ::=
{joint-iso-itu-t international-organization(23) set(42)
set-vendors(9) wineco(43)}

Return-of-sales ::= SEQUENCE
{version BIT STRING
{version1 (0), version2 (1)} DEFAULT {version1},
no-of-days-reported-on INTEGER
{week(7), month (28), maximum (56)} (1..56) DEFAULT week,
time-and-date-of-report CHOICE
{two-digit-year UTCTime,
four-digit-year GeneralizedTime},
-- If the system clock provides a four-digit year,
-- the second alternative shall be used. With the
-- first alternative the time shall be interpreted
-- as a sliding window.
reason-for-delay ENUMERATED
{computer-failure, network-failure, other} OPTIONAL,
-- Include this field if and only if the
-- no-of-days-reported-on exceeds seven.
additional-information SEQUENCE OF PrintableString OPTIONAL,
-- Include this field if and only if the
-- reason-for-delay is "other".
sales-data SET OF Report-item,
... ! PrintableString : "See wineco manual chapter 15" } 
```

```txt
Report-item ::= SEQUENCE
{item OBJECT IDENTIFIER,
item-description ObjectDescriptor OPTIONAL,
-- To be included for any newly-stocked item.
bar-code-data OCTET STRING,
-- Represents the bar-code for the item as specified
-- in the wineco manual chapter 29.
ran-out-of-stock BOOLEAN DEFAULT FALSE,
-- Send TRUE if stock for item became exhausted at any
-- time during the period reported on.
min-stock-level REAL,
max-stock-level REAL,
average-stock-level REAL
-- Give minimum, maximum, and average levels during the
-- period as a percentage of normal target stock-level--
wineco-items OBJECT IDENTIFIER ::=
{joint-iso-itu-t international-organization(23) set(42)
set-vendors(9) wineco(43)stock-items (0)}
END

Wineco-common-types
{joint-iso-itu-t internationalRA(23) set(42)
set-vendors(9) wineco(43) modules(2) common(3)}
DEFINITIONS
AUTOMATIC TAGS ::=
BEGIN

EXPORTS OutletType, Address, Security-Type;
-- IMPORTS Security-Type FROM
-- SET-module
-- {joint-iso-itu-t internationalRA(23) set(42) module(6) 0};
--Removed for this appendix to avoid needing the import,
--and replaced by the type below.

Security-Type ::= SEQUENCE{
    algorithm OBJECT IDENTIFIER,
    encoding OCTET STRING}

--OutletType is not populated in main text--
OutletType ::= SEQUENCE
{type ENUMERATED{mail-order, retail},
description CHARACTER STRING}

--Address is not populated in main text--
Address ::= SEQUENCE
{name UTF8String,
town UTF8String,
country UTF8String}
END 
```

# 3 Compiler output for C support for the Wineco protocol

This appendix contains the text produced by the "OSS ASN.1 Tools" product to provide support for a C implementation of "Return-of-sales" and "Report-item" in our Wineco protocol. (Some of this text is generated just for wineco, some is generic definitions obtained from an include file, for example "GeneralizedTime" and "ossBoolean"): 

```c
typedef struct {
    short year; /* YYYY format when used for GeneralizedTime */
    /* YY format when used for UTCTime */

    short month;
    short day;
    short hour;
    short minute;
    short second;
    short millisec;
    short mindiff; /* UTC +/- minute differential */
    ossBoolean utc; /* TRUE means UTC time */
} GeneralizedTime;

typedef GeneralizedTime UTCTime;

typedef struct ObjectID {
    unsigned short length;
    unsigned char *value;
} ObjectID;

typedef struct Report_item {
    unsigned char bit_mask;
# define ran_out_of_stock_present 0x80
    ObjectID item;
char *item_description; /* NULL for not present */
struct {
    unsigned int length;
    unsigned char *value;
} bar_code_data;
ossBoolean ran_out_of_stock; /* ran_out_of_stock_present not set in
* bit_mask implies value is FALSE */
double min_stock_level;
double max_stock_level;
double average_stock_level;
} Report_item;

typedef struct Return_of_sales {
    unsigned char bit_mask;
# define version_present 0x80
# define no_of_days_reported_on_present 0x40
# define reason_for_delay_present 0x20
# define additional_information_present 0x10
    unsigned char version; /* version_present not set in bit_mask
* implies value is { version1 } */ 
```

```c
#    define version1 0x80
#    define version2 0x40
unsigned short no_of_days_reported_on; /* no_of_days_reported_on_present not set * in bit_mask implies value is week */
#    define week 7
#    define month 28
#    define maximum 56
struct {
    unsigned short choice;
    define two_digit_year_chosen 1
    define four_digit_year_chosen 2
    union {
    UTCTime two_digit_year; /* to choose, set choice to * two_digit_year_chosen */
    GeneralizedTime four_digit_year; /* to choose, set choice to * four_digit_year_chosen */
    } u;
} time_and_date_of_report;
enum {
    computer_failure = 0,
    network_failure = 1,
    other = 2
} reason_for_delay; /* optional; set in bit_mask * reason_for_delay_present * if present */
struct _seqof1 {
    struct _seqof1 *next;
    char *value;
} *additional_information; /* optional; set in bit_mask * additional_information_present if present */
struct _setof1 {
    struct _setof1 *next;
    Report_item value;
} *sales_data;
} Return_of_sales; 
```

# 4 Compiler output for Java support for the Wineco protocol

This appendix contains the text for Java support for the "Return-of-sales" and the "Report-item" types in the Wineco protocol. This is a part of the output produced by the "OSS ASN.1 Tools" product when it is fed with the Wineco modules. This is a bit more bulky than Annex 3 - does that say anything? Whoops - BAD STATEMENT - no way can one appear to be criticising Java! This is more than Figure 999 stuff!. The Java code is bulkier because it contains all the methods for setting and reading fields and for inserting and deleting items in SEQUENCE OF, so it does rather more than the C code in Appendix 3. If you don't know Java, you will certainly want to ignore this appendix. Even if you do know Java, you will probably only want to look at a few sample classes and methods. Here is the Java code: 

```java
package wineco.wineco_returns_protocol;
import com.oss.asn1.*;
import com.oss.util.*;
import wineco.*;
import wineco.wineco_common_types.*;

public class Return_of_sales extends Sequence {

    /**
    The default constructor.
    */
    public Return_of_sales() {}

    protected ASN1World getASN1World()
    { return wineco.Wineco.cASN1World; }
    protected int getTypeIndex()
    { return Wineco_returns_protocol.Return_of_sales_PDU; }

    /**
    Construct from a IAAPI Value Reference.
    */
    public Return_of_sales(ASN1World world, int index)
    { ASN1Module.getValueReference(world, this, index); }

    /**
    Construct with components.
    */
    public Return_of_sales(
    Version version,
    No_of_days_reported_on no_of_days_reported_on,
    Time_and_date_of_report time_and_date_of_report,
    Reason_for_delay reason_for_delay,
    Additional_information additional_information,
    Sales_data sales_data)
    {
    SetVersion(version);
    SetNo_of_days_reported_on(no_of_days_reported_on);
    SetTime_and_date_of_report(time_and_date_of_report);
    SetReason_for_delay(reason_for_delay);
    SetAdditional_information(additional_information);

    }
} 
```

```txt
SetSales_data(sales_data);
}

/**
Construct with required components.
*/
public Return_of_sales(
    Time_and_date_of_report time_and_date_of_report,
    Sales_data sales_data)
{
    SetTime_and_date_of_report(time_and_date_of_report);
    SetSales_data(sales_data);
}

protected void initComponents()
{
    mComponents[0] = new Version();
    mComponents[1] = new No_of_days_reported_on();
    mComponents[2] = new Time_and_date_of_report();
    mComponents[3] = new Reason_for_delay();
    mComponents[4] = new Additional_information();
    mComponents[5] = new Sales_data();
}

// Instance initializer
{
    mComponents = new AbstractData[6];
    mPresentBits = new java.util.BitSet(mComponents.length);
}

// Methods for field "version"
public Version getVersion()
{
    return (Version)mComponents[0];
}
public void SetVersion(Version version)
{
    mComponents[0] = version;
    SetComponentPresent(0);
}
public void SetVersionToDefault() {SetComponentAbsent(0); }
public boolean hasDefaultVersion() { return componentIsPresent(0); }
public boolean hasVersion() { return componentIsPresent(0); }
public void deleteVersion() { SetComponentAbsent(0); }

public static class Version extends BitString {
    /**
    The default constructor.
    */
    public Version() { super(new byte[1], 2); }

    /**
    Construct Bit String from a byte array and significant bits.
    @param value the byte array to set this object to.
    @param sigBits the number of significant bits.
    */
    public Version(byte[] value, int sigBits)
    { super(value, sigBits); }

    protected ASN1World getASN1World()
    { return wineco.Wineco.cASN1World; }

    // Named list definitions.
    public static final int version1 = 0;
S, 31 May 1999 
```

```lisp
public static final int version2 = 1;
} // End class definition for Version

// Methods for field "no_of_days_reported_on"
public No_of_days_reported_on getNo_of_days_reported_on()
{
    return (No_of_days_reported_on)mComponents[1];
}
public void SetNo_of_days_reported_on
    (No_of_days_reported_on no_of_days_reported_on)
{
    mComponents[1] = no_of_days_reported_on;
    SetComponentPresent(1);
}
public void SetNo_of_days_reported_onToDefault()
    {SetComponentAbsent(1); }
public boolean hasDefaultNo_of_days_reported_on()
    {return componentIsPresent(1); }
public boolean hasNo_of_days_reported_on()
    {return componentIsPresent(1); }
public void deleteNo_of_days_reported_on()
    {SetComponentAbsent(1); }

public static class No_of_days_reported_on extends INTEGER {

    /**
    The default constructor.
    */
    public No_of_days_reported_on() {}
    public No_of_days_reported_on(short value) { super(value);}
    public No_of_days_reported_on(int value) { super(value);}
    public No_of_days_reported_on(long value) { super(value);}
    protected ASN1World getASN1World()
    { return wineco.Wineco.cASN1World; }

    // Named list definitions.
    public static final No_of_days_reported_on week =
    new No_of_days_reported_on(7);
    public static final No_of_days_reported_on month =
    new No_of_days_reported_on(28);
    public static final No_of_days_reported_on maximum =
    new No_of_days_reported_on(56);
    private final static No_of_days_reported_on cNamedNumbers[] = {week, month, maximum};
    protected final static long cFirstNumber = 7;
    protected final static boolean cLinearNumbers = false;
    protected INTEGER[] getNamedNumbers() { return cNamedNumbers;}
    protected boolean hasLinearNumbers() { return cLinearNumbers;}
    protected long getFirstNumber() { return cFirstNumber;}
} // End class definition for No_of_days_reported_on

// Methods for field "time_and_date_of_report"
public Time_and_date_of_report getTime_and_date_of_report()
{
    return (Time_and_date_of_report)mComponents[2];
}
public void SetTime_and_date_of_report
    (Time_and_date_of_report time_and_date_of_report)
{
    mComponents[2] = time_and_date_of_report;
} 
```

```java
public static class Time_and_date_of_report extends Choice {

    /**
    The default constructor.
    */
    public Time_and_date_of_report() {}

    protected ASN1World getASN1World()
    { return wineco.Wineco.cASN1World; }

    /**
    Construct from a IAAPI Value Reference.
    */
    public Time_and_date_of_report(ASN1World world, int index)
    { ASN1Module.getValueReference(world, this, index); }

    public static final int two_digit_year_chosen = 1;
    public static final int four_digit_year_chosen = 2;

    // Methods for field "two_digit_year"
    public static Time_and_date_of_report
    createTime_and_date_of_reportWithTwo_digit_year
    (UTCTime two_digit_year)
    {Time_and_date_of_report __object =
    new Time_and_date_of_report();
    __object.SetTwo_digit_year(two_digit_year);
    return __object;
    }
    public boolean hasTwo_digit_year() {
    return getChosenFlag() == two_digit_year_chosen;
    }
    public void SetTwo_digit_year (UTCTime two_digit_year) {
    SetChosenValue(two_digit_year);
    SetChosenFlag(two_digit_year_chosen);
    }
    // Methods for field "four_digit_year"
    public static Time_and_date_of_report
    createTime_and_date_of_reportWithFour_digit_year
    (GeneralizedTime four_digit_year)
    {Time_and_date_of_report __object =
    new Time_and_date_of_report();
    __object.SetFour_digit_year(four_digit_year);
    return __object;
    }
    public boolean hasFour_digit_year() {
    return getChosenFlag() == four_digit_year_chosen;
    }
    public void SetFour_digit_year
    (GeneralizedTime four_digit_year) {
    SetChosenValue(four_digit_year);
    SetChosenFlag(four_digit_year_chosen);
    }
    // Method to create a specific choice instance
    protected AbstractData createInstance(int chosen) {
    switch(chosen) {
    case two_digit_year_chosen: return
    new UTCTime();
    case four_digit_year_chosen: return
    new GeneralizedTime();
    default: throw
    new InternalError("Choice.createInstance()");
    }
    }
} // End class definition for Time_and_date_of_report 
```

```txt
// Methods for field "reason_for_delay"
public Reason_for_delay getReason_for_delay()
{
    return (Reason_for_delay)mComponents[3];
}
public void SetReason_for_delay(Reason_for_delay reason_for_delay)
{
    mComponents[3] = reason_for_delay;
    SetComponentPresent(3);
}
public boolean hasReason_for_delay()
    { return componentIsPresent(3); }
public void deleteReason_for_delay()
    { SetComponentAbsent(3); }

public static class Reason_for_delay extends Enumerated {

    /**
    The default constructor.
    */
    public Reason_for_delay() {super(cFirstNumber);}
    protected Reason_for_delay(long value) { super(value); }

    protected ASN1World getASN1World()
    { return wineco.Wineco.cASN1World; }

    // Named list definitions.
    public static final Reason_for_delay computer_failure =
    new Reason_for_delay(0);
    public static final Reason_for_delay network_failure =
    new Reason_for_delay(1);
    public static final Reason_for_delay other =
    new Reason_for_delay(2);
    private final static Reason_for_delay cNamedNumbers[] =
    {computer_failure, network_failure, other};
    protected final static long cFirstNumber = 0;
    protected final static boolean cLinearNumbers = false;
    protected Enumerated[] getNamedNumbers() { return cNamedNumbers;}
    protected boolean hasLinearNumbers() { return cLinearNumbers;}
    protected long getFirstNumber() { return cFirstNumber;}
} // End class definition for Reason_for_delay

// Methods for field "additional_information"
public Additional_information getAdditional_information()
{
    return (Additional_information)mComponents[4];
}
public void SetAdditional_information
    (Additional_information additional_information)
{
    mComponents[4] = additional_information;
    SetComponentPresent(4);
}
public boolean hasAdditional_information()
    { return componentIsPresent(4); }
public void deleteAdditional_information()
    { SetComponentAbsent(4); }

public static class Additional_information extends SequenceOf {

    /**
    The default constructor.
    */ 
```

```lisp
public Additional_information() {}

protected ASN1World getASN1World()
    { return wineco.Wineco.cASN1World; }

/**
Construct from a IAAPI Value Reference.
*/
public Additional_information(ASN1World world, int index)
{ASN1Module.getValueReference(world, this, index); }

/**
Add an Element to the SEQUENCE OF/SET OF.
*/
public synchronized void add(PrintableString element)
{
    super.addElement(element);
}
/**
Set an Element in the SEQUENCE OF/SET OF.
*/
public synchronized void set
(PrintableString element, int atIndex)
{
    super.SetElement(element, atIndex);
}
/**
Get an Element from the SEQUENCE OF/SET OF.
*/
public synchronized PrintableString get(int atIndex)
{
    return (PrintableString) super.getElementById(atIndex);
}
/**
Insert an Element into the SEQUENCE OF/SET OF.
*/
public synchronized void insert
(PrintableString element, int atIndex)
{
    super.insertElement(element, atIndex);
}
/**
Remove an Element from the SEQUENCE OF/SET OF.
*/
public synchronized void remove(PrintableString element)
{
    super.removeElement(element);
}
/**
Create an instance of SEQUENCE OF/SET OF.
*/
public AbstractData createInstance()
{
    return ((AbstractData) new PrintableString());
}
} // End class definition for Additional_information

// Methods for field "sales_data"
public Sales_data getSales_data()
{
    return (Sales_data)mComponents[5];
}
public void SetSales_data(Sales_data sales_data)
{
    }
} 
```

```txt
mComponents[5] = sales_data;
}

public static class Sales_data extends SetOf {

    /**
    The default constructor.
    */
    public Sales_data() {}

    protected ASN1World getASN1World()
    { return wineco.Wineco.cASN1World; }

    /**
    Construct from a IAAPI Value Reference.
    */
    public Sales_data(ASN1World world, int index)
    { ASN1Module.getValueReference(world, this, index); }

    /**
    Add an Element to the SEQUENCE OF/SET OF.
    */
    public synchronized void add(Report_item element)
    {
    super.addElement(element);
    }
    /**
    Set an Element in the SEQUENCE OF/SET OF.
    */
    public synchronized void set(Report_item element, int atIndex)
    {
    super.SetElement(element, atIndex);
    }
    /**
    Get an Element from the SEQUENCE OF/SET OF.
    */
    public synchronized Report_item get(int atIndex)
    {
    return (Report_item) super Element(atIndex);
    }
    /**
    Insert an Element into the SEQUENCE OF/SET OF.
    */
    public synchronized void insert
    (Report_item element, int atIndex)
    {
    super.insertElement(element, atIndex);
    }
    /**
    Remove an Element from the SEQUENCE OF/SET OF.
    */
    public synchronized void remove(Report_item element)
    {
    super.removeElement(element);
    }
    /**
    Create an instance of SEQUENCE OF/SET OF.
    */
    public AbstractData createInstance()
    {
    return ((AbstractData) new Report_item());
    }
} // End class definition for Sales_data
// End class definition for Return_of_sales 
```

```java
public class Report_item extends Sequence {

    /**
    The default constructor.
    */
    public Report_item() {}

    protected ASN1World getASN1World()
    { return wineco.Wineco.cASN1World; }

    /**
    Construct from an IAAPI Value Reference.
    */
    public Report_item(ASN1World world, int index)
    { ASN1Module.getValueReference(world, this, index); }

    /**
    Construct with components.
    */
    public Report_item(
    ObjectIdentifier item,
    ObjectDescriptor item_description,
    OctetString bar_code_data,
    boolean ran_out_of_stock,
    double min_stock_level,
    double max_stock_level,
    double average_stock_level)
    {
    SetItem(item);
    SetItem_description(item_description);
    SetBar_code_data(bar_code_data);
    SetRan_out_of_stock(ran_out_of_stock);
    SetMin_stock_level(min_stock_level);
    SetMax_stock_level(max_stock_level);
    SetAverage_stock_level(average_stock_level);
    }

    /**
    Construct with required components.
    */
    public Report_item(
    ObjectIdentifier item,
    OctetString bar_code_data,
    double min_stock_level,
    double max_stock_level,
    double average_stock_level)
    {
    SetItem(item);
    SetBar_code_data(bar_code_data);
    SetMin_stock_level(min_stock_level);
    SetMax_stock_level(max_stock_level);
    SetAverage_stock_level(average_stock_level);
    }

    protected void initComponents()
    {
    mComponents[0] = new ObjectIdentifier();
    mComponents[1] = new ObjectDescriptor();
    mComponents[2] = new OctetString();
    mComponents[3] = new BOOLEAN();
    mComponents[4] = new Real();
    mComponents[5] = new Real();
    mComponents[6] = new Real();
} 
```

```lisp
// Instance initializer
{
    mComponents = new AbstractData[7];
    mPresentBits = new java.util.BitSet(mComponents.length);
    mComponents[3] = new BOOLEAN();
    mComponents[4] = new Real();
    mComponents[5] = new Real();
    mComponents[6] = new Real();
}

// Methods for field "item"
public ObjectIdentifier getItem()
{
    return (ObjectIdentifier)mComponents[0];
}
public void SetItem(ObjectIdentifier item)
{
    mComponents[0] = item;
}

// Methods for field "item_description"
public ObjectDescriptor getItem_description()
{
    return (ObjectDescriptor)mComponents[1];
}
public void SetItem_description(ObjectDescriptor item_description)
{
    mComponents[1] = item_description;
    SetComponentPresent(1);
}
public boolean hasItem_description()
    { return componentIsPresent(1); }
public void deleteItem_description()
    { SetComponentAbsent(1); }

// Methods for field "bar_code_data"
public OctetString getBar_code_data()
{
    return (OctetString)mComponents[2];
}
public void SetBar_code_data(OctetString bar_code_data)
{
    mComponents[2] = bar_code_data;
}

// Methods for field "ran_out_of_stock"
public boolean getRan_out_of_stock()
{
    return ((BOOLEAN) mComponents[3]).booleanValue();
}
public void SetRan_out_of_stock(boolean ran_out_of_stock)
{
    ((BOOLEAN) mComponents[3]).SetValue(ran_out_of_stock);
    SetComponentPresent(3);
}
public void SetRan_out_of_stockToDefault()
    {SetComponentAbsent(3); }
public boolean hasDefaultRan_out_of_stock()
    { return componentIsPresent(3); }
public boolean hasRan_out_of_stock()
    { return componentIsPresent(3); }
public void deleteRan_out_of_stock() 
```

```cpp
{
    SetComponentAbsent(3);
}

// Methods for field "min_stock_level"
public double getMin_stock_level()
{
    return ((Real) mComponents[4]).doubleValue();
}
public void SetMin_stock_level(double min_stock_level)
{
    ((Real) mComponents[4]).SetValue(min_stock_level);
}

// Methods for field "max_stock_level"
public double getMax_stock_level()
{
    return ((Real) mComponents[5]).doubleValue();
}
public void SetMax_stock_level(double max_stock_level)
{
    ((Real) mComponents[5]).SetValue(max_stock_level);
}

// Methods for field "average_stock_level"
public double getAverage_stock_level()
{
    return ((Real) mComponents[6]).doubleValue();
}
public void SetAverage_stock_level(double average_stock_level)
{
    ((Real) mComponents[6]).SetValue(average_stock_level);
}
} // End class definition for Report_item 
```

## 5 ASN.1 resources via the Web

This appendix provides a single link to an OSS Nokalva site that contains both links to other Web resources and extensions of this book. In particular, it contains: 

References to other publications (both Web-based and hard-copy) that are relevant to readers of this book. 

• A glossary of terms relevant to ASN.1, including all the acronyms used in this book. (Most of the acronyms used here are also included in the index, which will provide you with a quick look-up and perhaps a little more information.) 

Details of, and/or links to other web-based ASN.1 resources such as mailing lists, Olivier Dubuisson's site with his book, the Unicode site, my own site with my book "Understanding OSI", the International Register site, ITU-T and ETSI sites, a site giving the allocations for some parts of the Object Identifier tree, etc etc. 

More details of specifications that are defined using ASN.1, with links to electronic versions of those specifications where these are known to be publicly available. 

Errata sheets for this book as and when they are produced. 

• An electronic copy of this book. 

The URL for the OSS Nokalva site is: 

http://www.nokalva.com 

Please come and visit! 

And just in case things might move – URLs have a habit of changing – a cross-link is also provided at: 

http://www.larmouth.demon.co.uk/books 

## Index

{
...}....229
7
7-layer model....25
A
abstract syntax....25
Abstract Syntax Notation One....16, 328
abstract syntaxes....345
ABSTRACT-SYNTAX....49, 73, 76
ANY....230
ANY DEFINED BY....231
API....117, 122
application-required modules....77
application-required types....76
applications of ASN.1....357
ASN.1 module....62
ASN.1 tools....39, 44
ASN.1-compiler-tool....111
automatic tagging....68
AUTOMATIC TAGGING....54
AUTOMATIC TAGS....66
B
Bacchus-Naur Form....42
Basic Encoding Rules....30, 236, 252
BER....30, 252
Binary-based Specification....24
BIT STRING....84
BMPString....153
BOOLEAN....80
C
canonical....34
canonical order of tags....291
CGM....35
CHARACTER STRING....233
character string types....97, 100, 149, 338
value notation....155
Character-based Specification....24
collections....102, 157
colon....58
comment....58
Common Object Request Broker Architecture....32
compiler....111
COMPONENTS OF....94
© OS, 31 May 1999 

Computer Graphics Metafile....35
concrete syntax....34
CONSTRAINED BY....220
constraints....97, 108
contained subtype constraints....166
CORBA....32
Courier....43, 325, 334

D
date/time types....91
DEFAULT....51
design issues....123
development process....18
distinguished values....80
duplicating text....64

E
EDIFACT....41
effective alphabet constraint....290
effective size constraint....290
ellipsis....69, 130, 182, 352
EMBEDDED PDV....232
Encoding....33
encoding rules....16, 30, 236
ENUMERATED....82
ERROR....345
exception handling....131, 139
exception specification....134
exceptions....104, 181
EXPLICIT....54
explicit tagging....68
EXPLICIT TAGS....66
EXPORTS....71
extensibility28, 60, 66, 70, 97, 104, 129, 139, 181, 282
EXTENSIBILITY IMPLIED....66
EXTERNAL....231

G
GeneralizedTime....91
GeneralString....153
governor....56
GraphicString....153

H
holes....26, 97, 105, 188, 190, 275 

## I

IA5String ..... 152
IDL ..... 32
IETF ..... 15
IMPLICIT ..... 54
implicit tagging ..... 67
IMPLICIT TAGS ..... 66
IMPORTS ..... 71
information object classes ..... 107, 209
information object sets ..... 201
inner subtyping ..... 166
insertion point ..... 70, 184, 308
INSTANCE OF ..... 276
INTEGER ..... 80
Interface Definition Language ..... 32, 191
International Standards Organization ..... 15, 25
International Telecommunications Union
Telecommunications Standards Sector ..... 15
Internet Engineering Task Force ..... 15
Internet Protocol ..... 16, 39
IP23, 39
IPv6 ..... 28
ISO ..... 15, 25
ISO646String ..... 151
ITU-T ..... 15, 43, 361 

## L

layering....25   
layout....57   
leading bit....85, 266   
Light-Weight Encoding Rules....316   
line monitor....38, 140   
line numbers....63   
LWER....316 

## M

machine-readable version....64
macros....97, 106, 345
mailing list....140
management issues....123
mapping....117
MBER....319
Message Handling Systems....43, 359
Minimum Bit Encoding Rules....319 

## N

named bits....84, 85, 86, 266  
names....57  
NULL....88  
NumericString....150 

## O

OBJECT IDENTIFIER.....49, 89, 97, 100, 143, 334 

object identifier encoding....270
object identifier tree....144
ObjectDescriptor....90
OCTET STRING....87
ODA....36
Office Document Architecture....36, 353
OID tree....90
OMG....15
Open Management Group....15
Open Systems Interconnection....25
open types....134
OPERATION....345
OSI....25
OSI layering....189
OSS ASN.1 Tools....13, 110, 372, 374 

## P

Packed Encoding Rules....30, 243, 278
parameterization....108, 134, 205, 221
people....325
PER....30, 243, 278
PER visible constraints....284
permitted alphabet constraints....163
PrintableString....89, 151
protocol....22
Protocol specification....24
Publication style....62 

## R

range constraint....82, 97, 162, 164  
REAL....83, 337  
relational constraint....108  
RELATIVE OID....336  
remote operations....190  
ROSE....190 

## S

scope rules....81
Secure Electronic Transactions....15, 365
selection type notation....93
semantic model....109
semi-colon....58
SEQUENCE....95
SET....15, 95, 147, 365
size constraints....164
sliding window....91
style....128
subsetting....168
subtypes....97, 102, 159 

## T

T61String....152
table constraint....108
tagging environment....66 

tags ....54, 97, 103, 136, 172  
TCP/IP ....16, 23  
TeletexString....152  
time differential....92  
TLV ....29, 40, 236, 239  
top-level type....49  
trailing bit ....85, 266  
transfer syntax....30, 34  
Transmission Control Protocol ....16  
type assignment....56  
TYPE-IDENTIFIER....225 

## U

Unicode....342
UniversalString....153
Useful Type....90
user-defined constraint....108, 220 

UTCTime....91
UTF8String....154
V
value assignments....56
value reference assignment....56
variable syntax....216
version brackets....97, 104, 181
VideotexString....152
VisibleString....151
W
WITH SYNTAX....216
X
X.400....43, 358 