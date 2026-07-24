# ASN.1 Complete

by Prof John Larmouth 

## Dedication

This book is dedicated to the girls at Withington Girls' School that are there with my daughter Sarah-Jayne and to the boys at The Manchester Grammar School that are there with my son James, in the hope that it may some day be of use to some of them! 

## Contents

Contents 3
Foreword 13
Introduction 15
1 The global communications infrastructure 15
2 What exactly is ASN.1? 16
3 The development process with ASN.1 18
4 Structure of the text. 18
SECTION I ASN.1 OVERVIEW 21
Chapter 1 Specification of protocols 22
1 What is a protocol? 22
2 Protocol specification - some basic concepts 24
2.1 Layering and protocol "holes" 25
2.2 Early developments of layering 26
2.3 The disadvantages of layering - keep it simple! 28
2.4 Extensibility 28
2.5 Abstract and transfer syntax 30
2.6 Command line or statement-based approaches 32
2.7 Use of an Interface Definition Language 32
3 More on abstract and transfer syntaxes 32
3.1 Abstract values and types 32
3.2 Encoding abstract values 33
4 Evaluative discussion 35
4.1 There are many ways of skinning a cat - does it matter? 35
4.2 Early work with multiple transfer syntaxes 35
4.3 Benefits 36
Efficient use of local representations 36
Improved representations over time 36
Reuse of encoding schemes 36
Structuring of code 37
Reuse of code and common tools 38
Testing and line monitor tools 38
Multiple documents requires "glue" 38
The "tools" business 39
5 Protocol specification and implementation - a series of case studies 39
5.1 Octet sequences and fields within octets 39
5.2 The TLV approach 40
5.3 The EDIFACT graphical syntax 41
5.4 Use of BNF to specify a character-based syntax 42
5.5 Specification and implementation using ASN.1 - early 1980s 43
5.6 Specification and implementation using ASN.1 - 1990's 44
Chapter 2 Introduction to ASN.1 47
© OS, 31 May 1999 3 

1 Introduction 47
2 The example 48
2.1 The top-level type 49
2.2 Bold is what matters! 49
2.3 Names in italics are used to tie things together 49
2.4 Names in normal font are the names of fields/elements/items 50
2.5 Back to the example! 50
2.6 The BranchIdentification type 52
2.7 Those tags 54
3 Getting rid of the different fonts 55
4 Tying up some lose ends 56
4.1 Summary of type and value assignments 56
4.2 The form of names 57
4.3 Layout and comment 57
5 So what else do you need to know? 58

Chapter 3 Structuring an ASN.1 specification 60
1 An example 61
2 Publication style for ASN.1 specifications 62
2.1 Use of line-numbers. 63
2.2 Duplicating the ASN.1 text 64
2.3 Providing machine-readable copy 64
3 Returning to the module header! 65
3.1 Syntactic discussion 65
3.2 The tagging environment 67
3.2.1 An environment of explicit tagging 68
3.2.2 An environment of implicit tagging 68
3.2.3 An environment of automatic tagging 68
3.3 The extensibility environment 69
4 Exports/imports statements 71
5 Refining our structure 73
6 Complete specifications 76
7 Conclusion 77

Chapter 4 The basic data types and construction mechanisms - closure 78
1 Illustration by example 79
2 Discussion of the built-in types 80
2.1 The BOOLEAN type 80
2.2 The INTEGER type 80
2.3 The ENUMERATED type 82
2.4 The REAL type 83
2.5 The BIT STRING type 84
2.6 The OCTET STRING type 87
2.7 The NULL type 88
2.8 Some character string types 88
2.9 The OBJECT IDENTIFIER type 89
2.10 The ObjectDescriptor type 90
2.11 The two ASN.1 date/time types 91
3 Additional notational constructs 93
3.1 The selection-type notation 93
3.2 The COMPONENTS OF notation 94
3.3 SEQUENCE or SET? 95
3.4 SEQUENCE, SET, and CHOICE (etc) value-notation 96
4 What else is in X.680/ISO 8824-1? 97 

Chapter 5 Reference to more complex areas 99
1 Object identifiers 100
2 Character string types 100
3 Subtyping 102
4 Tagging 103
5 Extensibility, exceptions and version brackets 104
6 Hole types 105
7 Macros 106
8 Information object classes and objects and object sets 107
9 Other types of constraints 108
10 Parameterization 108
12 The ASN.1 semantic model 109
13 Conclusion 109

Chapter 6 Using an ASN.1 compiler 110
1 The route to an implementation 110
2 What is an ASN.1 compiler? 111
3 The overall features of an ASN.1-compiler-tool 113
4 Use of a simple library of encode/decode routines 113
4.1 Encoding 114
4.2 Decoding 115
5 Using an ASN.1-compiler-tool 116
5.1 Basic considerations 116
5.2 What do tool designers have to decide? 116
5.3 The mapping to a programming-language data structure 117
5.4 Memory and CPU trade-offs at run-time 118
5.5 Control of a tool 119
6 Use of the "OSS ASN.1 Tools" product 120
7 What makes one ASN.1-comiler-tool better than another? 121
8 Conclusion 122

Chapter 7 Management and design issues for ASN.1 specification and implementation 123
1 Global issues for management decisions 124
1.1 Specification 124
1.1.1 To use ASN.1 or not! 124
1.1.2 To copy or not? 124
1.2 Implementation - setting the budget 125
1.2.1 Getting the specs 125
1.2.2 Training courses, tutorials, and consultants 126
1.3 Implementation platform and tools 126
2 Issues for specifiers 127
2.1 Guiding principles 127
2.2 Decisions on style 128
2.3 Your top-level type 128
2.4 Integer sizes and bounds 129
2.5 Extensibility issues 130
2.6 Exception handling 131
2.6.1 The requirement 131
2.6.2 Common forms of exception handling 131
2.6.2.1 SEQUENCE and SET 131
2.6.2.2 CHOICE 131
2.6.2.3 INTEGER and ENUMERATED 132
2.6.2.4 Extensible strings 132
2.6.2.5 Extensible bounds on SET OF and SEQUENCE OF 132

OS, 31 May 1999    5 

2.6.2.6 Use of extensible object sets in constraints 133
2.6.2.7 Summary 133
2.6.3 ASN.1-specified default exception handling 133
2.6.4 Use of the formal exception specification notation 134
2.7 Parameterization issues 134
2.8 Unconstrained open types 135
2.9 Tagging issues 136
2.10 Keeping it simple 136
3 Issues for implementors 137
3.1 Guiding principles 137
3.2 Know your tool 138
3.3 Sizes of integers 138
3.4 Ambiguities and implementation-dependencies in specifications 139
3.5 Corrigenda 139
3.6 Extensibility and exception handling 139
3.7 Care with hand encodings 140
3.8 Mailing lists 140
3.9 Good engineering - version 2 **will** come! 140
4 Conclusion 141

SECTION II FURTHER DETAILS 142

Chapter 1 The object identifier type 143
1 Introduction 143
2 The object identifier tree 145
3 Information objects 146
4 Value notation 147
5 Uses of the object identifier type 148

Chapter 2 The character string types 149
1 Introduction 150
2 NumericString 150
3 PrintableString 151
4 VisibleString (ISO646String) 151
5 IA5String 152
6 TeletexString (T61String) 152
7 VideotexString 152
8 GraphicString 153
9 GeneralString 153
10 UniversalString 153
11 BMPString 153
12 UTF8String 154
13 Recommended character string types 154
14 Value notation for character string types 155
15 The ASN.1-CHARACTER-MODULE 157
16 Conclusion 158

Chapter 3 Subtyping 159
1 Introduction 159
2 Basic concepts and set arithmetic 160
3 Single value subtyping 162
4 Value range subtyping 162
5 Permitted alphabet constraints 163

© OSS,31 May 1999 

6 Size constraints 164
7 Contained sub-type constraints 166
8 Inner Subtyping 166
8.1 Introduction 166
8.2 Subsetting Wineco-Protocol 168
8.3 Inner subtyping of an array 170
9 Conclusion 171

Chapter 4 Tagging 172
1 Review of earlier discussions 172
2 The tag name-space 173
3 An abstract model of tagging 176
4 The rules for when tags are required to be distinct 179
5 Automatic tagging 180
6 Conclusion 180

Chapter 5 Extensibility, Exceptions, and Version Brackets 181
1 The extensibility concept 181
2 The extension marker 182
3 The exception specification 183
4 Where can the ellipsis be placed? 183
5 Version brackets 184
6 The {...} notation 185
7 Interaction between extensibility and tagging 185
8 Concluding remarks 187

Chapter 6 Information Object Classes, Constraints, and Parameterization 188
1 The need for "holes" and notational support for them 189
1.1 OSI Layering 189
1.2 Hole support in ASN.1 190
2 The ROSE invocation model 190
2.1 Introduction 190
2.2 Responding to the INVOKE message 192
3 The use of tables to complete the user specification 193
3.1 From specific to general 195
4 From tables to Information Object Classes 196
5 The ROSE OPERATION and ERROR Object Class definitions 198
6 Defining the Information Objects 199
7 Defining an Information Object Set 201
8 Using the information to complete the ROSE protocol 203
9 The need for parameterization 205
10 What has not been said yet? 208

Chapter 7 More on classes, constraints, and parameterization 209
1 Information Object Class Fields 209
1.1 Type fields 210
1.2 Fixed type value fields 211
1.3 Variable type value fields 212
1.4 Fixed type value set fields 213
1.5 Variable type value set fields 213
1.6 Object fields 214
1.7 Object set fields 214
1.8 Extended field names 215
2 Variable syntax for Information Object definition 216

© OS, 31 May 1999    7 

3 Constraints re-visited - the user-defined constraint 220
4 The full story on parameterization 221
4.1 What can be parameterized and be a parameter? 222
4.2 Parameters of the abstract syntax 224
4.3 Making your requirements explicit 225
4.3.1 The TYPE-IDENTIFIER class 225
4.3.2 An example - X.400 headers 225
4.3.3 Use of a simple SEQUENCE 226
4.3.4 Use of an extensible SEQUENCE 227
4.3.5 Moving to an information object set definition 227
4.3.6 The object set "Headers" 228
4.4 The (empty) extensible information object set 229
5 Other provision for "holes" 230
5.1 ANY 230
5.2 ANY DEFINED BY 231
5.3 EXTERNAL 231
5.4 EMBEDDED PDV 232
5.5 CHARACTER STRING 233
5.6 OCTET STRING and BIT STRING 233
6 Remarks to conclude Section II 234

SECTION III ENCODINGS 235

Chapter 1 Introduction to encoding rules 236
1 What are encoding rules, and why the chapter sub-title? 236
2 What are the advantages of the encoding rules approach? 238
3 Defining encodings - the TLV approach 239
4 Extensibility or "future proofing" 240
5 First attempts at PER - start with BER and remove redundant octets 241
6 Some of the principles of PER 243
6.1 Breaking out of the BER straight-jacket 243
6.2 How to cope with other problems that a "T" solves? 244
6.3 Do we still need T and L for SEQUENCE and SET headers? 245
6.4 Aligned and Unaligned PER 246
7 Extensibility - you have to have it! 246
8 What more do you need to know about PER? 247
9 Experience with PER 248
10 Distinguished and Canonical Encoding Rules 250
11 Conclusion 251

Chapter 2 The Basic Encoding Rules 252
1 Introduction 252
2 General issues 253
2.1 Notation for bit numbers and diagrams 253
2.2 The identifier octets 254
2.3 The length octets 256
2.3.1 The short form 256
2.3.2 The long form 257
2.3.3 The indefinite form 258
2.3.4 Discussion of length variants 259
3 Encodings of the V part of the main types 260
3.1 Encoding a NULL value 260
3.2 Encoding a BOOLEAN value 261

8 © OSS,31 May 1999 

3.3 Encoding an INTEGER value 261
3.4 Encoding an ENUMERATED value 262
3.5 Encoding a REAL value 262
3.5.1 Encoding base 10 values 262
3.5.2 Encoding base 2 values 263
3.5.3 Encoding the special real values 265
3.6 Encoding an OCTET STRING value 266
3.7 Encoding a BIT STRING value 266
3.8 Encoding values of tagged types 267
3.9 Encoding values of CHOICE types 268
3.10 Encoding SEQUENCE OF values 268
3.11 Encoding SET OF values 269
3.12 Encoding SEQUENCE and SET values 269
3.13 Handling of OPTIONAL and DEFAULT elements in sequence and set 270
3.14 Encoding OBJECT IDENTIFIER values 270
3.15 Encoding character string values 273
3.16 Encoding values of the time types 275
4 Encodings for more complex constructions 275
4.1 Open types 275
4.2 The embedded pdv type and the external type 276
4.3 The INSTANCE OF type 276
4.4 The CHARACTER STRING type 276
5 Conclusion 277

Chapter 3 The Packed Encoding Rules 278
1 Introduction 279
2 Structure of a PER encoding 279
2.1 General form 279
2.2 Partial octet alignment and PER variants 280
2.3 Canonical encodings 281
2.4 The outer level complete encoding 281
3 Encoding values of extensible types 282
4 PER-visible constraints 284
4.1 The concept 284
4.2 The effect of variable parameters 285
4.3 Character strings with variable length encodings 286
4.4 Now let's get complicated! 286
5 Encoding INTEGERs - preparatory discussion 288
6 Effective size and alphabet constraints. 289
6.1 Statement of the problem 289
6.2 Effective size constraint 290
6.3 Effective alphabet constraint 290
7 Canonical order of tags 291
8 Encoding an unbounded count 291
8.1 The three forms of length encoding 292
8.2 Encoding "normally small" values 295
8.3 Comments on encodings of unbounded counts 296
9 Encoding the OPTIONAL bit-map and the CHOICE index. 296
9.1 The OPTIONAL bit-map 296
9.2 The CHOICE index 297
10 Encoding NULL and BOOLEAN values. 297
11 Encoding INTEGER values. 297
11.1 Unconstrained integer types 298
11.2 Semi-constrained integer types 298
OS, 31 May 1999    9 

11.3 Constrained integer types 299
11.4 And if the constraint on the integer is extensible? 300
12 Encoding ENUMERATED values. 301
13 Encoding length determinants of strings etc 302
14 Encoding character string values. 304
14.1 Bits per character 304
14.2 Padding bits 305
14.3 Extensible character string types 306
15 Encoding SEQUENCE and SET values. 306
15.1 Encoding DEFAULT values 307
15.2 Encoding extension additions 307
16 Encoding CHOICE values. 310
17 Encoding SEQUENCE OF and SET OF values. 311
18 Encoding REAL and OBJECT IDENTIFIER values. 312
19 Encoding an Open Type 312
20 Encoding of the remaining types 313
21 Conclusion 313

Chapter 4 Other ASN.1-related encoding rules 315
1 Why do people suggest new encoding rules? 315
2 LWER - Light-Weight Encoding Rules 316
2.1 The LWER approach 317
2.2 The way to proceed was agreed 317
2.3 Problems, problems, problems 317
2.4 The demise of LWER 319
3 MBER - Minimum Bit Encoding Rules 319
4 OER - Octet Encoding Rules 320
5 XER - XML (Extended Mark-up Language) Encoding Rules 321
6 BACnetER - BAC (Building Automation Committee) net Encoding Rules 321
7 Encoding Control Specifications 322

SECTION IV HISTORY AND APPLICATIONS 323

Chapter 1 The development of ASN.1 324
1 People 325
2 Going round in circles? 326
3 Who produces Standards? 327
4 The numbers game 328
5 The early years - X.409 and all that 329
5.1 Drafts are exchanged and the name ASN.1 is assigned 329
5.2 Splitting BER from the notation 330
5.3 When are changes technical changes? 331
5.4 The near-demise of ASN.1 - OPERATION and ERROR 331
6 Organization and re-organization! 333
7 The tool vendors 334
8 Object identifiers 334
8.1 Long or short, human or computer friendly, that is the question 334
8.2 Where should the object identifier tree be defined? 336
8.3 The battle for top-level arcs and the introduction of RELATIVE OIDs 336
9 The REAL type 337
10 Character string types - let's try to keep it short! 338
10.1 From the beginning to ASCII 338
10.2 The emergence of the international register of character sets 338

10 © OSS,31 May 1999 

10.3 The development if ISO 8859 340
10.4 The emergence of ISO 10646 and Unicode 340
10.4.1 The four-dimensional architecture 340
10.4.2 Enter Unicode 342
10.4.3 The final compromise 343
10.5 And the impact of all this on ASN.1? 343
11 ANY, macros, and Information Objects - hard to keep that short (even the heading has gone to two lines)! 345
12 The ASN.1(1990) controversy 348
13 The emergence of PER 349
13.1 The first attempt - PER-2 349
13.2 The second attempt - PER-1 352
14 DER and CER 353
15 Semantic models and all that - ASN.1 in the late 1990s 354
16 What got away? 355

Chapter 2 Applications of ASN.1 357
1 Introduction 357
2 The origins in X.400 358
3 The move into Open Systems Interconnection (OSI) and ISO 359
4 Use within the protocol testing community 360
5 Use within the Integrated Services Digital Network (ISDN) 361
6 Use in ITU-T and multimedia standards 361
7 Use in European and American standardization groups 362
8 Use for managing computer-controlled systems 363
9 Use in PKCS and PKIX and SET and other security-related protocols 364
10 Use in other Internet specifications 365
11 Use in major corporate enterprises and agencies 366
12 Conclusion 366

APPENDICES 367

1 The Wineco protocol scenario 368
2 The full protocol for Wineco 369
3 Compiler output for C support for the Wineco protocol 372
4 Compiler output for Java support for the Wineco protocol 374
5 ASN.1 resources via the Web 384

NDEX 385 

This page is deliberately left blank for global page layout. 

# Foreword

This text is primarly written for those involved in protocol specification or in the implemnentation of ASN.1-based protocols. It is expected, however, that it will be of interest and use to a wider audience including managers, students, and simply the intellectually curious. 

The Introduction which follows should be at least scanned by all readers, and ends with a discussion of the structure of the text. Thereafter, readers generally have a reasonable degree of freedom to take sections and chapters in any order they choose, and to omit some (or many) of them, although for those with little knowledge about ASN.1 it would be sensible to read the whole of Section I first, in the order presented. 

Here is a rough guide to what the different types of reader might want to tackle: 

Managers: Those responsible for taking decisions related to possible use of ASN.1 as a notation for protocol specification, or responsible for managing teams implementing protocols defined using ASN.1, should read Section I ("ASN.1 Overview"), and need read no further, although Section IV ("History and Applications") might also be of interest. This would also apply to those curious about ASN.1 and wanting a short and and fairly readable introduction to it. 

Protocol specifiers: For those designing and specifying protocols, much of Section I ("ASN.1 Overview") and Section IV ("History and Applications") should be scanned in order to determine whether or not to use ASN.1 as a specification language, but Section II ("Further details") is very important for this group. 

• Implementors using an ASN.1 tool: For this group, Section I ("ASN.1 in Brief") and Section II ("Further Details") will suffice. 

Implementors doing hand-encodings: (or those who may be developing ASN.1 tools) must supplement the above sections by a careful reading of Section III ("Encodings") and indeed of the actual ITU-T Recommendations/ISO Standards for ASN.1. 

Students on courses covering protocol specification techniques: Undergraduate and postgraduate courses aiming to give their students an understanding of the abstract syntax approach to protocol specification (and perhaps of ASN.1 itself) should place the early parts of Section I ("ASN.1 Overview") and some of Section IV ("History and Applications") on the reading list for the course. 

• The intellectually curious: Perhaps this group will read the whole text from front to back and find it interesting and stimulating! Attempts have been made wherever possible to keep the text light and readable - go to it! 

There is an electronic version of this text available, and a list of further ASN.1-related resources, at the URL given in Appendix 5. And importantly, errata sheets will be provided at this site for down-loading. 

The examples have all been verified using the "OSS ASN.1 Tools" package produced and marketed by Open Systems Solutions (OSS), a US company that has (since 1986) developed and marketed tools to assist in the implementation of protocols defined using ASN.1. I am grateful to OSS for © OS, 31 May 1999 13 much support in the production of this book, and for the provision of their tool for this purpose. Whilst OSS has given support and encouragement in many forms, and has provided a number of reviewers of the text who have made very valued comments on early drafts, the views expressed in this text are those of the author alone. 

John Larmouth (j.larmouth@iti.salford.ac.uk) 

May 1999 

# Introduction

## Summary:

This introduction: 

• describes the problem ASN.1 addresses, 

• briefly says what ASN.1 is, 

• explains why it is useful. 

## 1 The global communications infrastructure

We are in a period of rapid advance in the collaboration of computer systems to perform a wider range of activity than ever before. Traditional computer communications to support human-driven remote logon, e-mail, file-transfer, and latterly the World-Wide Web (WWW) are being supplemented by new applications requiring increasingly complex exchanges of information between computer systems and between appliances with embedded computer chips. 

Some of these exchanges of information continue to be human-initiated, such as bidding at auctions, money wallet transfers, electronic transactions, voting support, or interactive video. Others are designed for automatic and autonomous computer-to-computer communication in support of such diverse activities as cellular telephones (and other telephony applications), meter reading, pollution recording, air traffic control, control of power distribution, and applications in the home for control of appliances. 

In all cases there is a requirement for the detailed specification of the exchanges the computers are to perform, and for the implementation of software to support those exchanges. 

The most basic support for many of these exchanges today is provided by the use of TCP/IP and the Internet, but other carrier protocols are still in use, particularly in the telecommunications area. However, the specification of the data formats for messages that are to be passed using TCP (or other carriers) requires the design and clear specification of application protocols, followed by (or in parallel with) implementation of those protocols. 

For communication to be possible between applications and devices produced by different vendors, standards are needed for these application protocols. The standards may be produced by recognised international bodies such as the International Telecommunications Union Telecommunications Standards Sector (ITU-T), the International Standards Organization (ISO), or the Internet Engineering Task Force (IETF), or by industrial associations or collaborative groups and consortia such as the International Civil Aviation Organization (ICAO), the Open Management Group (OMG) or the Secure Electronic Transactions (SET) consortium, or by individual multinational organizations such as Reuters or IBM. 

These different groups have various approaches to the task of specifying the communications standards, but in many cases ASN.1 plays a key role by enabling: 

• Rapid and precise specification of computer exchanges by a standardization body. 

• Easy and bug-free implementation of the resulting standard by those producing products to support the application. 

In a number of industrial sectors, but particularly in the telecommunications sector, in securityrelated exchanges, and in multimedia exchanges, ASN.1 is the dominant means of specifying application protocols. (The only other major contender is the character-based approach often used by IETF, but which is less suitable for complex structures, and which usually produces a much less compact set of encodings). A description of some of the applications where ASN.1 has been used as the specification language is given in Chapter of Section IV. 

## 2 What exactly is ASN.1?

The term "TCP/IP" can be used to describe two protocol specifications (Transmission Control Protocol - TCP, and Internet Protocol - IP), or more broadly to describe the complete set of protocols and supporting software that are based around TCP/IP. Similarly, the term "ASN.1" can be used narrowly to describe a notation or language called "Abstract Syntax Notation One", or can be used more broadly to describe the notation, the associated encoding rules, and the software tools that assist in its use. 

The things that make ASN.1 important, and unique, are: 

It is an internationally-standardised, vendor-independent, platform-independent and language-independent notation for specifying data-structures at a high level of abstraction. (The notation is described in Sections I and II). 

It is supported by rules which determine the precise bit-patterns (again platformindependent and language-independent) to represent values of these data-structures when they have to be transferred over a computer network, using encodings that are not unnecessarily verbose. (The encoding rules are described in Section III). 

It is supported by tools available for most platforms and several programming languages that map the ASN.1 notation into data-structure definitions in a computer programming language of choice, and which support the automatic conversion between values of those data-structures in memory and the defined bit-patterns for transfer over a communications line. (The tools are described in Chapter 6 of Section I). 

There are a number of other subtle features of ASN.1 that are important and are discussed later in this text. Some of these are: 

• It addresses the problem of, and provides support for, interworking between deployed "version 1" systems and "version 2" systems that are designed and deployed many years apart. (This is called "extensibility"). 

• It provides mechanisms to enable partial or generic specification by one standards group, with other standards groups developing (perhaps in very different ways) specific specifications. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/16c9e5c60eb11b368f596af252be01d84aa39e04912cea14086594093a974fb6.jpg)



© OS, 31 May 1999


The development process with ASN.1 • It recognises the potential for interworking problems between large systems capable of handling long strings, large integer values, large iterative structures, and small systems that may have a lesser capability. 

It provides a range of data-structures which is generally much richer than that of normal programming languages, such as the size of integers, naming structures, and character string types. This enables precision in the specification of the range of values that need to be transferred, and hence production of more optimal encodings. 

## 3 The development process with ASN.1

The flow diagram illustrates the development process from inception to deployment of initial systems. 

(But it must be remembered that this process is frequently an iterative one, with both early revisions by the standardization group to "get it right" and with more substantial revisions some years later when a "version 2" standard is produced.) 

Some key points to note from the diagram: 

The decision to employ ASN.1 as the notation for defining a standard is a key one. It requires a good understanding of the ASN.1 notation by the standardization group, but provides a rich set of facilities for a clear specification. Alternative means of protocol specification are discussed in Chapter 1 of Section I. 

There is no need for the standardization group (or implementors) to be concerned with the detailed bit-patterns to be used to communicate the desired semantics: details of encoding are "hidden" in the ASN.1 encoding rule specifications and in the run-time support provided by the ASN.1 tools. 

The implementation task is a simple one: the only code that needs to be written (and debugged and tested) is the code to perform the semantic actions required of the application. There is no need to write and debug complex parsing or encoding code. 

## 4 Structure of the text.

Section I covers the most commonly encountered features of the ASN.1 notation. It also briefly introduces all other aspects of the notation, with full coverage in Section II. It is intended that those who are not primarily responsible for writing specifications using ASN.1 or for coding implementations, but who need a basic understanding to assist in or to manage development (of standards or implementations), will obtain all that they need from Section I. Those with primary responsibility for writing or coding will need Section II also. 

Section III describes the principles behind the ASN.1 encoding rules, and much of the detail. However, this text is really only for the curious! There is no need for standards' writers or coders to know about these encodings (provided that a tool is used for the implementation). 

Section IV completes the text (apart from various supporting appendices) by giving some details of the history of ASN.1, and of the applications that have been specified using it. 

A detailed treatment of ASN.1 is a fairly "heavy" subject, but I have tried to inject just a little lightness and humour where possible. Skip what you wish, read what interests you, but please, enjoy! 

This page is deliberately left blank for global page layout. 

## SECTION I

ASN.1 Overview 

# Chapter 1 Specification of protocols

# (Or: Simply saying simply what has to be said!)

## Summary:

This chapter: 

• introduces the concept of a "protocol" and its specification, 

• provides an early introduction to the concepts of 

– layering, 

– extensibility, 

– abstract and transfer syntaxes, 

• discusses means of protocol specification, 

describes common problems that arise in designing specification mechanisms and notations. 

(Readers involved in protocol specification should be familiar with much of the early "concepts" material in this Chapter, but may find that it provides a new and perhaps illuminating perspective on some of the things they have been trying to do.) 

## 1 What is a protocol?

A computer protocol can be defined as: 

A well-defined set of messages (bit-patterns or - increasingly today - octet strings) each of which carries a defined meaning (semantics), together with the rules governing when a particular message can be sent. 

However, a protocol rarely stands alone. Rather, it is commonly part of a "protocol stack", in which several separate specifications work together to determine the complete message emitted by a sender, with some parts of that message destined for action by intermediate (switching) nodes, and some parts intended for the remote end system. 

In this "layered" protocol technique: 

One specification determines the form and meaning of the outer part of the message, with a "hole" in the middle. It provides a "carrier service" (or just "service") to convey any material that is placed in this "hole". 

• A second specification defines the contents of the "hole", perhaps leaving a further hole for another layer of specification, and so on. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/7cd54121a46a9fe3787092adb2f9127d006952d02ad0042e705cd6dc8daefb5a.jpg)


Figure 1 illustrates a TCP/IP stack, where real networks provide the basic carrier mechanism, with the IP protocol carried in the “hole” they provide, and with IP acting as a carrier for TCP (or the the less well-known User Datagram Protocol - UDP), forming another protocol layer, and with a (typically for TCP/IP) monolithic application layer - a single specification completing the final “hole” 

The precise nature of the "service" provided by a lower layer - lossy, secure, reliable - and of any parameters controlling that service, needs to be known before the next layer up can make appropriate use of that service. 

We usually refer to each of these individual specification layers as "a protocol", and hence we can enhance our definition: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/987dcce712b06bf72f9525e536a24a057d4a7a90c6fbe5c2c33420bfcf055d12.jpg)


Note that in figure 1, the “hole” provided by the IP carrier can contain either a TCP message or a UDP message - two very different protocols with different properties (and themselves providing a further carrier service). Thus one of the advantages of "layering" is in reusability of the carrier service to support a wide range of higher level protocols, many perhaps that were never thought of when the lower layer protocols were developed. 

When multiple different protocols can occupy a hole in the layer below (or provide carrier services for the layer above), this is frequently illustrated by the layering diagram shown in Figure 2. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/6c135ef9542a5bc8a4e511bda26875e59ee0b7cbb00a63c374f3b54af0a76015.jpg)


## 2 Protocol specification - some basic concepts

Protocols can be (and historically have been) specified in many ways. One fundamental distinction is between character-based specification versus binary-based specification. 

Character-based specification 

The "protocol" is defined as a series of lines of ASCII encoded text. 

Binary-based specification 

The “protocol” is defined as a string of octets or of bits. 

For binary-based specification, approaches vary from various picture-based methods to use of a separately defined notation with associated application-independent encoding rules. 

The latter is called the "abstract syntax" approach. This is the approach taken with ASN.1. It has the advantage that it enables designers to produce specifications without undue concern with the encoding issues, and also permits application-independent tools to be provided to support the easy implementation of protocols specified in this way. Moreover, because application-specific implementation code is independent of encoding code, it makes it easy to migrate to improved encodings as they are developed. 

## 2.1 Layering and protocol "holes"

The layering concept is perhaps most commonly associated with the International Standards Organization (ISO) and International Telecommunications Union (ITU) "architecture" or "7-layer model" for Open Systems Interconnection (OSI) shown in Figure 3. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/1ad82fdda110e725d718cebbdc82e324cbd464d339fee7fb2fdd514be44c36a2.jpg)


While many of the protocols developed within this framework are not greatly used today, it remains an interesting academic study for approaches to protocol specification. In the original OSI concept in the late 1970s, there would be just 6 layers providing (progressively richer) carrier services, with a final "application layer" where each specification supported a single endapplication, with no "holes". 

It became apparent, however, over the next decade, that even in the "application layer" people wanted to leave "holes" in their specification for later extensions, or to provide a means of tailoring their protocol to specific needs. For example, one of the more recent and important protocols - Secure Electronic Transactions (SET) - contains a wealth of fully-defined message semantics, but also provides for a number of "holes" which can transfer "merchant details" which are not specified in the SET specification itself. So we have basic messages for purchase requests and responses, inquiry requests and responses, authorization requests and responses, and so on, but within those messages there are “holes” for “message extensions” - additional information specific to a particular merchant. 

It is thus important that any mechanism or notation for specifying a protocol should be able to cater well for the inclusion of "holes". This has been one of the more important developments in ASN.1 in the last decade, and will be a subject of much further discussion in this book. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/bccba813122354976dbcb03453c366b5e1fc53f6f1ef37545702fd03696fc32b.jpg)


"Catering well" for the inclusion of "holes" implies that the notation must have defined mechanisms (preferably uniformly applied to all specifications written using that notation) to identify the contents of a hole at communications time. (In lower layers, this is sometimes referred to as the "protocol id" problem). Equally important, however, are notational means to clearly identify that a specification is incomplete (contains a hole), together with well-defined mechanisms to relate the (perhaps later in time) specification of the contents of holee to the location of the holes themselves. 

## 2.2 Early developments of layering

The very earliest protocols operated over a single link (called, surprisingly, "LINK" protocols!), and were specified in a single monolithic specification in which different physical signals (usually voltage or current) were used to signal specific events related to the application. (An example is the “off-hook” signal in early telephony systems). If you wanted to run a different application, you re-defined and re-built your electronics! 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/9218128021496d6003ca6bef3566782d85e128a551ef265108380aa430def55d.jpg)



Figure 4: Application communication with ASN.1


This illustrates the major advantage of "layering": it enables reusability of carrier mechanisms to support a range of different higher-layer protocols or applications, as illustrated in Figure 2. 

Nobody today would dream of providing a single monolithic specification similar to the old "LINK" protocols: perhaps the single most important step in computer communication technology was to agree that current, voltage, sound, light, signalling systems would do nothing more than transfer a two-item alphabet - a zero or a one - and that applications would build on that. Another important step was to provide another "layer" of protocol to turn this continuous flow of bits into delimited or "framed" messages with error detection, enabling higher layer protocols to talk about "sending a message" (which may get lost, may get through, but the unit of discussion is the message). 

But this is far too low a level of discussion for a book on ASN.1! Between these electrical levels and the normal carriers that ASN.1 operates with we have layers of protocol concerned with addressing and routing through the Internet or a telecoms network, and concerned with recovery from lost messages. 

At the ASN.1 level, we assume that an application on one machine can "talk" to an application on another machine by reliably sending octet strings between themselves. (Note that all ASN.1- defined messages are an integral multiple of 8-bits - an octet string, not a general bit-string). This is illustrated in Figure 4. 

Nonetheless, many ASN.1-defined applications are still specified by first specifying a basic "carrier" service, with additional specifications (perhaps provided differently by different groups) to fill in the holes. This is illustrated in Figure 5. As we will see later, there are many mechanisms in ASN.1 to support the use of "holes" or of "layering". 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/a9475ec5fb9b2fbe6548cfd2841c7919ca53073e6c69ef503f460b9632e0a6dd.jpg)



Figure 5: Generic and specific protocols with ASN.1


People have sometimes described the OSI 7-layer model as "layering gone mad". Layering can be an important tool in promoting reusability of specifications (and code), and in enabling parts of the total specification (a low or a high layer), to be later improved, extended (or just mended!) without affecting the other parts of the total specification. This desirable feature will, of course, only be achieved if the means for linking the different parts of the specification together to form the complete whole are sufficiently rich. 

## 2.3 The disadvantages of layering - keep it simple!

Layering clearly carries important advantages in reusability, but it also carries the major disadvantage that in order to implement completely some given application, many different documents may have to be consulted, and the "glue" for linking these together may not always be precise enough to ensure that implementations by different vendors interwork. 

It is important, therefore, in designing protocols, that the desire for generality and long-life be tempered by an equal desire to keep the total specification simple. This is again a theme that we will return to later - ASN.1 makes it possible to write very simple and clear specifications very easily and quickly. But it also contains powerful features to support layering and "extensibility" (see below). The decision to use or to not use such features must be one for the designer. There are circumstances where their use is essential for a good long-lasting specification. There are other cases where the added complexity (and sometimes implementation size) does not justify the use of advanced features. 

## 2.4 Extensibility

A remark was made earlier that layering enables "later improvement" of one of the layers without affecting the specification of layers above and below. This concept of "later improvement" is a key phrase, and has an importance beyond any discussion of layering. One of the important aspects of protocol specification that became recognised in the 1980s is that a protocol specification is rarely (probably never!) completed on date xyz, implemented, deployed, and left unchanged. 

## Extensibility provision

Part of a version 1 specification designed to make it easy for future version 2 (extended) systems to interwork with deployed version 1 systems 

There is always a "version 2". And implementations of version 2 need to have a ready means of interworking with the already-deployed implementations of "version 1", preferably without having to include in version 2 systems a complete implementation of both version 1 and version 2 (sometimes called "dual-stacks"). Mechanisms enabling version 1 and version 2 exchanges are sometimes called a "migration" or "interworking strategy" between the new and the earlier versions. In the transition from IPv4 to IPv6 (the “IP” part of “TCP/IP”), it has perhaps taken as much work to solve migration problems as it took to design IPv6 itself! (An exaggeration of course, but the point is an important one - interworking with deployed version 1 systems matters.) 

It turns out that provided you make plans for version 2 when you write your version 1 specification, you can make the task of "migration" or of defining an "interworking strategy" much easier. 

We can define extensibility provision as 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/12dc63bc43a52e5c3e3620d0df1e8c558b24eae9b01057dbca740163c5bc08e1.jpg)



Figure 6: Version 1 and Version 2 interworking


elements of a version 1 specification that allow the encapsulation of unknown material at certain points in the version 1 messages, and 

specification of the actions to be taken by the version 1 system if such material is present in a message. 

Provision for extensibility in ASN.1 is an important aspect which will be discussed further later in this book, and is illustrated in Figure 6. 

Extensibility was present in early work in ITU-T and ISO by use of a very formalised means of transferring parameters in messages, a concept called "TLV" - Type, Length, Value, in which all pieces of information in a message are encoded with a type field identifying the nature of that piece of information, a length field delimiting the value, and then the value itself, an encoding that determines the information being sent. This is illustrated in Figure 7 for parameters and for groups of parameters. The approach is generalised in the ASN.1 Basic Encoding Rules (BER) to cover groups of groups, and so on, to any depth. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/e1a733d9b238047233b62f4047b7f2b011dc56b635b9aadb1c3e355f454d6e4d.jpg)



Figure 7: The “TLV” approach for parameters and groups


Note that the encoding used for the value only needs to unambiguously identify application information within the context of the parameter identified by the type field. This concept of distinct octet-strings that identify information within the context of some explicit "class" or "type" identifier is an important one that will be returned to later. 

By requiring in the version 1 specification that parameters that are "unrecognized" - added in version 2 - should be silently ignored, the designers of version 2 have a predictable basis for interworking with deployed version 1 systems. Of course, any other well-specified behaviour could be used, but "silently ignore" was a common specification. ASN.1 provides a notation for defining the form of messages, together with “encoding rules” that specify the actual bits on the line for any message that can be defined using the notation. The "TLV" described above was incorporated into the earliest ASN.1 encoding rules (the Basic Encoding Rules or BER) and provides very good support for extensibility due to the presence in every element of the "T" and the "L", enabling "foreign" (version 2 ) material to be easily identified and skipped (or relayed). It does, however, suffer from encoding identification and length fields which are often unnecessary apart from their use in promoting extensibility. For a long time, it was thought that this verbosity was an essential feature of extensibility, and it was a major achievement in encoding rule design when the ASN.1 Packed Encoding Rules (PER) provided good support for extensibility with little additional overhead on the line. 

## 2.5 Abstract and transfer syntax

The terms abstract and transfer syntax were primarily developed within the OSI work, and are variously used in other related computer disciplines. The use of these terms in ASN.1 (and in this book) is almost identical to their use in OSI, but does not of course make ASN.1 in any way dependent on OSI. 

The following steps are necessary when specifying the messages forming a protocol (see Figure 8): 

• The determination of the information that needs to be transferred in each message; this is a "business-level" decision. We here refer to this as the semantics associated with the message. 

The design of some form of data-structure (at about the level of generality of a high-level programming language, and using a defined notation) which is capable of carrying the required semantics. The set of values of this data-structure are called the abstract syntax of the messages or application. We call the notation we use to define this data structure or set of values we the abstract syntax notation for our messages. ASN.1 is just one of many possible abstract syntax notations, but is probably the one most commonly used. 

The crafting of a set of rules for encoding messages such that, given any message defined using the abstract syntax notation, the actual bits on the line to carry the semantics of that message are determined by an algorithm specified once and once only (independent of the application). We call such rules encoding rules, and we say that the result of applying them to the set of (abstract syntax) messages for a given application defines a transfer syntax for that application. A transfer syntax is the set of bit-patterns to be used to represent the abstract values in the abstract syntax, with each bit-pattern representing just one abstract value. (In ASN.1, the bit-patterns in a transfer syntax are always a multiple of 8 bits, for easy carriage in a wide range of carrier protocols). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/6a0b8ba39a687b6c93df3255aeeb608fb178a7c74e4a60d7138bf126d741d57a.jpg)



Figure 8: From abstract specification to bits-on-the-line


We saw that early LINK protocols did not clearly separate electrical signalling from application semantics, and similarly today, some protocol specifications do not clearly separate the specification of an abstract syntax from the specification of the bits on the line (the transfer syntax). It is still common to directly specify the bit-patterns to be used (the transfer syntax), and the semantics associated with each bit-pattern. However, as will become clear later, failure to clearly separate abstract from transfer syntax has important implications for reusability and for the use of common tools. With ASN.1 the separation is complete. 

## 2.6 Command line or statement-based approaches

Another important approach to protocol design (not the approach taken in ASN.1) is to focus not on a general-purpose data-structure to hold the information to be transferred, but rather to design a series of lines of text each of which can be thought of as a command or a statement, with textual parameters (frequently comma separated) within each command or statement. This approach predated the use of ASN.1, but is still frequently employed today, more commonly in Internet-defined protocols (for example, the Internet Hyper-Text Transfer Protocol - HTTP - that supports the World-Wide Web) than in ITU-T/ISO-defined protocols. A further discussion of this approach is given in 5.4 below. 

## 2.7 Use of an Interface Definition Language

The use of an Interface Definition Language (IDL) is very similar to the abstract syntax approach of ASN.1. Here, however, the model is of objects interacting over a network through defined interfaces which enable the functions or methods of an object to be invoked, and its results to be returned. The model is supported by an Interface Definition Language that enables the datastructures which are passed across each interface to be specified at a high-level of abstraction. 

Probably the most important IDL today is the Common Object Request Broker Architecture (CORBA) IDL. In CORBA, the IDL is supported by a wealth of specifications and tools including encoding rules for the IDL, and means of transfer of messages to access interfaces across networks. 

A detailed comparison of ASN.1 and CORBA goes beyond this text, and remarks made here should be taken as this author’s perception in mid 1999. In essence, CORBA is a complete architecture and message passing specification in which the IDL and corresponding encodings form only a relatively small (but important) part. The CORBA IDL is simpler and less powerful than the ASN.1 notation, and as a result encodings are generally much more verbose than the Packed Encoding Rule (PER) encodings of ASN.1. ASN.1 is generally used in protocol specifications where very general and flexible exchange of messages is needed between communicating partners, whereas CORBA encourages a much more stylised “invocation and response” approach, and generally needs a much more substantial suporting infrastructure. 

## 3 More on abstract and transfer syntaxes

## 3.1 Abstract values and types

Most programming languages involve the concept of types or classes (and notation to define a more complex type by reference to built-in types and "construction mechanisms"), with the concept of a value of a type or class (and notation to specify values). ASN.1 is no different. 

So, for example, in C we can define a new type “My-type” as: 

```txt
typedef struct My-type {
    short first-item;
    boolean second-item} My-type; 
```

The equivalent definition in ASN.1 appears below. 

In ASN.1 we also have the concept of values of basic types or of more complex structures. These are often called abstract values (see Figure 8 again), to emphasise that we are considering them without any concern for how they might be represented in a computer or on a communications line. For convenience, these abstract values are grouped together into types. So for example, we have the ASN.1 type notation 

## INTEGER

that references the integer type, with abstract values from (more or less) minus infinity to plus infinity. We also have the ASN.1 type notation 

## BOOLEAN

that references the boolean type with just two abstract values "TRUE" and "FALSE". 

We can define a type of our own: 

$$
\begin{array}{r l} \text {My - type} & : := \text {SEQUENCE} \\ & \left\{\text {first - item} \quad \text {INTEGER}, \right. \\ & \left. \text {second - item} \quad \text {BOOLEAN} \right\} \end{array}
$$

each of whose abstract values is a pair of values, one "integer" and one "boolean". The important point, however, is that for many purposes, we don't care about (or discuss) any internal structure of the values in "My-type". Just like "integer" and "boolean", it is simply a convenient means of referencing a set of abstract values. 

## 3.2 Encoding abstract values

So (to summarise the above discussion) for any type that can be defined using ASN.1, we say that it contains (represents) a set of abstract values. (See Figure 8 again). 

## But now for the important part:

When any (correct!) set of encoding rules are applied to the abstract values in any given ASN.1 type, they will produce bit-patterns (actually octet-strings) for each value such that any given octet string corresponds to precisely one abstract value. 

Note that the reverse is not necessarily true - there may be more than one octet string for a given abstract value. This is another way of saying that there may be options in the encoding rules. (ASN.1 requires all conforming decoders to handle any encodings that a conforming encoder is allowed to use). 

If we restrict encoder options so that for any given abstract value in the type there is precisely one encoding, we say that the encoding rules are canonical. Further discussion of canonical encoding rules appears in Section III. 

Now let us consider a designer wanting to specify the messages of a protocol using ASN.1. It would be possible to define a set of ASN.1 types (one for each different sort of message), and to say that the set of abstract values to be transmitted in protocol exchanges (and hence needing encoding) are the set of all the abstract values of all those 

<table><tr><td>Abstract syntax</td></tr><tr><td>The set of abstract values of the top-level type for the application</td></tr></table>

ASN.1 types. The observant reader (some people won't like me saying that!) will have spotted that the above requirement on a correct set of encoding rules is not sufficient for unambiguous communication of the abstract values, because two abstract values in separate but similar ASN.1 types could have the same octet-string representation. (Both types might be a sequence of two integers, but they could carry very different semantics). 

It is therefore an important requirement in designing protocols using ASN.1 to specify the total set of abstract values that will be used in an application as the set of abstract values of a single ASN.1 type. This set of abstract values is often referred to simply as the abstract syntax of the application, and the corresponding set of octet-strings after applying some 

## Transfer syntax

A set of unambiguous octet strings used to represent a value from an abstract syntax during transfer 

set of encoding rules is referred to as a possible transfer syntax for that application. Thus the application of the ASN.1 Basic Encoding Rules (as in Figure 8) to an ASN.1 type definition produces a transfer syntax (for the abstract syntax) which is a set of bit patterns that can be used to unambiguously represent these abstract values during transfer. 

Note that in some other areas, where the emphasis is on storage of data rather than its transfer over a network, the concept of abstract syntax is still used to represent the set of abstract values, but the term concrete syntax is sometimes employed for a particular bit-pattern representation of the material on a disk. Thus some authors will talk about "concrete transfer syntax" rather than just “transfer syntax”, but this term is not used in this book. 

We will see later how, if we have distinct ASN.1 types for different sorts of messages, we can easily combine them into a single ASN.1 type to use to define our abstract syntax (and hence our transfer syntax). There is specific notation in the post-1994 version of ASN.1 to clearly identify this "top-level" type. All other ASN.1 type definitions in the specification are there solely to give support to this top-level type, and if they are not referenced by it (directly or indirectly), their definition is superfluous and a distracting irrelevance! Most people don't retain superfluous type definitions in published specifications, but sometimes for historical reasons (or through sloppy editing or both!) you may encounter such material. 

In summary then: ASN.1 encoding rules provide unambiguous octet-strings to represent the abstract values in any ASN.1 type; the set of abstract values in the top-level type for an application is called the abstract syntax for that application; the corresponding octet-strings representing those abstract values unambiguously (by the use of any given set of encoding rules) is called a transfer syntax for that application. 

Note that where there are several different encoding rule specifications available (as there are for ASN.1) there can in general be several different transfer syntaxes (with different verbosity and extensibility - etc - properties) available for a particular application, as shown in Figure 8. 

In the OSI world, it was considered appropriate to allow run-time negotiation of which transfer syntax to use. Today, we would more usually expect the application designer to make a selection based on the general nature and requirements of the application. 

## 4 Evaluative discussion

## 4.1 There are many ways of skinning a cat - does it matter?

Whilst the clear separation of abstract syntax specification (with associated semantics) from specification of a transfer syntax is clearly "clean" in a puristic sort of way, does it matter? Is there value in having multiple transfer syntaxes for a given application? The ASN.1 approach to protocol design provides a common notation for defining the abstract syntax of any number of different applications, with common specification text and common implementation code for deriving the transfer syntax from this. Does this really provide advantages over the character line approach discussed earlier? Both approaches have certainly been employed with success. Different experts hold different views on this subject, and as with so much of protocol design, the approach you prefer is more likely to depend on the culture you are working within than on any rational arguments. Indeed, there are undoubted advantages and disadvantages to both 

approaches, so that a decision becomes more one of which criteria you consider the most important, rather than on any absolute judgement. So here (as in a number of parts of this book) Figure 999: Readers take warning (modified - "Smoking" replaced by "This discussion" - from text that appears on all UK cigarette packets!) applies. (I will refer back to Figure 999 whenever a remark appears in this book that may be somewhat contentious). 

Government Health Warning This discussion can damage your health! 

Figure 999: Readers take warning 

## 4.2 Early work with multiple transfer syntaxes

Even before the concepts of abstract and transfer syntax were spelled out and the terms defined, protocol specifiers recognised the concepts and supplied multiple transfer syntaxes in their specifications. 

Thus in the Computer Graphics Metafile (CGM) standard, the body of the standard defines the functionality represented by a CGM file (the abstract syntax), with three additional sections defining a "binary encoding", a "character encoding", and a "clear-text encoding". The "binary encoding" was the least verbose, was hard for a human to read (or debug), was not easy to produce with a simple program, and required a storage or transfer medium that was 8-bit transparent. The "character encoding" used two-character mnemonics for "commands" and parameters, and was in principle capable of being produced by a text editor. It was more human readable, but importantly mapped to octets via printing ASCII characters and hence was more robust in the storage and transfer media it could use (but was more verbose). The “clear-text” encoding was also ASCIIbased, but was designed to be very human-readable, and very suitable for production by a humanbeing using a suitable text editor, or for viewing by a human-being for debugging purposes. It could be employed before any graphical interface tools for CGM became available, but was irrelevant thereafter. 

These alternative encodings are appropriate in different circumstances, with the compactness of the "binary encoding" giving it the market edge as the technology matured and tools were developed. 

## 4.3 Benefits

Some of the benefits which arise when a notation for abstract syntax definition is employed are identified below, with counter arguments where appropriate. 

## Efficient use of local representations

Suppose you have an application using large quantities of material which is stored on machinetype-A in a machine-specific format - say with the most significant octet of each 16-bit integer at the lower address byte. On machine-type-B, however, because of differing hardware, the same abstract values are represented and stored with the most significant octet of each 16-bit integer at the higher address byte. (There are usually further differences in the machine-A/machine-B representations, but this so-called "big-endian/little-endian" representation of integers is often the most severe problem.) 

When transferring between machine-type-A and machine-type-B, it is clearly necessary for one or both parties (and if we are to be even-handed it should be both!) to spend CPU cycles converting into and out of some agreed machine-independent transfer syntax. But if we are transferring between two separate machines both of machine-type-A, it clearly makes more sense to use a transfer syntax closely related to the storage format on those machines. 

This issue is generally more important for applications involving the transfer of large quantities of highly structured information, rather than for small headers negotiating parameters for later bulk transfer. An example where it would be relevant is the Office Document Architecture (ODA) specification. This is an ISO Standard and ITU-T Recommendation for a large structure capable of representing a complete service manual for (for example) a Boeing aircraft, so the application data can be extremely large. 

## Improved representations over time

It is often the case that the early encodings produced for a protocol are inefficient, partly because of the desire to be "protective", or to have encodings that are easy to debug, in the early stages of deployment of the application, partly from simple time pressures. It can also be because insufficient effort is put into the "boring" task of determining a "good" set of "bits-on-the-line" for this application. 

Once again, if the bulk of the protocol is small compared with some "bulk-data" that it is transferring, as is the case - for most messages - with the Internet’s Hyper-Text Transfer Protocol (HTTP) or File Transfer Protocol (FTP), then efficiency of the main protocol itself becomes relatively unimportant. 

## Reuse of encoding schemes

If we have a clear separation of the concept of abstract syntax definition from transfer syntax definition, and have available a notation for abstract syntax definition (such as ASN.1) which is independent of any application, then specification and implementation benefits immediately accrue. The task of generating "good" encoding rules for that notation can be done once, and these rules can be referenced by any application that uses that notation to define its abstract syntax. This is not only a major saving of effort if a new application is to be specified, but it also provides a specification of a transfer syntax that has already been argued over, agreed, and gotten debugged! 

This approach also ensures a common "look-and-feel" to the resulting transfer syntaxes over a number of different applications, with well-understood characteristics and familiarity for implementors. It also makes possible the emergence of tools, discussed below. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/88eca2573ee4e25529fb40020dfbe0367da2820def52467752adc54ad10ea756.jpg)


The advantage extends to the implementation. Where there is a clear notation and well-defined encoding rules that are application-independent, it becomes possible to provide a set of generic encode/decode routines that can be used by any application. This significantly reduces implementation effort and residual bugs. Figure 9 illustrates this situation, where the greyed-out text describes effort which is not required due to the re-use of existing material. 

## Structuring of code

If the specification of the encodings is kept clearly separate from the abstract syntax specification, and if the latter can be easily (by a tool or otherwise) mapped into data-structures in the implementation language, this encourages (but of course does not require) a modular approach to © OS, 31 May 1999 37 implementation design in which the code responsible for performing the encodings of the data is kept clearly separate from the code responsible for the semantics of the application. 

## Reuse of code and common tools

This is perhaps the major advantage that can be obtained from the separation of abstract and transfer syntax specification, which is characteristic of ASN.1. 

By the use of so-called ASN.1 "compilers" (dealt with more fully in a Chapter 7 of this section and which are application-independent), any abstract syntax definition in ASN.1 can be mapped into the (abstract) data-structure model of any given programming language, through the textual representation of data-types in that language. Implementors can then provide code to support the application using that (abstract) data-structure model with which they are familiar, and can call an application-independent piece of code to produce encodings of values of that data-structure for transmission (and similarly to decode on reception). 

It is very important at this point for the reader to understand why "(abstract)" was included in the above text. All programming languages (from C to Java) present to their users a "memory-model" by which users define, access, and manipulate structures. Such models are platform independent, and generally provide some level of portability of any associated code. However, in mapping through compilers and run-time libraries into real computer memory (concrete representation of the abstract data-structures), specific features of different platforms intrude, and the precise representation in memory differs from machine-type to machine-type (see the "big-endian/littleendian" discussion in Chapter 4 of Section III). 

A tool-vendor can provide (possibly platform-specific, but certainly application-independent) runtime routines to encode/decode values of the abstract data-structures used by the implementor, and the implementor can continue to be blissfully unaware of the detailed nature of the underlying hardware, but can still efficiently produce machine-independent transfer syntaxes from values stored in variables of the implementation language. 

As with any discussion of code structure, reusability, and tools, real benefits only arise when there are multiple applications to be implemented. It is sometimes worth-while building a generalpurpose tool to support a single implementation, but more often than not it would not be. Tools are of benefit if they can be used for multiple implementations, either by the same implementors or by a range of implementors. 

Tools for ASN.1 have only really emerged and matured because ASN.1 has become the specification language of choice for a wide range of applications. 

## Testing and line monitor tools

The use of a common notation to define the syntax of messages makes it possible to automate many aspects of total protocol support that go beyond the simple implementation of a protocol. For example, it becomes possible to automatically generate test sequences, and to provide generic line-monitors or “sniffers”. 

## Multiple documents requires "glue"

Separation of abstract and transfer syntax specification, whilst distinct from layering, has some common aspects. It promotes reusability of specifications and code, but it means that more than one document has to be obtained and read before it is possible to implement the application. It also means that unless the "glue" between the two parts of the total specification is well-defined, there is scope for errors. 

In the case of ASN.1, the "glue" is the ASN.1 notation itself, and there have been almost no instances of the "glue" coming "unstuck" for normal use. However, when we come to the question of canonical encoding rules - where there has to be a distinct bit-pattern, but only one, for each abstract value, the "glue" has to include a very clear definition of exactly what are the abstract values in any given ASN.1 type. This caused some problems, and much debate, with the ASN.1 specifications in the first decade of their use, for some theoretical constructions! (But for all realworld applications, it never proved a problem). 

Another disadvantage arises if specification documents, particularly of the "glue" - the ASN.1 notation, are not freely (without cost) available to anyone that wants them. This has been theoretically a problem with ASN.1 over the last decade-and-a-half, but I suspect that almost everybody that couldn't afford to pay ITU-T/ISO prices for the ASN.1 documents has managed to get them one way or another! 

## The "tools" business

Expressing an abstract syntax in a high-level application-independent notation such as ASN.1 enables, but does not itself require, the use of tools, and it was some five years after the first specifications using ASN.1 were produced that "ASN.1 tools" began to emerge onto the market place. 

Today a new business area of "ASN.1 tools" for the notation and its encoding rules has been generated, with a commercial advantage for those who can justify the cost of acquiring a tool to help their implementation task. 

## 5 Protocol specification and implementation - a series of case studies

This section completes this chapter with discussion of a number of approaches to protocol specification and implementation, ending with a simple presentation of the approach that is adopted when ASN.1 is used. 

## 5.1 Octet sequences and fields within octets

Protocols for which all or much of the information can be expressed as fixed-length fields all of which are required to be present have traditionally been specified by drawing diagrams such as that shown in Figure 10: Traditional approach. 

Figure 10 is part of the Internet Protocol Header (the Internet Protocol is the IP protocol of the TCP/IP stack illustrated in Figure 2. A similar picture is used in X.25 level 2 to define the header fields. 

<table><tr><td colspan="4"></td><td>Octet number</td></tr><tr><td colspan="4">Protocol ID</td><td>1</td></tr><tr><td colspan="4">Length</td><td>2</td></tr><tr><td colspan="4">Version</td><td>3</td></tr><tr><td colspan="4">Lifetime</td><td>4</td></tr><tr><td>S P</td><td>M S</td><td>E / R</td><td>Type</td><td>5</td></tr><tr><td colspan="4">Segment length</td><td>6,7</td></tr><tr><td colspan="4">Checksum</td><td>8,9</td></tr><tr><td colspan="4">etc</td><td></td></tr></table>


Figure 10: Traditional approach


This approach was very popular in the early days, when implementations were performed using assembler language or languages such as BCPL or later C, allowing the implementor close contact with the raw byte array of a computer memory. 

It was relatively easy for the implementor to read in octets from the communications line to a given place in memory, and then to hard-wire into the implementation code access to the different fields (as shown in the diagram) as necessary. Similarly for transmission. In this approach the terms "encoding" and "decoding" were not usually used. 

The approach worked well in the middle seventies, with the only spectacular failures arising (in one case) from a lack of clarity in the specification of which end of the octets (given in the diagram) was the most significant when interpreting the octet as a numerical value, and which end of the octets (given in the diagram) was to be transmitted first on a serial line. The need for a very clear specification of these bit-orders in binary-based protocol specification is well-understood today, and in particular is handled within the ASN.1 specification, and can be ignored by a designer or implementor of an ASN.1-based specification. 

## 5.2 The TLV approach

Even the simplest protocols found the need for variable length "parameters" of messages, and for parameters that could be optionally omitted. This has been briefly described earlier (see Figure 7) in section 2.4. 

In this case, the specification would normally identify some fixed-length mandatory header fields, followed by a "parameter field" (often terminated by a length count). The "parameter field" would be a series of one or more parameters, each encoded with an identification field, a length field, and then the parameter value. The length field was always present, even for a fixed-length parameter, and the identification field even for a mandatory parameter. This ensured that the basic "TLV" structure was maintained, and enabled "extensibility" text to be written for version 1 systems to skip parameters they did not recognise. 

An implementor would now write some fairly general-purpose code to scan the input stream and to place the parameters into a linked list of buffers in memory, with the application-specific code then processing the linked buffers. Note, however, that whilst this approach was quite common in several specifications, the precise details of length encoding (restricted to a count of 255 or unrestricted, for example), varied from specification to specification, so any code to handle these parameters tended to be application-specific and not easily re-usable for other applications. 

As protocols became more complicated, designers found the need to have complete groups of parameters that were either present or omitted, with all the parameters in a given group collected together in the parameter field. This was the approach taken in the Teletex (and later the OSI Session Layer) specifications, and gave rise to a second level of TLV, with an outer identifier for a parameter group, a length field pointing to the end of that group, and then the TLV for each parameter in the group (revisit Figure 7). 

This approach was also very appropriate for information which required a variable number of repetitions of a given parameter value. 

At the implementation level, the code to "parse" an input octet string is now a little more complex, and the resulting data-structure to be passed to the application-specific code becomes a two level tree-structure rather than a simple linked list, level 1 nodes being parameter groups, and level 2 nodes parameters. 

This approach has been presented above in a very "pure" form, but in fact it was rarely so pure! The Teletex and Session Protocols actually mixed together at the top level parameter group TLVs and parameter TLVs! 

Those who already have some familiarity with the ASN.1 Basic Encoding Rules - BER - (described in much more detail later), will recognise that this TLV approach was generalised to form the basic (application-independent) encoding used by BER. For BER, the entire message is wrapped up with an identifier (that distinguishes it from any other message type in the same abstract syntax) and a length field pointing to the end of the message. The body is then, in general, a sequence of further TLV triplets, with the “V” part of each triplet being either further TLV triplets (etc to any depth), or being a "primitive" field such as an integer or a character string. This gives complete support for the power of normal programming language data-structure definitions to define groupings of types and repetitions of types to any depth, as well as providing support at all levels for optional elements and for extensibility. 

## 5.3 The EDIFACT graphical syntax

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/ea238cbcd27fa3a5365b9000475b7e41f90bfba8aaf650955aa2ce0c4bb94247.jpg)


This approach comes closest to ASN.1, with a clear (graphical) notation for abstract syntax specification, and a separate encoding rule specification. An example of the Electronic Data Interchance For Administration, Commerce and Transport (EDIFACT) graphical syntax is given in Figure 11: EDIFACT graphical syntax. As with ASN.1, the definition of the total message can be done in conveniently sized chunks using reference names for the chunks, then those chunks are combined to define the complete message. So in Figure 11 we have the message fragment (defined earlier or later) "UNH" which is mandatorily present once, similarly "AAA", then "BBB" which is conditional and is present zero to ten times, then "CCC" similarly, then up to 200 repetitions of a composite structure consisting of one "DDD" followed by up to ten "EEE", etc. 

The actual encoding rules were, as with ASN.1, specified separately, but were based on character encoding of all fields. The graphical notation is less powerful than the ASN.1 notation, and the range of primitive types much smaller. The encoding rules also rely on the application designer to ensure that a type following a repeated sequence is distinct from the type in that repeated sequence, otherwise ambiguity occurs. This is a problem avoided in ASN.1, where any legal piece of ASN.1 produces unambiguous encodings. 

At the implementation level, it would be possible to map the EDIFACT definition into a datastructure for the implementation language, but I am not aware of any tools that currently do this. 

## 5.4 Use of BNF to specify a character-based syntax

This approach has been briefly described earlier, and is common in many Internet protocols. 

Where this character-based approach is employed, the precise set of lines of text permitted for each message has to be clearly specified. This specification is akin to the definition of an abstract syntax, but with more focus on the representation of the information on the line than would be present in an ASN.1 definition of an abstract syntax. 

The notation used to define this syntax is usually some variation of a notation frequently used to define the syntax of programming languages (and indeed used to define the syntax of ASN.1 itself), something called Bacchus-Naur Form (BNF), named after its original inventors. 

For example, in ASN.1, the BNF statements: 

```autohotkey
EnumeratedType ::= ENUMERATED { Enumeration }
Enumeration ::= NamedNumber |
    Enumeration, NamedNumber
NamedNumber ::= identifier(SignedNumber)
SignedNumber ::= number | - number 
```

are used to specify that one of the constructs of the language consists of the word “ENUMERATED”, followed, in curly brackets, by a comma-separated list with each item being an identifier followed by a number (possibly preceded by a minus sign) in round brackets. 

Unfortunately, there are many variations of BNF in use today, and most applications employing it find it necessary to define their own particular BNF notation. This makes it more difficult than it should be to use common tools to support BNF-based specifications. 

BNF is a relatively low-level notational support tool. It is very powerful for defining arbitrary syntactic structures, but it does not in itself determine how variable length items are to be delimited or iteration counts determined. Even where the same BNF notation is employed, the "look-and-feel" of two protocols defined in this way can still be very different, as the means of terminating strings (quotation marks, reserved characters, reserved characters with escapes) or of variable length repetitions of items, have to be written into the specific application using the BNF notation for this definition. 

Of course, as with any tool, if the design is a good one, a good result can come out. Many of the Internet protocol designs take this approach, and the best designers ensure that the way in which length and iteration terminations are achieved follows as closely as possible the approach taken in other related specifications, and is consistent for different fields and commands within that application. 

Software tools to support BNF-based specifications are usually restricted to lexical analysis of an incoming string, and generally result in the application-specific code and encoding matters being more closely intertwined than would normally be the case if an ASN.1 tool was used. 

Identification fields for lines in the messages tend to be relatively long names, and "enumerations" also tend to use long lists of names, so the resulting protocol can be quite verbose. In these approaches, length fields are normally replaced by reserved-character delimiters, or by end-of-line, often with some form of escape or extension mechanism to allow continuation over several lines (again these mechanisms are not always the same for different fields or for different applications). 

In recent years there has been an attempt to use exactly the same BNF notation to define the syntax for several Internet protocols, but variations still ensue. 

At implementation-time, a sending implementation will typically hard-wire the encoding as a series of "PRINT" statements to print the character information directly onto the line or into a buffer. On reception, a general-purpose tool would normally be employed that could be presented with the BNF specification and that would parse the input string into the main lexical items. Such tools are available without charge for Unix systems, making it easy for implementations of protocols defined in this way to be set as tasks for Computer Science students (particularly as the protocol specifications tend also to be available without charge!). 

In summary then, this approach can work well if the information to be transferred fits naturally into a two-level structure (lines of text, with an identifier and a list of comma-separated text parameters on each line), but can become complex when a greater depth of nesting of variable numbers of iterated items becomes necessary, and when escape characters are needed to permit commas as part of a parameter. The approach also tends to produce a much more verbose encoding than the binary approach of ASN.1 BER, and a very much more verbose encoding than the ASN.1 Packed Encoding Rules (PER). 

## 5.5 Specification and implementation using ASN.1 - early 1980s

ASN.1 was first developed to support the definition of the set of X.400 Message Handling Systems CCITT (the International Telegraph and Telephone Consultative Committee, later to be renamed ITU-T) Recommendations, although the basic ideas were taken from the Xerox Courier Specification. 

X.400 was developed by people with a strong application interest in getting the semantics of the information flows for electronic messaging right, but with relatively little interest in worrying about the bit-level encoding of messages. It was clear that they needed more or less the power of data-structure definition in a high-level programming language to support their specification work, and ASN.1 was designed to provide this. 

Of course, notation closer to an actual programming language could have been used, but this would not have made the application easy to implement for those who might be forced (for platform reasons) to use a different language. Moreover, whilst using an existing language might solve the notational problem, there would still be work needed to define encodings, as in-memory representations of data structures from even the same language on the same platform differed (and still differ today) from compiler-writer to compiler-writer. 

So ASN.1 was produced, and was heavily used by X.400 and by many other ITU-T and ISO specifications, where its power and the freedom it gave to designers to concentrate on what mattered - the application semantics - was much appreciated. Later, ASN.1 became used in many telecommunications applications, and applications in specific business sectors (and most recently for SET - Secure Electronic Transactions). 

In the early 1980s, the only ASN.1 tools around were simple syntax checkers to help the designers get the specification right. The encoding rules were the TLV-based BER described earlier, and implementation architectures tended to be similar to those used for the character command-line approach described earlier. That is to say, some routines were produced to generate the "T" and the "L" part of an encoding (and the "V" part for the primitive types such as integer and boolean), and the structure of the message was hard-wired into the implementation by repeated calls to these subroutines to generate T and L parts for transmission down the line. On reception, quite simple (and application-independent) parsing code could be written to take the input stream of nested TLV encodings and to produce a tree-structure in memory with the leaves of the tree containing encodings of primitive items like integers, booleans, character strings, etc. The application code would then "tree-walk" this structure to obtain the input values. 

Thus in these early days, the ASN.1 notation: 

• Provided a powerful, clear and easy to use way of specifying information content of messages. 

• Freed application designers from concerns over encoding. 

Provided application-independent encoding making development of reusable code and sophisticated tools possible, although not instantly realised. 

Gave implementors a set of encoding rules to implement that were not as verbose as the BNF-based approach, and no harder (but no easier either) to implement. 

## 5.6 Specification and implementation using ASN.1 - 1990’s

It is of course still possible to produce an implementation of an ASN.1-based protocol without tools. What was done in the 1980s can still be done today. However, there is today great pressure to reduce the "time-to-market" for implementations, and to ensure that residual bugs are at a minimum. Use of tools can be very important in this respect. 

There are today two main families of ASN.1 encoding rules, the original (unchanged) BER, and the more recent (standardised 1994) PER (Packed Encoding Rules). The PER encoding rules specification is more complex than that of BER, but produces very much more compact encodings. (For example, the encoding of a boolean value in PER uses only a single bit, but the TLV structure of BER produces at least 24 bits!) 

There seems to be a "conventional wisdom" emerging that whilst encoding/decoding without a tool for BER is an acceptable thing to do if you have the time to spare, it is likely to result in implementation bugs if PER is being employed. The reader should again refer to Figure 999: Readers take warning!. This author would contend that there are implementation strategies that make PER encoding/decoding without tools a very viable proposition. Certainly much more care at the design stage is needed to correctly identify the field-widths to be used to encode various elements, and when padding bits are to be added (this comment will be better understood after reading the chapter on PER), but once that is done, hard-wiring a PER encode/decode into application code is still (this author would contend) possible. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/e9922eda025c3aa157ec837ecbab410e406929d8621bc13b50d9f86c59df8d8e.jpg)



Figure 12: Use of an ASN.1 tool for implementation


Nonetheless, today, good tools, called "ASN.1 compilers", do exist, and for any commercial development they are good value for money and widely used. How would you implement an 

ASN.1 specification using a tool? This is covered more fully (with examples based on the "OSS ASN.1 Tools" package) in the last chapter of this section. However, the basic outline is as follows (see Figure 12). 

The ASN.1 produced by the application designer is fed into the "compile phase" of the tool. This maps the ASN.1 into a language data-structure definition in any one of a wide range of supported languages (and platforms), including C, C++, and Java. The application code is then written to read and write values from these data-structures, concentrating solely on the required semantics of the application. 

When an encode is needed, a run-time routine is called which uses information provided by the compile phase about certain aspects of the ASN.1 definition, and which "understands" the way in which information is represented in memory on this platform. The run-time routine encodes the entire message, and returns the resulting octet string. A similar process is used for decoding. Any issues of big-endian or little-endian byte order (see 2.3 of Section III Chapter 4), or mostsignificant bits of a byte, are completely hidden within the encode/decode routines, as are all other details of the encoding rule specifications. 

Of course, without using a tool, a similar approach of mapping ASN.1 to a language datastructure and having separate code to encode and decode that data-structure is possible, but is likely to be more work (and more error prone) than the more "hard-wired" approach outlined above. But with a tool to provide the mapping and the encode/decode routines, this is an extremely simple and fast means of producing an implementation of an ASN.1-based application. 

In conclusion then, using a tool, ASN.1 today: 

Provides a powerful, clear and easy to use way for protocol designers to specify the information content of messages. 

Frees application designers from concerns over encoding, identification of optional elements, termination of lists, etc. 

• Is supported by tools mapping the ASN.1 structures to those of the main computer languages in use today. 

Enables implementors to concentrate solely on the application semantics without any concern with encoding/decoding, using applicationindependent run-time encode/decode routines producing bug-free encodings for all the ASN.1 encoding rules. 

## ASN.1 allows

## Designers to concentrate on application semantics

Design without encodingrelated bugs and with compact encodings available 

Implementors to write minimum code to support the application - fast development 

Bug-free encode/decode with absence of interworking problems. 

# Chapter 2 Introduction to ASN.1

# (Or: Read before you write!)

## Summary:

The best way of learning any language or notation is to read some of it. This chapter presents a small example of ASN.1 type definitions and introduces the main concepts of: 

• built-in key-words, 

• construction mechanisms, 

• user-defined types with type-reference-names, 

• identifiers or "field-names", 

• alternatives. 

There is a reference to "tagging" which is discussed in more detail in Section II. 

This chapter is intended for beginners in ASN.1, and can be skipped by those who have already been exposed to the notation. 

## 1 Introduction

Look at Figure 13. The aim here is simply to make sense of the data-structure it is defining - the information that transmission of a value of this structure would convey. 

Figure 13 is an "artificial" example designed to illustrate the features of ASN.1. It does not necessarily represent the best "business solution" to the problem it appears to be addressing, but the interested reader could try to invent a plausible rationale for some of its more curious features. For example, why have different "details" been used for "uk" and for "overseas" when the "overseas" case can hold any information the "uk" case can? Plausible answer, the "uk" case was in version 1, and the "overseas" was added later when the business expanded, and the designer wanted to keep the same bits-on-the-line for the "uk" case. 

This example is built-on as this book proceeds, and the scenario for this "Wineco protocol" appears in Appendix 1 with the complete protocol in Appendix 2. 

ASN.1 is not, of course, normally published in multiple fonts, but rather in just one font (Courier very often). We will return to that point later! 

## 2 The example

Refer to figure 13 constantly! Note that the lines of four dots are not part of the ASN.1 syntax – they just mean that I have not completed that part of the specification. 

```txt
Order-for-stock ::= SEQUENCE
{order-no INTEGER,
name-address BranchIdentification,
details SEQUENCE OF
SEQUENCE
{item OBJECT IDENTIFIER,
cases INTEGER},
urgency ENUMERATED
{tomorrow(0),
three-day(1),
week(2)} DEFAULT week,
authenticator Security-Type}
.....
.....
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
...
.....
....
Security-Type ::= SET
{ ....
.....
.... } 
```

## 2.1 The top-level type

There is nothing in the example (other than that it appears first) to tell the reader clearly that "Orderfor-stock" is the top-level type, the type whose values form the abstract syntax, the type which when encoded provides the messages that are transmitted by this application. In a real ASN.1 specification, you would discover this from humanreadable text associated with the specification, or in post-1994 ASN.1 by finding a statement: 

All application specifications contain a (single) ASN.1 type that defines the messages for that application. It will often (but need not) appear first in the specification, and is a good place to start reading! 

```txt
my-abstract-syntax ABSTRACT-SYNTAX ::=
{Order-for-stock IDENTIFIED BY
{joint-iso-itu-t international-organization(23) set(42) set-vendors(9)
wineco(43) abstract-syntax (1)} 
```

This simply says that we are naming the abstract syntax "my-abstract-syntax", that it consists of all the values of the type "Order-for-stock", and that if it were necessary to identify this abstract syntax in an instance of computer communication, the value given in the third line will be used. This is your first encounter with a piece of ASN.1 called "an OBJECT IDENTIFIER value" (which you will frequently find in ASN.1 specifications). The whole of that third line is actually just equivalent to writing a string of numbers: 

$$
\left\{ \begin{array}{c c c c c c} 2 & 2 3 & 4 2 & 9 & 4 3 & 1 \end{array} \right\}
$$

But for now, lets ignore the OBJECT IDENTIFIER value and go back to the main example in figure 13. 

## 2.2 Bold is what matters!

he parts in bold are the heart of the ASN.1 language. They are reserved words (note that they mainly are all upper-case - case does matter in ASN.1), and reference built-in types or construction mechanisms. A later chapter goes through each and every built-in type and construction mechanism! 

## 2.3 Names in italics are used to tie things together

The parts in italic are names which the writer has freely chosen to name the application’s types. They usually carry a good hint to a human reader about the sort of information that type is intended to carry, but for a computer, their sole purpose is to link together different parts of the specification. 

Most names present in a specification are either 

- names of built-in types or other built-in keywords (usually all upper case), or 

- type-reference-names (mixed case, starting upper), or 

- names of elements or alternatives in more complex types (mixed case, starting lower), or 

(less commonly seen) valuereference-names (mixed case, starting lower), or 

- names of enumerations (mixed case starting lower). 

So, for example, we have the type-reference-name "BranchIdentification" appearing in the third line of "Order-for-stock". This is legal if and only if somewhere else in the specification (in this case further down, but it could have been earlier) there is precisely one "type assignment" giving a type for "BranchIdentification". As far as a computer is concerned, the whole of the text following 

## BranchIdentification ::=

starting with "SET", and up to the closing curly bracket matching the one following "SET", can be used to textually replace the type-reference-name "BranchIdentification" wherever it appears. The resulting ASN.1 would be unchanged. Of course, if "BranchIdentification" is referenced in many different places, we would then have multiple copies of the text of the associated type, which would be very error prone, and would make the specification hard to read, so use of typereference-names in such cases is a “good thing”. But that is a matter of style that is dealt with in a later chapter. 

## 2.4 Names in normal font are the names of fields/elements/items

The names in normal font are again chosen arbitrarily by the application designer, and again are irrelevant to a computer, but help a human reader to understand the specification. They also provide a "handle" for human-readable text to clearly specify the semantics associated with the corresponding part of the specification. 

It may be helpful initially to think of the normal font words as the names of fields of a record structure, with the following bold or italic word giving the type of that field. The correct ASN.1 terminology is to say that the normal font words are either: 

• naming elements of a sequence, 

• naming elements of a set, 

• naming alternatives of a choice, or 

• (in one case only) naming enumerations. 

If an ASN.1 tool is used to map the ASN.1 specification to a data-structure definition in a programming language, these normal font names are mapped to identifiers in the chosen language, and the application code can set or read values of the corresponding parts of the data-structure using these names. 

The alert reader - again! - will immediately wonder about the length of these names, and the characters permitted in them, and ask about any corresponding problems in doing a mapping to a given programming language. These are good questions, but will be ignored for now, except to say that all ASN.1 names can be arbitrarily long, and are distinct even if they differ only in their hundredth character, or even their thousandth (or later)! Quite long names are fairly common in ASN.1 specifications. 

## 2.5 Back to the example!

So .... what information does a value of the type "Order-for-stock" carry when it is sent down the line? 

"Order-for-stock" is a structure with a sequence of fields or "elements" (an ordered list of types whose values will be sent down the line, in the given order). The first field or element is called "order-no", and holds an integer value. The second is called "name-address" and is itself a fairly complex type defined later, with a lot of internal structure. The next top-level field is called "details", and is also a fairly complex structured field, but this time the designer, purely as a matter of style, has chosen to write out the type "in-line" rather than using another type-referencename. 

This field is a "SEQUENCE OF", that is to say, an arbitrary number of repetitions of what follows the "SEQUENCE OF" (could be zero). There is ASN.1 notation to require a minimum or maximum number of repetitions, but that is not often encountered and is left to later. 

What follows is another "SEQUENCE", binding together an "OBJECT IDENTIFIER" field called "item" and an "INTEGER" field called "cases". (Remember, we are ordering stocks - cases - of wine!). So the whole of "details" is arbitrarily many repetitions of a pair of elements - an object identifier value and an integer value. 

You already met object identifier values when we discussed identification of the abstract syntax for this application. Object identifiers are world-wide unambiguous names. Anybody can (fairly!) easily get a bit of the object identifier name space, and these identifiers are frequently used in ASN.1-based applications to name a whole variety of objects. In the case of this example, we use names of this form to identify an "item" (in this case, the "item" is probably some stock item - identification of a particular wine). We also see later that the application designer has chosen to use identifications of this same form in "BranchIdentification" to provide a "unique-id" for a branch. 

Following the "details" top-level field, we have a field called "urgency" which is of the built-in type "ENUMERATED". Use of this type name requires that it be followed by a list of names for the enumerations (the possible values of the type). In ASN.1, but not in most programming languages, you will usually find the name followed by a number in round brackets, as in this example. These numbers were required to be present up to 1994, but can now be automatically assigned if the application-designer so desires. They provide the actual values that are transmitted down the line to identify each enumeration, so if the "urgency" is "deliver it tomorrow", what is sent down the line in this field position is a zero. (The reason for requiring the numbers to be assigned by the designer in the early ASN.1 specifications is discussed later, but basically has to do with trying to avoid interworking problems if a version 1 specification has an extra enumeration added in version 2 - extensibility again!) 

Again, the “urgency” field has a feature not found in programming language data-structure definition. We see the keyword "DEFAULT". What this means for the Basic Encoding Rules (BER - the original ASN.1 Encoding Rules) is that, as a sender's option, that field need not be transmitted if the intended value is the value following the word "DEFAULT" - in this case "week". This is an example where there is more than one bit-pattern corresponding to a single abstract value - it is an encoders option to choose whether to encode a "DEFAULT" value or not. For the later Packed Encoding Rules, the encoder is 

Keyword DEFAULT: Identifies a default value for an element of a SEQUENCE or SET, to be assumed if a value for that element is not included. 

Keyword OPTIONAL: Identifies an element for which a value can be omitted. Omission carries different semantics from any normal value of the element. 

required to omit thid simple field if the value is "week", and the decoder assumes that value. (If "urgency" had been a more complex data type the situation is slightly different, but that is a matter for Section III.) 

There is another ASN.1 keyword similar to "DEFAULT", namely "OPTIONAL" (not included in the example in figure 13). Again, the meaning is fairly obvious: the field can be omitted, but there © OS, 31 May 1999 51 is no presumption of any default value. The key-word might be associated, for example, with a field/element whose name was "additional-information". 

Just to return briefly to the question of "What are the precise set of abstract values in the type?", the answer is that the presence of DEFAULT does not change the number of abstract values, it merely affects encoding options, but the presence of OPTIONAL does increase the number of abstract values - an abstract value with an optional field absent is distinct from any abstract value where it is present with some value, and can have different application semantics associated with it. 

Finally, in "Order-for-stock", the last element is called "authenticator" and is of some (possibly quite complex) type called "Security-Type" defined by the application designer either before or after its use in "Order-for-stock". It is shown in figure 13 as a "SET", with the contents not specified in the example (in a real specification, of course, the contents of the "SET" would be fully-defined). "SET" is very similar to "SEQUENCE". In BER (the original ASN.1 encoding rules), it again signals a senders (encoders) option. The top-level elements (fields) of the SET, instead of being transmitted in the order given in the text (as they are for SEQUENCE) are transmitted in any order that is convenient for the sender/encoder. Today, it is recognised that encoder options are a "BAD THING" for both security reasons and for the extra cost they impose on receivers and particularly for exhaustive testing, and there are many who would argue that "SET" (and the corresponding "SET OF") should never be used by application designers, and should be withdrawn from ASN.1! But please refer to Figure 999 again! 

Figure 13 shows "Security-Type" being defined later in the specification, but actually, this is precisely the sort of type that is more likely to be imported by an application designer from some more specialised ASN.1 specification that defines types (and their semantics) designed to support security features. 

There are mechanisms in ASN.1 (discussed later) to enable a designer to reference definitions appearing in other specifications, and these mechanisms are often used. You will, however, also find that some application designers will copy definitions from other specifications, partly to make their own text complete without the need for an implementor to obtain (perhaps purchase!) additional texts, partly to ensure control over and "ownership" of the definition. If you are using this book with a colleague or as part of some course, you can have an interesting debate over whether it is a good thing to do this or not! 

## 2.6 The BranchIdentification type

Now let us look briefly at the "BranchIdentification" type, which illustrates a few additional features of the ASN.1 notation. (For now, please completely ignore the numbers in square brackets in this definition. These are called "tags", and are discussed at the end of this chapter.) 

This time it has been defined as a "SET", so in BER the elements are transmitted in any order, but we will take them in textual order. 

As an aside (but an important aside), we have already mentioned in Chapter 1 that BER uses a TLV type of encoding for all elements. Clearly, if the sender is able to transmit the elements of a "SET" in any order, the value used for the "T" in the TLV of each element has to be different. (This would not be necessary for SEQUENCE, unless there are OPTIONAL or DEFAULT elements whose presence or absence had to be detected). It is this requirement that gives rise to the "tag" concept introduced briefly below, and covered more fully later. 

The first listed element is "unique-id", an "OBJECT IDENTIFIER" value, which has already been discussed. The only other element is "details". Notice that the name "details" was also used in "Order-for-Stock". This is quite normal and perfectly legal - the contexts are different. 

It is usual for application designers to use distinct names for top-level elements in a SEQUENCE or SET, but it was not actually a requirement prior to 1994. It is now a requirement to have distinct names for the elements of both "SEQUENCE" and "SET" (and for the alternatives of a "CHOICE" - see below). The requirement was added partly because it 

Names of elements and alternatives Should all be distinct within any given SEQUENCE, SET, or CHOICE (a requirement post-1994). 

made good sense, but mainly because the ASN.1 notation for the values of a type could in some circumstances be ambiguous if this rule was not followed. 

Looking at "details": this is a "CHOICE", meaning that what goes in this field-position is one of a number of possible alternatives - in this case there are three possibilities: the "uk", "overseas", and "warehouse" alternatives. (Again, the alert reader will recognise that with the TLV approach used in BER, the "T" assigned to each of these alternatives has to be distinct if the receiver/decoder is to correctly determine which one is being transmitted.) 

The "uk" alternative is a "SEQUENCE" of three elements: a "name", a "type" and a "location". The latter two elements have type names in italics that are therefore presumably fairly complex, and will be defined earlier or later in the specification. They are not discussed further here. The "name" is a "VisibleString". This is one of a rather long list (about a dozen) of ASN.1 types which are "character strings" - strings of characters from some specified character repertoire. The names of these types are all mixed upper-lower case, and are one of the few exceptions (the types carrying calendar date and time are the other main exception) to the rule that built-in types in ASN.1 (names that cannot be re-defined by the user) are always entirely upper-case (like "INTEGER", "BOOLEAN", etc). 

Values of the "VisibleString" type are strings of printing ASCII characters, plus "space". Thus they are fine for UK or USA names, but would not cope well with other European countries, and very badly with names from other parts of the world! 

ASN.1 has many character string types providing support ranging from pure ASCII text through to text containing characters from any language in the world. 

By contrast, the "name" element for the "overseas" alternative has a type "UTF8String". If you are into character encoding schemes, you will have heard of UNICODE (and/or ISO 10646!) and UTF8! If you are not .... well, the area is discussed more fully later! Suffice it to say that "UTF8String" can contain characters from any of the languages of the world, but with the interesting property that if the characters just happen to be ASCII characters, the encoding is precisely ASCII! 

The UTF8 encoding scheme for characters is relatively new, and was only added to ASN.1 in 1998. It can legally only be used if the application designer references the 1998 (or later) ASN.1 specification. 

But .... - we have already noted that some restrictions were added in 1994 (names of elements of a "SEQUENCE", "SET" etc were required to be distinct, for example). Suppose you can't be bothered to upgrade your (300 pages long!) specification to conform to 1994 or later, but still want to use UTF8String in a new version? Well, legally, you CAN'T. ("Oh yeah?", you say, "What government has passed that law?", "Which enforcement agency will punish me if I break it?". I remain silent!) But as an implementor/reader, and if you see it happening, you will know what it © OS, 31 May 1999 53 means! Of course, as part of an application design team, you would make absolutely sure it did not happen in your specifications, wouldn't you? 

Back to figure 13! The third alternative in the "details" is "warehouse", and this itself is another "CHOICE", with just two alternatives - "northern" and "southern" each with a type "NULL". What is "NULL"? "NULL" formally is a type with just a single value (which is itself perhaps confusingly called "NULL"). It is used where we need to have a type, but where there is no additional information to include. It is sometimes called a "place-holder". Note that in the "warehouse" case, we could just as well have used a BOOLEAN to decide "northern" v "southern", or an ENUMERATED. Just as a matter of style (and to illustrate use of "NULL"!) we chose to do it as a choice of NULLs. 

## 2.7 Those tags

Now let's discuss the numbers in square brackets - the "tags". In post-1994 ASN.1, it is never necessary to include these numbers. If they would have been required pre-1994, you can (post-1994) ask for them to be automatically generated (called AUTOMATIC TAGGING), and need never actually include them. However, in existing published specifications, you will frequently encounter tags, and should have some understanding of them. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/9274f0aad38622d5ac5526ffa742a92c0e9e41afa8baae3361bab1d614d2a701.jpg)


In some of the very oldest ASN.1-based application specifications you will frequently find the keyword "IMPLICIT" following the tag, and occasionally today the opposite keyword "EXPLICIT". These qualify the meaning of the tag, and are fully described in Chapter 3. 

Why do we have tags? Remember the basic structure of BER: for a "SEQUENCE", there is a TLV for each element of the sequence; these are placed end-to-end to form the "V" part of an outer-level TLV. By default the "T" part of the TLV for any basic ASN.1 type such as "INTEGER" or "BOOLEAN" has a value that is specified in the ASN.1 specification itself, and the "T" part of the outer-level TLV for a "SEQUENCE" again has a value that is specified in the ASN.1 specification. 

This means that by default, the encoding of the "northern" "NULL" and of the "southern" "NULL" will be identical - the receiver/decoder would not know which was sent. The encoding has violated the necessary and obvious rule that for each alternative of a "CHOICE" the "T" used for each alternative should be different. The purpose of the tag is to over-ride the default "T" value with a value specified in the tag. So with the example as written, the "northern" "T" contains zero, and the "southern" "T" contains one. Similarly, it is important to override the default tag on the outer-level "T" for at least one of the "uk" and "overseas" "SEQUENCE" encodings. (As a matter of style, we chose to over-ride both). 

A later section fully explains the rules about when tags have to be inserted. (Pre-1994, figure 13 would be illegal without at least some of the numbers in square brackets - the tags). The rules are "the minimum necessary to avoid ambiguity", and once that is understood, the reader will be able to remember the detailed rules easily enough. However, there is (normally) no penalty in overriding a default tag, and as a matter of style and of a "don't think about it, just do it!" philosophy, it is quite common to see (as in figure 13) tags sequentially assigned to each of the elements of every "CHOICE" construction, whether strictly necessary or not. Similarly (but not done in figure 

13), it is also quite common (pre-1994) to see tags applied with sequential tag numbers to all elements of "SEQUENCE" and of "SET" constructions. 

A final introductory comment: the above has implied that tags are just plain old numbers. In fact, the tag name-space, the value encoded in the "T" part of a TLV is slightly more complicated than that. You will sometimes find the key-words "APPLICATION" or "PRIVATE" or "UNIVERSAL" after the opening square bracket, for example: 

$$
\text { Tagged - type }: := [ \text { APPLICATION   1 } ] \text { Order - For - Stock }
$$

These key-words define the "class" of the tag. In their absence, the "class" is so-called "contextspecific", which is by far the most common class of tag that is applied. Full details of tagging appears in Section II, Chapter 4. 

## 3 Getting rid of the different fonts

Suppose you have a normal ASN.1-based application specification using a single font. How do you apply fonts as in figure 13? 

First, in principle, you need to know what are the reserved words in the language, including the names of the character string and the date/time types, and you make sure these become bold! In practice, you can make a good guess that any name that is all upper-case goes to bold, but this is not a requirement. The "Address" type-reference-name in figure 4 could have been "ADDRESS", and provided that change was made everywhere in the specification, the result is an identical and totally legal specification. But as a matter of style, all upper-case for type reference names is rarely used. 

Any other name which begins with an initial upper case letter you set to italics - it is a typereference-name. Type-reference-names are required to begin with an upper-case letter. After that they can contain upper or lower case interchangeably. 

You will see in figure 13 a mixture of two distinct styles. In one case a type-reference-name ("Order-for-stock") made up of three words separates the words by a hyphen. In another case a type-reference-name ("OutletType") uses another upper-case letter to separate the words, and does not use the hyphen. "Security-Type" uses both! 

You normally don't see a mix of these three styles in a single specification, but all are perfectly legal. Hyphens (but not two in adjacent positions, to avoid ambiguity with comment - see below) have been allowed in names right from the first approved ASN.1 specification, but were not allowed by drafts prior to that first approved specification, so early writers had no choice, and used the "OutletType" style. Of course, nobody ever reads the ASN.1 specification itself - they just copy what everybody else does! So that style is still the most common today. It is, however, just that - a matter of style, and an unimportant one at that – all three forms are legal and it is a personal preference which you think looks neater or clearer. 

And finally, the normal font: most names starting with a lower-case letter are names of elements or alternatives ("order-no", "urgency", etc), and again such names are required to start with an initial lower-case letter, but can thereafter contain either upper or lower case. 

Names beginning with lower case are also required for the names of values. A simple example is the value "week" for the "urgency". 

Application specifications can contain not only type assignment statements such as those appearing in figure 13 (and which generally form the bulk of most application specifications), but can also contain statements assigning values to "value-reference-names". The general form of a value reference assignment is illustrated below: 

$$
\text { my - default - cases   INTEGER }: := 2 0
$$

which is defining the value-reference-name "my-default-cases", of type "INTEGER" to reference the integer value "20". It could then be used in the "cases" element in figure 13 as, for example: 

cases INTEGER DEFAULT my-default-cases 

## 4 Tying up some lose ends

## 4.1 Summary of type and value assignments

First, let us summarise what we have seen so far. ASN.1 specifies a number of pieces of notation (type-notation) which define an ASN.1 type. Some are very simple such as "BOOLEAN", others are more complex such as that used to define an enumerated type or a sequence type. A type-reference-name is also a piece of type-notation that can be used wherever ASN.1 requires a piece of type-notation. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/fce15995a047c1c9921a4483ec2c2a88321173db3e51e3106619cb2d9bd9aec5.jpg)


Similarly, ASN.1 specifies a number of pieces of value-notation (any type you can write with ASN.1 has a defined value-notation for all of its values). Again, some notations for values are very simple, such as "20" for integer values, others are more complex, such as the notation for object identifier values that you saw at the start of this chapter, or the notation for values of sequence types. Again, wherever ASN.1 requires value-notation, a value-reference-name can be used (provided it has been assigned a value somewhere). 

The general form of a type assignment is: 

$$
\text { type - reference - name } \quad : := \quad \text { type - notation }
$$

and of a value assignment is: 

$$
\text { value - reference - name   type - notation }: := \text { value - notation }
$$

where the value-notation has to be the "correct" value-notation for the type identified by the typenotation. This is an important concept. Anywhere in ASN.1 where you can use type-notation (for example to define the type of an element of a "SET" or "SEQUENCE", you can use any legal typenotation. However, where value-notation is allowed (for example, in value assignments or after DEFAULT), there is always a corresponding type-notation called the governor (which might be a type-reference-name) which restricts the syntax of the value-notation to that which is permitted for the type identified by the type-notation. 

So far, you have seen value notation used in the "IDENTIFIED BY" at the start of the chapter, and following the word DEFAULT. There are other uses that will be described later, but it remains the case that value-notation is used much less often than type-notation. 

## 4.2 The form of names

All names in ASN.1 are mixed upper/lower case letters and digits and hyphens (but not two adjacent or one at the end, to avoid confusion with comment), starting either with an upper case letter or with a lower case letter, depending on what the name is being used for. (As you will have guessed by now, they cannot contain the space character!) In every case of naming in ASN.1, the case of the first letter is fixed. If an upper-case letter is legal, a lower case letter will not be, and vice-versa. Names can be arbitrarily long, and are different names if they differ in either content or case at any position in the name. 

Note that because names can contain only letters and digits and hyphens, a name that is followed by any other character (such as an opening curly bracket or a comma), can have the following character adjacent to it with no space or new-line, or as a matter of purely personal style, one or more spaces or new-lines can be inserted. 

## 4.3 Layout and comment

Layout is "free-format" - anywhere that you can put a space you can put a new-line. Anywhere you have a new-line you can remove it and just leave a space. So a complete application specification can appear as a single line of text, and indeed that is basically the way a computer sees it! 

Names and layout Names contain letters, digits, or hyphens. They are arbitrarily long. Case is significant. Layout is free format. Comment starts with a pair of adjacent hyphens and ends with a pair of adjacent hyphens or a new-line. 

As a matter of style, everybody puts a new line between each type or value assignment statement, and generally between each element of a set or sequence and the alternatives of a choice. The layout style shown in figure 13 is that preferred by this author, as it makes the pairing of curly brackets very clear, but a perhaps slightly more common layout style is to include the opening curly bracket after "SEQUENCE" on the same line as the key-word "SEQUENCE", for example: 

## SEQUENCE { items OBJECT IDENTIFIER, cases INTEGER }

Still other authors (less common) will put the closing curly bracket on a line of its own and align it vertically with its matching opening bracket. All pure (and utterly unimportant!) stylistic matters. 

On a slightly more serious vein, there was pre-1994 value notation for the “CHOICE” type in the “BranchIdentification” that would allow: 

## details warehouse northern value-ref

as a piece of value notation (where “value-ref” is a value reference name for the “NULL” value). Remember that ASN.1 allows names to be used before they are assigned in a type or value assignment, and a poor dumb computer can be hit at the start of the specification with something looking like: 

In this case, it cannot determine where the first assignment ends - after "jack" or after "jill" or after “joseph” - it depends on the actual type of “Fred” - defined later). This can give a computer a hard time! Some of the early tool vendors could not cope with this (even tho' it probably never actually occurred!), and asked for the "semi-colon" character to be used as a statement separator in ASN.1. To this day, if you use these tools, you will need to put in semicolons between all your type assignments. (The "OSS ASN.1 Tools" package does not impose this requirement). The requirement to insert semi-colons in ASN.1 specifications was resisted, but to assist tool vendors a "colon" was introduced into the value notation for "CHOICE", so that post-1994 the above value notation would be written: 

## details : warehouse : northern : value-ref

(With or without the spaces, but with the colon.) And (for example): 

$$
\text {   joe   Fred   }:: := \text {   jack   }: \text {   jill   joseph   Mary   }:: := \text {   etc   etc   }
$$

has the end of the first assignment after “jill”, whilst: 

$$
\text {   joe   Fred   }:: := \text {   jack   }: \text {   jill:   joseph   Mary   }:: := \text {   etc   etc   }
$$

has the end of the first assignment after “joseph”. This is another small area where the 1994 specification imposed additional requirements not present pre-1994. 

Comment can be inserted wherever spaces and new-lines are allowed. Comment begins with a pair of hyphens (with no space between them), and ends either on the first new-line or with another pair of hyphens. (This is the only case where "new-line" is different from other forms of whitespace.) 

This is a perfectly good and consistent rule, but is not quite the same as that used for a certain well-known programming language, so take care! If you want a block of comment spread over several lines, you need a pair of hyphens at the start of each line. 

## 5 So what else do you need to know?

Really, you are now pretty well able to go away and read ASN.1 specifications! But as you have taken the trouble to obtain (perhaps you've even paid for!) this text, you will expect it to go on a bit further. 

In the next few chapters we look at the outer-level structure of an ASN.1-based application specification, and go through the various built-in types and construction mechanisms (like "SEQUENCE"), and the associated value notations. That text is boring! You will need to read it quickly! 

This will complete all you need to read. Most of the ASN.1 that was produced prior to 1994, with the exception of a few less commonly used "advanced" features like sub-typing and mechanisms for "holes", which are left to Section II. Section II also contains most of the discussion of the "new" features that were introduced in 1994, and is important reading for anybody involved in writing application specifications. 

Section I ends with a more detailed discussion of how to produce implementations using "ASN.1 compilers", and some further guidelines related to implementation. 

# Chapter 3 Structuring an ASN.1 specification

(Or: The walls, floors, door-ways and lifts, with some environmental considerations!) 

## Summary:

ASN.1-based application specifications consist mainly of type definitions as illustrated in Section 1 Chapter 2, but these are normally (and are formally required to be) grouped into collections called modules. 

This chapter: 

• introduces the module structure, 

• describes the form of module headers, 

• shows how to identify modules, 

• describes how to export and import type definitions between modules. 

The chapter also discusses: 

• some issues of publication format for a complete application specification, and 

• the importance of making machine-readable copy of the ASN.1 parts available. Part of the definition of a module is the establishment of: 

• a tagging environment, 

• an extensibility environment 

for the type-notations appearing in that specification. The meaning and importance of these terms is discussed in this chapter, with final details in Section II. 

```txt
Modules
All ASN.1 type and value assignments are required to appear within a module, starting with a module header and ending with "END". 
```

## 1 An example

The example we gave in figure 13 had one top-level type ("Order-for-stock"), and a number of supporting types, most of which we left incomplete. We will still leave the supporting types incomplete (and, indeed, will use three lines of four dots for the body of all the types to avoid repetition), but will now otherwise turn the example in Figure 

```txt
Wineco-ordering-protocol
{joint-iso-itu-t internationalRA(23) set(42) set-vendors(9)
wineco(43) modules(2) ordering(1)}
DEFINITIONS
    AUTOMATIC TAGS ::=
BEGIN
    Order-for-stock ::= SEQUENCE
    { ....
    ....
    ....}
    BranchIdentification ::= SET
    { ....
    ....
    ....}
    Security-Type ::= SET
    { ....
    ....
    ....}
    OutletType ::= SEQUENCE
    { ....
    ....
    ....}
    Address ::= SEQUENCE
    { ....
    ....
    ....}
END
Figure 14: A complete single-module ASN.1 specification 
```

13 into a complete ASN.1 specification that follows the rules of the language, and that could be fed into an ASN.1 compiler tool. 

NOTE — The use of three lines of four dots used in figures 13 and 14 is not legal ASN.1! It is used in this book out of sheer laziness! In a real specification there would be a complete list of named and fullyspecified (directly or by type-reference-names) elements. In figure 14, it is assumed that no further typereference-names are used in the body of these types - they use only the built-in types of the language like INTEGER, BOOLEAN, VisibleString, etc. 

The complete specification is shown in figure 14. 

This example forms what is called an ASN.1 module consisting of a six-line (in this - simple! - case) module header, a set of type (or value) assignment statements, and an "END" statement. This is the smallest legal piece of ASN.1 specification, and many early specifications were of this form - a single module. Today, it is more common for a complex protocol to be presented in a number of ASN.1 modules (usually within a single physical publication or set of Web pages). This is discussed further later. 

It is very common in a real publication for the module header to appear at the start of a page, for there then to be up to ten or more pages of type assignments (with the occasional value assignment perhaps), and then the END statement, which terminates the module. Normally there would be a page-break after the END statement in a printed specification, whether followed by another module or not. 

But Figure 14 is typical of early ASN.1 specifications, where the total protocol specification was probably only a few pages of ASN.1, and a single self-contained module was used for the entire specification. 

Note that whilst the use of new-lines and indentation at the start of this example is what is commonly used, the normal ASN.1 rule that white-space and new-lines are interchangeable applies here too - the module header could be on a single line. 

We will look in detail at the different elements of the module header later in this chapter, but first we discuss a little more about publication style. 

## 2 Publication style for ASN.1 specifications

Over the years, different groups have taken different approaches to the presentation of their ASN.1 specifications in published documents. Problems and variation stem from conflicting desires: 

a) A wish to introduce the various ASN.1 types that form the total specification gradually (often in a "bottom-up" fashion), within normal human-readable text that explains the semantics of the different types and fields. 

b) A wish to have in the specification a complete piece of ASN.1 that conforms to the ASN.1 syntax and is ready to feed into an ASN.1 tool, with the type definitions in either alphabetical order of type-reference-name, or in a "top-down" order. 

c) The desire not to repeat text, in order to avoid unintended differences, and questions of which text takes precedence if differences remain in the final product. 

There is no one perfect approach - application designers must make their own decisions in these areas, but the following two sub-sections discuss some common approaches. 

You may want to consider adding linenumbers to your ASN.1 to help references and cross-references ... but these are not part of the language! 

## 2.1 Use of line-numbers.

One approach is to give line numbers sequentially to the entire ASN.1 specification, as partly shown in figure 15 (again, lines of four dots are used to indicate pieces of the specification that have been left out). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/3ff709074aaf3ad62fc8b7b5f2031ce23327b8c0a325639ab62328cdacf00d5f.jpg)


It is important to note that if this specification is fed into an ASN.1 tool, the line numbers have to be removed - they are not part of the ASN.1 syntax, and the writer knows of no tool that provides a directive to ignore them! 

If you have tools to assist in producing it (and they exist), this line-numbered approach also makes it possible to provide a cross-reference at the end of the specification which gives, for each typereference-name, the line number of the type assignment where it is given a type, followed by all the line numbers where that reference is used. For a large specification, this approach is VERY useful to readers. If you don't do this, then you may wish to re-order your definitions into alphabetical order. 

Once you decide to use line numbers, there are two main possibilities. You can: 

Only put the ASN.1 in one place, as a complete specification (usually at the end), and use the line-numbers to reference the ASN.1 text from within the normal human-readable text that specifies the semantics. 

• Break the line-numbered ASN.1 into a series of "figures" and embed them in the appropriate place in the human-readable text, again using the line-numbers for more specific references. 

The latter approach only works well if the order you have the type definitions in (in the total specification) is the same as the order in which you wish to introduce and discuss them in the main text. 

## 2.2 Duplicating the ASN.1 text

A number of specifications have chosen to duplicate the ASN.1 text (usually but not necessarily without using line numbers). In this case the types are introduced with fragments of ASN.1 embedded in the human-readable text, and the full module specification with the module header and the "END" are presented as either the last clause of the document, or in an Appendix. 

You may choose to repeat your ASN.1 text, fragmented in the body of your specification and complete in an annex - but be careful the texts are the same! 

Note that where ASN.1 text is embedded in normal human-readable text, it is highly desirable for it to be given a distinctive font. This is particularly important where the individual names of ASN.1 types or sequence (or set) elements or choice alternatives are embedded in a sentence. Where a distinctive font is not possible, then use of italics or of quotation marks is common for such cases. (Quotation marks are generally used in this text.) 

If ASN.1 text appears in more than one place, then it used to be common to say that the collected text in the Appendix "took precedence if there were differences". Today it is more common to say that "if differences are found in the two texts, this is a bug in the specification and should be reported as such". 

## 2.3 Providing machine-readable copy

An annex collecting together the entire ASN.1 is clearly better than having it totally fragmented within many pages of printed text, no matter how implementation is to be tackled. 

If your implementors use tools, they will want machine-readable copy: consider how to provide this, and to tell them where it is! 

Prior to the existence of ASN.1 tools, the ASN.1 specification was there to tell an implementor what to code up, and would rarely need to be fed into a computer, so printed text sufficed. With the coming of ASN.1 compilers, which enable a major part of the implementation to be automatically generated directly from a machine-readable version of the ASN.1 specification, some attention is needed to the provision of such material. 

Even if the "published" specification is in electronic form, it may not be easy for a user to extract the formal ASN.1 definition because of the format used for publication, or because of the need to remove the line-numbers discussed above, or to extract the material from "figures". 

Wherever possible, the "published" specification should identify an authoritative source of machine-readable text for the complete specification. This should currently (1998) be ASCII encoded, with only spaces and new-lines as formatting characters, and using character names (see Section II Chapter 2) for any non-ASCII characters in value notations. It is, however, likely that the so-called UTF8 encodings (again see Section II Chapter 2), allowing direct representation of any character, will become increasingly acceptable, indeed, preferable. 

It is unfortunate that many early ASN.1 specifications were published by ISO and ITU-T, who had a history of making money from sales of hard-copy specifications and did not in the early days provide machine-readable material. However, a number of Editors of the corresponding Standards and Recommendations did obtain permission to circulate (usually without charge) a machinereadable copy of the ASN.1 (usually as ASCII text), but the availability of such material was not always widely publicised. 

```txt
001 Wineco-ordering-protocol
002 {joint-iso-itu-t internationalRA(23) set(42) set-vendors(9)
003 wineco(43) modules(2) ordering(1)}
004 DEFINITIONS
005 AUTOMATIC TAGS ::=
006 BEGIN
007
008 Order-for-stock ::= SEQUENCE
009 {order-no INTEGER,
010 name-address BranchIdentification,
.....
Figure 16: The module header 
```

It is unfortunate that many ASN.1 specifications have had to be re-keyed from printed copies for use in tools, with all the errors that can cause. The better tool vendors have built-up over time a stock of machine-readable specifications (either obtained from Editors or by re-keying themselves) for the most common protocols, and will supply these to their customers on request. (The URL in Appendix 5 provides a link to a list of many ASN.1-based specifications, and in some cases to sources of machine-readable specifications where these are known to exist.) 

## 3 Returning to the module header!

## 3.1 Syntactic discussion

Figure 16 repeats the module header lines (with line numbers). 

Let us take the items in turn. The first line contains the module name, and is any ASN.1 name beginning with a capital letter. It is intended to identify the module and its contents for human-beings, and would normally be distinct from any other module name in the same application specification. This is not, however, a requirement, as ASN.1 has no actual concept of a complete application specification (only of a complete and legal module)! We return later to the question of a "complete specification". 

<table><tr><td>The module header provides</td></tr><tr><td>A module name</td></tr><tr><td>A unique module identification</td></tr><tr><td>Definition of the tagging environment</td></tr><tr><td>Definition of the extensibility environment</td></tr></table>

The second/third line is called the module identifier, and is another case of an object identifier value. This name-form is required to be distinct from that of any other module - not just from those in the same application specification, but from any ASN.1 module ever-written or ever to-bewritten, world-wide! (Including - tho' some might say Figure 999 applies – any later version of this module.) 

Strictly speaking, you don't need to include this second/third line. It was introduced into ASN.1 in about 1988, and was left optional partly for reasons of backwards compatibility and partly to take account of those who had difficulty in getting (or were too lazy to try to get!) a bit of the object identifier name space. 

It is today relatively easy to get some object identifier name-space to enable you to give worldwide unambiguous names to any modules that you write, but we defer a discussion of how to go about this (and of the detailed form of an object identifier value) to Section II. Suffice it to say that the object identifier values used in this book are "legitimate", and are distinct from others (legally!) used to name any other ASN.1 module in the world. If name-space can be obtained for this relatively unimportant book ....! 

The fourth line and the sixth line are "boiler-plate". They say nothing, but they have to be there! No alternative syntax is possible. (The same applies to the "END" statement at the end of the module.) 

The fifth line is one of several possibilities, and determines the "environment" of the module that affects the detailed interpretation of the type-notation (but not of type-reference-names) textually appearing within the body of the module. 

Designers please note: Not only is it illegal ASN.1 to write a specification without a module header and an "END" statement, it can also be very ambiguous because the "environment" of the type-notation has not been determined. 

So ... what aspects of the "environment" can be specified, and what syntax is possible in this fifth line? 

There are two aspects to the "environment", called (in this book) "the tagging environment" and "the extensibility environment". The reader will note that these both contain terms that we have briefly mentioned before, but have never properly explained! Please don't be disappointed, but the explanation here is again going to be partial - for a full discussion of these concepts you need to go to Section II. 

The tagging environment (with the string used in line 4 to specify it given in parenthesis) is one of the following: 

• An environment of explicit tagging (EXPLICIT TAGS). 

• An environment of implicit tagging (IMPLICIT TAGS). 

• An environment of automatic tagging (AUTOMATIC TAGS). 

Omission of all of these implies an environment of explicit tagging. (This is for historical reasons, as an environment of explicit tagging was the only available tagging environment up to the 1988 specification). 

The extensibility environment (with the string used in line 4 to specify it given in parenthesis) is one of the following: 

• An environment requiring explicit extensibility markers (no mention of extensibility in line 4). 

• An environment of implied extensibility markers (EXTENSIBILITY IMPLIED). 

We discuss these environments below. If both a tagging and an extensibility environment are being specified, the text for either one can come first. 

## 3.2 The tagging environment

The treatment here leans heavily on the effect of tagging in a TLV-style encoding, and on BER in particular. It was to assist in such an encoding scheme that tagging was introduced into ASN.1. A more abstract treatment of tagging applicable to any encoding rules is given in Section II. 

To look more closely at the effects of tagging, let us review a section from figure 13, repeated in figure 17. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/f92632cdb905fcb92ee7ccd610a45468e680a87601a75ce4342a4b3b49627228.jpg)


We have already noted that in BER a SEQUENCE is encoded as a TLV, with the "V" part being a series of TLVs, one for each element of the sequence. Thus the "overseas" element is a TLV, with the "V" part consisting of three TLVs, one for each of the three elements. We have also stated that the tag "[1]" over-rides the tag value in the outermost "T" for the "overseas" sequence. 

Similarly, we have noted that the tag [0] and the tag [1] on the NULLs overrides the default tag on the TLV for each NULL. In this case, the encoding no longer contains the default tag for NULL, and the fact that this TLV does actually represent a NULL (or in other cases an INTEGER or a BOOLEAN etc) is now only implied by the tag in the "T" part - you need to know the type definition to recognise that [0] is in this case referring to a NULL. We say that we have "implicitly tagged the NULL". Similarly, the "overseas" "SEQUENCE" was implicitly tagged with tag "[1]". 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/5d0af9e3e9438d9529ad3c2bb40b3caa41372d35d10e406a50ca190fd1e01a44.jpg)


But what about the tag we have placed on the "warehouse" "CHOICE"? There is a superficial similarity between "CHOICE" and "SEQUENCE" (they have almost the same following syntax), but in fact they are very different in their BER encoding. With "SEQUENCE", following elements are wrapped up in an outer-level TLV wrapper as described earlier, but with "CHOICE", we merely take any one of the TLV encodings for one of the alternatives of the "CHOICE", and we use that as the entire encoding (the TLV) for the "CHOICE" itself. 

Where does that leave the tagging of "warehouse"? Well, at first sight, it will over-ride the tag of the TLV for the "CHOICE" (which is either "[0]" or "[1]" depending on which alternative was selected) with the tag "[2]". Think for a bit, and then recognise that this would be a BUST specification! The alternatives were specifically given (by tagging the NULLs) distinct tags precisely so as to be able to know which was being sent down the line in an instance of communication, but now we are over-riding both with a common value ("[2]")! This cannot be allowed! 

To cut a long story short - two forms of tagging are available in ASN.1: 

implicit tagging: (this is what has been described so far), where the new tag over-rides the old tag and type information which was carried by the old tag is now only implicit in the encoding; this cannot be allowed for a "CHOICE" type; and 

• explicit tagging: we add a new TLV wrapper specifically to carry the new tag in the "T" part of this wrapper, and carry the entire original TLV (with the old tag) in the "V" part of this wrapper; clearly this is OK for "CHOICE". 

Whilst implicit tagging is forbidden for "CHOICE" types (it is an illegal ASN.1 specification to ask for it), both implicit and explicit tagging can be applied to any other type. However, whilst explicit tagging retains maximum type information, and might help a dumb line-monitor to produce a sensible display, it is clearly more verbose than implicit tagging. 

<table><tr><td>implicit tagging - overrides the &quot;T&quot; part</td></tr><tr><td>explicit tagging - adds an extra TLV wrapper</td></tr></table>

Now, what do the different tagging environments mean? 

## 3.2.1 An environment of explicit tagging

With an environment of explicit tagging, all tags produce explicit tagging unless the tag (number in square brackets) is immediately followed by the keyword "IMPLICIT". 

An environment of explicit tagging was the only one available in the early ASN.1 specifications, so it was common to see the word "IMPLICIT" almost everywhere, reducing readability. Of course, it was - and is - illegal to put "IMPLICIT" on a tag that is applied to a "CHOICE" type-notation, or to a type-reference-name for such notation. 

## 3.2.2 An environment of implicit tagging

With an environment of implicit tagging, all tags are applied as implicit tagging unless one (or both) of the following apply: 

• The tag is being applied to a "CHOICE" type-notation or to a type-reference-name for such notation; or 

• The keyword "EXPLICIT" follows the tag notation. 

In the above cases, tagging is still explicit tagging. In practice most specifications written between about 1986 and 1995 specified an environment of implicit tagging in their module headers, and it was unusual to see either the keyword "IMPLICIT" or the keyword "EXPLICIT" after a tag. Occasionally, EXPLICIT was used for reinforcement, and occasionally (mainly in the security world to guarantee an extra TLV wrapper) on specific types within an environment of implicit taggin 

<table><tr><td>An environment of implicit tagging only produces implicit tagging where it is legal - there is no need to say &quot;EXPLICIT&quot; on a &quot;CHOICE&quot;.</td></tr></table>

## 3.2.3 An environment of automatic tagging

The rules about explicit and implicit tagging add to what is already a complicated set of rules on when tagging is needed, and in the 1994 specification, partly to simplify things for the application designer, and partly because the new Packed Encoding Rules (PER) were not TLV-based and made little use of tags, the ability to specify an environment of automatic 

<table><tr><td>Automatic tagging</td></tr><tr><td>Set up this environment and forget about tags!</td></tr></table>

tagging was added. 

In this case, tags are automatically added to all elements of each sequence (or set) and to each alternative of a choice, sequentially from "[0]" onwards (separately for each “SEQUENCE”, “SET”, or “CHOICE” construction). They are added in an environment of implicit tagging EXCEPT that if tag-notation is present on any one of the elements of a particular “SEQUENCE” (or “SET”) element or “CHOICE” alternative, then it is assumed that the designer has taken control, and there will be NO automatic application of tags. (The tag-notation that is present is interpreted in an environment of implicit tagging in this case.) 

It is generally recommended today that "AUTOMATIC TAGS" be placed in the module header, and the designer can then forget about tags altogether! However (refer back to figure 999 please!), there is a counter-argument that "AUTOMATIC TAGS" can be more verbose than necessary in BER, and can give more scope for errors of implementation if ASN.1 tools are not used. You take your choice! But I know what mine would be! 

## 3.3 The extensibility environment

We have already discussed the power of a TLVstyle of encoding to allow additions of elements in version 2, with version 1 specifications able to skip and to ignore such additional elements. (This extensibility concept actually generalises to things other than sequences and sets, but these are sufficient for now.) 

## The extensibility marker

An ellipsis (or a pair) which identifies an insertion point where version 2 material can be added without affecting a version 1 system's ability to decode version 2 encodings. 

If we are to retain some extensibility capability in ASN.1 and we are to introduce encoding rules that are less verbose than the TLV of BER (such as the new PER), then a designer's requirements for extensibility in his application specification have to be made explicit. 

We also need to make sure not only that encoding rules will allow a version 1 system to find the end of (and perhaps ignore) added version 2 material, but also that the application designer clearly specifies the actions expected of a version 1 system if it receives such material. 

To make this possible, the 1994 specification introduced an extensibility marker into the ASN.1 notation. In the simplest use of this, 

the type-notation "Order-for-stock" could be written as in figure 18. 

Here we are identifying that we require encoding rules to permit the later addition of outer-level elements between "urgency" and "authenticator", and additional enumerations, in version 2, without ill-effect if they get sent to version 1 systems. (Full details are in Section II.) (Should we have been happy to add the version 2 elements at the end after "authenticator", then a single ellipsis would have sufficed.) 

```txt
Order-for-stock ::= SEQUENCE
{order-no INTEGER,
name-address BranchIdentification,
details SEQUENCE OF
SEQUENCE
{item OBJECT IDENTIFIER,
cases INTEGER},
urgency ENUMERATED
{tomorrow(0),
three-day(1),
week(2), ... } DEFAULT week,
...
...
authenticator Security-Type}
Figure 18: Order-for-stock with extensibility markers 
```

The place where the ellipses are placed, and where new version 2 material can be safely inserted without upsetting deployed version 1 systems is called (surprise, surprise!) the insertion point. You are only allowed to have one insertion point in any given sequence, set, choice, etc. 

The alert reader (you should be getting used to that phrase by now, but it is probably still annoying 

- sorry!) will recognise that in addition to warning encoding rules to make provision, it is also necessary to tell the version 1 systems what to do with added material. In the case of new outerlevel elements, it may appear "obvious" that the required action would be to silently ignore the added elements. But what should a version 1 system do if it receives an "urgency" value that it 

Exception specification Specification of the behaviour of a version 1 system in the presence of added version 2 elements or values. 

does not know about? There is a further piece of notation (section II again, I am afraid, if you want details!) called the exception specification which can be added immediately after the extensibility ellipsis. (The exception specification starts with an exclamation mark, so you will know it when you see it!). 

Application designers are encouraged to provide exception specifications when they use extensibility markers, although this has not been made mandatory. 

In an environment requiring explicit extensibility markers, the ellipsis, and any implications on encoding rules and version 1 behaviour which stem from the presence of an ellipsis, only occurs if the ellipsis is textually present in the specification wherever it is required. 

In an environment of implied extensibility markers, all type-notations in that environment which do not already contain an extensibility marker in constructions where such markers are permitted automatically have one added at the end of the construction. 

So if the type-notation of figure 18 was in an environment of implied extensibility, an additional extension marker would be automatically inserted at the end of the "SEQUENCE{....}" construction in the "details" "SEQUENCE OF". 

At the time of writing this text, extension markers are being extensively used, but few designers have chosen to specify an environment of implied extensibility markers, even tho' the cost of having additional, perhaps unnecessary, insertion points for the insertion of version 2 material is low in terms of bits on the line. 

Environment of implied extensibility markers: an environment where any construction without an extensibility marker (and which is allowed one) has one added (at its end). 

The problem probably stems from three problems with using this environment: 

• The insertion point is always at the end - you have no control over its position. 

• When producing the version 2 specification, you have to actually insert the ellipses explicitly before your added elements - and you might forget! 

There is no provision (when this environment is used) for the presence of an exception specification with the extension marker, so all rules for the required behaviour of version 1 systems in the presence of version 2 elements or values have to be generic to the entire specification. 

Concluding advice: Think carefully about where you want extension markers and about the handling you want version 1 systems to give to version 2 elements and values (using exception specifications to localise and make explicit those decisions), but do not attempt a blanket solution using an environment of implied extensibility. 

## 4 Exports/imports statements

It has taken a lot of text to describe the effects of a six-line header! There is much less text in the ASN.1 Standard/Recommendation! But we are not yet done! 

Following the sixth line ("BEGIN") and (only) before any type or value assignment statements, we can include an exports statement (first) and/or an imports statement. These are usually regarded as part of the module header. 

## Exports/Imports statements

A pair of optional statements at the head of a module that specify the use of types defined in other modules (import), or that make available to other modules types defined in this module (export). 

At this point it is important to highlight what has been only hinted at earlier: there is more in the ASN.1 repertoire of things that have reference names than just types and values, although these are by far the most important (or at least, the most prolific!) in most specifications. 

Pre-1994 (only) we add macro names, and post-1994 we add names of information object classes, information objects, and information object sets. These can all appear in an export or an import statement, but for now we concentrate only on type-reference-names and value-reference-names. 

An exports statement is relatively simple, and is illustrated in figure 19, where we have taken our type definitions for "OutletType" and "Address", put them into a module of commonly used types, and exported them, that is to say, made them available for use in another module. 

```txt
Wineco-common-types
{ joint-iso-itu-t internationalRA(23) set(42) set-vendors(9)
wineco(43) modules(2) common(3)}
DEFINITIONS
AUTOMATIC TAGS ::=
BEGIN

EXPORTS OutletType, Address;

OutletType ::= SEQUENCE
{ ....
.....
.... }
Address ::= SEQUENCE
{ ....
.....
.... }
......
END

Figure 19: The common types module (first attempt) 
```

In reality there would be more supporting types in "Wineco-common-types" which we are choosing not to export - they are not available for use in other modules. There would probably also be rather more types exported. 

Note the presence of the semi-colon as a statement terminator for the "EXPORTS" statement. We will see this being used to terminate the “IMPORTS” statement also. These are the only two cases where ASN.1 has a statement terminator. 

Note also that for historical reasons (“EXPORTS” was only added in 1988) the omission of an “EXPORTS” statement has the semantics "everything is available for import by another module", whilst: 

Absence of an EXPORTS statements means "exports EVERYTHING". The statement "EXPORTS ;" means "exports NOTHING". 

## EXPORTS ;

has the semantics "nothing is available for import by another module". 

Next we are going to assume that the "Security-Type" which we first used in Figure 13 is being imported from the Secure Electronic Transactions (SET) specification (a totally separate publication), and will be used in our "Wineco-common-types" module but also in our other modules. We import this for use in the "Wineco-common-types" module, but also export it again to make the imports clauses of our other modules simpler (they merely need to import from "Wineco-common-types"). This "relaying" of type definitions is legal. 

```txt
Wineco-common-types
{ joint-iso-itu-t internationalRA(23) set(42) set-vendors(9)
    wineco(43) modules(2) common(3)}
DEFINITIONS
AUTOMATIC TAGS ::=
BEGIN

EXPORTS OutletType, Address, Security-Type;

IMPORTS Security-Type FROM
SET-module
{joint-iso-itu-t internationalRA(23) set(42) module(6) 0};

OutletType ::= SEQUENCE
{ ....
.....
.... }
Address ::= SEQUENCE
{ ....
.....
.... }
......

END

Figure 20: The common types module (enhanced) 
```

This changes figure 19 to figure 20. 

As with EXPORTS, the text between "IMPORTS" and "FROM" is a comma separated list of reference names. We will see how to import from more than one other module in the next figure. 

Note at this point that if a type is imported from a module with a particular tagging or extensibility environment into a module with a different tagging or extensibility environment, the type-notation for that imported type continues to be interpreted with the environment of the module in which it was originally defined. This may seem obvious from the way in which the environment concept was presented, but it is worth reinforcing the point - what is being imported is in some sense the "abstract type" that the type-notation defines, not the text of the type-notation. 

## 5 Refining our structure

## The final example

We now use several modules, we have a CHOICE as our top-level type and we clearly identify it as our top-level type, We use an object identifier value-reference-name, we use APPLICATION class tags, we handle invalid encodings, we have extensibility at the toplevel with exception handling. We are getting quite sophisticated in our use of ASN.1! 

Now we are going to make quite a few changes! We will add a second top-level message (and make provision for more) called "Return-of-sales" defined in another module, and we will now include the “ABSTRACT-SYNTAX” statement (mentioned in Chapter 2) to define our new toplevel type in yet another module, that we will put first. 

We will do a few more cosmetic changes to this top-level module, to illustrate some slightly more advanced features. We will: 

use "APPLICATION" class tags for our top-level messages. This is not necessary, but is often done (see later discussion of tag classes) 

• assign the first part of our long object identifiers to the value-reference-name "wineco-OID" and use that as the start of our object identifiers, a commonly used feature of ASN.1. 

add text to "ABSTRACT-SYNTAX" to make clear that if the decoder detects an invalid encoding of incoming material our text will specify exactly how the system is to behave. 

The final result is shown in Figure 21, which is assumed to be followed by the text of Figure 20. Have a good look at Figure 21, and then read the following text that "talks you through it". 

Lines 001 to 006 are nothing new. Note that in lines 10 and 13 we will use "wineco-OID" (defined in lines 015 and 016) to shorten our object identifier value, but we are not allowed to use this in the module header, as it is not yet within scope, and the object identifier value must be written out in full. 

Line 007 simply says that nothing is available for reference from other modules. 

```tcl
001 Wineco-common-top-level
002 { joint-iso-itu-t internationalRA(23) set(42) set-vendors(9)
003 wineco(43) modules(2) top(0)}
004 DEFINITIONS
005 AUTOMATIC TAGS ::= 
006 BEGIN
007 EXPORTS ;
008 IMPORTS Order-for-stock FROM
009 Wineco-ordering-protocol
010 {wineco-OID modules(2) ordering(1)}
011 Return-of-sales FROM
012 Wineco-returns-protocol
013 {wineco-OID modules(2) returns(2)};
014
015 wineco-OID OBJECT IDENTIFIER ::= 
016 { joint-iso-itu-t internationalRA(23)
017 set(42) set-vendors(9) wineco(43)}
018 wineco-abstract-syntax ABSTRACT-SYNTAX ::= 
019 {Wineco-Protocol IDENTIFIED BY
020 {wineco-OID abstract-syntax(1)}
021 HAS PROPERTY
022 {handles-invalid-encodings}
023 --See clause 45.6 --
}
024
025 Wineco-Protocol ::= CHOICE
026 {ordering [APPLICATION 1] Order-for-stock,
027 sales [APPLICATION 2] Return-of-sales,
028 ... ! PrintableString : "See clause 45.7"
029 }
030
031 END
--New page in published spec.
032 Wineco-ordering-protocol
033 { joint-iso-itu-t internationalRA(23) set(42) set-vendors(9)
034 wineco(43) modules(2) ordering(1)}
035 DEFINITIONS
036 AUTOMATIC TAGS ::= 
037 BEGIN
038 EXPORTS Order-for-stock;
039 IMPORTS OutletType, Address, Security-Type FROM
040 Wineco-common-types
041 {wineco-OID modules(2) common (3)};
042
043 wineco-OID OBJECT IDENTIFIER ::= 
044 { joint-iso-itu-t internationalRA(23)
045 set(42) set-vendors(9) wineco(43)}
046
047 Order-for-stock ::= SEQUENCE
048 { ....
.... } ....
.... BranchIdentification ::= SET
070 { ....
.... .... }
.... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .... .. 
```

Lines 008 to 013 are the imports we were expecting from our other two modules. Note the syntax here: if we had more types being imported from the same module, there would be a comma separated list as in line 039, but when we import from two different modules lines 011 to 013 just run on from lines 008 and 010 with no separator. 

Lines 015 and 017 provide our object identifier value-reference-name with a value assignment. It is a (very useful!) curiosity of the value notation for object identifiers that it can begin with an object identifier value-reference-name which "expands" into the initial part of a full object identifier value, and is then added to, as we see in lines 010, 013, and 020. If you want to jump ahead, and are interested, the OID tree is more fully described in Chapter 1 of Section II. 

Lines 018 to 023 are the "piece of magic" syntax that defines the top-level type, names the abstract syntax, and assigns an object identifier value to it - something which in older specifications would be done in human-readable text. In fact, this syntax is not "ad hoc" it is an example of an information object assignment statement which will be discussed in Section II. 

The "HAS PROPERTY" and lines 22 to 23 is the only "property" that can be specified at present. The inclusion of this syntax is partly to counter an old OSI view-point that decoding was a separate layer from the application, and that if decoding failed to produce a recognised abstract value, all you could do was abort the connection! (Do check Figure 999 again!) Stupid idea! But including lines 20 to 23 reassures the reader that the specification does indeed contain (in clause 45.6) text to cover what to do in this case. 

Lines 025 to 029 define the single-ASN.1-type that we need for our top-level messages to ensure that each encoding (of either or our main message types) is unambiguous. If we simply applied BER to the two types "Order-for-stock" and "Return-of-sales-data", we could (and probably would) get a bit-pattern used for a value of one type also being used as an encoding for a value of the other type. By forming a new CHOICE type, the rules for tag uniqueness of a CHOICE type solve this problem. Notice that we have used "AUTOMATIC TAGS" in line 005, so there was no need to add any tags in lines 026 and 027, but as a matter of personal preference and style, we chose to take complete control of the "T" value in the outermost TLV of our messages and make one an encoding of "[APPLICATION 0]" and the other of "[APPLICATION 1]", no matter what the original tags were. Some designers argue that this is helpful for hand-encoders - it is certainly irrelevant to those using a tool. Notice that the presence of tags in lines 026 and 027 disables automatic tagging for the CHOICE in line 025, temporarily replacing the tagging environment with an environment of implicit tagging. 

Line 028 tells us that in version 2 we suspect we may need more outer-level messages, and that encoding rules must ensure that adding such messages does not prevent version 1 systems from correctly receiving messages that were in version 1. The exclamation mark and following material (the exception specification - described in detail in Section II) in line 028 tells us that clause 45.7 details the actions that a version 1 system should take if it receives messages added in version 2 (or later). 

Lines 032 to 101 are our second module (the development of the original Figure 13), and contain nothing new. Note, however, that lines 043 and 045 are a repetition of 015 to 017, and this might seem undesirable. It would have been possible to define "wineco-OID" in yet another module (with lots of other value-reference-names we might need), and to import that name from that module. However, we would not (for obvious "infinite recursion") reasons be allowed to use "wineco-OID" in the "FROM" for that import, so we would end up writing out as much text (and repeating it in each module where we wish to do the import) as we have written in lines 015 to 017 and 043 to 045. What we have is about as minimal as we can get. 

Lines 102 to 139 are our third module, structurally the same as 032 to 101, and introducing nothing new. The whole specification then concludes with the text of Figure 20, giving our "common-type" module, which we have already discussed. 

```txt
--New page in published spec.
102 Wineco-returns-protocol
103 { joint-iso-itu-t internationalRA(23) set(42)
104 set-vendors(9) wineco(43) modules(2) returns(2)}
105 DEFINITIONS
106 AUTOMATIC TAGS ::= 
107 BEGIN
108 EXPORTS Return-of-sales;
109 IMPORTS OutletType, Address, Security-Type FROM
110 Wineco-common-types
111 {wineco-OID modules(2) common (3)};
112
113 wineco-OID OBJECT IDENTIFIER ::= 
114 {iso identified-organization icd-wineco(10)}
115
116 Return-of-sales ::= SEQUENCE
117 { ....
.... .... }
.... ....
.... ....
.... ....
139 END
Figure 21 (last part):Last figure for this chapter! 
```

## 6 Complete specifications

As was stated earlier, there is no concept in ASN.1 of a "complete specification", only of correct (complete) modules, some of which may include an "ABSTRACT-SYNTAX" statement to identify a top-level type (or which may contain a top-level type identified in human-readable text). 

In many cases if a module imports a type from some other module, the two modules will be in the same publication (loosely, part of the same specification), but this is not a requirement. Types can be imported from any module anywhere. 

Suppose we take a top-level type in some module, and follow the chain of all the type-referencenames it uses (directly or indirectly) within its own module, and through import and export links (again chained to any depth) to types in other modules. This will give us the complete set of types that form the "complete specification" for the application for which this is the top-level type, and the specifications of all these types have (of course) to be available to any implementor of that application and to any ASN.1 compiler tool assisting in the implementation. Purely for the purposes of the final part of this chapter of this book, this tree of type definitions will be called the application-required types. 

It is important advice to any application designer to make it very clear early in the text of any application specification precisely which additional (physical) documents are required to obtain the definitions of all the application-required types. 

But suppose we now consider the set of modules in which these application-required types were defined. (Again, purely for the next few paragraphs, we will call these the application-required modules). 

In general, the module textually containing the top-level type probably does not contain any types other than those which are application-required types (although there is no requirement that this be so). But as soon as we start importing, particularly from modules in other publications which were perhaps produced to satisfy more general requirements, then there are likely to be some types defined in application-required modules that are not application-required types! 

As we shall see later, tools vary in their intelligence. There are some tools that require you to physically extract referenced types and put everything into the same module with the top-level type first! This is at the extreme bad end, and can give real problems if the tagging or extensibility environments of the different modules are different. 

The best tools will allow you to present them with machine-readable text (perhaps in several files) that contains all the application-required modules (and a directive identifying the top-level type), and will extract from those modules only the application-required types, mapping only those to data structures in your chosen programming language. (This keeps the memory requirement for the implementation to a minimum). 

Remember the discussion you had with yourself earlier (as a potential application designer) about the pros and cons of referencing (importing) or textually copying types from other modules? You may re-open that discussion! 

## 7 Conclusion

We have come a long way from our simple type assignments in Figure 13! 

The high-level structure of an ASN.1-based application specification has been described and explored, and most of the important concepts have now been introduced. 

But a word of caution: the simple protocol we have used here for illustration would probably be better structured as the single-ASN.1-module outlined in Figure 14. The additional power (but complexity) of multiple modules with export/import is important for large specifications, but should not be used unnecessarily - keep it as simple as possible! If the Figure 14 structure will do, stay with Figure 14! 

It now remains to complete the discussion of the ASN.1 type and value notations for the simple built-in types and the construction mechanisms (this is done in the next chapter), and (in Section II – with an introduction in the Chapter 5 of this section) to give a fuller treatment of the more advanced concepts we have mentioned, and to discuss more of the features added in 1994. 

The reader should, however, now be able to read and to understand the bulk of most real ASN.1 specifications produced before 1994, and to recognise the use of some features introduced in the 1994 ASN.1. Read on! 

# Chapter 4 The basic data types and construction mechanisms - closure

## (Or: You need bricks - of various shapes and sizes!)

## Summary:

There are a number of types that are pre-defined in ASN.1, such as: 

• INTEGER, 

• BOOLEAN, 

• UTF8String. 

These are used to build more complex user-defined types with construction mechanisms such as: 

• SEQUENCE, 

• SET, 

• CHOICE, 

• SEQUENCE OF, 

• SET OF, 

• etc. 

Many of these construction mechanisms have appeared in the examples and illustrations of earlier chapters. 

This chapter completes the detailed presentation of all the basic ASN.1 types, giving in each case a clear description of: 

• the type-notation for the type, 

• the set of abstract values in the type, and 

• the value-notation for values of that type. 

Additional pieces of type/value-related notation are also covered, largely completing the discussion of syntax commonly used in pre-1994 specifications. 

The chapter ends with a list of additional concepts whose treatment is deferred to either the next chapter (Discussion of advanced features), or to Section II. 

## 1 Illustration by example

In order to illustrate some of the type and value notations, we will define our Return-of-Sales message as in Figure 22. Figure 22 has been designed to include all the basic ASN.1 types apart from NULL, and provides the hook for further discussion of these types. 

Figure 22 has been carefully constructed to complete your introduction to all the basic ASN.1 types - that's it folks! 

Have a good look at Figure 22. It should by now be fairly easy for you to understand its meaning. If you have no problems with it, you can probably skip the rest of this chapter, unless you want to understand ASN.1 well-enough to write a book, or to deliver a course, on it! (We included winecoitems in Figure 22 to reduce the verbosity of the object identifier values in figure 23 later!) 

```txt
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
... ! PrintableString : "See wineco manual chapter 15"}
Figure 22 (part 1): Illustration of the use of basic ASN.1 types 
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
}
wineco-items OBJECT IDENTIFIER ::=
{ joint-iso-itu-t internationalRA(23) set(42) set-vendors(9)
wineco(43) stock-items (0)}
Figure 22 (part 2): Illustration of the use of basic ASN.1 types 
```

## 2 Discussion of the built-in types

## 2.1 The BOOLEAN type

(See "ran-out-of-stock" in figure 22). There is nothing to add here. A "BOOLEAN" type has the obvious two abstract values, true and false, but notice that the value-notation is the words "TRUE" or "FALSE" all in capital letters. You can regard the use of capitals as either consistent with the fact that (almost) all the built-in names in ASN.1 are all upper-case, or as inconsistent with the fact that ASN.1 requires that value-reference-names begin with a lower case letter! ASN.1 does not always obey its own rules! 

## 2.2 The INTEGER type

(See "number-of-days-reported-on" in figure 22). This example is a little more complicated than the simple use of "INTEGER" that we saw in Figure 13! The example here contains what are called distinguished values. In some early ASN.1 specifications (ENUMERATED was not added until around 1988) people would sometimes use the “INTEGER” type with a list of distinguished values where today they would use “ENUMERATED”. In fact, the syntax can look quite similar, so we can write the equivalent of the example in figure 13 as: 

<table><tr><td>The integer type</td></tr><tr><td>Just the word INTEGER, nice and simple!; and/or</td></tr><tr><td>Add a distinguished value list; and/or</td></tr><tr><td>Add a range specification (subtyping); then</td></tr><tr><td>Put an extension marker and exception specification in the range specification! (Getting complicated again!)</td></tr></table>

```txt
urgency INTEGER
{tomorrow (0),
    three-day (1),
    week (2)} DEFAULT week 
```

It is, however, important here to notice some important differences. The presence of the list following “INTEGER” is entirely optional (for “ENUMERATED” it is required), and the presence of the list does in no way affect the set of abstract values in the type. 

The following two definitions are almost equivalent: 

```txt
My-integer ::= INTEGER {tomorrow(0), three-day (1), week(2)} 
```

and 

```autohotkey
My-integer ::= INTEGER
tomorrow My-integer ::= 0
three-day My-integer ::= 1
week My-integer ::= 2 
```

The difference lies in ASN.1 scope rules. In the second example the names "tomorrow" etc are value-reference-names that can be assigned only once within the module, can be used anywhere within that module where an integer value is needed (even, in fact, as the number on an enumeration or in another distinguished value list or in a tag - but all these uses would be unusual!), and can appear in an EXPORTS statement at the head of the module. On the other hand, in the first example, the names "tomorrow" etc cannot be exported, can appear (with the same or different values) in other distinguished value lists, or indeed as value-reference names for a value of some totally different type. The name "tomorrow" in the first example has the meaning of identifying the zero value of “My-integer” ONLY when it appears in value notation that is governed by the type “My-integer”, such as when it is used as the “DEFAULT” value for a sequence element of that type. 

Notice also that although we have been using numbers in distinguished value lists in ascending order, there is no requirement for this - the order is irrelevant, and does not affect the resulting definitions. 

We have seen that a decimal number can be used as value-notation for a positive integer value. Negative values are, for example: 

```txt
minus-two INTEGER ::= -2 
```

but you are not allowed to write "-0", nor is any form of binary or hex notation valid as valuenotation for the “INTEGER” type. 

What are the set of abstract values for “INTEGER”? An early draft of the ASN.1 specification actually stated the maximum and minimum values of ASN.1 integers, based on restrictions imposed by BER encodings. However, a calculation showed that with a communications line running at a terabit a second, it would take approximately 100 million years to transmit the largest or smallest value! ASN.1 integers are "effectively unbounded". (And in the more recent PER encodings, there is no limit on the size of an integer value.) 

This raises the beginnings of a discussion that more properly belongs in a later chapter - do you really have to write your implementation code to handle arbitrarily large integers? If we look again at "no-of-days-reported-on" in Figure 13, we see the text "(1..56)" following the distinguished value list. (This can be present whether we have a distinguished value list or not). 

This is our first example of a subtype constraint - a notation that restricts the range of our integer, or subsets it. In this case it is saying that the only values a conforming sender is permitted to send are values in the range 1 to 56, and it is clear that an implementor need only allocate one byte for this field. A fuller discussion of subtype notation (for other types as well as for the integer type) appears later, but this simple restriction of the range of an integer is by far the most common use of this notation. Application designers are encouraged to place a range constraint such as this on “INTEGER” types whenever they can do so, and to explicitly state in comment if they expect implementors to truly handle arbitrarily large integers. However, as an implementor, if you see simply "INTEGER", with no range constraint and no clarifying text, it is usually a safe assumption that a four-octet integer value will be the largest you will receive. 

One final point: the similarity of the syntax for defining distinguished values to that for defining enumerations can be confusing. As the definition of distinguished values does not change in any way the set of abstract values in the type or the way they are encoded, there is never any "extensibility" question in moving to version 2 - if additional distinguished values are added, this is simply a notational convenience and does not affect the bits on the line. So the ellipsis extensibility marker (available for the list in the enumerated type), is neither needed nor allowed in the list of distinguished values (although it can appear in a range constraint, as we will see later). 

## 2.3 The ENUMERATED type

(See "urgency" in figure 13 and "reason-for-delay" in figure 22). There is little to add to our earlier discussions. The numbers in round brackets were required pre-1994, and are optional post-1994. The type consists precisely and only of values corresponding to each of the listed names. 

Numbers for encodings needed pre-1994, optional post-1994. 

The numbers were originally present to avoid extensibility problems - if version 2 added a new enumeration, it was important that this should not affect the values used (in encodings) to denote original enumerations, and the easiest way to ensure this was to let the application designer list the numbers to be used. Post-1994, extensibility is more explicit, and we might see: 

$$
\begin{array}{l} \text {Urgency - type : : = ENUMERATED} \\ \{\text {tomorrow}, \\ \text {three - day}, \\ \text {week}, \\ \dots , \\ \quad -- \text {Version 1 systems should assume any other value} \\ \quad -- \text {means "week".} \\ \text {month} \} \end{array}
$$

Here "month" was added in version 2, although the requirement placed on version 1 systems when version 1 was first specified actually means that such deployed systems will treat "month" as "week". This illustrates the importance of thinking hard about the exception handling you want from version 1 systems. If instead the version 1 spec had said "treat any unknown enumeration as tomorrow", then the effect of adding "month" in version 2 might have been less satisfying! Notice that in this case we chose to give the exception-handling behaviour in comment after the ellipsis, rather than using an exception specification - this is quite satisfactory, particularly if the exception handling is peculiar to this field. Selection of appropriate exception handling is discussed further in 2.6 of Chapter 7. 

Finally, if you want to be really weird, you can put numbers in for some enumerations and not for others. If you are lucky, the result will still be legal! Go and read the ASN.1 specification if you want to do daft things like that, this book will not help you! 

## 2.4 The REAL type

(See "min-stock-level" etc in Figure 22). The type-notation for the “REAL” type is given in Figure 22. This is the only option. 

```txt
Real
Two sets of abstract values, Base 10 and Base 2, distinct even if mathematically equal. The value notation is a comma-separated list of integers for the mantissa, the base (2 or 10), and the exponent. Also PLUS-INFINITY and MINUS-INFINITY. 
```

The value notation is slightly curious. Here are examples of some pieces of value notation for the real type: 

```autohotkey
v1 REAL ::= {mantissa 314159, base 10, exponent -5}
v2 REAL ::= {mantissa 3141590, base 10, exponent -6}
v3 REAL ::= {mantissa 1, base 2, exponent -1}
v4 REAL ::= {mantissa 5, base 10, exponent -1}
v5 REAL ::= 0
v6 REAL ::= {mantissa 0, base 2, exponent 100}
v7 REAL ::= {mantissa 0, base 10, exponent 100} 
```

Notice that apart from v5, these are all comma-separated lists of three numbers. (Commaseparated lists occur frequently in ASN.1 value notation and were chosen for type REAL because an ASN.1 tool may encounter the value notation when the governor is a type-reference name that has not yet been defined, and the tool needs a simple means of finding the end of the notation). The mathematical value being identified by {x, y, z} is (x times (y to the power z)), but y is allowed to take only the values 2 and 10. 

There are also explicitly included (and encoded specially) two values with the following value notation: 

```txt
PLUS-INFINITY
MINUS-INFINITY 
```

Again, all upper-case letters. When "REAL" was first introduced, there was discussion of adding additional special "values" such as "OVERFLOW", or even "PI" etc, but this never happened. 

That is really all you need to know, as the "REAL" type is infrequently used in actual application specifications. The rest of the discussion of the "REAL" type is a bit academic, and you can omit it without any “real” damage to your health! But if you want to know which of v1 to v7 represent the same abstract value and which different ones, read on! 

You might expect from the name that the abstract values are (mathematical) real numbers, but for those of a mathematical bent, only the rationals are included. 

Formally, the type contains two sets of abstract values, one set comprising all the numbers with a finite representation using base 10, and the other set comprising all the numbers with a finite representation base 2. (Notice that from a purely mathematical point of view, the latter values are a strict subset of the former, but the former contains values that are not in the latter set). In all ASN.1 encoding rules, there are binary encodings for "REAL", and there are also decimal encodings as specified in the ISO standard ISO 6093. This standard specifies a character string to represent the value, which is then encoded using ASCII. An example of these encodings is: 

## but ISO 6093 contains many options!

It is possible (post-1994) to restrict the set of abstract values in "REAL" to be only the base 10 or only the base 2 set, effectively giving the application designer control over whether the binary or the decimal encoding is to be used. Where the type is unrestricted, it is theoretically possible to put different application semantics on a base 10 value from that on the mathematically-equal base 2 value, but probably no-one would be daft enough! (Actually, "REAL" is not used much anyway in real protocols). 

But just to wrap this discussion up ... looking at the values v1 to v7 above, we can observe that the value-reference-names listed on the same line below are value notation for the same abstract value, and those on different lines are names for different abstract values: 

```csv
v1, v2
v3
v4
v5, v6
v7 
```

(V5 equals V6 because V5 is defined to represent the base2 value zero.) 

## 2.5 The BIT STRING type

(See "version" in figure 22). There are two main uses of the bitstring type. The first is that given for "version", where we have a list of named bits associated with the type. The second and simplest is the type-notation: 

<table><tr><td>BIT STRING is often used with named bits to support a bit-map for version negotiation.</td></tr></table>

## BIT STRING

Note that, as we would expect, this is all upper-case, but as we might not expect, the name of the type (effectively a type-reference-name) contains a space! The space is not merely permitted, it is required! Again ASN.1 breaks its own rules! 

We will return to figure 22 in a moment. Let us take the simpler case where there is no list of named bits. 

If a field of a sequence (say) is defined as simply "BIT STRING", then this can be a sign of an inadequately-specified protocol, as semantics need to be applied to any field in a protocol. "BIT STRING" with no further explanation is one of several ways in which "holes" can legally be left in ASN.1 specifications, but to the detriment of the specification as a whole. 

We will see later that where any "hole" is left, it is important to provide fields that will clearly identify the content of the hole in an instance of communication, and to either ensure that all communicating partners will understand all identifications (and the resulting contents of the hole), or will know what action to take on an unknown identifier. ASN.1 makes provision for such "holes" and the associated identification, and it is not a good idea to use "BIT STRING" to grow your own "holes" (but some people do)! 

So ... BIT STRING without named bits has a legitimate use to carry encodings produced by wellidentified algorithms, and in particular to carry encryptions for either concealment or signature purposes. But even in this case, there is usually a need to clearly identify the security algorithm to be 

<table><tr><td>BIT STRING without named bits is also frequently used as part or a more complex structure to carry encrypted information.</td></tr></table>

applied, and perhaps to indirectly reference specific keys that are in use. The BIT STRING data type is (legitimately) an important building block for those providing security enhancements to protocols, but further data is usually carried with it. 

The use of BIT STRING with named bits as for "version" in figure 13 is common. The names in curly brackets simply provide names for the bits of the bit-string and the associated bit-number. It is important to note that the presence of a named bit list (as with distinguished values for integers), does not affect the type. The list in no way constrains the possible length of the bit-string, nor do bits have to be named in order. 

ASN.1 talks about "the leading bit" as "bit zero", down to the "trailing bit". Encoding rules map the "leading bit" to the "trailing bit" of a bit-string type into octets when encoding. 

(BER - arbitrarily, it could have chosen the opposite rule - specifies that the leading bit be placed in the most significant bit of the first octet of the encoding, and so on.) 

How are these names of bits used? As usual, they can provide a handle for reference to specific bits by the human-readable text. They can also, however, be used in the value notation. 

The obvious (and simplest) value notation for a bitstring is to specify the value in binary, for example: 

## '101100110001'B

If the value is a multiple of four bits, it is also permissible to use hexadecimal: 

$$
^ \prime \mathrm{B31} ^ {\prime} \mathrm{H}
$$

(Note that in ASN.1 hexadecimal notation, only upper case letters are allowed.) 

If, however, there are named bits available, then an additional value notation is available which is a comma-separated list of bit-names within curly brackets (see, for example, the “DEFAULT” value of “version” in figure 22). The value being defined is one in which the bit for every listed bit-name is set to one, and all other bits are set to zero. 

The alert reader (I have done it again!) will spot that this statement is not sufficient to define a bitstring value, as it leaves undetermined how many (if any) trailing zero bits are present in the value. So the use of such a "value-notation" if the length of the bitstring is not constrained does not really define a value at all - it defines a set of values! All those with the same one bits, but zero to infinity trailing zero bits! 

The ASN.1 specifications post around 1986 get round this problem with some weasel words (slightly changed in different versions): "If a named bit list is present, trailing zero bits shall have no semantic significance"; augmented later by "encoding rules are free to add (or remove) trailing zero bits to (or from) values that are being encoded"! 

<table><tr><td>BIT STRING with named bits raises interesting issues about what is the precise set of abstract values of such a type:</td></tr><tr><td>IGNORE SUCH QUESTIONS, they don&#x27;t matter!</td></tr></table>

This issue is not a big one for normal BER, where it does not matter if there is doubt over whether some value exactly matches the "DEFAULT" value, but it matters rather more in the canonical encoding rules described later. 

The most common use for named bits is as a "version" map, as illustrated in figure 13. Here an implementation would be instructed to set the bits corresponding to the versions that it is capable of supporting, and - typically - there would be some reply message in which the receiver would set precisely one bit (one of those set in the original message), or would send some sort of rejection message. 

## Formal/advanced discussion

NOTE — Most readers should skip this next bit! Go on to OCTET STRING, that has fewer problems! If you insist on reading on, please read figure 999 again! 

There have been many different texts in the ASN.1 specifications over the last 15 years associated with “BIT STRING” definitions with named bits. Most have been constrained by the desire: 

a) not to really change what was being specified, or at least, not to break current deployed implementations; and 

b) not to add a large amount of text that would seem to imply a) above even if it didn't really do it! 

The result is that you as an alert and intelligent reader(!) may well be able to take issue with what follows, depending on the vintage of the specification that you are reading, and/or on whether people insist on calling you an "ASN.1 Expert"! 

The ASN.1 Standard seems to imply that the presence of a named bit list (and the extent of such a list) has no impact on the set of abstract values in the type being defined. However, abstract values are there to enable application designers to associate different application semantics with them, with the assurance that each value will have a distinct encoding, and with the equal assurance that for canonical encodings there will be precisely one encoding for each value. 

(Controversial remark follows!) The specification states that "application designers should ensure that different (application) semantics are not associated with ... values (of types with named bits) which differ only in the number of trailing zero bits". What this is actually saying is that such apparently distinct abstract values are actually a single abstract value. 

The only remaining issue is how such abstract bitstring values should be represented by encoding rules. The standard gives guidance: "encoding rules are free to add (or remove) arbitrarily many trailing zero bits to (or from) values that are being encoded or decoded". Perhaps not the best way of expressing it, but the principles are clear: 

when a named bit list is present, we have just one abstract value corresponding to different bit-patterns that differ only in the number of their trailing zero bits; 

• encoding rules are (of course!) free to represent this abstract value how they like, but one option is to encode any one of those bit-patterns that differ only in their trailing zero bits. 

For BER, which does not claim to provide a single encoding for each abstract value, the rules permit arbitrarily many trailing zero bits in the encoding. (The decision to allow this was necessary to avoid breaking existing implementations when this rather abstract(!) problem was first understood.) Existing BER implementations will frequently include trailing zero bits in the encoding of a value of a bitstring type with a named-bit list. 

For canonical encoding rules, however, including PER, a single encoding is necessary, and at first sight saying that such encoding rules never have trailing bits in the encoding looks like a good solution. 

But the choice of encoding (and indeed the selection of the precise abstract bitstring value - from the set of abstract values with the same semantics - that is to be used for encoding) is complicated if there are length constraints at the abstract level on the bitstring type. 

The matter is further complicated because in BER-related encoding rules, length constraints are "not visible" - do not affect the encoding! In PER, they may or may not be visible! 

The up-shot of all this is that in the canonical versions of BER trailing zero bits are never transmitted in an encoding, but the value delivered to the application is required to have sufficient zero bits added (the minimum necessary) to enable it to satisfy any length constraints that might have been applied. (Such constraints are assumed to be visible to the application and to the Application Program Interface -API- code, whether they are visible to - affect - the encoding rules or not.) 

PER, where (some) length constraints are PER-visible, changes this slightly: what is transmitted is always consistent with PER-visible constraints - so (the minimum number of) trailing zero bits are present in transfer if they are needed to satisfy a length constraint. The encoding can thus be delivered to the application unchanged, provided there are no not-PER-visible constraints applied, otherwise the canonical BER rules would apply - the application gets a value that is permitted by the constraints and carries the same application semantics as that derived directly from the transmitted encoding. 

And if you have read this far, I bet you wish you hadn't! It kind of all works, but it is not simple! 

Issues like this do not affect the normal application designer - just do the obvious things and it will all work, nor do they affect the normal implementor that obeys the well-known rules: encode the obvious encoding; be liberal in your decoding. 

These issues are, however, of importance to tool vendors that provide an option for "strict diagnostics" if incoming material is perceived to be erroneous. In such cases a very precise statement of what is "erroneous" is required! 

## 2.6 The OCTET STRING type

(See "bar-code-data" in figure 22). Once again, a space is needed between "OCTET" and "STRING"! And once again, an octetstring is a tempting candidate to "carry anything" - a delimited hole. (But don't be tempted!) Yet again, it is not appropriate unless supported by identification fields and exception handling. ASN.1 provides better 

The OCTET STRING type is simple - but don't use it! It usually represents a poorly-supported "hole", and it is better to use a pre-fabricated "hole" - see later! 

mechanisms to support "holes". 

In the case shown in figure 22, the precise contents of the octet string are (hopefully!) wellspecified in “chapter 29 of the wineco manual”. However, this specification is not very general. The intent is clearly to provide a container for additional identification information, using some encoding outside of ASN.1. In general, and over time, there may be a number of different encodings of various forms of identification that the designer may wish to carry in this octetstring, and again we see the need for additional identification fields saying "this is a bar-code version 1" - or something else, and "this is how it is encoded today", rather than hard-wiring these decisions into "chapter 29". Once again, we see we are discussing "holes". 

In summary (but see Figure 999 again!) it is probably a BAD THING to have OCTET STRING or BIT STRING (other than for version bit-maps) fields in application specifications unless you really know what you are doing and really want to "dig your own hole". But of course, perhaps you do! 

The value notation for OCTET STRING is always hexadecimal or binary as illustrated earlier for bitstring. If the result is not an integral multiple of eight bits, then zero bits are added at the end. 

## 2.7 The NULL type

(See "warehouse" in figure 13). Formally, NULL is a type that has just one value. The value-notation for this value is rather confusingly: 

For NULL, you know it all - a place-holder: no problems. 

## NULL

again, all upper-case, where one might expect an initial lower-case letter. 

The normal use is very much as in figure 13 - where we need a type to provide a TLV (whose presence or absence carries some semantics), but where there is no additional information to be carried with the type. NULL is often referred to as a "place-holder" in ASN.1 courses. 

## 2.8 Some character string types

(See "additional-information" in figure 22 and "name" (twice) in figure 13). In the examples so far, you have met "PrintableString" (present in the earliest ASN.1 drafts), "VisibleString" (deprecated synonym "ISO646String"), and "UTF8String" (added in 1998). There are several others. 

Despite not being all-upper-case, these (and the other character string type names) have been reserved words (names you may not use for your own types) since about 1988/90. The early designers of ASN.1 felt (rightly!) that the character string types and their names were a bit "ad hoc", and gave them a somewhat reduced status! 

Actually, in the earliest ASN.1 specification, there was the concept of "Useful Types", that is, types that were defined using the ASN.1 notation rather than pure human-language, and these all used mixed upper/lower-case. The character string types were originally included as "Useful types", and were defined as a tagged OCTET STRING. Today (since about 1990 when they became reserved words) they are regarded as fairly fundamental types with a status more-or-less equal to that of INTEGER or BOOLEAN. 

The set of characters in "PrintableString" values is "hard-wired" into ASN.1, and is roughly the old telex character set, plus lower-case letters. The BER encoding in the "V" part of the TLV is the ASCII encoding, so the reduced character set over "VisibleString" (following) is not really useful, although a number of application specifications do use "PrintableString". 

The set of characters in "VisibleString" values is simply the printing ASCII characters plus "space". The BER encoding in the "V" part of the TLV is, of course, ASCII. 

The set of characters in "UTF8String" is any character - from Egyptian hieroglyphs to things carved in wood in the deepest Amazon jungle to things that we will in due course find on Mars - that has been properly researched and documented (including the ASCII control characters). The BER (and PER if the type is not constrained to a reduced character set) encoding per character is variable length, and has the "nice" property that for ASCII characters the encoding per character is one octet, stretching to three octets for all characters researched and documented so far, and going to at most six octets per character once we have all the languages of the galaxy in there! Those who are "into" character set stuff may recognise the name "Unicode". UTF8 is an encoding scheme covering the whole of Unicode (and more) that is becoming (circa 1999) extremely popular for communication and storage of character information. Advice: If you are designing a new protocol, use UTF8String for your character string fields unless you have a very good reason not to do so. 

## 2.9 The OBJECT IDENTIFIER type

(See "item" and "wineco-items" in figure 22, and module identifiers in figure 21.) Values of the object identifier type have been used and introduced from the start of this book. But we are still going to postpone to a later chapter a detailed discussion of this type! 

OBJECT IDENTIFIER perhaps more used than any other basic ASN.1 type - you can get some name-space in lots of ways, but you don't really need it! 

The OBJECT IDENTIFIER type may well lay claim to being the most used of all the ASN.1 types (excluding the constructors SEQUENCE, SET, and CHOICE, of course). Wherever world-wide unambiguous identification is needed in an ASN.1- based specification, the object identifier type is used. 

Despite the apparent verbosity of the value-notation, the encoding of values of type object identifier is actually very compact (the human-readable names present in the value notation do not appear in the encoding). For the early components of an object identifier value, the mapping of names to integer values is "well-known", and for later components in any value-notation, the corresponding integer value is present (usually in round brackets). 

The basic name-space is a hierarchically allocated tree-structure, with global authorities responsible for allocation of top-level arcs, and progressively more local authorities responsible for the lower-level arcs. 

For you (as an application designer) to be able to allocate values from the object identifier name space, you merely need to "get hung" from this tree. It really doesn't matter where you are "hung" from (although encodings of your values will be shorter the nearer you are to the top, and international organizations tend to be sensitive about where they are "hung"!). 

For a standards-making group, or a private company, or even an individual, there are a range of mechanisms for getting some of this name-space, most of which require no administrative effort (you probably have an allocation already!). These mechanisms are described later, although such is the proliferation of branches of the OID tree (as it is often described) that it is hard to describe all the finer parts! 

It has been a criticism of ASN.1 that you need to get some OID space to be able to authoritatively write ASN.1 modules. This is actually not true - the module identifier is not required. However, most people producing ASN.1 modules do (successfully) try to get a piece of the OID space and do identify their modules with OID values. But if this provides you with problems, it is not a requirement. 

## 2.10 The ObjectDescriptor type

(See "item-description" in figure 22). The typenotation for the ObjectDescriptor type is: 

## ObjectDescriptor

without a space, and using mixed upper and lower case! This is largely a historical accident. This type was formally-defined as a tagged 

## ObjectDescriptor

Yes, mixed case! You will never see it in a specification, and you are unlikely to want to use it - ignore this text! 

"GraphicString" (another character string type capable of carrying most of the world's languages, but regarded as obsolete today). Because its definition was by an ASN.1 type-assignment statement, it was deemed originally to be merely a "Useful Type", and was given a mixed upper/lower-case name with no space. Today, the term "Useful Type" is not used in the ASN.1 specification, and the use of mixed case for this built-in type is a bit of an anachronism. 

The existence of the type stems from arguments over the form of the OBJECT IDENTIFIER type. There were those who (successfully) argued for an identification mechanism that produced short, numerical, identifiers when encoded on the line. There were others who argued (unsuccessfully) for an identification mechanism that was "human-friendly", and contained a lot of text (for example, something like a simple ASCII encoding of the value notation we have met earlier), and perhaps no numbers. As the debate developed, a sort of compromise was reached which involved the introduction of the "OBJECT IDENTIFIER" type - short, numerical, guaranteed to be worldwide unambiguous, but supplemented by an additional type "ObjectDescriptor" that provided an indefinitely long (but usually around 80 characters) string of characters plus space to "describe" an object. The "ObjectDescriptor" value is not in any way guaranteed to be world-wide unambiguous (the string is arbitrarily chosen by each designer wishing to describe an object), but because of the length of the string, usually it is unambiguous. 

There is a strong recommendation in the ASN.1 specification that whenever an object identifier value is allocated to identify an object, an object descriptor value should also be allocated to describe it. It is then left for application designers to include in their protocol (when referring to some object) either an "OBJECT IDENTIFIER" element only, or both an "OBJECT IDENTIFIER" and an "ObjectDescriptor", perhaps making the inclusion of the latter "OPTIONAL". 

In practice (apart from the artificial example of figure 22!) you will never encounter an "ObjectDescriptor" in an application specification! Designers have chosen not to use it. Moreover, the rule that whenever an object identifier value is allocated for some object, there should also be an object descriptor value assigned, is frequently broken. 

Take the most visible use of object identifier values - in the header of an ASN.1 module: what is the corresponding object descriptor value? It is not explicitly stated, but most people would say that the module name appearing immediately before the object identifier in the header forms the corresponding object descriptor. Well - OK! 

But there are other object identifier values originally assigned in the ASN.1 specification itself, such as: 

```txt
{iso standard 8571} 
```

This identifies the numbered standard (which is actually a multi-part standard), and also gives object identifier name-space to those responsible for that standard. There is, however, no corresponding object descriptor value assigned! 

## 2.11 The two ASN.1 date/time types

Yes, you did indeed interpret figure 22 correctly - UTCTime is a date/time type that carries only a twodigit year! 

You will also notice that both "UTCTime" and "GeneralizedTime" are again mixed upper/lower-

UTCTime and GeneralizedTime 

Simple in concept, easy to use, but not without their problems! 

case. Again this is a historical accident: they were defined using an ASN.1 type-assignment statement as a tagged "VisibleString", and were originally listed as "Useful Types". 

Why both? Was GeneralizedTime added later? Yes and no! In the early drafts in 1982, UTCTime was all that was present, and contained the specification of the character string to be used to represent dates and times "hard-wired" into the ASN.1 specification: that is to say, the complete text defining this type was present in the ASN.1 specification. 

GeneralizedTime was added before the first ASN.1 specification was published in 1984, but did not contain the full specification - it referred to what was then a new ISO Standard (ISO 8601). However, early users of ASN.1 were already finalising their texts based on use of UTCTime, and it was left in the ASN.1 specification. The fact that UTCTime only used a two digit year and GeneralizedTime a four-digit year was not even a subject of discussion in 1982! (The other difference between the two types was in the precision of the time - at best a precision of a second for UTCTime, more for GeneralizedTime). 

Slightly less forgivable was the Directory work, which was not published until 1988, but also used UTCTime! It is possible that the attraction of a "hard-wired" specification - you don't need to seek out another publication in order to see what you are getting - was an influence in encouraging designers to use UTCTime (rather than GeneralizedTime) during the 1980s. 

The comment in figure 22 about interpreting a UTCTime value as a "sliding window" is one of three varying recommendations often made for two-digit year fields: 

(DEFAULT in the past). Interpret as a year between 1900 and 1999 - the default setting, and certainly the intent in 1982, but a bad idea today! 

(SIMPLE proposal for now). Interpret as a year between 1950 and 2049 - simple, and it buys us another 50 years! 

• (SLIDING WINDOW - works forever!). Interpret any 2-digit year that matches the bottom two digits of the current year as the current year. Interpret all other values as years within a window from the current year minus fifty years to the current year plus 49 years (or minus 49 to plus 50 - a matter of choice - but it should be clearly defined). This means that on the 31 December each year, the interpretation of dates fifty years in the past changes to an interpretation as a date fifty years in the future. If there never are dates in your system that are fifty years in the past (and no need to refer to any that are more than forty-nine years in the future), this system clearly works, and allows two-digit years to be used indefinitely. A neat solution! 

What does "UTC" stand for? It comes from the CCIR (Consultative Committee on International Radio), and stands for "Co-ordinated Universal Time" (the curious order of the initials comes from the name in other languages). In fact, despite the different name, "GeneralizedTime" also records Co-ordinated Universal Time. What is this time standard? Basically, it is Greenwich Mean Time, but for strict accuracy, Greenwich Mean Time is based on the stars and there is a separate time standard based on an atomic clock in Paris. Co-ordinated Universal Time has individual "ticks" based on the atomic clock, but from time-to-time it inserts a "leap-second" at the end of a year (or at the end of June), or removes a second, to ensure that time on a global basis remains aligned with the earth's position round the sun. This is, however, unlikely to affect any ASN.1 protocol! 

What is the exact set of values of UTCTime? The values of the type are character strings of the following form: 

<table><tr><td>yymmddhhmmZ</td></tr><tr><td>yymmddhhmmssZ</td></tr><tr><td>yymmddhhmm+hhmm</td></tr><tr><td>yymmddhhmm-hhmm</td></tr><tr><td>yymmddhhmmss+hhmm</td></tr><tr><td>yymmddhhmmss-hhmm</td></tr></table>

"yymmdd" is year (00 to 99), month (01 to 12), day (01 to 31), and "hhmmss" is hours (00 to 23), minutes (00 to 59), seconds (00 to 59). 

The "Z" is a commonly-used suffix on time values to indicate "Greenwich Mean Time" (or UTC time), others being "A" for one hour ahead, "Y" for one hour behind, etc, but these are NOT used in ASN.1. 

If the "+hhmm" or "-hhmm" forms are used (called a time differential), then the first part of the value expresses local time, with UTC time obtained by subtracting the "hhmm" for "+hhmm", and adding it for "-hhmm". The ASN.1 specification contains the following example (another example, added in 1994 shows a "yy" of "01" representing 2001!): 

```txt
If local time is 7am on 2 January 1982 and co-ordinated universal time is 12 noon on 2 January 1982, the value of UTCTime is either of "8201021200Z" or "8201020700-0500". 
```

GeneralizedTime is the same overall format, but has a four-digit year, and allows "any of the precisions specified in ISO 8601". 

GeneralizedTime is not without its problems, however. ISO Standards undergo revision from time to time, and referencing them from within another specification can allow things to change under your feet! It became clear in the mid-1990s that many people had implemented GeneralizedTime assuming that the maximum available precision for seconds was three digits after the decimal point (a milli-second). On closer inspection of ISO 8601 (current version), it is clear that unlimited precision is permitted - there is no restriction on the number of digits after the decimal point. It was an uncompleted homework task for the author to try to find earlier versions (and in particular the version current in 1982!) of ISO 8601 to determine for how long an arbitrary precision had been permitted. Perhaps a reviewer will undertake the research? Otherwise it is left as another small exercise for the reader! 

Another issue arising with both UTCTime and GeneralizedTime relates to canonical encodings: should the different precisions be regarded as different encodings for the same abstract value (a given time) where trailing zeros are present ("8202021200Z" v "820202120000Z"), or as different abstract values (because precision is a part of the abstract information conveyed)? A similar question occurs with the time differential. It actually doesn't matter much which approach is taken, so long as those using canonical encoding rules know the answer. The current text says that the precision and time differential are different ways of encoding a time (a single abstract value), and that in canonical encoding rules, the time differential shall not be present (and the "Z" shall), and that there shall be no trailing zeros in the precision, so the example "8202022120000Z" is not legal in the canonical encoding rules. This is another area where arguments can continue over the precise set of abstract values of this type. 

## 3 Additional notational constructs

## 3.1 The selection-type notation

There is no example in figure 22! I have only seen "selection types" used in one application specification. They are not common! 

The SELECTION TYPE notation - you are unlikely ever to see this - forget it! 

The ASN.1 specification talks about "The selection type", but the heading in this clause is more accurate - 

this is a piece of notation more akin to "IMPORTS" than to a type definition: it references an existing definition. 

The selection-type notation takes the following form: 

```typescript
identifier-of-a-choice-alternative < Type-notation-for-a-CHOICE 
```

For example, given: 

```txt
Example-choice ::= CHOICE
{alt1 Type1,
alt2 Type2,
alt3 Type3} 
```

Then the following type-notation can be used wherever type-notation is required within the scope (module) in which "Example-choice" is available: 

```shell
alt1 < Example-choice
alt2 < Example-choice
alt3 < Example-choice 
```

This notation references the type defined as the named alternative of the identified choice type, and should be seen as another form of type-reference-name. Notice that if the selection-type notation is in a module different from that in which "Example-choice" was originally defined, any tagging or extensibility environment applied to the referenced type is that of the module containing the original definition of Example-choice, not that of the selection-type notation. 

Value notation for "a selection type" is just the value notation for the selected type. 

In other words, for the type-notation "alt3 < Example-choice", the value-notation is the valuenotation for "Type3". (The identifier "alt3" does not appear in the value-notation for the "selection type", nor are there any colons present.) 

## 3.2 The COMPONENTS OF notation

This is another example of a rarely-used piece of notation that references the inner part of a sequence or set. The only reason to use it is that you can avoid an extra TLV wrapper in BER! It is again not illustrated in figure 22! 

The COMPONENTS OF notation you won't often see this either, so forget this too! 

What follows is described in relation to "SEQUENCE", but applies equally to "SET". However, a "COMPONENTS OF" in a "SEQUENCE" must be followed by type-notation for a sequence-type (which remember may, and usually will, be a type-reference-name), and similarly for SET. 

Suppose we have a collection of elements (identifiers and type-notation) that we want to include in quite a few of the sequence types in our application specification. Clearly we do not want to write them out several times, for all the obvious reasons. We could, of course, define a type: 

```txt
Common-elements ::= SEQUENCE
{element1 Type1,
element2 Type2,
...
element23 Type23} 
```

and include that type as the first (or last) element of each of our "actual" sequences: 

```css
First-actual-sequence ::= SEQUENCE
{used-by-all Common-elements,
next-element Some-special-type,
next-again Special2,
etc The-last} 
```

We do the same for all the sequences we need these common elements in. That is fine. (And with PER it really is fine!) But with BER, if you recall the way BER works, we get an outer-level TLV for "First-actual-sequence", and in the "V" part a TLV for each of its elements, and in particular a TLV for the "used-by-all" element. Within the "V" part of that we get the TLVs for the elements of "Common-elements". But if we had copied - textually - the body of "Common-elements" into "First-actual-sequence", there would be no TLV for "Common-elements" - we would have saved (with BER) two or three - perhaps four! - octets! 

If we use "COMPONENTS OF", we can write: 

```css
First-actual-sequence ::= SEQUENCE
{
    COMPONENTS OF Common-elements,
    next-element Some-special-type,
    next-again Special2,
    etc The-last} 
```

The "COMPONENTS OF" notation provides for such copying without textually copying - it "unwraps" the sequence type it references. 

Note that there is no identifier on the "COMPONENTS OF element". This is not optional - the "identifier" must be omitted. The "COMPONENTS OF is not really an element of the SEQUENCE - it is a piece of notation that extracts or unwraps the elements. It is often referred to as "textual substitution", but that is not quite correct (alert reader!) because the tagging and extensibility environment for the extracted elements remains that of the module where they were originally defined. 

There is some complexity if automatic tagging is applied and COMPONENTS OF is used. The reader has two choices: just forget it and note that it all works (unless you are a hand-coding implementor, in which case see the next option!), or as a good exercise (none are formally set in this book!) go to the ASN.1 specification and work out the answer! 

## 3.3 SEQUENCE or SET?

The type-notation for SEQUENCE, SET, SEQUENCE OF and SET OF has been wellillustrated in earlier text and examples, together with the use of "DEFAULT" and "OPTIONAL". Remember that in BER (not CER/DER/PER), the default value is 

```txt
An application designer can generally choose to use SEQUENCE or SET more or less arbitrarily. Read this text then use SEQUENCE always! 
```

essentially advisory. An encoder is permitted to encode explicitly a default value, or to omit the corresponding TLV, entirely as an encoders option. 

We have already discussed briefly the differences between 

$$
\text { SEQUENCE } \{\dots \} \quad \text { and } \quad \text { SET } \{\dots \}
$$

from an encoding point of view in BER (the TLVs are in textual order for SEQUENCE, in an order chosen by the encoder for SET), and also from the more theoretical stand-point that "order is not semantically significant" in SET. 

The problem is that if we regard the abstract value as a collection of unordered information, and we want a single bit-pattern to represent that in an encoding, we have to invent some more-or-less arbitrary criteria to order the collection in order to form a single bit-pattern encoding! This can make for expensive (in CPU and perhaps also in memory terms) encoding rules. In the case of SET { .... }, if we want to remove encoders options, it is possible to use either textual order (not really a good idea) or tag order (tags are required to be distinct among the elements in a SET) to provide the ordering as a static decision. However, in the case of "SET OF", no-one has found a way of providing a single bit-pattern for a complete set-of value without doing a run-time sort of the encodings of each element! This can be expensive! 

We will return to this point when we discuss the canonical (CER) and distinguished (DER) encoding rules in Section III, but advice today (but see figure 999!) would be: Best to keep off "SET {", and avoid "SET OF" like the plague! 

One very small detail to mention here: the default tag provided for "SET {" and for "SET OF" is the same. It is different from that provided for "SEQUENCE {" and for "SEQUENCE OF", but these are also the same. This only matters if you are carefully applying tags within CHOICEs and SETs etc with the minimal application of tags. In this case you will have studied and be happy with later text on tagging, and will carefully check the ASN.1 specification to determine the © OS, 31 May 1999 95 default tag for all types! If you are a normal mortal, however, you will routinely apply tags to everything (pre-1994), or will use "AUTOMATIC TAGS" (post-1994), and the fact that the default tag for "SEQUENCE {" is the same as that for "SEQUENCE OF" will not worry you in either case! 

## 3.4 SEQUENCE, SET, and CHOICE (etc) value-notation

We have used the type notation for these constructions almost from the first page of this book, but now we need to look at their valuenotation. (Actually, you will never encounter this except in courses or an illustrative annex to the ASN.1 specification, but it reinforces the point that for any type you can define with ASN.1 there is a well-defined notation for all of its values.) 

```txt
SEQUENCE, SET, CHOICE, etc value-notation
You won't ever need to write it, and will only ever read it in courses and ASN.1 tutorials and silly books like this, but here it is. It is good to complete your education! 
```

To say it simply: value notation for "SET {" and "SEQUENCE {" is a pair of curly braces containing a comma-separated list. Each item in the list is the identifier for an element of the "SEQUENCE {" (taken in order) or "SET {" (in any order), followed by value-notation for a value of that element. Of course this rule is recursively applied if there are nested "SEQUENCE {" constructs. 

For "SET OF" and "SEQUENCE OF" we again get a pair of curly braces containing a commaseparated list, with each item being the value notation for a value of the type-notation following the "OF". 

```txt
todays-return Return-of-sales ::=
{version {version2},
no-of-days-reported-on 8,
time-and-date-of-report
two-digit-year:"9901022359Z",
reason-for-delay {network-failure},
-- additional-information not included
sales-data
{--Report-item 1:
{item {wineco-items special-tiop (112)},
item-description "Special Reserve Purchase Tio Pepe",
-- A newly-stocked item.
bar-code-data 'A0B98764934174CDF'H,
-- ran-out-of-stock is defaulted to FALSE.
min-stock-level {mantissa 2056, base 10, exponent -2},
max-stock-level {mantissa 100, base 10, exponent 0},
average-stock-level {mantissa 7025, base 10, exponent -2} },
--Report-item 2:
{item {wineco-items own-dry-sherry (19)},
bar-code-data 'A0B897632910DFE974'H,
ran-out-of-stock TRUE,
min-stock-level {mantissa 0, base 10, exponent 1},
max-stock-level {mantissa 105, base 10, exponent 0},
average-stock-level {mantissa 5032, base 10, exponent -2} }
--Only two report items in this illustration
}
Figure 23: A value for "return-of-sales" 
```

Finally, for "CHOICE", it is NOT what you might expect - no curly braces! Instead you get the identifier of one of the alternatives, then a colon (:), then value notation for a value of that alternative. There is no value notation for any occurrence of tags, nor for extensibility markers or exception specifications. The colon in choice values was not present pre-1994. 

This should be sufficient for the reader to work through figure 23, which is cast as "todays-return" a (random) value for the type "Return-of-sales" given in figure 22. 

## 4 What else is in X.680/ISO 8824-1?

This chapter has attempted to cover "Basic ASN.1" - the material present in the first of the four documents specifying the ASN.1 notation, and in common use in specifications today. There is, however, some additional material in this first of the ASN.1 documents that has been deferred to later chapters. For completeness of this chapter, this is briefly mentioned below. 

The additional areas are: 

Extensibility and version brackets: This is a big subject, touched on briefly already, and first introduced in 1994. (Exception specifications are a related subject, but don't appear in X.680 - they are in X.682 - and are also treated later.) 

• Tagging: Touched on briefly already. This was important in the past, but with the introduction of automatic tagging in 1994 is much less important now. 

The object identifier type: This was fully-covered in X.680/ISO 8824-1 pre-1998, but parts of the material are now split off into another Recommendation/Standard. Previous chapters of this book produced a lot of introductory material, but the discussion remains incomplete! 

Hole types: This term is used for the more formal ASN.1 terms EXTERNAL, EMBEDDED PDV, CHARACTER STRING, and "Open Types" (post-1994). And dare we mention ANY and ANY DEFINED BY (pre-1994)? If you have never heard of ANY or ANY DEFINED BY, that is a good thing. But you will have to be sullied by later text - sorry! 

The character string types: There are about a dozen different types for carrying strings of characters from various world-wide character sets. So far we have met PrintableString, VisibleString, GraphicString, and UTF8String, and discussed them briefly. There is a lot more to say! 

Sub-typing, or constrained types: This is a big area, with treatment split between X.680/ISO 8824-1 and X.682/ISO 8824-3. We have already seen an example of it with the range constraint "(1..56)" on "no-of-days-reported-on" in figure 22. This form is the one you will most commonly encounter or want to use, but there are many other powerful notations available if you have need of them. 

Macros: We have to end this chapter on an obscenity! Some reviewers said, "Don't dirty the book with this word!" But macros were very important (and valued) in ASN.1 up to the late 1980s, and will still be frequently encountered today. But I hope none of you will be driven to writing one! Sections I and II will not tell you much more about macros, but the historical material in Section IV discusses their introduction and development over the life of ASN.1. It is a fascinating story! 

Additionally, there are a number of new concepts and notations that appear in X.681/ISO 8824-2, X.682/ISO 8824-3, and X.683/ISO 8824-4 (published in 1994). These are: information object classes (including information object definition and information object sets), and parameterization. 

Where the above items have already been introduced (in this chapter or earlier), their detailed treatment is left to a chapter of Section II. Where they have not yet been discussed, a brief introduction appears in the following short chapter. 

# Chapter 5 Reference to more complex areas

# (Or: There is always more to learn!)

## Summary:

This chapter provides an introduction to concepts and notation that are treated more fully in Section II. Some of these features have been briefly mentioned already, but without a full treatment. This includes: 

• Object identifiers 

• Character string types 

• Subtyping 

• Tagging 

• Extensibility, exceptions, and version brackets 

Other topics that are introduced here for the first time are: 

• Hole types 

• Macros 

• Information object classes and objects and object sets 

• Other types of constraint 

• Parameterization 

• The ASN.1 semantic model 

An introduction is provided here for the reader who wishes to ignore Section II. As at mid-1998, there are no areas or concepts concerned with the ASN.1 notation that have not been at least introduced by the end of this chapter. 

The aim of the text in this chapter is: 

• to describe the concept and the problem that is being addressed; 

to illustrate where necessary key aspects of the notational support so that the presence of these features in a published protocol can be easily recognised; and 

• to summarise the additional text available in Section II. 

If further detail is needed on a particular topic (if something takes the reader's interest), then the appropriate chapter in Section II can be consulted. The Section II chapter provides "closure" on all items mentioned in this chapter unless otherwise stated. 

## 1 Object identifiers

The OBJECT IDENTIFIER type was briefly introduced in Chapter 4 (clause 2.9) of this section, where the broad purpose and use of this type was explained (with the type notation). Examples of its value notation have appeared throughout the text, although these have not completely illustrated all possible forms of this value notation. 

A more detailed discussion of the form of the 

OBJECT IDENTIFIERs have a simple type notation, and a value notation that has already been seen. The "Further Details" chapter tells you about the form of the name space and how to get some, and provides discussion of the value notation. 

object identifier tree (the name-space) is given in Section 2 (Further Details) Chapter 1, together with a full treatment of the possible forms of value notation. 

Earlier text has given enough for a normal understanding of this type and the ability to read existing specifications. It is only if you feel you need some object identifier name space and don't know how to go about getting some that the "Further Details" material will be useful. This material also contains some discussion about the (legal) object identifier value notation that omits all names and uses numbers only, and about the (contentious) value notation where different names are associated with components, depending on where the value is being published and/or the nature of lower arcs. 

## 2 Character string types

The names of types whose values are strings of characters from some particular character repertoire have appeared throughout the earlier text, and Chapter 4 Clause 2.8 of this section discussed in some detail the type notations: 

## PrintableString VisibleString ISO646String UTF8String

although the treatment introduced terms such as "Unicode" that may be unfamiliar to some readers. 

There has also been little treatment so far of the value notation for these types, nor has the precise set of characters in each repertoire been identified fully. 

There are many more character string types than you have met so far, and mechanisms for constructing custom types and types where the character repertoire is not defined until runtime. The value notation provides both a simple "quoted string" mechanism and a more complex mechanism to deal with "funny" characters. 

Section II (Further Details) Chapter 2 provides a full treatment of the value notation and provides references to the precise definitions of the character repertoires for all character string types. It describes the following additional character string types that you will encounter in published specifications (all the character string types are used in at least one published specification): 

```txt
NumericString
IA5String
TeletexString
T61String
VideotexString
GraphicString
GeneralString
UniversalString
BMPString
UTF8String 
```

The simplest value notation for the character string types is simply the actual characters enclosed in quotation marks (the ASCII character QUOTATION MARK, usually represented as two vertical lines in the upper quartile of the character glyph). For example: 

## "This is an example character string value"

The (alert - I hope we still have some!) reader will ask four questions: 

• How do I express characters appearing in character string values that are not in the character set repertoire used to publish the ASN.1 specification? (Publication of ASN.1 specifications as ASCII text is common). 

• How do I include the ASCII QUOTATION MARK character (") in a character string value? 

• Can I split long character string values across several lines in a published specification? 

• How do I precisely define the white-space characters and control characters in a character string value? 

These are topics addressed in the "Further Details" section. 

In summary: 

• A QUOTATION MARK character is included by the presence of adjacent quotation marks (a very common technique in programming languages). 

ASN.1 provides (by reference to character set standards), names for all the characters in the world (the names of these characters use only ASCII characters), and a value notation which allows the use of these names. 

• Cell references are also available for ISO 646 and for ISO 10646 to provide precise specification of the different forms of white-space and of control characters appearing in ASCII. 

An example of a more complex piece of character string value notation described in the "Further Details" section is: 

$$
\{\text { nul }, \{0, 0, 4, 2 9 \}, \text { cyrillicCapitalLetterIe }," A B C" \}
$$

go to "Further Details" if you want to know what that represents! 

The above provision is, however, not the end of the story. If UniversalString or BMPString or UTF8String are used, then ASN.1 has built-in names (again defined by reference to character set standards) for about 80 so-called "collections" of characters. Here are the names of some of these collections: 

```txt
BasicLatin
BasicGreek
Cyrillic
Katakana
IpaExtensions
MathematicalOperators
ControlPictures
Dingbats 
```

Formally, these collections are subsets (subtypes - see the next clause of this chapter) of the BMPString type, and it is possible to build custom character string types using combinations of these pre-defined types. 

Section II Chapter 2 provides full coverage of these features, but a more detailed discussion of the form and historical progression of character set standardization has been placed in Section IV (History and Applications). Readers interested in gaining a full understanding of this area may wish to read the relevant chapter in Section IV before reading the Section II chapter. 

Finally, ASN.1 also includes the type: 

## CHARACTER STRING

which can be included in a SEQUENCE or SET (for example) to denote a field that will contain a character string, but without (at this stage) determining either the character repertoire or the encoding. 

This is an incomplete specification or "hole", and is covered in Section II Chapter 7. If this character string type is used, both the repertoire and the encoding are determined by announcement (or if the OSI stack is in use, by negotiation) at run-time, but can be constrained by additional specification using "constraints" (see "Other types of constraint" below), either at primary specification time, or by "profiles" (additional specifications produced by some group that reduces options in a base standard). 

## 3 Subtyping

There has been little text on this subject so far. We have seen an example of: 

$$
\text { INTEGER } (1.. 5 6)
$$

to specify an integer type containing only a subset of the integer values - those in the range from 1 to 56 inclusive. This is called "simple subtyping" and was provided in the ASN.1 Specifications from about 

From simple subtyping through to relational constraints. ASN.1 provides powerful mechanisms for selecting a subset of the values of an ASN.1 type, and (in PER) for encoding that selected subset in a very efficient manner. 

1986 onwards. 

Simple subtyping enables a subset of the values of any ASN.1 type to be selected to define a new type, using a variety of quite powerful mechanisms. Note that an abstract syntax (the set of abstract values that can be communicated) for a "Full Class" protocol is normally defined as the set of values of a single ASN.1 type (see Chapter 1 clauses 2.1, 2.3 and 3, and Chapter 3 clause 4). If a "Basic Class" protocol is needed, then this can conveniently be defined as a subset of those values. The "simple subtyping" mechanisms described in Section II Chapter 3 contain enough power to enable such a specification to be formally provided using the ASN.1 notation. 

An example of a more complex form of subtyping would be: 

```txt
Basic-Ordering-Class ::= Wineco-Protocol
(WITH COMPONENTS
ordering (Basic-Order) PRESENT,
sales ABSENT }) 
```

Note that all subtyping (and application of constraints - see below) is done by syntax which is enclosed in round parentheses and follows some piece of type notation (frequently a type reference name). 

It is, however, possible to also view the notation: 

INTEGER (1..56) 

as putting a constraint on the integer field, and this gives rise to considerations of what is to be done if the constraint is violated in received material. (This should normally only occur if the sender has implemented a later version of the protocol where the constraint has been relaxed. This is covered in Chapter 5 of Section II (see below). 

A number of other forms of constraint have been introduced into ASN.1 in 1994 related to constraining what can fill in a "hole", or to relating the contents of that "hole" to the value of some other field. These other forms of constraint are covered in Section II Chapter 9. 

## 4 Tagging

Earlier text has dipped in and out of tagging, but has never given a full treatment. The TLV concept (which underlies tagging) was introduced in Chapter 1 Clause 5.2, and further text on ASN.1 tagging appeared in Chapter 2 Clause 2.7 and Chapter 3 Clause 3.2, where tagging was described entirely in relation to the TLV encoding philosophy, and the concepts of "implicit tagging" and "explicit tagging" were introduced. 

Up to 1994, getting your tags right was fundamental to writing a correct specification. Post-1994, AUTOMATIC TAGS in the module header enables them to be forgotten. So details are relegated to Section II. If you want to read and understand a specification (or even to implement one), you already know enough about the tag concept, but if you want to take control of your tags (as you had to pre-1994), you will need the Section II material 

```txt
[3] INTEGER
My-Useful-Type ::= [APPLICATION 4] SEQUENCE { .... }
[PRIVATE 4] INTEGER
[UNIVERSAL 25] GraphicString 
```

Section II Chapter 4: 

• Gives a full treatment of the different classes of tag. 

Provides an abstract model of types and values that makes the concepts of explicit and implicit tagging meaningful, even if encoding rules are being employed that are not TLVbased. 

• Discusses matters of style in the choice of tag-class used in a specification. 

• Gives the detailed rules on when tags on different elements of sets and sequences or alternatives of choices are required to be distinct. 

## 5 Extensibility, exceptions and version brackets

The first two terms - extensibility and exceptions - have been mentioned in several places already. 

Clause 2 of the Introduction defined "extensibility" as the means of providing interworking between deployed "version 1" systems and "version 2" systems that are designed and deployed many years later. 

You will recognise the use of extensibility provision by an ellipsis (three dots), of exception specification by the use of an exclamation mark (!), and of version brackets by the use of an adjacent pair of open square brackets with a matching adjacent pair of closing square brackets. 

```txt
If a very great provision is made for 
```

extensibility, then almost every element in an encoding has to be "wrapped up" with a length field and an identification, even when both parties (if they know the full specification) are perfectly aware that these are fixed values. In other words, we are forced into a "TLV" (see Chapter 1 clause 5.2) style of encoding. If, however, we restrict the places where a version 2 specification can add new material (and wrap up only the new version 2 material), we can produce a much more efficient encoding. This is provided by the Packed Encoding Rules (PER). 

The extension marker was briefly introduced in Chapter 3 clause 3.3, together with the exception specification that identifies actions that version 1 systems should take with any added material. 

Section 2 Chapter 5: 

• expands on the Chapter 3 text; 

• describes all the places where extension markers can be placed; 

• illustrates the exception specification; and 

• introduces and describes the concept of "version brackets" (see below). 

When extensibility provision was first introduced into ASN.1, every added sequence or set element was "wrapped up", but it later became apparent that this was not necessary - all that needed "wrapping up" was the totality of the material added in this place in the new version. Hence we have the concept of bracketing this material together with so-called "version brackets". This is 

```txt
SEQUENCE
{field1 TypeA,
    field2 TypeB,
    ... ! PrintableString : "See clause 59",
    -- The following is handled by old systems
    -- as specified in clause 59.
    [[ v2-field1 Type2A,
    v2-field2 Type2B ]],
    [[ v3-field1 Type3A,
    v3-field2 Type3B ]],
    ...
    -- The following is version 1 material.
    field3 TypeC} 
```

## Figure 24: Illustration of extensibility markers and version brackets

illustrated in figure 24, which is repeated and described more fully in Section II Chapter 5. 

Notice that it is not mandatory to include version brackets. If they are absent the effect is as if each element of the sequence had been added separately in a succession of versions. 

Note also that if there is no further version 1 material ("field3 TypeC" in Figure 24 is not present), then the final ellipsis is not required, and will frequently be omitted. 

## 6 Hole types

Chapter 2 Clause 2.1 introduced the concept of "holes": parts of a specification left undefined to allow other groups to "customise" the specification to their needs, or to provide a carrier mechanism for a wide variety of other types of material. 

You can leave a hole by using one of several ASN.1 types, but it may be better to use Information Object Classes instead! 

In general, specifiers can insert in their protocols any ASN.1 type and leave the semantics to be associated with values of that type undefined. This would constitute a "hole". Thus "holes" can in principle be provided using INTEGER or PrintableString! But usually when specifiers leave a "hole", they want the container to be capable of carrying an arbitrary bit-pattern. Thus using OCTET STRING or BIT STRING to form a "hole" would be more common. This is generally not recommended, as there are specific ASN.1 types that are introduced to clearly identify the presence of a hole, and in some cases to provide an associated identification field which will identify the material in the "hole". 

Provision for "hole"s has been progressively enriched during the life of ASN.1, and some of the early mechanisms are deprecated now. The following are the types normally regarded as "hole" types, and are described fully in Section II Chapter 7: 

## 7 Macros

ASN.1 contained (from 1984 to 1994) a very complex piece of syntax called "the macro notation". It was removed in 1994, with equivalent (but much improved) facilities provided by the "Information Object Class" and related concepts (see below). 

Many languages, graphics packages, and word processors, have a macro facility. The name "macro" is very respectable. However, the use of this term in ASN.1 bears very little relationship to its use in these other packages. 

There is much controversy surrounding macros. They were part of ASN.1 for its first decade, but produced many problems, and were replaced by Information Object Classes in 1994. You will not often see text defining a macro (and should certainly not write any today), but you may still see in older specifications text whose form depends on a macro definition imported into a module. 

```txt
MY-MACRO MACRO ::=
BEGIN
TYPE NOTATION ::= ....
.....
VALUE NOTATION ::= ....
.....
END 
```

## Figure 25: The structure of a macro definition

Section IV ("History") says a little more about what macros are all about. You are unlikely to meet the definition of a macro (use of the macro notation) in specifications that you read, but figure 25 illustrates the general structure (the four dots representing further text whose form is defined by the macro notation specification). This piece of syntax can appear anywhere in a module where a type reference assignment can occur, and the name of the macro (conventionally always in upper case) can be (and usually is) exported from the module for use in other modules. 

The macro notation is the only part of ASN.1 that is not covered fully in this book! Readers of this book should NEVER write macros! However, you will encounter modules which import a macro name and then have syntax that is an invocation of that macro. Again, a macro invocation can appear anywhere that a type definition can appear. 

One standard that contains a lot of "holes" is called "Remote Operations Service Element (ROSE)". ROSE defines (and exports) a macro called the OPERATION macro to enable its users to provide sets of information to complete the ROSE protocol. A typical piece of syntax that uses the OPERATION macro would look like Figure 26 (but most real examples are much longer). 

```txt
lookup OPERATION
    ARGUMENT IA5String
    RESULT OCTET STRING
    ERRORS {invalidName, nameNotFound}
    ::= 1

Figure 26: An example of use of the ROSE OPERATION macro ©OSS.31 May 1999 
```

To fully understand this you need some knowledge or ROSE. ROSE is briefly described in Section II Chapter 7, partly because of its wide-spread use, but mainly because it provides good illustrations of macro use, Information Object Class specification, and exception handling. 

The OPERATION macro definition was replaced in the 1994 ROSE specification by specification of an OPERATOR Information Object Class, and specifications including syntax like figure 26 are gradually being changed make us of the OPERATOR Information Object Class instead. 

## 8 Information object classes and objects and object sets

When protocol specifiers leave "holes" in their specification, there are frequently several such holes, and the users of the specification need to provide information of a specified nature to fill in these holes. Most of the uses of the macro notation were to enable these users to have a notation to specify this additional information. 

Information Object Classes (with objects and object sets) was the main addition to the ASN.1 notation in 1994, replacing macros with a much enhanced functionality. Detail in these areas are left to Section II, but an increasing number of old specifications are being revised to use this notation, and most new specifications use it. These areas are important! 

The Information Object Class concept recognises that specifiers leaving "holes" need to clearly identify where these holes are, but more particularly to be able to list the information required to complete the "hole". In the simplest case, the information needed will be a set of ASN.1 types (with their associated semantics) that can fill the hole, together with either an integer or an object identifier value which is associated with that type and its semantics. The identifier will be carried in the carrier protocol, as well as a value of the type. 

ASN.1 provides a syntax for defining the form of information to be collected. This is illustrated in figure 27: 

```txt
MY-CLASS ::= CLASS
    {&Type-to-fill-hole,
    &identifier INTEGER}
Figure 27: Notation to define an Information Object Class 
```

Note the use of the "&" character. This is the only place that "&" is used in ASN.1, and its presence is a clear indication that you need to read the Section II material on Information Object Classes! 

<table><tr><td>Table constraints, relational constraints- the way to constrain holes in amanner consistent with the definition ofan Information Object Set. Go toSection II.</td></tr><tr><td>User-defined constraints - a catch-allfor any other constraint that you need!</td></tr></table>

Once a specifier has defined an Information Object Class (and typically exported the reference name), users can then define sets of objects of that class, and link them into the base protocol. This is amplified and illustrated in Section II. 

## 9 Other types of constraints

There are forms of constraint that are a little more complex than the simple subtyping discussed earlier. They are called "table constraints", "relational constraints", and "user-defined" constraints. The first two are closely related to the use of a defined set of information objects to fill in holes in a consistent manner. The latter relates to specification of hole contents which can not be done in a wholly formal manner within the ASN.1 notation. Like simple subtyping, these constraints always appear in round brackets following a type name (or a hole specification). They are illustrated and described in Section II 

## 10 Parameterization

The ability to parameterize an ASN.1 specification is a very simple but extremely powerful mechanism. It was introduced in 1994. The concept of dummy parameters of functions or methods in a programming language is quite 

Parameterization - very simple but very powerful. All ASN.1 reference names can have a dummy parameter list, actual parameters are supplied when they are used. 

common, with actual parameters being supplied when the function or method is invoked. 

In a similar way, an ASN.1 type-reference name can be given dummy parameters, with actual parameters being supplied when that type is used. 

For example: 

$$
\begin{array}{l} \text {My - Type} \left\{\text {INTEGER:dummy1, Dummy2} \right\}: := \\ \text {SEQUENCE} \\ \left\{\text {first - field Dummy2,} \right. \\ \text {second - field INTEGER (1..dummy1)} \end{array}
$$

Here "My-Type" has two dummy parameters, the first an integer used to provide a bound on "second-field", and a second that provides the type for the first field. Typically, My-Type will be used in several different places in the total specification, with different actual parameters in each case. 

Parameterization is an important tool to enable the linking of Information Object Sets defined by user groups into the holes left by the original specifier, although its use is wider than this. 

## 12 The ASN.1 semantic model

There are many places in ASN.1 where the phrase "must be of the same type as" appears. For example, if a dummy parameter is the value of some type, then the actual parameter "must be of the same type as the dummy parameter". A value following DEFAULT "must be of the same type as the type preceding the word DEFAULT". It is clear that if the types in question are the same type-reference name, then they "are the same type". But suppose 

Abstractions, abstractions, models, models. Everybody has their own. 

But sometimes they need to be explicit in order to express clearly what is legal and what is not. 

the two types in question are specified with textually distinct but identical text? Or textually distinct but with some minor variations in the text? Are they still "the same type"? What "minor variations" might be permitted? ASN.1 text up to 1999 had little to say to clarify these questions! Fortunately, difficult cases rarely appear in real specifications, but writers of ASN.1 tools do need to know what is legal and what is not (or to make assumptions themselves)! 

An attempt was made in 1990 to remove all such phrases and provide more rigour in these areas, but it proved impossible to get satisfactory text agreed in time, and at the last minute text for the 1994 specification reverted back to the original "must be of the same type". 

Work in this area, however, continued. It was recognised that to solve the problem there needed to be a well-defined "abstract model" or "mental model" or "semantic model" (the latter term was eventually chosen) to define the underlying abstractions that were represented by a piece of ASN.1 text, with the starting point being the concept of a type as a container of a set of abstract values as first described in Chapter 1 Clause 3.1. 

At the time of writing (early 1999), the work is complete and agreed, and publication is expected later in 1999. 

## 13 Conclusion

This completes the discussion of the ASN.1 notation for Section I "ASN.1 Overview" (the remaining chapters discuss ASN.1 tools and management and design issues). If more detail is needed on any of the topics that have not been fully described in this section, then the appropriate chapter of Section II should be consulted. These are largely independent, and can be taken in any order. 

For more details about Encoding Rules, see Section III, and for a history of the development of ASN.1 and some of its applications, see Section IV. 

# Chapter 6 Using an ASN.1 compiler

## (Or: What it is all about - producing the bits on the line!)

## Summary:

This chapter: 

• describes approaches to implementation of ASN.1-defined protocols, 

• briefly describes what needs to be done if an ASN.1 compiler is not available, 

• describes in detail the concept and operation of an ASN.1 compiler, 

illustrates the implementation process (when using an ASN.1 compiler), with examples of programming language structures produced by the "OSS ASN.1 Tools" product, 

• discusses what to look for when seeking a "best buy" in an ASN.1 compiler. 

This chapter talks about implementation architectures, strategy, and so on. It is therefore inevitably incomplete and partial. The issues it discusses are not standardised, and different implementors will produce different approaches. It is also the case that what is "best" on one platform may well not be "best" on a different platform. 

This chapter gives an insight into the implementation of protocols specified using ASN.1, but much of the detail depends on knowledge of programming languages such as C and Java, and knowledge of BER encodings that are covered in Section III. Nonetheless, those without such knowledge can still gain useful information from this chapter. But if you are not a programmer, read the next clause then skip the rest completely! 

## 1 The route to an implementation

We discussed in Chapter 1 clause 5.6 (and illustrated Its all so simple with a compiler! it in figure 12) the implementation process using an ASN.1 compiler. Before reading this chapter, you 

may wish to review that material. You simply "compile" your ASN.1 into a programming language of your choice, include the compiler output with application code that deals with the semantics of the application, (really) compile and link. Your own code reads/writes language datastructures, and you call ENCODE/DECODE run-time routines provided by the ASN.1 compiler vendor when necessary (and provide an interface to your lower layer APIs.) 

## 2 What is an ASN.1 compiler?

We all know what "a compiler" normally means - a programme that reads in the text of a programme written in a high-level language and turns it into instructions that can be loaded into computer memory and obeyed by some particular computer hard-ware, usually involving a further linkingloader stage to incorporate run-time libraries. 

<table><tr><td>What does it mean to &quot;compile&quot; a datastructure definition?</td></tr></table>

But ASN.1 is not a programming language. It is a language for defining data structures, so how can you "compile" ASN.1? 

The term compiler is a little bit of a misnomer, but was first used to distinguish very advanced tools supporting the implementation of ASN.1-defined protocols from early tools that provided little more than a syntax-checking and pretty-print capability. In the rest of this chapter, we will use the term "ASN.1-compiler-tool", rather than "compiler". 

There are several ways of implementing a protocol defined using ASN.1. The three main options are discussed below. 

Write all necessary code to encode and decode values in an ad hoc way. This is only suitable for the very simplest ASN.1 specifications, and leaves you with the full responsibility for debugging your encoding code, and for ensuring that you have the ability to handle all options on decoding. (The same statement would apply to character-based protocols defined using BNF, where there are some tools to help you, but they do not provide anything like as much support as an ASN.1-compiler-tool with an ASN.1-based specification). We will not discuss this option further. 

• Use a pre-built and pre-tested set of general-purpose library routines with invocations such as: 

$$
\text { encode\_untagged\_int   (int\_val,   output\_buffer) };
$$

However, the above is just about the simplest invocation you will get. In most cases you will also want to provide an implicit or explicit tag (of one of three possible classes), and for constructed types such as SEQUENCE, support in this way can become quite complex. This approach also only really works well with BER, where constraints are irrelevant and there is a relatively rigid encoding of tags and lengths. This approach pre-dated the development of ASN.1-compiler-tools, and is discussed a little further later. 

Use an ASN.1-compiler-tool that lets you put values into a programming language datastructure corresponding to your ASN.1 type (and generated by the ASN.1-compiler-tool automatically from your ASN.1 type) and then make a single invocation of "encode" when you have all your values in place, to produce a complete encoding of the value of that type. This provides the simplest implementation, with the least constraints on the structure of the application code, and is the approach discussed most in this chapter. It works equally well for PER, DER and CER as it does for BER, and makes maximum use of tested and debugged code for all aspects of encoding. 

However, remember that we usually have to decode as well as to encode. In the case of the third option (use of an ASN.1-compiler-tool), decoding is no more difficult than encoding. Run-time routines provided by the ASN.1-compiler-tool will take an encoding of the value of an ASN.1 type and set all the fields of the programming language data-structure corresponding to that type. 

With the middle option, encoding is basically a series of invocations of appropriate library routines, but for decoding there is the further problem of parsing the received bit-string into a treestructure of primitive values, and then tree-walking this parse tree to find the primitive values. Again, this is more easily possible with BER than with PER, because with BER the parse tree can be constructed without knowledge of the type of the value being decoded. 

The use of a library of encode routines and of a parse tree are discussed further below (briefly), but the chapter concentrates mainly on the use of an ASN.1-compiler-tool, as this provides a simple approach to implementation of ASN.1-based specifications, with effectively a 100% guarantee (assuming the ASN.1-compiler-tool is bug-free!) that: 

• Only correct encodings of values will be produced. 

• No correct encoding will "blow" the decoder, values being correctly extracted from all possible correct encodings. 

As an illustration of what ASN.1-compiler-tools produce, we will use a part of our wineco specification, that for "Return-of-sales", which references "Report-item". These were first shown in Figure 22 (part 2) in Chapter 4 of this section, and are repeated here without the comments. The C and Java structures and classes produced by the "OSS ASN.1 Tools" product (a good example of an ASN.1-compiler-tool product) are given in Appendices 3 and 4, and those familiar with C and Java may wish to compare these structures and classes with figure 28. (The "OSS ASN.1 Tools" product also provides mappings to C++, but we do not illustrate that in this book – it is too big already!) 

```txt
Return-of-sales ::= SEQUENCE
{version BIT STRING
{version1 (0), version2 (1)} DEFAULT {version1},
no-of-days-reported-on INTEGER
{week(7), month (28), maximum (56)} (1..56)
DEFAULT week,
time-and-date-of-report CHOICE
{two-digit-year UTCTime,
four-digit-year GeneralizedTime},
reason-for-delay ENUMERATED
{computer-failure, network-failure, other} OPTIONAL,
additional-information
SEQUENCE OF PrintableString OPTIONAL,
sales-data SET OF Report-item,
... ! PrintableString : "See wineco manual chapter 15" }
Report-item ::= SEQUENCE
{item OBJECT IDENTIFIER,
item-description ObjectDescriptor OPTIONAL,
bar-code-data OCTET STRING,
ran-out-of-stock BOOLEAN DEFAULT FALSE,
min-stock-level REAL,
max-stock-level REAL,
average-stock-level REAL}
Figure 28 - An example to be implemented 
```

## 3 The overall features of an ASN.1-compiler-tool

An ASN.1-compiler-tool is composed of a "compiler", application-independent programming language text to be included with your implementation (for C, this is .H and .C files), and libraries to be linked into your final executable. For some platforms, the compiler may also emit text which has to be compiled to produce a DLL which will be used at run-time. 

<table><tr><td>This does it all. Take your ASN.1 type. &quot;Compile&quot; it into a language data-structure. Populate it with values. Call ENCODE. Done! Decoding is just as easy.</td></tr></table>

The overall pattern is that the "compiler" phase takes in ASN.1 modules, and produces two main outputs. These are: 

Data-structure definitions (for the language you have chosen) that correspond to the ASN.1 type. 

Source text (for the language you have chosen) which will eventually produce either tables or code which the run-time routines in the supplied libraries can use to perform encode/decode operations, given only pointers to this information and to the in-core representation of the values to be encoded (and a handle for the buffer to encode into). This text includes all details of tagging in your ASN.1 types, so you never need to worry about tags in your implementation code. 

For some platforms, the situation can be just a bit more complex. The compiler may output text which you must compile to produce a DLL for use by your application. 

The next section looks at the use of a simple library of encode/decode routines, and then we look at the output from the "compiler" part of the "OSS ASN.1 Tools" compiler and the use of that tool. 

## 4 Use of a simple library of encode/decode routines

The earliest support for ASN.1 implementations (after simple syntax checkers and "pretty print" programs had been produced) was a library of routines that helped in the generation of BER tag (identifier) fields, BER length fields, and the encoding of BER primitive types. 

A library of encode/decode routines (one for each ASN.1 type) is better than nothing. But complications arise in the handling of nested SEQUENCE types etc, particularly in relation to length fields. 

Some implementations today still use this approach. It is better than doing everything from scratch! 

The approach is described in terms of a BER encoding. For a PER encoding it tends to work rather less well, and the ASN.1-compiler-tool approach would be more appropriate here. 

## 4.1 Encoding

Encoding of untagged primitive items is trivial - but add tagging and add constructed types with nesting of SEQUENCE OF within SEQUENCE within another SEQUENCE OF (etc), and .... well, life is not quite so simple if all you have available is a library that just does identifier and length encodings for you (and encodings of primitive values). 

Encoding using a library of routines can get messy, because you often need to know the length of an encoding before you encode it! 

Before the emergence of ASN.1-compiler-tools, a common approach to encoding a sequence such as "Report-item" (see Figure 28) would be to have code looking something like Figure 29 (using pseudo-code). 

```txt
Get value for "item" into x1
encode-oid (x1, buffer_x[1])
Get value for "item-description" into x2
encode_obje_desc (x2, buffer_x[2])
Get "bar-code-data" into x3
encode_octet_str (x3, buffer_x[3])
Get "ran-out-stock" value into x4
IF x4 is true THEN
    encode_boolean (true, buffer_x[4])
ELSE
    Set buffer_x[4] to an empty string
END IF
...
etc, encoding the last item into buffer_x[7] say.
...
encode-sequence (buffer_x, 1, 7, buffer_y)
-- This encodes the contents of buffer_x from 1 to 7
-- into buffer_y with a "SEQUENCE" wrapper.
-- Note that in practice the SEQUENCE may be tagged
-- resulting in a more complicated calling sequence
Pass buffer_y to lower layers for transmission.
Clear buffer_x, buffer_y

Figure 29 - Pseucode to encode "Report-item" 
```

Here we assume we have routines available in a library we have purchased that will take a value of any given ASN.1 primitive type (using some datatype in the language capable of supporting that primitive type) and returning an encoding in a buffer. Finally, we call another library routine that will put all the buffers together (note the copying that is involved here) and will generate the "T" and the "L" for a SEQUENCE (assuming we are using BER), returning the final coding in buffer_y. 

Clearly, if we have more complex nested structures in our ASN.1, this can become quite messy unless we are using a programming language that allows full recursion. We have effectively hardwired the ASN.1 structure into the structure of our code, making possible changes to version 2 of the protocol more difficult. 

There are some things that can be done to eliminate some of the copying. Part of the problem is that we cannot generate the BER octets for the length octets of a SEQUENCE until we have encoded all the elements of that sequence and counted the length of that encoding. 

For encoding a SEQUENCE there are (at least!) four ways to reduce/eliminate this problem of having to copy encodings from one buffer to another. These are: 

Do a "trial encoding" which just does enough to determine the length of each element of the sequence (this really needs to be a recursive call if our structure involves many levels of SEQUENCE or SEQUENCE OF), then generate the SEQUENCE header into the final buffer, then encode each of the SEQUENCE elements into that buffer. 

• Use the indefinite length form, in which case we can generate the sequence header into our final buffer and then encode into that buffer each of the elements of the sequence, with a pair of zeros at the end. 

• Use the "trick" of allocating space for a long-form length encoding which is a length of length equal to 2, followed by two blank octets that we will fill in later once the length is known, and then encode each element into the same final buffer. 

• Use (assuming it is available!) a "gather" capability in the interface to lower layer software which enables you to pass a chain of buffers to that software, rather than a single contiguous piece of memory. 

These approaches have been shown to work well for BER, but for CER/DER/PER, they can be either not possible (CER/DER demands minimum octets for length encoding) or more difficult/complex. 

## 4.2 Decoding

Decoding using library routines is not quite so easy. You need a general-purpose parser - relatively easy for BER (less easy for PER), tree-walking code, and then the basic decode routines for primitive types. This rather parallels what you have to do with character-based encodings - but with character-based encodings you need a quite sophisticated tool to split the incoming character string (based on input of the 

For decoding you need a generalpurpose parser, then you tree-walk. The library approach is easier with BER than with PER as the TLV structure is independent of the datatype. 

BNF) into a tree-structure of "leaf" components for processing. Producing a parse tree of BER is rather easier. 

In general, use of a simple library of encode-decode routines with ASN.1 is neither complex nor more simple than use of parsers for character-based protocols defined using BNF, although it is arguable that the original ASN.1 definition is more readable to a "layman" than a BNF description of a character-based protocol. 

It is also the case that parsing an incoming BER encoding into a tree-structure (where each leaf is a primitive type) is a great deal easier than producing a syntax tree from a character-based encoding defined using BNF. 

Decode implementations for BER can take advantage of the use of bit 6 of the identifier octets to identify whether the following "V" part is constructed, enabling application-independent code to produce a tree-structure with primitive types at the leaves. That tree-structure is then "walked" by the application-specific code to determine the values that have been received. 

This "library of useful routines" approach is certainly better than doing everything from scratch! But things are so much simpler with an ASN.1-compiler-tool as described below. 

## 5 Using an ASN.1-compiler-tool

## 5.1 Basic considerations

An ASN.1-compiler-tool makes everything much more of a one-step process (for the user of the tool). All the decisions on how to encode (copying buffers, doing trial encodings, using indefinite length, using long-form definite length with a length of two) are buried in the run-time support of the ASN.1-compiler-tool, as are the mechanisms for parsing an incoming encoding into components that can then be placed into memory in a 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/9618460df4096b78044f561048c2fe35916b905f1069a78938e5986454bc2a57.jpg)


form which matches a programming-language data-structure. 

ASN.1-compiler-tools are specific to a given platform (meaning hardware, operating system, programming language, and perhaps even development environment) and you will need to find one that is available for the platform that you are using. If you are using C, C++, or Java, on commonly used hardware and operating systems you will have no problem, but if you are locked into some rather archaic language (sorry if I sound rude!), life may be more difficult. 

A particular product may support several of these languages in one software package, using "compiler directives", or you may have to pay for several versions of a product if you want support for multiple platforms (C and Java, say). In some cases "cross-compilation" (which some ASN.1-compiler-tools support) can provide implementation support on older platforms. Basically, you need to "filter" available tools according to whether they can support directly or through crosscompilation the platform you want/need to use, then choose the "best" (see later section in this chapter). 

"Want/need" is important here. Sometimes the implementation platform is fixed and almost impossible to change for either historical reasons or for reasons of company policy, but more often, there are costs associated with the use of different platforms (procurement of hardware which is not "in-company", training costs of programmers, etc etc) which must be balanced against the "quality" (and cost) of available tools for these platforms. 

## 5.2 What do tool designers have to decide?

There are three very critical decisions in the design of a good ASN.1-compiler-tool - how to map ASN.1 data-structures to programming-language datastructures, how to make CPU/memory trade-offs in the overall run-time support, and how to handle memory allocation and buffer management during encode/decode operations. But other important 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/f19f6c3bf8d6ef1b46d1d516810ba7b70471713b61e2fb652cc75c5960f52347.jpg)


decisions are how much user control, options, and flexibility to provide in these areas. All of these factors contribute to the "quality" of any particular tool. 

The designers of the ASN.1-compiler-tool will have made some important decisions. We will see later that the quality of these decisions very much affects the quality of the ASN.1-compiler-tool (and the ease and flexibility with which you can use it to help you to produce protocol implementations). 

The most important areas they have had to address (and which affect the quality of the resulting ASN.1-compiler-tool) are: 

• How to map ASN.1 into programming-language data-structures? 

• What are the right trade-offs between run-time encoding/decoding speed and memory requirements? 

• How to handle memory allocation when performing encode and decode operations? 

• How much user control should be provided (and how - global directives or local control) on the behaviour of the tool for mappings and for run-time operation? 

None of these decisions are easy, but the best tools will provide some degree of user control in all these areas, through the use of "compiler directives", ideally both in terms of global default settings as well as specific local over-rides. (For example, for two-octet, four-octet, or truly indefinite-length integers). 

## 5.3 The mapping to a programming-language data structure

The designers of the ASN.1-compiler-tool will have determined a mapping from any arbitrarily complicated set of ASN.1 types into a related (and similarly complicated) set of datatypes in your chosen language. And they will have written a program (this is the bit that is usually called the "compiler") which will take in the text of an ASN.1 module (or several modules linked by EXPORTS and IMPORTS) and will process the module(s) to generate as output the mapping of the types in those modules into the chosen target language. 

This is perhaps the most important design decision. It is often called "defining the API for ASN.1", and in the case of C++ there is an X-Open standard for this. Get that wrong, and there will be some abstract values of the ASN.1 type that cannot be represented by values of the programminglanguage data-structure. Or perhaps the programming-language data-structure generated will just produce programminglanguage-compiler error messages when you try to use it! 

How does that help you? Well, your pseudo-code for encoding "Report- item" now looks more like figure 30. 

```txt
Get value for "item" into Report-item.item
Get value for "item-description" into
Report-item.item-description
Get "bar-code-data" into Report-item.bar-code-data
Get "ran-out-of-stock" value into
Report-item.ran-out-of-stock
...
etc, setting all the fields of Report-item
...
Call Encode (CompilerInfo, Report-item, Buffer)
Pass Buffer to lower layers for transmission
Clear Buffer 
```


Figue 30 - Pseudo-code to encode using an ASN.1-compiler-tool


Note that however complicated a nested structure of types or repetitions of SEQUENCE OF there are, there is just one call of "Encode" at the end to encode your complete message from the values you have set in your programming language data-structure. 

For incoming messages, the process is reversed. Your own code does no parsing, and no treewalking. It merely accesses the fields of the programming-language data-structure that the "compiler" part of the tool generated for you. 

"CompilerInfo" in the call of "Encode" is information passed from the "compiler" part of the tool to the run-time routines. This passes (inter alia) the tagging to be applied for BER. Although largely invisible to you (you do not need to understand the form of this information), it is absolutely essential to enable the run-time routines to provide their encode/decode functions. 

## 5.4 Memory and CPU trade-offs at run-time

What is this parameter "CompilerInfo"? This is a vital magic ingredient! This is produced by the compiler, and contains the "recipe" for taking the contents of memory pointed to by "Return-of-sales" (for example), finding from that memory the actual values for the ASN.1 type, and encoding those 

Interpretation of tables is a pretty compact way of performing a task, but open code is faster! With the best tools you choose. 

values with correct tags, correct use of DEFAULT, etc. It essentially contains the entire information present in the ASN.1 type definition. 

There are (at least!) two forms this "CompilerInfo" can take: 

• It can be a very compact set of tables which are used in an interpretive fashion by "Encode" to determine how to encode the contents of the memory containing a value of (eg) "Return-of-sales" (and similarly for "decode"). 

It can be (rather more verbose, but faster) actual code to pick up the value of each field in turn to do the encoding of that field (and to merge the pieces together into larger SEQUENCE, SEQUENCE OF, etc structures). In general, open code is probably more appropriate for PER than for BER, as tags and lengths are often omitted in PER, whereas a table-driven approach, defining the tags to be encoded and letting the interpreter generate the lengths, may be more appropriate for BER. It is horses for courses! 

Just as there are many different implementation architectures for hand-encoding, so there are many different possible architectures for the design of tools. With implementation architectures, all that matters is that the bits-on-the-line are correct. And similarly with an ASN.1-compiler-tool, all that really matters is that it produces a programming-language data-structure that can represent all abstract values of the ASN.1 type, and that it efficiently produces correct encodings for values placed in that data-structure. (With similar remarks concerning decoding.) I don't know exactly how the "OSS ASN.1 Tools" product goes about producing an encoding (or decodes), but it does produce the right results! 

## 5.5 Control of a tool

There are a host of options that can be incorporated into an ASN.1-compiler-tool (and/or the run-time libraries that support it). For example: 

Inevitably there are options you want to leave to the user. How best to do that? 

• The language or platform to "compile" for. 

• How to represent ASN.1 INTEGER types in the programming-language data-structures. 

• Whether to use arrays or linked-list structures in the mapping from ASN.1 to your programming-language (for example, for "SEQUENCE OF"). 

• Which encoding rules to use for encoding (and to assume for decoding). 

(Slightly more subtle) Which encoding rules can be selected at run-time - all or only a subset? (This affects the library routines that are included, and hence the size of the executable.) 

• Which encodings to use in the non-canonical encoding rules. 

• Whether the user prefers the fastest possible encode/decode or the smallest executable. 

• (Fairly unimportant) The names of the directories and files that will be used at both compile-time and run-time. 

• And many others. 

The control by the user can be expressed by a global configuration file, by command-line directives, by an "options" button in a Windows-based product, by "compiler directives" embedded in the ASN.1 source, or by run-time call parameters, or by several of these, with one providing a global default and another overriding that default locally. With the "OSS ASN.1 Tools" product, compiler directives are included after a type definition (where a subtype specification might go) as a specialised form of comment. For example: 

$$
\text { SET } - - <   \text { LINKED } > - - \text { OF   INTEGER }
$$

## 6 Use of the "OSS ASN.1 Tools" product

Here we describe how to encode values with one particular tool. The process with other ASN.1- compiler-tools is similar. 

<table><tr><td>Put your values in the language data-structure and call ENCODE. That is all there is to it! More-or-less!</td></tr></table>

When you use the "OSS ASN.1 Tools" product to support an application written using the C programming language, you input an ASN.1 specification (and identify the top-level type that forms the abstract syntax, or PDU, to the compiler via a compiler directive). This can be defined using a single module or several modules. There are four outputs (but only the last two are important for correct ASN.1 input): 

• A "pretty-print" listing (not really very important). 

• Error and warning messages if your ASN.1 is a bit "funny". 

• A ".h" header file that contains the mapping of your ASN.1 types into C language datastructures. 

• A ".c" control file that conveys information from the compiler to the run-time routines that you will invoke to encode and decode. 

The latter is pretty incomprehensible (but vitally important), and you ignore it, other than to compile it with your C compiler and link in the resulting object file as part of your application. 

The ".h" file is included with your own code, and compiled to form the main part of your application, which will include calls to "encode" and "decode". You also link in a run-time library. At this stage you may wish to look at Appendices 3 and 4, which have not been included in ths chapter due to their bulk. 

Appendix 3 gives most of the ".h" file for "Return-of-sales" and "Report-item" for the C language implementation (and some parts of relevant "include" files). Appendix 4 gives the equivalent for a Java implementation. 

I offer no explanation or discussion of these appendices - if you are a C or Java programmer, the text (and its relation to the ASN.1 definitions) will be quite understandable. If you are not, just ignore them! 

And there you have it! Of course, the original application standard could have been published in "pseudo-C" or in Java instead of using ASN.1, but would that really have been a good idea? For once I will express an opinion - NO. Ask the same question in 1982/4 and it would have been COBOL or Pascal (or perhaps Modula) that we would have been talking about. And even if you define your structures in "pseudo-C", you still have to make statements about the encoding of those structures, the most important being about the order of the bytes in an integer when transmitted down the line, about the flattening of any tree structures you create, about the size of integers and of pointers, and so on. It really is rather simpler with ASN.1 - let the ASN.1-compiler-tool take the strain! 

The appendices are not of course the entire compiler output. There is also the control information used by the run-time routines to perform the encode/decode, but the implementor need never look at that, and it is not shown here. 

## 7 What makes one ASN.1-comiler-tool better than another?

There are many dimensions on which the quality of a tool can be judged. The major areas to be looked at are: 

• The extent of support for the full ASN.1 notation. 

<table><tr><td>OK. So you want to buy an ASN.1-compiler-tool? What to look for in a best-buy? It is not as easy as buying a washing-machine! Here are some things you might want to look for or beware of.</td></tr></table>

• The mappings to programming-language data-structures. 

• Run-time memory/CPU trade-offs. 

• Memory allocation mechanisms. 

• The degree of user control over options. 

We have already had some discussion of most of these areas when we discussed the sorts of decisions a tool vendor needs to take. Here we highlight a few points of detail. It is, however, important to recognise that with the best tools, absolutely none of the problems listed below will arise. Indeed, many of the problems occurred only in early tools before they were fullydeveloped. 

Some early tools provided no support for ASN.1 value notation, so you needed to remove all value assignments from your module and replace "DEFAULT" by "OPTIONAL", handling the default value in your application code. 

Other early tools could only handle a single module (no support for IMPORTS and EXPORTS), so you had to physically copy text to produce a single module. The better tools today will handle multiple modules, and (once you have identified your top-level message to them) will extract from those modules precisely and only those types that are needed to support your top-level message. 

Another issue is whether you can use the ASN.1 definition as published, or whether you have to help the parser in the tool by adding a semi-colon to the end of each of the assignment statements in your module. 

There are other tools that are designed simply to support one particular protocol, and will recognise only the types that appear in that protocol. If that protocol is extended in version 2 to use more types, you may have to wait for an upgrade to your tool before you can implement version 2! 

There is also the issue of the 1994 extensions to ASN.1 - Information Object Classes etc, described in Section II. This is probably the area where you are most likely to still find lack of support in some tools. 

The mapping to the programming-language data-structure is a very critical area. If this is got wrong you may not be able to set all the values you should be able to! 

Note also that ASN.1 allows arbitrary length names for identifiers (with all characters significant), and is case sensitive. In some programming languages, characters after (e.g.) the 31st are simply discarded. Does the tool ensure that long names (which are quite common in ASN.1) are mapped into distinct programming language names in an ergonomic way that you can understand? 

What about INTEGER types? A good tool will give you control (usually through either global directives or directives you embed into the ASN.1 text against a particular type) over the mapping of INTEGER types, for example into a short, normal, long, or huge (represented as a string) integer. 

There are also efficiency considerations in the mappings. On some platforms there is the concept of "native" integer types. Mapping directly into these can be much more efficient than proceeding in a more generic (platform-independent) manner. 

It is important here to remember that the mappings from ASN.1 to a programming language (usually called an "ASN.1 Application Programme Interface (API)" are in general not standardised, so each tool vendor does their own thing. (Work was done within X-Open on standardisation of the mapping to C++ - called the ASN.1/C++ API - but I am not sure whether the document was finally ratified. If you want to use C++ as your implementation language, you may want to ask your tool vendor about whether they use that mapping or not.) 

We discussed earlier the option of a largely interpretative table-driven approach (using little memory) versus an approach based on generated code (taking more memory but faster) to run-time encoding and decoding. This is one area where you will probably be looking for options in the use of the tool that will enable you to choose for each application or platform which approach you want taken. 

And finally, we discussed earlier the means of providing user control over tool options and the range of such options that can be controlled. 

All these factors contribute to the "quality" of a tool, but you will certainly want to look at the cost as well! Most tool vendors charge a licence fee that gets you just one copy of the ASN.1-compilertool, but unlimited copies of the run-time support (which you clearly need if you are to distribute your resulting application!). 

## 8 Conclusion

This chapter has discussed how to build an actual implementation for a protocol that has been defined using ASN.1. It is followed by some discussion of management and design issues for consideration by managers, specifiers, and implementors, to complete Section I of this book. 

# Chapter 7 Management and design issues for ASN.1 specification and implementation

# (Or: Things you need to think about!)

Summary: 

This chapter: 

• collects together many of the issues and "style" decisions mentioned elsewhere in the text; 

• identifies some global issues for management decisions; 

• identifies matters that specifiers need to consider; 

• identifies matters that implementors need to consider. 

The section on management decisions should be understandable to anyone who has read Section I. The remaining sections will require a knowledge of material covered in Section II, assume a quite detailed knowledge of ASN.1, and cover some fairly abstruse areas. 

A word of caution: I am not a believer in management gurus and elaborate "methodologies". Most of the headings below have the word "issues" in them. The following text is designed to give the reader some idea of the options, and things they should consider. At the end of the day you make the decisions, not me! I try as much as possible to suggest areas you should think about, rather than to tell you what I think you should do. If occasionally I move towards the latter, I apologise and please feel free to ignore my advice! 

Much of what is being said in this chapter is opinion (Figure 999 again!), not fact, and there are others who may well have different and perhaps opposite views to some of the suggestions made here. 

# 1 Global issues for management decisions

## 1.1 Specification

## 1.1.1 To use ASN.1 or not!

This has been well-discussed in Chapter 1, when a variety of techniques for defining protocols were described. This of course is the number 1 decision, but may be more conditioned by the culture within which the protocol specification is being made, or on the specification notation that has been used for other related protocols. 

If you have read this far, and you are able to influence the specification language used for a protocol, then I am sure you will ensure that ASN.1 is seriously considered. Go on to the next clause! 

By now, you should have a clear view of the ease of producing a specification using ASN.1, and of the ease of implementing such a protocol provided an ASN.1 tool is available. 

The counter-argument is that, simply because of its ease of use, ASN.1 does not force you to keep your specification simple (but of course does not prevent you from doing so!), and the more complex the protocol becomes the more your implementors will need tool support, and tools do cost money! 

However, if you are expecting your protocol to be implemented by commercial firms, with perhaps ten to twenty man-years of effort going into the implementation, the cost of purchasing a tool becomes totally insignificant. Paying money for a professionally-developed, supported, and robust tool is often more effective in the long run than use of a "freebie". (The main counter-argument to this is probably the Apache Web server - probably the most popular Web server in use today, and it is free! But there is an English saying "the exception proves the rule".) 

## 1.1.2 To copy or not?

If you need an ASN.1 type defined in (and exported by) another standard, there is a clear argument for importing that type into your own module(s). This is commonly done for ROSE datatypes and object classes, and 

Copying is wrong, yes? You may be able to get permission, and it may be the better solution. Look at the issues below. 

for X.500 Directory Names and for X.509 certificates. In this case you would, of course, also include a clear reference to the source that your were importing from. 

There is, however, another option that has been taken by some specifiers, and that is to simply copy a type definition into your own specification (of course also giving the semantics related to the fields). This is arguably in violation of the copyright laws, or at least of intellectual property rights, unless your specification is to be published by the same standards body as the one you are copying from, but it has ocurred in a number of specifications, even when the above caveat does not apply! 

There are three main reasons for copying (embedding) rather than importing and referencing: 

• It gives you control over the material, preventing problems and confusion if the referenced material is changed in a later version in a way that is not compatible with your own specification. 

• It means that your implementors only need to obtain your documents - your specification is complete and self-contained. 

• You want only a simplified version of the copied material (this is often the reason why you find copies of the ROSE material in other specifications, rather than direct use of IMPORT). 

Decisions on this issue are not easy, and should be taken consciously after appropriate discussion. 

There are no other real management issues related to specification (but many more details for specifiers are discussed below), so we now turn to issues related to implementation. 

## 1.2 Implementation - setting the budget

Any commercial project needs detailed costings, but it can be easy to overlook some of the hidden costs (or opportunities to spend money wisely!) when undertaking an implementation of an ASN.1-based specification. Some of these are mentioned below. 

Just a few things you should not forget about when doing your costings ... 

## 1.2.1 Getting the specs

There are two sets of specifications that you need - those for the protocol you are implementing and those for ASN.1 itself. 

Of course you need the specification for your protocol. But also for ASN.1, and possibly for anything either of these reference. 

In most cases you will want to use the latest versions of both the protocol specification and the ASN.1 specifications, but occasionally there may be some industry or community of interest agreement on use of older versions. (The ASN.1 1990 issue is discussed in Chapter 1 of Section IV). Be careful, too, to look out for corrigenda and addenda to the specifications. The place you obtained your specifications from should be able to alert you to this. In some cases there may be draft corrigenda or addenda in circulation. In this latter case, you may need to investigate further and perhaps try to contact the chairman or rapporteur or editor of the standards to discover the stability of these documents. Draft corrigenda and draft addenda do not always become approved corrigenda or addenda (at least not without sometimes substantial change). 

Note that ITU-T now have a Web-site from which (provided you have set up an account) you can purchase all ITU-T specifications and down-load copies over the Web. ETSI (European Telecommunications Standards Institute) have a similar site, but ETSI standards are free! Many of these use ASN.1 as their specification language. Links to these sites can be obtained via Appendix 5. 

In the case of your protocol specifications (but not the ASN.1 specifications themselves) it will be important to try to get hold of an electronic copy of the ASN.1 parts of the specification if you are going to use a tool, otherwise you will have the tedious and error-prone task of keying in that text. 

The vendor of your tool is likely to be able to help you here, and electronic copies of ASN.1 specifications usually circulate without charge and are sometimes on the Web. Another source of an electronic copy is the Editor of the protocol specification, who will usually be happy to provide one provided there are no commercial vendors of electronic versions and provided he knows you have bought the printed version of the specifications. 

You will need to get these specifications in a timely manner for your project, and in both cases (ASN.1 specs and your protocol specs) you will probably find you need some supporting specifications as well, and these need to be identified early in the project. 

In the case of the ASN.1 specifications, full details of the encoding of REAL, of GeneralizedTime and of most of the character set types require reference to additional separate specifications, so if these types are used in your protocol specification, you will need to obtain these other specifications as well. 

It is ISO advice that when one Standard references another, you should always use the latest version of the referenced Standard. This can, however, sometimes be dangerous, and it is always well to check publication dates to see which version of a referenced Standard was current at the time of publication of the referencing Standard, and see what impact the changes made might have on your protocol. 

## 1.2.2 Training courses, tutorials, and consultants

Another cost that is easily over-looked (and time for it not included in the project plan) is training time and the cost of courses for your implementation team. 

Commercial courses are commercial! (But your tool vendor may have a bundle that includes some courses and tutorial material for you). 

A "theory only" course on ASN.1 (covering more or less the same technical material as this book, but without the sorts of discussions that are appearing in this chapter and in a few other places) will take about two days. A course with some hands-on work writing ASN.1 specifications and using a tool could be as long as four days. 

You may also want to supplement such courses with purchases of this book! (Or of the companion volume by Olivier Dubuisson - available in both French and English. See Appendix 5 for a link.) 

Similarly, there are commercial courses available giving a good introduction to many of the protocols that are specified using ASN.1, and if these are available for the protocol you are implementing, you will probably want to use them. Frequently the speaker/trainer/presenter will be active in standardization of that protocol, and can alert you to the state of any addenda and corrigenda that may be circulating. 

Finally, there are a (small) number of people that advertise themselves as "ASN.1 consultants". They will give implementation advice, or will take an outline of a protocol you want written and produce the ASN.1 for you. But you pay consultancy prices! 

## 1.3 Implementation platform and tools

You may have no choice on the implementation platform (hardware, operating system, programming language), due to the need to extend an existing system, or to your firms global policies, or simply due to the operating system and programming language experience of your existing employees. 

There are many factors involved in taking decisions on implementation platforms, but there can be interactions between tool choice and platform choice. 

But if you do have a choice, a decision on the platform should be taken along with the decision on whether to use a tool, and if so which one. (Aspects of the "quality" of a tool were discussed in the previous chapter, and should be considered here.) 

At least one tool vendor will provide their tool for any platform, provided a C-compiler or a Ccross-compiler exists for that platform. Tools supporting programming in C, C++, and Java are all available. 

## 2 Issues for specifiers

This clause discusses a number of points that those involved in protocol specification using ASN.1 should consider. 

## 2.1 Guiding principles

There are four main principles to keep in mind (some apply to all protocol design, whether using ASN.1 or not). These principles may sound very obvious, but they are often overlooked: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/b5a17021ebf675f51bc5b4d6fc04ac4a8f5984366727c2bf6464de7684b9487e.jpg)


• Simplicity: Keep it as simple as possible, whilst being as general and flexible as necessary. 

Unambiguous and complete: Make absolutely sure you have left no ambiguities in your specification, and no implementation dependence in your specification unless you consciously decide to do so. In the latter case, make sure that such dependencies are clearly stated, not just implied or hidden, and that you consider the full interworking problems of such dependencies. 

Avoid options: Try to avoid encoder options unless there is a very good reason for them, as this reduces decoder implementation costs and testing costs. Allowing options on what parts of the total specification need be implemented is also dangerous, and unless done carefully can seriously limit interworking (but is often done!). A detailed application of this principle says "Don't use SET or SET OF, always use SEQUENCE or SEQUENCE OF instead". 

• Think about the next version: There always will be a next version if your protocol takes off. How might it differ? How do you want added material to be handled by version 1 systems? 

Most of these principles map into some specific ASN.1 features and their use that are described further below. 

## 2.2 Decisions on style

The best advice is for you to look at as many different specifications as you can and make a conscious decision on the various style issues. 

Some simple things to consider are: 

<table><tr><td>A good style makes the specification easy to read and follow, a bad one makes it hard. The actual bits on the line may be just the same!</td></tr></table>

• Fonts: Use of different fonts to distinguish formal material from English text. 

• Order of definitions: Top-down listing of type definitions or alphabetical listing? 

• Module structure: Grouping of related definitions into modules and the order and overall structure of modules. 

• Line numbers and indexes: Possible use of line numbering and provision of an index (showing where defined and where used for each reference name) for the specification. 

• Lengths of reference names: Long names can be clearer, but can clutter-up a specification. Don't rely on the name alone to define (imply) the associated semantics. 

• Duplicated text: Try not to duplicate text where several messages have common elements, but where this is clearer than (for example) using parameterization, do not be afraid of it if it makes the specification simpler. 

• Number of parameters: If you have a lot of parameters in a reference name definition, consider defining an Information Object Class to bundle them into a single parameter, as described in Section II Chapter 7. 

Web publication: There are a lot of standards that now have their ASN.1 (or even the complete specification) on the Web. An approach some take is to provide hyper-text links from every use of a reference name to the definition of that name, but of course you need an ASN.1 tool to generate the HTML for you in this case, or it would be too tedious and error prone to produce. You also still need to provide the "ASCII" txt of your specification for input input an ASN.1 compiler-tool. 

Other issues are a little more than "style", or warrant a longer discussion than can be provided in a bullet. These are discussed below. 

## 2.3 Your top-level type

You need to very clearly specify what is the top-level type that defines your messages. This should be a single type, and will almost always be an extensible CHOICE type. Include in this CHOICE all and only those types that define one of your complete outer-

<table><tr><td>This is your set of messages. Give it the importance and prominence it deserves. All other types are simply there to support this type.</td></tr></table>

level messages, not types that might be used in constraints on open types, for example. 

You may use the ABSTRACT-SYNTAX notation to identify this top-level type, or you can just make it very clear by English text and by placing it in a conspicuous position - perhaps in a module of its own. 

ABSTRACT-SYNTAX is not often used in current specifications, partly because it was added to ASN.1 at a relatively late date, and partly because the associated object identifier value is needed in communications only if the full OSI stack is being used, but it provides a very clear way of identifying your top-level types. 

As with all cases where you use the extensibility marker, you should think about, and specify clearly, what you want version 1 systems to do if they receive messages that have been added in version 2. If you leave this undefined (implementation-dependent), you have violated one of the four principles above, and it will probably end up biting you! 

## 2.4 Integer sizes and bounds

This is a detailed issue, and relates not just to the size of integers but also to the length of strings and to iterations of SEQUENCE OF and SET OF. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/f3f65777b38dcaae9c113508504d1c56820c7ae559d8d46672d169574ed44f43.jpg)


If you are using PER, then it is very important that bounds be formally expressed using the subtype notation, as tools will perform encodings according to the bounds. If you are using BER, then the issue is not one of encoding, but concerns: 

• What size integer should be used in the internal processing of these fields? (How should they be mapped into your chosen programming language?) 

If you fail to give any specification, one implementation may map to (and encode and transmit) 4-octet integers, and another may only support 2-octet integers. Still others may increase implementation costs significantly by making strenuous but unnecessary efforts to handle arbitrarily large integers or arbitrarily long strings. 

These are, of course, issues with PER as well, but if you have placed bounds on INTEGER types, the implementor can deduce the appropriate size of integer to use internally. 

If a specification is littered with bounds, particularly if these are set in a single module and imported, or passed as parameters, it can make the specification (whilst totally clear to a computer!) less readable by a human being. An alternative can be to define your own type INTEGER4, but then this has to be exported and imported to wherever you want to use it. 

ASN.1 tools generally permit global statements on the size of programming language integers that the ASN.1 INTEGER type is to be mapped into, so that a clear statement in ordinary English that unless otherwise stated, INTEGER fields are expected to be implemented as 4 octet integers can suffice. 

Notice that there is a certain tension here between specification of bounds to ensure the smallest possible number of bits on the line when using PER encodings, versus guidance on what to use for mapping to programming language integers and internal processing. 

What is absolutely vital, however, is to make it clear when very large integers (such as those that appear in signatures in X.509 certificates) have to be supported for the ASN.1 INTEGER type. 

We have mainly concentrated on INTEGER in the above, but remember that there are bounds issues related to all of: 

• INTEGER values. 

• Lengths of BIT STRING, OCTET STRING, character string types, and GeneralizedTime. 

• Number of iterations of each SEQUENCE OF and SET OF. 

And in each case, you have the two main issues raised above: ensuring optimum PER encodings, and ensuring interworking. The latter is arguably the more important. 

As ia pointed out in Section II Chapter 7, if you really do decide to leave some bounds (or anything else) as implementation-dependent, then inclusion of a parameter of the abstract syntax clearly flags this, and you can then include an exception marker on the bound to specify what a receiver should do if the two implementation choices are not the same. If you do take this route, it would be as well to clearly explain in English text what you intend, your reasons for leaving implementation-dependence, and when you expect it (or do not expect it) to cause interworking problems. 

## 2.5 Extensibility issues

We have already mentioned the importance of considering what extensions you are likely to require in version 2, and the importance of inclusion of an ellipsis at appropriate points. 

Extensibility is important and will work for you - but only if you obey the rules when you write version 2! 

Most people do not use EXTENSIBILITY IMPLIED in the module header, preferring to explicitly include the ellipsis wherever necessary rather than have over-kill. This is probably clearer, and does allow separate exception handling in each case if this is desired (see below). 

It is important to recognise what changes you can and cannot make in your version 2 specification if you want interworking with deployed version 1 systems to be possible without some separate version negotiation or requiring version 2 implementors to support "dual stacks". 

You can only add material where you have put your ellipses in version 1. Unless you originally wrote "EXTENSIBILITY IMPLIED", you cannot add new ellipses in version 2 (except in new types you add as extensions, of course), nor can you remove ellipses. And you cannot change existing types, for example from: 

## INTEGER

to 

## CHOICE { INTEGER , OBJECT IDENTIFIER }

A last addition to "what you can't do" (but of course this list is not exhaustive!) is optionality: You cannot add or remove OPTIONAL or DEFAULT from existing elements (although you can, if you wish, add another mandatory element at your ellipsis with the same type as an earlier OPTIONAL element). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/34e48647b11bb6207d907c99875b0320f0d1689793bdf82d105251ae972b52a7.jpg)


## 2.6 Exception handling

## 2.6.1 The requirement

It is absolutely vital that when you use ellipsis you give a clear statement of what behaviour you expect: 

<table><tr><td>Version 1 must be told what to do when hit by version 2 - and you must remember what you told it to do when you write version 2!</td></tr></table>

• From version 1 systems if they receive added material. 

• How version 2 systems where mandatory fields have been added are to handle messages from version 1 systems. 

The former is the more common case, as version 2 additions tend usually to be marked OPTIONAL. 

## 2.6.2 Common forms of exception handling

## 2.6.2.1 SEQUENCE and SET

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/5210ea855fc4aa07e32f679c37d63e5c84e8731e28a3b0956066ed2c98aff195.jpg)


Consider first added elements in a SEQUENCE or 

SET. It is extremely common here to specify that these are to be silently ignored by version 1 systems (you then need to consider the implications of this in your version 2 protocol). 

The simplest cases first - silently ignore. 

ASN.1 tools are likely to support the removal of such material within the decode routines, so that the application code is never even aware that it has been hit by a version 2 message, unless action is taken to specifically indicate to the tool that such material has to be passed up (for example, for relaying). 

## 2.6.2.2 CHOICE

In the case of CHOICE, the situation is more difficult, and will depend on the precise interactions that occur within your protocol. 

The simplest case is your top-level CHOICE, where there is probably some defined responses to top-level messages from an initiator of an exchange, and you can make provision in those responses for some form of "Sorry, I have not implemented that, I am just a version 1 system" indication. (Such provision needs to be made in the version 1 response messages, of course.) 

Consider now the case where an extensible CHOICE is embedded in a sequence, and perhaps is an extensible choice of some character string types which in version 2 has new types added. 

It would be possible for a version 1 system receiving a version 2 value of such a type to treat that value as an empty string - effectively to ignore it, and to say in subsequent processing "No value available for this field". Of course, many other actions are possible, depending on your detailed protocol and the importance of the CHOICE field. Only you can decide what would be appropriate. 

## 2.6.2.3 INTEGER and ENUMERATED

For extensible ranges on INTEGER, or for extensible ENUMERATIONS, the situation is not clear-cut. One option can be to define (in version 1) a mapping of any new version 2 value into a specific version 1 value, and specify the processing of that value as version 1 behaviour. 

Another difficult one. Is there a version 1 value that all version 2 values can be mapped to without causing too many problems? Otherwise you need to look at just how the integer or enumeration is going to affect subsequent processing. 

You need to try to think (when writing version 1) why you might be making the extension in version 2, and whether this behaviour would work out OK. You need to re-visit that discussion when you do eventually make version 2 additions! 

Mapping to a version 1 value will not always be right, and the presence of a version 2 value may need to be carried as an "unknown value" through several stages of further processing (perhaps even into a database), and its effect on later code which is processing that value should be fully determined in version 1. 

## 2.6.2.4 Extensible strings

The next case we need to consider are strings that had a limited (but extensible) maximum size in version 1, and the size in version 2 was increased. 

Two main options, both obvious: Require version 1 to support at the processing level longer strings, or truncate. 

Here again we see a conflict between the need to use constraints to get a tight PER encoding, and what we really want implementors to support in subsequent processing. 

It would be possible in this case to say (in version 1) that the constraint determines the maximum for version 1 senders (it is all that is considered necessary at present), but that version 1 receivers should be capable of handling in their implementation sizes up to (say) twice the version 1 limit - and perhaps truncate after that. 

But again, depending on the subsequent use and processing of the string field, options such as treating a version 2 value as "unknown value" can also be appropriate. 

## 2.6.2.5 Extensible bounds on SET OF and SEQUENCE OF

This situation is very similar to the situation with bounds on strings. 

Very similar to strings, as you would expect. 

It is clearly possible to require version 1 systems to support greater iterations on receipt. It is also possible to specify that they process the iterated material up to some limit of iterations, and then ignore the rest of the material (equivalent to truncating a string), possibly with some form of error return. 

Bounds on SET OF and SEQUENCE OF iterations are, however, relatively uncommon (with or without extension markers), so this case does not often arise. But the reader will be aware from earlier text that this means potential interworking problems or expensive implementations: few implementations will truly support an unlimited number of iterations unless told that they are required to do so. 

The problem, however, is that real implementation limits are more likely to be on the total size of the iterated material when mapped into an implementation programming language data structure, rather than on the number of iterations per se. This perhaps explains why bounds on iteration counts are often left unspecified. 

## 2.6.2.6 Use of extensible object sets in constraints

Finally, we consider the case where an extensible Information Object Set is used as a table or relational constraint, as in ROSE. Here it would be common to have some form of error response such as the ROSE REJECT message if a version 2 object is received. 

<table><tr><td>Our last example, both the most complex and the simplest!</td></tr></table>

But in other cases the option of silently ignoring (perhaps linked to an additional "criticality" field) the version 2 object, or to treat it as a version 1 object, can also be possibilities. 

## 2.6.2.7 Summary

In the above we have used six main mechanisms: 

• Silently ignore. 

• Give some form of error response. 

<table><tr><td>Six mechanisms were described earlier - someone please find another one and we will have the magic seven!</td></tr></table>

• Map to a version 1 value or object. 

• Include a special "unknown value" in version 1 and specify its processing. 

• Take the added material or unknown choice or value and relay it on unchanged. 

• Process as much as possible then truncate (silently or with some form of error response). 

Depending on the actual extensible construct, where that construct is used, the semantics associated with it, and how it affects later (perhaps much later) processing, we can choose one of these behaviours - or perhaps determine that another application-specific handling is more appropriate. 

## 2.6.3 ASN.1-specified default exception handling

ASN.1 has been criticised for not specifying default exception handling behaviour, but I hope the above discussion of options makes it clear that good and appropriate exception handling must be related to the needs of a specific protocol, and will frequently differ in different places in the protocol. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/d1a7e2b74d870eba93cb1d91e50273e262fe0be6d1c5d54b6115e7ee2e9c045d.jpg)


It would be positively dangerous to allow specifiers to put in ellipses without thinking through the implications of different sorts of version 1 exception handling behaviour. Ellipsis is not an easy option. It was introduced originally to ensure that the efficient PER encodings were such that some interworking would still be possible between version 1 and version 2 systems, but even with BER, if version 2 additions are made without a clear (earlier) specification of version 1 behaviour, serious problems result. 

It may be difficult, it may be a chore, but giving serious consideration to extensibility issues and the associated exception handling is part of the job of a protocol specifier - the job is more than just defining a few data structures! 

Unfortunately, if a bad job is done on exception handling in version 1, it is quite possibly a wholly new (and innocent!) group of specifiers producing version 2 that will suffer from the bad version 1 design. But I am afraid that is life! 

## 2.6.4 Use of the formal exception specification notation

Before leaving this discussion of extensibility, we must make some mention of the use of the formal exception specification notation (the notation that starts with "!"). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/50b606681376e7defe01a60290b42527658cd4dee413e781786c97c43a8ce49f.jpg)


The important thing (emphasised in the previous clause) is that exception handling should be very clearly stated, and the places in the protocol that particular handling is to be used are clearly identified. If there are relatively few uses of ellipsis, and particularly if the required exception handling is the same for all of them, then there is no real gain in including the formal exception specification notation, and English language text can suffice. (This might be the case if the only ellipses are at the end of SEQUENCE constructs, and the required behaviour in all cases is to silently ignore added material). 

(Actually, that is not quite true - inclusion of the formal notation tells a reader that exception handling has been thought about, and that there is somewhere in the text details of required behaviour, and it is my own personal view that there should be formal exception specification notation wherever extensibility occurs, but I know that there are others that disagree with me!) 

In a protocol with perhaps four or five different exception handling procedures specified (to be used with different instances of ellipsis, each behaviour applying to several instances of ellipsis), then use of the formal notation (perhaps simply using "!1", "!2, etc) on each ellipsis can be a simple and convenient way of identifying clearly which behaviour applies to which. Something similar to this is done very effectively in the ROSE protocol (using value reference names for "1", "2", etc), as described in Section II Chapter 6. 

## 2.7 Parameterization issues

Parameterization is powerful and can be the only way of achieving certain "re-usability" goals, particularly where one group provides a carrier protocol and several other groups fill in the holes in different ways to produce a complete specification. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/9610e63a25ddb6f3a979eaea379f33382be7b35ad2610de3ead33363fc7323a4.jpg)


But if a parameterized type is instantiated only a limited number of times within a single specification, then it may be that parameterization is unnecessary, and that the same effect can be achieved more clearly by using different (but similar) type or value definitions. 

Object Set parameters of the abstract syntax are a very good way of providing precise specifications of "must implement all, but can add" versus "can implement a subset, but can't add" versus "this is a guide, add or subtract", but are currently unfamiliar to many readers of ASN.1, and should be accompanied by explanatory text. 

Integer parameters of the abstract syntax (used in bounds) are also a very good way of clearly indicating that (for whatever reason), you have chosen to leave implementation-dependent features in your specification. 

But in both these cases, it is essential that exception handling procedures be fully specified, as discussed earlier. 

The use of the {...} notation is a form of parameterization, declaring that the object set to be used is implementation dependent, and is generally a less clear and precise notation than parameterization (but there are those that would disagree!). 

It is important if this notation is used, that text clearly specifies how it is intended (by whom and where) for the specification to be completed, and what implications there are on interworking, and what exception handling is to be applied. If that is done, this notation can produce a less cluttered specification than a lot of different parameters (object sets of various classes) being passed from the top-level type all the way down to where they are being used as a constraint. 

Finally, remember (Section II, Chapter 7) that if you have a lot of parameters of a parameterised type (or other form of reference name), you can reduce them to a single object set parameter by defining a suitable Information Object Class whose objects carry the complete set of information for each parameter. This can be a very useful simplification and reduction of verbosity in your text. 

## 2.8 Unconstrained open types

Unconstrained open types - elements of sequences looking like, for example: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/65769f7f387f58331163e4ce633614f1208502e7cb56dee68533e01a3ae0c029.jpg)


## OPERATION.&Type

are syntactically allowed in ASN.1 as part of the Seoul (see Section IV Chapter 1) introduction of the Information Object Class concept, but that was largely in response to a perceived need to provide syntax that was semantically equivalent to the old "raw ANY", and I hope the reader (at least those that have read Section II) by now appreciates that a "raw ANY" (and hence an unconstrained open type) is a BAD THING. 

All that a tool can deliver for this construct is an octet string. And even the implementor of the application has no clear indication of where to look to find out the possible types that can occur in this element, the semantics associated with those types, and which type has actually appeared in a given instance of communication, that is, how to decode and interpret the octet string. 

As a specifier in the years 2000 onwards, please don't use this form, even 'tho' you are allowed to! Look at the ROSE chapter (Section II Chapter 6) to see how to give a more precise and implementable specification of these sorts of constructs. I suspect that if ASN.1 is still going strong in 2010, forbidding this unconstrained construct may become possible (I am likely to campaign for it!), provided nobody shouts "1990, 1990!" (again, see Section IV Chapter 1!). 

## 2.9 Tagging issues

If you are writing a new specification, you should use AUTOMATIC TAGS (and - as an aside - not specify enumeration values for enumerations). But if you are adding to an existing specification, life can be more complicated. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/18c78ca07d19ca8aaf0bd550daa7242373d939bb01e7572bee9cb7da46211385.jpg)


Remember that a textually present tag construct automatically disables automatic tagging in a CHOICE, SEQUENCE, or SET - you are back in control (with IMPLICIT tagging). 

If you have good reasons not to use AUTOMATIC TAGS, then you need to have a much greater understanding of tagging, but should then always use IMPLICIT TAGS in your module header. Using an explicit tagging environment in modern specifications would be confusing, and you would either have a very verbose protocol (with BER), or a specification that was littered with the word IMPLICIT. 

If you choose, to specify that certain tags are EXPLICIT, the reasons for this will be obscure to most readers, and you should indicate in your text why this was done. 

There are usually two possible reasons: in an implicit tagging environment, tags on a choice type do in fact become explicit tags. It can help people implementing without a tool if this is made clear in the specification by writing in the word EXPLICIT (it is redundant to a computer, but may help a human being). 

The other reason is some desire to essentially associate some semantics or categorization with particular tag values, and to ensure that (in BER) there is a length wrapper round the actual type being identified. A similar motivation comes from use of a type constraint on an open-type when PER is used. Both of these (rather obscure) devices appear in some security specifications. 

Of course, all the above discussion of tagging assumes you have written your type definitions within the defined ASN.1 module framework, not just written it stand-alone! I am sure that readers of this book would never do that! 

## 2.10 Keeping it simple

ASN.1 has a number of powerful mechanisms for providing clear specifications, but you will often find people recommending that some of them not be used in the interests of a simpler specification. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/421b6f0fae836f035fed97e6cd76635ed5f08fad7ba68e69f0833455177ab221.jpg)


There can sometimes be justification in this, but what appears simple tends very much to depend on what has been frequently encountered in the past, and new notational constructs may take a little time to gain a ready acceptance and recognition. Once understood and recognised, they can provide a clearer (and hence simpler) specification than the alternative of English text. 

There is a second reason sometimes put forward for not using certain constructs, which is that some current-day tools will accept those constructs, but make no use of them, instead relying on so-called "compiler directives" (usually a specialised form of ASN.1 comment) that provide the same effect (and which in some cases pre-date the introduction of the notation into ASN.1). 

Notations that fall into this category for either or both reasons are (in no particular order): 

• Use of ABSTRACT-SYNTAX. 

• Use of parameters of the abstract syntax (variable constraints). 

• Use of a type constraint on an Open Type. 

• Use of the {...} notation. 

• Use of the ! exception specification notation. 

I would not recommend avoidance of any of these, but I would caution that where these constructs (or of any other construct that is not - yet - widely used) are used, it can be sensible to include an ASN.1 comment, or introductory text in the main body of the specification, saying how and why the constructs are being used and their precise meaning for this protocol. That way, such constructs will become familiar to all, and become "simple"! 

## 3 Issues for implementors

This section is slightly shorter than the "issues for specifiers", but quite a few of the earlier topics recur here. The difference is that you (the implementor) are on the receiving end, and if the specifiers have produced ambiguities or left implementation dependencies, you have to sort them out! (Implementors would also be well-advised to read carefully the two earlier parts of this chapter, as well, of course, as the whole of Section II.) 

## 3.1 Guiding principles

Principles for Internet implementors are often stated as: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/38782f259da13cc9987f15f5edd681a6a28f17bf413d7b98c5fd5abd2158e7e5.jpg)


• Strictly confirm to the specification in what you send. 

• Be forgiving in what you receive. 

That sounds like good advice, and it is often possible to write code that understands and processes things that are strictly invalid. 

This situation arises more often in Internet protocols than in ASN.1-based protocols, because the use of a text-based format often introduces more redundancy, and hence scope for "understanding" formally incorrect encodings, and because most Internet protocols rely on this principle to provide for interworking between version 1 and version 2 of a specification. The situation will rarely arise with PER, which has almost no redundancy, and an explicit extensions bit! 

With BER you could decide to be forgiving if you got a universal class 16 tag (SEQUENCE) with the primitive/constructor bit set to "primitive". Or you could be accidentally forbidding by just not bothering to write the code to check that bit once you had detected universal class 16! 

But if you are forgiving of errors (a primitive sequence, or integers exceeding stated bounds say), you should consider carefully the effect of being forgiving. This issue is very strongly related to extensibility - what you have got is implied extensibility (that you yourself have decided to introduce), and you are on your own to define the best exception handling procedures. 

I would recommend that in the case of ASN.1-based protocols it is rarely a good idea to silently ignore and process incorrect encodings which you are able to give meaning to (your own extensions). You may well choose to go on processing, but the error (with details of the sender) should at least be logged somewhere, and if the protocol permits it, sent back to the sender in some form of error message. 

## 3.2 Know your tool

In any development environment there are an immense number of features in the chose tool that can make an implementors life easier. It is important to become familiar with those features/options/parameters of the tool. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/47e2542608eb01b87aa4c7bb97e0c40fd51e517ba3df6c356279ebe3ad19fd3f.jpg)


Part of the "quality" aspects of a tool are the ease with which you can acquire an understanding of the functions it provides, and the detailed syntax needed to obtain those functions. Of course, you may regard the actual functions it does provide as more important, but functions that are not obvious in associated documentation or help files or are not easy to invoke are almost as bad as missing functions. 

## 3.3 Sizes of integers

This issue has been heavily discussed in the section for specifiers (which is relevant to implementors too). Tools will often give you control over the length of integer they map to, on a global basis (usually by command-line parameters), but will also give an over-ride for individual fields, usually by "compiler directives" - special forms of ASN.1 comment. 

You need to know exactly what was intended. With luck, the specification will tell you. Otherwise a good guess is four octets! But if you guess, cover your back - raise it as an issue in your implementatin team. 

The better tools will also allow you to specify that certain integer fields are to be treated as strings to allow them to be arbitrarily large (using dynamic memory allocation) subject to available memory. 

You have two problems: 

• Interpreting the intent of the specifier of the protocol. 

• Getting your tool to do what you want, if what you want is not part of the formal specification or contradicts it! 

The latter depends on the quality of the tool. So if your protocol specification says that a field is "INTEGER (0..7)", but you want it (for ease of programming and/or writing to a database) to be mapped to a four-octet integer, rather than a two or one-octet integer in the programming language of your choice, are you able to do it? 

The former can be the more difficult problem! If specifiers have obeyed the guidelines/exhortions in this area given earlier in this chapter, you should have no problem, but otherwise you may need to try to guess (from knowledge of the application and from other parts of the specification, or by enquiry from others (see below)), just what the intention was, or how others are interpreting it. 

## 3.4 Ambiguities and implementation-dependencies in specifications

Don't believe the box! It is hard to write a specification that is completely clean (particularly in the first published specification), and has totally specified the bits on the line that the implementation is required to produce under all circumstances. (I hate to say it, but if done well, the specifier’s job is harder than the implementor’s, but in the specifier's case it is a lot easier to do the job badly and not be found out! 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/61b5f4ed177844599f539088a7b49bbe1c9e4c13fee4f7a088ef4490c560a32e.jpg)


The most important advice to implementors - and this is very important - is that if you find things that are not said, raise them as an issue, at least within your team, but preferably with the specifiers themselves through some appropriate mailing list or group. 

Some of you will have heard of the Alternating Bit Protocol. A very similar protocol was specified for use over a particular LAN (no names, no pack drill!) in the late 1970s, but the specification did not say what the behaviour was to be when an ACK with the wrong number was received. The implementors decided that the "right" action was to immediately retransmit the last message (with the same sequence number), trusting the receiver to discard duplicates. Result: parasitic transmissions. Throughput dropped to half until the load backed off, with every packet being transmitted twice! 

If there is one clear duty on implementors, it is not to take their own decisions when specifications are unclear! 

## 3.5 Corrigenda

Implementors need to be as much aware as those in a more managerial capacity of what corrigenda are around, their status, and how they might impact the implementation in the future. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/ccbc1c2063210d090c3fd5f1ba3200742630e878510afb05b89eb3ad3b7c898d.jpg)


If you know something is coming, its arrival can be a lot less painful if it has been planned for! 

## 3.6 Extensibility and exception handling

This text is getting repetitive! If you are told clearly what the bits on the wire should be (and what you do in response to them), and how you are to handle unknown stuff coming in, and if your decoding tool is sufficiently good and flexible, then there are no problems. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/b85b814eaa3fb617220c04cf12290d6ad88a2e1912bda46e90c75a1992f9bf74.jpg)


Otherwise worry! 

## 3.7 Care with hand encodings

If, for whatever reason, you do not even have access to a well-debugged library of routines to encode simple types like INTEGER, etc, let alone access to a fully-fledged ASN.1 compiler, then you deserve sympathy! 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/d04a2e8fbf3c22707876f683ecf925cc65c62a1ecaacc651326b88b517dbd67e.jpg)


Producing ASN.1 encodings from scratch, by hand, is not impossible, and in one sense, not even difficult. (But it is probably easier to get it right first time with BER than with PER, unfortunately, due to the large number of optimisations in PER.) It is just time-consuming and error prone. 

First of all, you need to read Section III rather more carefully than you otherwise would! Then you need to spend a lot of time with the actual ASN.1 encoding specification that you are going to be using. 

Second, you will need some sort of ad hoc "line monitor" tool to display what you are producing in a format that will make it easy for you to check that you are producing what you intended. 

And lastly, you really need an ASN.1 tool! Not one that necessarily runs on your platform (lack of that is presumably why you are not using a tool), but one that can run on some other communicating platform, take your output, and display the values it thinks you are transmitting. 

Well, that was almost last! There is nothing like final inter-operability testing with a totally different complete implementation, particularly if it (and you!) have good error logging of things you think are erroneous about what you are receiving. 

## 3.8 Mailing lists

There is a mailing list you can use for general ASN.1 enquiries (see Appendix 5 for a link to this), and many protocol specifications today are supported by mailing lists, news groups, Web pages, etc. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/f48a711f97177a04632989edc9980b8ab779bc9146c7e29b659967ec2af87b1c.jpg)


These resources can be very valuable to you. (As can people that give ASN.1 and specificprotocol courses, who are usually willing to leave their e-mail addresses with you and to answer queries subsequent to their courses. 

## 3.9 Good engineering - version 2 **will** come!

Any protocol you implement will have a version 2 specification that you or your descendants (team-wise) will have to implement. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/b03d49b904cc5b522714645b625d32c1603ab7a04e562804a6fbeef0322bd28d.jpg)


All the usual good engineering principles apply to make sure that your code and documentation enables others to modify your implementation to support the version 2 specification as and when this is produced. 

You will get some hints in the extensibility provisions of version 1 of what areas the specifiers expect to change. This can help you to engineer the structure of your implementation to be easily able to accommodate those changes when they arrive. 

Just as getting exception handling as right as possible is a challenge for specifiers, getting an implementation architecture that enables extensions to be easily handled (and providing correct exception handling in version 1 when there are as yet no version 2 systems around to test against) is the challenge for the implementor. As for specifiers - this is part of your job, get it right! 

## 4 Conclusion

And that completes this first Section of the book. Many of you will be leaving us at this point (although you may find some parts of Section IV interesting). I hope you have found it useful. The more technically-minded will no doubt be proceeding to Sections II and III – read on! 

## SECTION II

## Further Details

# Chapter 1 The object identifier type

(Or: What's in a name?) 

Summary: The object identifier type, and its associated hierarchical name-space is heavily used by protocol specifiers that use ASN.1. It provides a world-wide unambiguous naming scheme that anyone can use, and has been used to name a very wide range of "things". 

Object identifiers are used to identify: 

a) ASN.1 modules 

b) Abstract and transfer syntaxes 

c) Managed objects and their attributes 

d) Components of Directory (X.500) names 

e) Headers of MHS messages (X.400) and MHS Body Types 

f) Banks and Merchants in Secure Electronic Transactions 

g) Character Repertoires and their encodings 

h) Parcels being tracked by courier firms 

i) And many other "things" or "information objects". 

## 1 Introduction

Final discussion of the object identifier type has been deferred to this "Further Details" Section, but as a type notation it is as simple as BOOLEAN. You just write: 

Object identifiers were introduced into ASN.1 in 1986 to meet a growing need for a name-space with globally unique short identifiers which permitted easy acquisition of name-space by anybody. 

OBJECT IDENTIFIER 

all upper case. The complexity arises with the set of values of this type, and with the value notation. 

First, we should note that the set of values is dynamically changing on a daily basis, and that no one computer system (or human-being) is expected to know what all the legal values are. The value notation has a structure, and each object identifier value can be mapped onto a sequence of simple integer values, but these structures do not matter. Treated as an atomic entity, an object identifier value (and its associated semantics) is either known to an implementation, or not known. This is all that matters. 

When this type is used in a computer protocol, it is almost always used in circumstances where there is (or should be!) a clear specification of the exception handling that is required if a received object identifier value does not match a known value. 

Note that all current ASN.1 encoding rules provide a canonical encoding of object identifier values (no encoder options) which is the same for all encoding rules and is also an integral multiple of eight bits (an octetstring). So storing those object identifier values for which the semantics is known as simple octet strings containing the ASN.1 encoding, and comparing incoming encodings with these, is a viable implementation option. 

We have met values of the type already as a way of identifying modules, and have seen some of the value notation. We must now discuss the model underlying such values and the allocation of 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/e2f8246a4fcb3140a547a0fc892decbf48a560bee214c1f877f68db98d0122f2.jpg)



© OSS,31 May 1999


object identifier name space. 

## 2 The object identifier tree

The underlying concept for object identifiers is a tree-structure, usually drawn as in figure II-1. Each object identifier value corresponds to precisely one path from the root down to a leaf (or possibly an internal node), with each component of the value notation identifying one of the arcs traversed on this path. 

The tree has a single root (usually drawn at the top as is the usual way with trees in computing!), and a number of arcs to the next level (all arcs go just to the next level), providing nodes at that level. Each node at the next level has arcs down to nodes at the next level below, and so on. Both the depth of the tree and the number of arcs from each node are unlimited. Some branches of the tree will be thickly populated with sub-arcs, others sparsely. Some branches will end early, others will go very deep. 

Every node is administered by some authority. That authority allocates arcs beneath that node, leading to a subordinate node, and determining: 

• The authority to which delegated responsibility for further allocation (beneath the subordinate node) has been passed, or an information object which is associated with that (leaf) node. (The "information object" concept is discussed further below.) 

• A number (unambiguous within all arcs from the current node) to identify the subordinate node from the current node (zero upwards, not necessarily consecutive). 

Optionally a name to be associated with the arc for use by human beings, and again providing identification within the arcs from the current node. 

The name in the third bullet is required to conform to the ASN.1 rules for a value-reference-name - that is, it must begin with a lower-case letter, and continue with letters (of any case) and digits and hyphens (but with no two consecutive hyphens). 

When "ccitt" became "itu-t", the ASN.1 standardisers tacitly accepted synonyms for names on arcs. 

Perhaps because of this, many users of ASN.1 now feel that arc names are relatively unimportant (certainly they don't affect the bits-on-the-line), and that once you have obtained a (numerical) object identifier allocation, you can use value notation for that object identifier with any names you choose when you wish to identify yourself, or to publish allocations beneath your node. Some would even assert the right to vary the names used in higher-level nodes. 

As at mid-1999, this area is in a state of flux. Earlier views would have said that names were allocated by the superior of an arc, and were immutable, otherwise there is much scope for human confusion. However, the text in the Specification does not entirely support this view, although I know it was the original intent! 

The contrary view (that in published OIDs any name can be used) is supported on two grounds: 

• There are issues of copyright or trademark of names, which superior nodes are often unwilling to get involved in, so they make no name allocation to their subordinate arcs, only a number. 

Lower arcs can sometimes be sensitive about appearing to be subordinate to (or part of) organizations whose names identify arcs between themselves and the root. In many cases such an association is at best a loose one, and some organizations will give out object identifier space to anyone who asks for it. 

It is likely that the standard will be clarified to assert not only that names are optional in the value notation for an object identifier, but also that all such names are arbitrarily chosen by those that include object identifier values in publications. However, it would be irresponsible to use misleading names on arcs, and it is probably best to either omit the name or to use the generally recognised one from any arcs above that which points to your node. 

## 3 Information objects

NOTE –The term "information object" was used in OBJECT IDENTIFIER text long before the introduction of the "Informaton Object Class" concepts and (perhaps confusingly) refers to a more general concept than the same words used in connection with Information Object Classes. 

The term information object used in this context emphasises the fact that object identifiers are usually used to identify relatively abstract objects, such as ASN.1 modules, the definition of some operation that a computer can perform, attributes of some system that can be manipulated by a management protocol, and so on. In other words, they usually identify some piece of specification (not necessarily written using ASN.1). In fact, an organization can be seen as just another type of information object, and in general a node can both be associated with an information object (of any sort) and also have further subordinate nodes. 

If an organization has been allocated a node, we say they have been "hung" from the tree. It is also possible to "hang" inanimate objects (like ASN.1 modules) from the tree, once you are the proud owner of a node! 

Distributed registration authorities provide space enough for all. Have you got hung on the Object Identifier tree yet? Get a piece of the action! 

It is very easy to learn the top bits of the tree, and then to "cheat". To "steal" an arc from some node, publishing allocations beneath that. Don't do it!. It is not hard to get "legal" object identifier name space. But .... see figure 999 .... there are those that advocate a top-level arc where arcs below that are only unambiguous within a very closed community - anyone can use any number, and caveat emptor! What this is really saying is that there is a suggestion that some Object Identifier values should be context-specific, all such values being identified by a special top-level arc. However, this proposal is merely that - a proposal. Such a top-level arc does not yet (mid 1999) exist, although the RELATIVE OID type discussed in Section IV perofrms a similar role. 

To identify an organization or object, we use an object identifier value. At the abstract level, this is simply a path from the root to the organization or object being identified. This path can be specified by giving the number of each arc in turn, together with the names (which may be empty/non-existent) associated with each of these arcs. The encoding rules use only the numbers of the arcs, so non-existent names are not a problem. The value notation has various forms (see below) that allow both the names and numbers to be specified. Figure II-1 shows one small part of the tree, with two branches taken to a depth of 4 and 5 arcs. 

## 4 Value notation

Note that in all the examples that follow, it would be legal to replace any number by a valuereference name of type INTEGER. If this value reference name had been assigned the value given in the examples below, then the resulting object identifier value is unchanged. It is, however, not common practice to do this. 

The value notation consists of a series of components, one for each arc leading to an identified object. In figure II-1 we can identify the objects at the bottom of the figure by: 

```txt
{iso standard 8571 abstract-syntax (2)}
and
{iso identified-organization dod (6) internet (1)}
and
{joint-iso-itu-t internationalRA (23) set (42) set-vendors (9) oss (12)} 
```

or equivalently, but less readably, by: 

```txt
{1 0 8571 2}
{1 3 6 1}
{2 23 42 9 12} 
```

The first value names an information object in the ISO Standard 8571, the second gives object identifier space to the IETF, and sub-arcs of this are heavily populated in the Internet specification for SNMP (Simple Network Management Protocol). The third value gives object identifier name space to Open Systems Solutions, a vendor associated with the Secure Electronic Transactions (SET) consortium. 

It is always permissible to use only numbers (but not common). In one case "8571" an arc has a number but no name, so the number appears alone, not in brackets. In most other cases, the name is given followed by the number in brackets. (The number is required to be in brackets if both are given). It is only for the top arcs (iso, standard, joint-iso-itu-t) that the numbers can be omitted, as these are "well-known" arcs, with their numerical values listed in the ASN.1 specification pre-1988 (they are now listed in X.660/ISO 9834-1). Whilst seeing specifications with these top-level numbers omitted is quite common, it is becoming increasingly the practice, particularly as ASN.1 is now being used by organizations only loosely associated with ITU-T or ISO (or not associated at all), to list the numbers in parenthesis for all arcs. 

Notice that this value notation does not contain commas between components. This is unusual for ASN.1 value notation, and was done to promote easy human readability, particularly of the early components with the numbers omitted. 

There is one other facility available when specifying object identifier values. We have already met it in figure 21, where we chose to define an object identifier value "wineco-OID" with five components, and then use that name immediately after the curly bracket in our IMPORTS statement. (It is only allowed immediately after the curly bracket). This is something that is quite commonly done, but note that it is not allowed for the module identifier, as the scope of reference names in the module has not yet been entered. Some specifications will define a large number of object identifier values, particularly in association with the definition of information objects, and a very common style is to assign these values in a single module to a series of value-referencenames, exporting those names. They will then be imported and used as necessary in other modules. 

## 5 Uses of the object identifier type

It is a common occurrence for a protocol to be written where there is a need to carry identification of "things". These "things" may be: 

• what it is: 

− operating on; 

− ordering; 

− reporting on; 

• information that it is carrying; 

• identification of specific actions to be undertaken on receipt of a message; 

• components of some more complex structure, such as Directory (X.500) names; 

• etc, etc. 

Some existing uses are listed in the "Summary" at the start of this chapter. 

We use the term "information objects" for "things", because at the end of the day a physical "thing" is identified by some piece of text or specification - a piece of information, and sometimes the "thing" is not a physical object but is a rather abstract "thing" such a an organization, but the "thing" is still identified by some specification - a piece of information. What is really being identified by an object identifier value is that more elaborate and precise specification of the thing - an "information object", rather than the "thing" itself, but the two are in 1-1 correspondence, so there is really no distinction. 

Where there is a need for the identification of an information object: 

• which must be world-wide unambiguous; and 

where allocations of identification to such information objects needs to be widely available to almost anybody; then 

use of ASN.1 object identifier values is a good way to go. 

In general, almost all users of ASN.1 have found the need for a naming scheme to identify information objects relevant to their application, and have chosen to use object identifier values for this purpose, and to include in their protocol fields that are OBJECT IDENTIFIER types to carry such values. The OBJECT IDENTIFIER type, and its associated naming structure is important and heavily used. 

# Chapter 2 The character string types

## (Or: Overcoming Genesis Chapter 11!)

Summary: This chapter discusses the complete set of character string types: 

• NumericString 

• PrintableString 

• VisibleString (ISO646String) 

• IA5String 

• TeletexString (T61String) 

• VideotexString 

• GraphicString 

• GeneralString 

• UniversalString 

• BMPString 

• UTF8String 

It describes their value notations, and gives recommendations on their use. 

Discussion of the character string "hole" type - CHARACTER STRING - is deferred until Chapter 7 of this section. 

## 1 Introduction

Here we will describe all the available (up to 1988) character string types apart from "CHARACTER STRING", which is described later under "Hole Types". For a full understanding of these types, the reader must be aware of the various approaches that have been taken to character encoding schemes for computers generally over the years. A full discussion of this, and of the historical development of support for character string types in ASN.1, is 

And God was displeased with the people of Babel for building their tower unto heaven, and sent a thunderbolt and scattered the peoples to the corners of the world giving them different languages. 

given in Section IV. Sufficient information is given here for the writing and understanding of ASN.1 specifications. If you want to skip some of this material, just go down to the section "Recommended character string types" (clause 13), and look at the paragraphs about the ones mentioned there. That is probably all you need! 

Character string types are considered by some to be unnecessary (won't a good old OCTET STRING do the job?). (See figure 999!). Yes, an OCTET STRING could be used. But you would then need to spell out clearly the precise encoding to be used, and to make clear to implementors the range of characters that were to be supported. Moreover, that specification would be in normal human-readable text or in ASN.1 comment, could not be understood by any tool assisting an implementation, and (as it is new text) would be a potential source of ambiguity and interworking problems. 

The types provided in ASN.1 cover the spectrum from the simplest requirements to the most ambitious. In general, if your character set requirements for a particular string are restricted, use the more restricted character set types to make this clear, even if the encoding is the same as for a type with a wider character repertoire. 

Note also that some of the latest character string types can only easily be supported by a programming language (such as Java) that uses 16 bits per character, supporting the Unicode encoding scheme. (This scheme is fully described in Section IV). Increasingly, however, (late 1990s) programming languages and operating systems and browsers and word processors and .... are all providing Unicode support, either for the 16-bits-per-character repertoire, or in some cases for a 32-bits-per-character repertoire. 

This does not mean that if the application designer has specified a field as (for example) UTF8String or UniversalString, you cannot implement that protocol in a language (or operating system) that does not have Unicode support, it just means that it may be harder work! 

## 2 NumericString

Values of the type are strings of characters containing the digits zero to 9 and space. The BER encoding is ASCII (8 bits per character), and the PER encoding is 4 bits per character unless the character repertoire has been further restricted by a "permitted alphabet constraint" (see Chapter 3 following), when it could be less. 

## 3 PrintableString

Values of the type are strings of characters containing an ad hoc list of characters defined in a table in the ASN.1 specification, and copied here as Figure II-2. 

This is basically the old telex character set, plus the lower case letters. You would probably tend not to use it today unless you had an application likely to be associated with devices with limited character input or display capabilities. 

<table><tr><td>Name</td><td>Graphic</td></tr><tr><td>Capital letters</td><td>A, B, ... Z</td></tr><tr><td>Small letters</td><td>a, b, ... z</td></tr><tr><td>Digits</td><td>0, 1, ... 9</td></tr><tr><td>Space</td><td>(space)</td></tr><tr><td>Apostrophe</td><td>&#x27;</td></tr><tr><td>Left Parenthesis</td><td>(</td></tr><tr><td>Right Parenthesis</td><td>)</td></tr><tr><td>Plus sign</td><td>+</td></tr><tr><td>Comma</td><td>,</td></tr><tr><td>Hyphen</td><td>-</td></tr><tr><td>Full stop</td><td>.</td></tr><tr><td>Solidus</td><td>/</td></tr><tr><td>Colon</td><td>:</td></tr><tr><td>Equal sign</td><td>=</td></tr><tr><td>Question mark</td><td>?</td></tr></table>

## 4 VisibleString (ISO646String)

The name "ISO646String" is a deprecated synonym for VisibleString (deprecated because the name contains a Standard number which is not in fact used in its definition, post 1986!), but you may encounter it. The character repertoire is described in the very old ISO Standard ISO 646, which laid the foundation for the better-known ASCII. Whilst this character repertoire was originally strictly not ASCII, but rather "the International Reference Version of ISO 646", it was widely interpreted by all ASN.1 users and implementors as simple plain ASCII, but printing characters plus space only. The original definition was by reference to the ISO 646 Standard, but post-1986 the definition was formally "Register Entry 2 (plus space) of the International Register of Coded Character Sets to be used with Escape Sequences". (See Section IV for more detail). This was changed in 1994 to reference "Register Entry 6", which is strict ASCII, recognising the normal interpretation by ASN.1 users. The coding in BER is 8 bits per character, and it is the same in PER if there is no subtyping applied to the type to restrict the range of characters (if there is, it could be less). 

## 5 IA5String

"International Alphabet 5" is specified in a very old ITU-T Recommendation, which again was the original reference for this type. Again, this was close to ASCII (ASCII was a "national variant" of International Alphabet 5, but the type is widely assumed to mean simply "the whole of ASCII, including control characters, space, and del". The precise reference today is "Register Entries 1 and 6 (plus space and delete) of the International Register of Coded Character Sets to be used with Escape Sequences", which is strict ASCII. The encoding is again 8 bits per character (possibly less in PER). 

## 6 TeletexString (T61String)

Again, the synonym is deprecated. Originally CCITT Recommendation T.61 specified the character repertoire for Teletex, and was referenced by the ASN.1 specification. (Today the corresponding specifications are in the ITU-T T.50 series.) The precise definition of this type has changed over time to reflect the increasing range of languages supported by the ITU-T teletex Recommendations. Today it includes Urdu, Korean, Greek, .... . Formally, it is Register Entries 6, 87, 102, 103, 106, 107, 126, 144, 150, 153, 156, 164, 165, 168, plus SPACE and DELETE! The encoding of each register entry is 8 bits per character, but there are defined escape codes (the ASCII "ESC" encoding followed by some defined octet values) to switch between the different register entries. It is quite hard to implement full support for this character string type, but it is extensively used in the X.400 and X.500 work. The character repertoires referenced have increased with each new version of ASN.1, and may continue to do so, under pressure to maintain alignment with the ITU-T Teletex Recommendations, which themselves are under pressure to support more and more of the world's character sets. This makes this type effectively an openended set of character repertoires, and would make any claims of "conformance" hard to define or sustain. Today, it is best avoided, but it was popular in the mid-1980s, and you will often encounter it. 

## 7 VideotexString

A little-used character string type that gives access to the "characters" used to build crude pictures on videotext systems. Typically a "character" is a 3x2 array, with each cell containing either a foreground colour or a background colour (determined by transmission of one of about five control characters), giving 64 different printing "characters" that can be used to build the picture. 

Formally, it is again a list of 17 register entries, partially overlapping those specified for TeletexString. 

## 8 GraphicString

This was a popular string type in the main OSI (Open Systems Interconnection) standards produced during the 1980s, and allowed any of the Register Entries in the International Register for printing characters (but not the control character entries). In its hey-day the International Register had a new entry added about every month or so, and eventually covered most of the languages of the world. If this text is used in an academic course, an interesting student exercise would be to discuss the implementation implications of using such a wide (and ever-expanding!) type definition. Since the development of ISO 10646/Unicode, additions to the International Register have become much less common, and coding schemes based on this Register can be regarded as obsolescent. 

## 9 GeneralString

This is similar to GraphicString, except that the register entries for control characters (of which there are many) can also be used. 

## 10 UniversalString

This is a string type that was introduced into ASN.1 in 1994, following the completion of the ISO Standard 10646 and the publication of the Unicode specification (see Section IV for more information on ISO 10646 and Unicode). The ISO 10646 standard (and the ASN.1 encoding in BER) envisages a 32-bits 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/0d12bb2cfa55905678efc224e2f4e6e43fb29fe192667be25f398dd9a9e5d60e.jpg)


per character encoding scheme, sufficient to cover all the languages of the world without using "combining characters", with a fair bit left over for the languages of Mars and most of the rest of the undiscovered Universe! It is only this type and UTF8String (see below) that can cover all the characters for which computer encodings have been defined (not quite true - there are some weird glyphs in the International Register that have not yet been put into ISO 10646). This type has not, however, proved popular among ASN.1 users. 

## 11 BMPString

The name comes from the "Basic Multilingual Plane" (BMP) of ISO 10646, which contains all characters with any commercial importance (all living languages), and can be encoded (and is in BER) with a fixed 16-bits per character. Whilst the formal ASN.1 definition references ISO 10646, the character set is the same as that defined in and more commonly known as the Unicode Standard produced by the Unicode Consortium. (Search the Web if you want to know more about 

Unicode, oar see Section IV). The fixed-size representation of 16-bits per character, holding Unicode characters, is becoming common in revisions of programming languages and operating systems, and is rapidly replacing ASCII as the default encoding for manipulating character data. This ASN.1 type was widely used during the mid-1990s by those application specifications upgrading to the 1994 ASN.1 specification. (It was not present in ASN.1 pre-1994). 

## 12 UTF8String

UTF8String is the recommended character string type for full internationalization without unnecessary verbosity. 

This encoding scheme was developed in the mid-1990s and the type was added to ASN.1 in 1998. The acronym stands for "Universal Transformation Format, 8 bit", but that does not matter much. Formally, the character repertoire is exactly the same as UniversalString - all defined characters can be represented. 

UTF8 is, however, a variable length encoding for each character, with the rather interesting property that (7-bit) ASCII characters encode as ASCII - in a single octet with the top bit set to zero, and none of the octets in the representation of a non-ASCII character have the top bit set to zero. ASCII is paramount! Most European language characters (like c-cedilla or u-umlaut) will encode in two octets, and the whole of the Basic Multi-lingual Plane, together with all characters identified so far, encode in at most three octets per character. If we ever do populate the whole of the ISO 10646 32-bit space, then UTF8 would use a maximum of six octets per character. 

Whilst use of a fixed 16-bits per character is becoming the norm for operating system interfaces and programming languages, use of UTF8 for storage and transmission of character data is the way everybody is going (as at mid-1999). As an implementor of an ASN.1-based application, you can expect that if you use an ASN.1 tool with a language that supports Unicode, the UTF8 transformations will be applied by the tool, invisibly to you, as part of the ASN.1 encode/decode process, giving you a simple 16-bits (or 32-bits) per character to work with in memory, but with an efficient transfer syntax. 

## 13 Recommended character string types

So having read right to the end, you can now make an informed judgment on which character string types to use! Here it is assumed you are writing a new specification and will conform to the post-1994 ASN.1, and hence can use all the facilities in the latest ASN.1. (A fuller discussion of the pre-1994/post-1994 issues appears in Section IV). 

If, for the expected implementation of your application, the input/output devices involved are likely to be able to handle the full Unicode 

For full internationalization, use UTF8String. Otherwise use the most restrictive character string type available for your needs. If input/output devices restrict your application, consider NumericString or PrintableString or VisibleString or IA5String. 

character set, and you want to be as general as possible, then UTF8String is for you! The earlier UniversalString and BMPString offer few if any advantages, and should be ignored. If, however, input or output is likely to be done on more limited devices, then you may wish to consider a more restricted character string type. 

GeneralString and GraphicString, based on the International Register are obsolete, and there is no case for using them in new specifications, although they were important in the 1980's. 

The same remark applies to TeletexString (T61String) and VideotexString: you are unlikely to want to use these unless you have strong links to the associated ITU-T Recommendations. 

If your application does require use of input/output devices that may only be able to support a limited range of characters, then you must seriously consider using only NumericString, PrintableString, VisibleString (ISO646String), or IA5String. NumericString is very limited, and is not fully international, but is better from the internationalization point of view than the other three (arabic numbers are accepted over more of the world than the full range of ASCII characters). PrintableString has the slight merit that it is hard-wired into ASN.1, so there can be no misunderstandings about what characters are included, but it is essentially a cut-down ASCII with few advantages over ASCII. If you want full ASCII, then you need VisibleString (no control characters) or IA5String (includes control characters). This will be fine for English-speaking communities, and is livable-with for a number of other European languages, but is generally deprecated in any sort of international specification. 

Ultimately, the choice has to be yours as the application designer - ASN.1 merely provides the notational tools, but you probably want to restrict your choice to NumericString, PrintableString, VisibleString, IA5String, and UTF8String. You should use UTF8String if input\output devices are not likely to play a strong determining role in implementations of your application (for example, if all associated input\output will be using general-purpose computer software for keyboard input and display). 

## 14 Value notation for character string types

This book gives full coverage of the ASN.1 notation, but there are a number of parts of that notation that you will rarely need or encounter. Value notation for character strings is in that category, and value notation for control characters or characters appearing in several languages is even less commonly needed. Skip-read this section and return to it later if you find you need it! 

Names exist for all UNICODE characters, and can be used in ASN.1 to give precision to the specification of character string values without concern about ambiguity of glyphs or the character set available on your publication medium. Cell references can also be used. 

The only value notation for character string types pre-1994 was to list the characters in quotation marks. This was fine for simple repertoires like PrintableString, but did not enable control characters to be specified for a type such as IA5String, and gives ambiguity problems in printed specifications with strings such as 

## "HOPE"

if the repertoire includes Cyrillic and Greek as well as ASCII! (Each of these four glyphs appears as a character in more than one of these alphabets). There are also potential problems in printed specifications in determining what white space in character string values is intended to represent (how many spaces, "thin" spaces, etc). 

Post 1994, two additional mechanisms are available for defining a character string precisely, both of them based on listing the characters individually. 

The notation is illustrated by the following: 

```txt
my-string1 UTF8String ::= {cyrillicCapitalLetterEn,
    greekCapitalLetterOmicron,
    latinCapitalLetterP,
    cyrillicCapitalLetterIe} 
```

```autohotkey
my-string4 IA5String ::= { {0, 0}, {0, 1}, {0, 3}, "ABC", {7, 15} } 
```

As you will guess, my-string3 is the same as my-string1 (and could be printed as "HOPE"!), and my-string4 is the same as my-string2. The last two notations reference the cells (giving group, plane, row, cell) of ISO 10646 or of ASCII (formally, of Register Entry 6 of the International Register) (giving table column as 0 to 7 and table row as 0 to 15). 

The last two notations can be used freely, but the character names used in the first two notations are only available if they have been imported into your module from a module which is defined (algorithmically) in the ASN.1 specification by reference to character names assigned in ISO 10646 (and Unicode). 

To make the above value notations valid, you need the following IMPORTS statement in your module: 

```txt
IMPORTS cyrillicCapitalLetterEn, greekCapitalLetterOmicron,
latinCapitalLetterP, cyrillicCapitalLetterIe,
nul, soh, etx, del FROM
ASN1-CHARACTER-MODULE
{joint-iso-itu-t asn1(1) specification(0) modules(0) iso10646(0)}; 
```

You will also note that you can mix the different notations - character names, quoted strings, cell references - within a single value definition. 

The above works, but if your "HOPE" was actually intended to be the ASCII characters, there is a less verbose method available post-1998. You can simply write: 

```txt
my-string5 UTF8String(BasicLatin)::= "HOPE" 
```

where "BasicLatin" is imported from the ASN.1 module. You can then, in a SEQUENCE say, have an element: 

```txt
string-element UTF8String DEFAULT my-string5 
```

What we are doing here is fairly obvious - we are "qualifying" the UTF8String type to say that we are only using the BasicLatin (ASCII) part, so the "HOPE" is now unambiguously the ASCII characters. Note that in the SEQUENCE, we use the full UTF8String type. This rather simple notation rests on two powerful and general concepts, those of subtyping and of value mappings. Subtyping is the definition of a new type which contains only a subset of the values of the socalled parent type. In this case the parent type is "UTF8String", and we are using a subtype of that (defined in the ASN.1 module) called "BasicLatin" to subtype it here. The above example could actually have been written: 

## my-string5 BasicLatin ::= "HOPE"

which perhaps makes it clearer that "my-string5" is latin characters, but makes it less clear that it can be used as a DEFAULT value for UTF8String (although it still can). Subtyping is discussed in more detail in the next chapter. Whichever way "my-string5" is defined, its use as a default value for UTF8String is dependent on a general concept in ASN.1 that if something is a valuereference-name of a subtype of some type, it can also be used as a value-reference-name for a value of the parent type, and in some cases of other "similar" types. This is the value mapping concept in the ASN.1 semantic model (introduced briefly in Section I and discussed more fully in Section IV), and in this case allows "my-string5" to be used not just as a value for UTF8String, but also, should you wish it, as a value for PrintableString and VisibleString. 

## 15 The ASN.1-CHARACTER-MODULE

This module has been mentioned above. It provides value-reference-names for all the ASCII control characters (explicitly listed), and for all the characters in Unicode/ISO 10646. The character names listed in the ISO 10646 Standard (and Unicode) are given in all upper case with spaces between words. To convert to an ASN.1 name you keep the upper case letter for the first letter of every word except for the first name, change all other letters to lower-case, then remove the spaces! This produces the names we used above, and also the rather long name: 

## cjkUnifiedIdeograph-4e2a

for the Chinese/Japanese/Korean (CJK) character which looks (to a Western eye!) like a vertical bar with a caret over it, and is named in ISO 10646 as "CJK Unified Ideograph-4e2a".. 

ISO 10646 also defines 84 collections - useful sets of characters. These names are mapped into ASN.1 names for subtypes of UTF8String by the same algorithm, except that as they are types (sets of string values, not single character values), they keep their initial upper-case letter. Here are a few examples of the names that are available for import: 

```txt
BasicLatin
Latin-1Supplement
LatinExtended-A
IpaExtensions
BasicGreek
SuperscriptsAndSubscripts
MathematicalOperators
BoxDrawing
etc 
```

## 16 Conclusion

The ASN.1 character string types have evolved over time as the character set standards themselves have changed, and as input/output devices and packages have become more capable of handling a wider and wider range of characters. 

Partly to provide a mechanism that would accommodate any character repertoire and encoding scheme, the CHARACTER STRING hole type was introduced. This is described in a later chapter. 

Mechanisms were also added over time to provide for a more precise tailoring of character repertoires to user's needs, and to provide a precise and unambiguous value notation for character strings which does not depend on (the perhaps restricted set of) glyphs available for any printed ASN.1 specification, or on the character repertoire (such as perhaps only ASCII) available for any machine-readable ASN.1 specification. 

The end result is a perhaps confusing, but wide-ranging and up-to-date set of types for character string fields. 

# Chapter 3 Subtyping

# (Or: Tighten up your data types!)

Summary: This chapter describes the ASN.1 subtype notation that allows the precise definition of the set (subset) of values that you wish to allow for a type. You can, for example, specify: 

• the range of an integer; 

• minimum and/or maximum length of a string; 

• the precise characters wanted from a character set; 

• minimum and/or maximum number of iterations in a SEQUENCE OF or SET OF. 

The full notation has considerable power and flexibility, but the above examples are the ones most commonly met. 

## 1 Introduction

The ASN.1 "subtype notation" is very powerful, and it would be nice to say that it is one of the things that makes ASN.1 great! However, whilst the simpler instances of its use (length limits on strings, limits on iterations of sequence-of, ranges on integers) are common, and it is important that you use them where you can, some of the other features of this notation are seen less often, and are perhaps less important. 

Customise your types to just the precise values you need - it can often reduce the number of bits-on-the-line by more than a factor of two (if PER is in use), and gives clear guidance to implementors for memory allocation decisions, such as the size of integer to use. 

Note also (before reading on - or skipping!) that flexibility in subtype notation was considerably enhanced in 1994, so some of the examples given below would not be legal pre-1994. Check the actual ASN.1 specification! 

We have very briefly met subtyping in figure 13, where (omitting the distinguished values) we had a sequence element of: 

$$
\text { no - of - days - reported - on } \quad \text { INTEGER   (1..56) }
$$

restricting the range of the integer field to the values 1 to 56. 

In the pre-1994 ASN.1, this notation in round brackets was regarded as producing a new type consisting of a subset (hence subtyping) of the values in the original or parent type. Post-1994, the view-point tends to be more that we are constraining the integer to be in the range 1 to 56. Why the difference? Well, post-1994 a number of other constraint mechanisms were introduced (also within a pair of round-brackets following the type being constrained), but more importantly, focussing on the notation as a constraint raises the question "And what if I get incoming material that violates the constraint?". The general issue of constraints (and associated exception handling) is left to Chapter 7 of this section, but here we will fully discuss the simple subtype notation, first introduced into ASN.1 in 1986. 

When subtyping was introduced into ASN.1, the Basic Encoding Rules were not changed. They were TLV-based, and using subtype information to, for example, eliminate the "L" part, would have destroyed the structure of the encoding. So up to 1994, application of subtyping merely helped the writer of application-code - it did not affect encoding, or the number of bits-on-the-line. With the introduction of the Packed Encoding Rules (PER), the encoding is affected by subtyping (particularly of integers). To gain maximum benefit from PER, application designers should include range information (and length constraints on strings, and iteration constraints on set-of and sequence-of) whenever they reasonably can. 

In PER there is the concept of "PER-visible constraints" - things that affect the encoding. Not all subtyping constructs are PER-visible (and in particular inner subtyping - see below - is never PER-visible for good reasons). It is tempting to suggest (see figure 999 again!) that you can ignore - don't learn about, don't use - any subtyping notation that is not PER-visible, but this would be bad advice, as a new super-PER could at some stage be defined that would take account of the more complex constraints. The right advice is: "If you intend your applications to use only a subset of the values of some type, then try to express that formally using the ASN.1 subtype notation, not just as comment." 

## 2 Basic concepts and set arithmetic

Before looking at the different forms of subtype notation, it is important to recognise that subtype notation (like tagging - see the next chapter) is formally producing a new type. So wherever ASN.1 requires/allows type-notation, you can instead write: 

The subtype notation is applied to a type (the parent type) and produces a new type that contains a subset of the set of abstract values in the parent type. 

## type-notation subtype-notation

although the "subtype-notation" has to be one of the allowed notations for the parent type given by "type-notation". "subtype-notation" always begins and ends with round brackets. 

This idea can be recursively applied. So you can, for example, write: 

My-string1 ::= PrintableString (SIZE (1..10)) (FROM ("A" .. "Z")) 

This first defines a type which is PrintableString restricted to strings between and 1 and 10 characters, then further restricts this to strings that contain only the characters "A" to "Z". 

There is another subtype notation that can do the same job in one go using set arithmetic. We can write: 

```sql
INTEGER ( A EXCEPT ( B EXCEPT C ) ) 
```

$$
\text { My - string2 }:: := \text { PrintableString } (\text  SIZE(1..10)INTERSECTIONFROM("A" .. "Z"))
$$

In this notation, the "SIZE (1..10)" selects the set of all values of PrintableString that have lengths between 1 and 10 inclusive. The "FROM ("A" .. "Z")" selects all values of PrintableString which contain only the characters "A" to "Z". The mathematical intersection of these sets gives exactly the same set of PrintableString values as was specified by My-String1 above. 

In general, the construction in round-brackets contains a number of terms separated by the words "INTERSECTION", "UNION", "EXCEPT", with the "normal" precedence (INTERSECTION binds tightest, EXCEPT binds least tightly). Each term formally identifies a set of values of the parent type (PrintableString in the case above), and normal set arithmetic is applied to determine which values are in the resulting new type. 

(As an aside, it is illegal ASN.1 if the set-arithmetic results in a type being defined that has no values!). 

Note also that, to avoid confusion for the reader on precedence 

## INTEGER ( A EXCEPT B EXCEPT C )

is disallowed, and has to be written as: 

```txt
INTEGER ( ( A EXCEPT B ) EXCEPT C ) 
```

whichever was intended. There is no equivalent restriction for UNION and INTERSECTION, because if both the "EXCEPT"s above are replaced by "UNION" (or by "INTERSECTION"), the two different bracket patterns produce identical resulting sets. 

It is also possible to write 

## INTEGER ( ALL EXCEPT (1..20) )

with the obvious meaning. ("ALL" can only be followed by "EXCEPT"). 

A more complex example (exercise for the reader - find a real-world example where this sort of construction would be useful!) would be: 

```txt
My-string3 ::= PrintableString
( SIZE (1..10) INTERSECTION FROM ("A" .. "Z")
UNION
("yes" UNION "no" UNION maybe)
EXCEPT
"A" UNION B) 
```

I think you can work out what that means, but if not, come back to it when you have read what follows! Note that the absence of quotation marks around "maybe" and "B" above was not a typo! "maybe" is assumed to be a value-reference-name for a value of type PrintableString (assigned elsewhere in this module), and B is assumed to be a type-reference-name for a subtype of PrintableString (also assigned elsewhere in this module)! Remember that wherever explicit valuenotation for a value is allowed, a value-reference-name is also allowed (provided it refers to a value of the parent type), and (less obviously perhaps) wherever a subset is needed for set arithmetic, a type-reference-name can be used (provided it refers to a subtype of the parent type). 

The alert-alert-reader (!) may be beginning to ask what the exact rules are about the way a valuereference-name or type-reference-name has to be defined in order to be legal in some set-arithmetic with a particular governor (parent type). This is covered in the description of the ASN.1 Semantic Model in Sectin IV, but it is sufficient to note for now that if it would make sense to a human reader it is almost certainly legal! 

Note that value-notation for a type defined using subtype-notation is not affected by that notation - it remains the normal value notation for the parent type. 

One final global comment: the word "INTERSECTION" can be replaced by the "caret" symbol: "^", and the word "UNION" by the "vertical-bar" symbol: "|", but you are recommended not to mix and match in any one application specification! For me, ASN.1 specifications tend to be quite verbose anyway - longish names are common - so I prefer the words! 

What then are the basic terms that we can use - either as stand-alone subtype constraints in round brackets, or as part of a possibly complex set-arithmetic expression, and what set of values do they identify? 

We treat each possibility below. Note that in some cases the clause has "subtyping" or "subtype" in its heading, and in other cases the word "constraint" is used. This reflects the terms used in the ASN.1 specification itself, and reinforces the point that for most purposes the two words are interchangeable. 

## 3 Single value subtyping

This can be applied to any parent type. (Remember that there is value notation for any type we can define in ASN.1). We just list the permitted value! Normally this would be accompanied by use of vertical bar or UNION. So: 

and 

```haskell
Yes ::= PrintableString ("Yes")
Yes-No ::= PrintableString ("Yes" | "No") 
```

are examples that use single value subtyping. The set of values identified by each use of single value subtyping is just that single value identified by the value notation. 

## 4 Value range subtyping

This can only be applied directly to integer and real types, but the same construction following the word "FROM" is used to restrict the set of characters that are permitted in some character string types (see "permitted alphabet" below). 

<table><tr><td>Value range subtyping is frequently applied to specify the range of integer values.</td></tr></table>

The end-points of a range of values are given, and the set of values identified by the notation is precisely those from one end-point to the other (including the end-points). This is the notation we encountered earlier, and which is often seen to constrain integer values: 

As usual, intersections and unions of these constraints are possible, but are rarely seen. 

## 5 Permitted alphabet constraints

This is a constraint which can only be applied to the character string types (not including the type "CHARACTER STRING"). 

In its simplest form this constraint is the word "FROM" followed by a character string containing a set of permitted characters. Thus: 

Some encoding rules (unaligned PER) will use the minimum number of bits per character, depending on how many different characters you allow in a string, so imposing alphabet constraints can save bits on the line. 

or 

```txt
String-of-vowels1 ::= PrintableString (FROM ("AEIOU"))
String-of-vowels2 ::= PrintableString (FROM ("AEIOU")
UNION
FROM ("aeiou")) 
```

would be possible examples. The opening bracket following "FROM" may appear unnecessary and looks cumbersome, but the syntax definition allows a fully general constraint following FROM, so 

```lisp
String-of-vowels3 ::= PrintableString (FROM ("AEIOU" UNION "aeiou")) 
```

is also permitted. 

The constraint following "FROM" is required to be one that could be directly applied to the parent type to produce a set of string values (call this the defining set of string values (a term used only in this book). The effect of "FROM" is to allow (in the subset of string values selected by "FROM") all strings of the parent type which contain (only) any of the characters in any of the string values in the defining set. 

An exercise: read this definition carefully, then answer the question "Are String-of-vowels2 and String-of-vowels3 equivalent definitions?". Read on when you have your answer! 

We reason it through. With "String-of-Vowels2", we first define two sets of PrintableString values. One is all strings made up of upper case vowels only and the other is all strings made up of lower case vowels only, and we take the union of these two sets. Thus the end result allows strings containing only vowels, but each string must be entirely upper case or entirely lower case. With "String-of-Vowels3", we first produce a set with just two string values, each of five characters: "AEIOU" and "aeiou". We then apply "FROM" to this set, allowing as the end result strings made up of arbitrary combinations of upper and lower case vowels, so "String-of-Vowels2" and "String-of-Vowels3" are not the same. 

The above used only single value subtype notation in the constraint following FROM, but any subtype notation that can be applied to the parent type can be used. In particular, value range subtyping is explicitly permitted for application to certain character string types when it is used in the constraint following FROM, and is restricted to strings containing only a single character. 

Thus we can write: 

```lisp
Hex-digit-String ::= PrintableString (FROM ("0"..."9" UNION "A"..."Z" UNION "a"..."z")) 
```

which first forms the set of all single character strings using digits and letters (62 string values), and then applies FROM to this set to generate the set of all PrintableString values containing only these 62 characters. 

The value range constraint can be used in this way for those character string types for which an ordering of the characters is well-defined (BMPString, IA5String, NumericString, PrintableString, VisibleString, UniversalString, UTF8String), but not for character string types based on the International Register of Coded Character Sets (GeneralString, GraphicString, TeletexString, or ViedotexString), where ordering is not easy to define. 

## 6 Size constraints

A size constraint has a similar structure to a permitted alphabet constraint. It consists of the word "SIZE" followed by any constraint specification (in parentheses) that can be applied to a non-negative integer. It can (only) be applied to a bit-string, an octet-string, a 

Size constraints use value ranges to specify the permitted lengths of strings and iteration counts. Their use can again save bits on the line. 

character string (including the type "CHARACTER STRING" introduced in a later chapter) or to a "SEQUENCE OF" or "SET OF" construction. Its effect is to select those values of the parent type that contain a number of characters or iterations equal to one of the integer values in the set selected (from non-negative integers) by the constraint following the word "SIZE". 

In the case of "SEQUENCE OF Xyz" and "SET OF Xyz", the constraint can appear after the type definition, or immediately before the "OF". This is necessary to allow constraints to be applied to both the iteration counts and to the type being iterated, in cases such as 

## SEQUENCE OF SEQUENCE OF PrintableString (SIZE (10))

This syntax would restrict the PrintableString to exactly ten characters, and cannot be used to constrain the iteration counts. To constrain these, you would use 

SEQUENCE (SIZE (10)) OF SEQUENCE OF PrintableString 

or 

SEQUENCE OF SEQUENCE (SIZE (10)) OF PrintableString 

Once again, ASN.1 is fully general in this area - the constraint notation appearing before the OF is a general constraint that can contain unions and intersections etc, although the pre-1994 specifications were more restrictive. 

In practice, the constraint following the word "SIZE" is almost always a single value constraint or a value range constraint, such as: 

$$
\begin{array}{c} \text {SEQUENCE (SIZE (1..100)) OF SEQUENCE (SIZE (20)) OF} \\ \text {PrintableString (SIZE (0..15))} \end{array}
$$

```txt
PrintableString ( SIZE (1..10) INTERSECTION FROM ("A"."Z")) 
```

which could represent a table of one to one-hundred rows with twenty columns, each cell containing a PrintableString which is either empty or up to 15 characters long. 

Going back to our Wineco-protocol, and referring to figure 22 in Section I Chapter 4, we originally defined "sales-data" as an unlimited number of "Report-item". It is generally quite hard for an implementor to support unlimited numbers of things, although with increasing memory sizes now easily available and large capacity disks, implementation of "effectively unlimited" (which is what we mean here) is possible. Both the BER and PER encodings will support the transfer of effectively unlimited numbers (and sizes) of things, but with PER the encoding will be more efficient if it is possible to limit counts and integer values, for example to values which can be held in two or four octets. 

It would be common practice to replace the "sales-data" line with: 

$$
\text { sales - data } \quad \text { SEQUENCE   (SIZE   (1..sales - ub))   OF   Report - Item }
$$

The value reference "sales-ub" is required to be an integer value reference, and might be assigned in a module which collects together all such bounds, using EXPORTS/IMPORTS to make it available in the context of figure 22. A typical assignment might be: 

```txt
sales-ub INTEGER ::= 10000 
```

Consider a final example using both FROM and SIZE: 

Take a moment to work out what this means before reading on. 

We first select the (finite) set of all strings with one to ten characters in them, and we intersect that with the (infinite set) of all strings made up solely of the characters "A" to "Z". The end result is the set of strings of one to ten characters which contain only the letters "A" to "Z". Note that exactly the same result is obtained by any of: 

```txt
PrintableString (SIZE (1..10)) (FROM ("A".."Z")) 
```

```txt
PrintableString (First) (Second) 
```

where 

```autohotkey
Second ::= PrintableString (FROM ("A" .. "Z")) 
```

## 7 Contained sub-type constraints

We have met this notation informally on a couple of occasions above. This form of constraint is where we provide a type reference name (for a subtype of the parent type) to identify the set of values to be included. This would not normally be useful unless it was within a more complex constraint using intersections, or with repeated application of constraints, as in the cases 

PrintableString ( First INTERSECTION Second ) 

and 

PrintableString (First) (Second) 

above. 

Note that pre-1994, use of a type reference name in this way in a constraint required the name to be preceded by the word "INCLUDES", and it is still permissible to write (for example): 

PrintableString (INCLUDES First INTERSECTION INCLUDES Second) 

or 

PrintableString (INCLUDES First EXCEPT INCLUDES Second) 

but these do not read very well, and it is best to omit the word "INCLUDES". 

## 8 Inner Subtyping

## 8.1 Introduction

Inner subtyping is an important and under-used tool. It is often the case that application designers have invented a new meta-notation of their own (not supported by ASN.1 tools) to produce specifications which could more sensibly have been written using inner subtyping (which is supported by the OSS tool). Not only does this 

Inner subtyping is an important mechanism that can help to give precision to the specification of subsets or conformance classes of a protocol. 

require the reader to get used to the ad hoc notation, but it can also make the implementor's work unnecessarily hard, with some sort of ad hoc pre-processing of the specification needed before use of ASN.1 tools. 

It is likely, perhaps probable, that this occurs through ignorance. Inner subtyping has an overall importance which is not brought out by its positioning as "just another subtyping notation" in the ASN.1 specification. 

The subtype notations described so far provide a very powerful tool for application designers to clearly specify the range of permitted values in their protocols for the basic types, but there is another requirement: some designers have a requirement to define a number of different subsets of a protocol to suit different purposes, different so-called "conformance classes". 

In the simplest case, we have a "Full Class" protocol in which each message is some defined ASN.1 type such as the "Wineco-Protocol" in figure 21 of Section 1 Chapter 3, but we also wish to define a "Basic Class" protocol in which some of the optional elements of sequences are required to be omitted, others are required to be always included, some of the choices are restricted, and some of the iterations and/or integer values have restricted values. 

If you consider the set of abstract values of the "Wineco-Protocol" type, you will recognise that all the restrictions described above (including requiring some optional elements to be present and others to be absent) are simply the selection of a particular subset of the "Wineco-Protocol" values - in other words, subtyping! 

There are, however, two additional requirements: 

• First, it needs to be possible to define both of the conformance classes without duplication of text (and hence scope for error). 

Secondly (for some but not all applications) the encoding of those values that are present in both the "Basic Class" protocol and the "Full Class" protocol should be the same in both protocols. 

The latter requirement is so as to enable easy interworking between "Full class" and "Basic Class" implementations. 

There is a relationship between this area and the "extensibility" issues described later, but there are differences. "Extensibility" refers to differences in specifications over time (different versions) where the maximal functionality is not known when the first systems are deployed, whereas here we are concerned with differences in implementations where maximal functionality is known from the start, permitting a somewhat simpler approach. 

In order to define all conformance classes without duplication of text, it is necessary to: 

• (first) define the "Wineco-Protocol" type with maximal functionality, providing it with a type reference name; then 

to use this type reference name and apply to it the constraints which generate the "Basic-Ordering-Class" and "Basic-Sales-Data-Class" (or other conformance classes). The latter is achieved by placing subtype constraint notation, in parentheses, following the type reference name. So we have: 

$$
\text { Basic - Ordering - Class }: := \text { Wineco - Protocol } (\dots \dots)
$$

The (.......) is the inner subtyping constraint, where we constrain the inner components of "Wineco-Protocol". 

It is important to note that in both BER and PER, the application of these constraints does not affect the encoding of the values that are in the selected subset - they are encoded exactly as in the "Full-Class" protocol. By contrast, if constraints (such as removal of some choices, or making optional fields mandatorily present or absent) were specified by an ad hoc meta-language that modified the ASN.1 text (or by explicitly writing out the Basic Class protocols), the encoding of values in the Basic Class would be different from that of the corresponding values in the Full Class, and care would also need to be taken that rules on unambiguous tags (see below) were not violated with any of the variants that were produced. 

This is another reason why use of inner subtyping should be preferred to an ad hoc "pre-processor" notation - it ensures that encodings and taggings are the same in all classes. 

## 8.2 Subsetting Wineco-Protocol

Once again, let us proceed with an illustration first. Consider figure II-3. This repeats the toplevel definition of figure 21, but now we have moved to version 2 (produced in AD 2002), and have an additional top-level choice available to enable us to up-load the contents of the electronic cash in our till. (The fact that this follows an extension marker makes no difference to the inner subtyping notation, and for the moment the presence of the extension marker line should be completely ignored.) Refer also to Appendix 2 that contains the full definition of Wineco-Protocol. 

```txt
Wineco-Protocol ::= CHOICE
{ordering [APPLICATION 1] Order-for-Stock,
sales [APPLICATION 2] Return-of-sales-data,
... ! PrintableString : "See clause 45.7",
e-cash-return -- Added in version 2 --
[APPLICATION 3] Cash-upload}

Basic-Ordering-Class ::= Wineco-Protocol
(WITH COMPONENTS
{ordering (Basic-Order) PRESENT,
sales ABSENT } )

Basic-Sales-Class ::= Wineco-Protocol
(WITH COMPONENTS
{ordering ABSENT,
sales (Basic-Return) PRESENT } )

Figure II-3: Constraining in version 2 
```

Here we have restricted the outer-level choice by making precisely one of the version 1 alternatives always present and the other always absent. We are further applying included subtype constraints (see above) "Basic-Order" and "Basic-Return" to the alternative that is present, restricting it further. We will shortly define the types "Basic-Order" and "Basic-Return". 

Notice that here we have listed every alternative present in version 1, giving PRESENT or ABSENT. This is called a "full specification". Despite being called a "full specification", it is not actually necessary to list every alternative. ABSENT is implied for any not listed, so the definition of "Basic-Sales-Class" is equivalent to: 

and to 

```txt
Basic-Sales-Class ::= Wineco-Protocol
(WITH COMPONENTS
{ordering ABSENT,
sales (Basic-Return) PRESENT,
e-cash-return ABSENT}
Basic-Sales-Class ::= Wineco-Protocol
(WITH COMPONENTS
{sales (Basic-Return) PRESENT} ) 
```

(Note that there must be at least one alternative listed, and that there must be exactly one listed as PRESENT in the "full specification".) 

There is also a "partial specification" notation in which the constraint starts with "... ,". This is shown in figure II-4, where we wish the Basic-Sales-Class2 protocol to include both "sales" and "e-cash-return" messages. "Partial specification" differs from the "full specification" only in that any alternatives not listed remain as possible unconstrained choices, and any listed are neither required to be ABSENT nor PRESENT if neither of these words are present (but may be constrained in other ways). Thus in figure II-4, either the "sales" (constrained by "Basic-Return") or the "e-cash-return" messages (unconstrained) are available and have to be implemented, but the "ordering" messages should never be sent or received and need not be implemented. 

```txt
Basic-Sales-Class2 ::= Wineco-Protocol
( WITH COMPONENTS
{...,
ordering ABSENT,
sales (Basic-Return) } )
Figure II-4: Constraining only the sales alternative 
```

Let us go on to specify what is a "Basic-Return". This is shown in figure II-5 as a constrained "Return-of-sales". Note that as usual in ASN.1, we could have put the constraint "in-line" in figure II-5 and made no use of the type reference name "Basic-Report-Item". This is just a matter of style. Figure II-6 shows the same definition but with the constraint "in-line" (we have not repeated the comments in figure II-6). Whilst more compact, it is arguable that the lack of a name to associate with the inner constraint on "Report-item" in figure II-6 makes that style less readable than the slightly more verbose style of figure II-5. Both notations do, however, express exactly the same semantics. 

```txt
Basic-Return ::= Return-of-sales
( WITH COMPONENTS
    {...,
    no-of-days-reported-on (7)
    -- reports must be weekly --,
    reason-for-delay ABSENT,
    additional-information ABSENT,
    sales-data (SIZE (1..basic-sales-ub)
    INTERSECTION
    (WITH COMPONENT
    (Basic-report-item) }) 
Basic-report-item ::= Report-item
( WITH COMPONENTS
    {...,
    item-description ABSENT
    -- Version 2 of Report-item allows omission
    -- of item-description even for newly-stocked
    -- items --} )
Figure II-5: Constraining "Return-of-Sales" 
```

Figures II-5 needs a little explanation of "sales-data". Here we are further constraining the number of "Report-item"s, and also restricting each "Report-item" to the subset "Basic-report-item". Notice that when we apply inner subtyping to a SEQUENCE or SET, we start the constraint with "WITH COMPONENTS", and then have paired curly brackets with the constraints (if any) on each component listed within the brackets following the name of the component. (You can see this with the constraint on "Report-item" (which is a SEQUENCE) in Figure II-5). Now suppose that one of the components of the outer SEQUENCE is a SEQUENCE 

```txt
Basic-Return ::= Return-of-sales
( WITH COMPONENTS
    {...,
    no-of-days-reported-on (7),
    reason-for-delay ABSENT,
    additional-information ABSENT,
    sales-data (SIZE (1..basic-sales-ub)
    INTERSECTION
    (WITH COMPONENT
    ( WITH COMPONENTS
    {...,
    item-description ABSENT }) )
    }
)

Figure II-6: Applying the constraint "in-line" 
```

OF or SET OF, then we can apply a constraint to the number of iterations of the SEQUENCE OF or SET OF by directly listing it following the component name, but if we wish to constrain the type being iterated, we have to apply a further inner subtyping constraint, but this time beginning with the words "WITH COMPONENT" (instead of "WITH COMPONENTS"), followed directly by the constraint to be applied to the type being iterated. 

## 8.3 Inner subtyping of an array

As a final example, let us return to our two-dimensional array of PrintableString introduced earlier. We will first define: 

## Generic-array ::= SEQUENCE OF SEQUENCE OF PrintableString

and we will then produce a "Special-array" by inner subtyping that will be (almost - see below) equivalent to our original definition of 

```txt
SEQUENCE (SIZE(1..100)) OF SEQUENCE (SIZE(20)) OF PrintableString (SIZE(0..15)) 
```

This is what we need: 

```lisp
Special-array ::= Generic-array
(SIZE (1..100) INTERSECTION
WITH COMPONENT
(SIZE (20) INTERSECTION
WITH COMPONENT (SIZE (0..15))
)
) 
```

Why only almost equivalent? It is important to remember that a PER encoding of a Generic-array with inner subtyping is always the general encoding (inner subtype constraints are not PER visible), so an implementation of Special-array with the above constraints will produce bits on the line identical with the corresponding values of "Generic-array", whilst putting in the constraints explicitly will produce a different (more compact) encoding. Where the constraints apply to all classes of implementation, or where interworking between different classes is not required, it is clearly better to embed the constraints explicitly. Where, however, interworking is required between a full implementation and a constrained implementation, it is generally better to use inner subtyping to express the constraint. 

## 9 Conclusion

"Simple subtyping" can indeed be simple - as when a range is specified for an INTEGER type, but requires care in writing (and a good understanding of the syntax when reading) if the very powerful set arithmetic and inner subtyping features are used. 

The simplest forms of range and size constraint are very simple to apply, and should be used whenever possible. The more complex forms using set arithmetic or inner subtyping are very powerful, but are for more specialised use. 

Because in the old Basic Encoding Rules (BER), subtyping never affected the bits on 

the line, there was a tendency for writers of ASN.1 protocols not to bother to think about subtyping, and there are many specifications which, if taken at face value, would require implementations to support indefinite length integers, even 'tho' everybody knows that was never the intention. 

Both to give precision to the requirements on implementation, and also because the more recent Packed Encoding Rules will reduce the bits on the line if subtyping is applied, it is now strongly recommended that in producing new or revised protocols, subtyping is applied wherever possible and sensible. This is particularly important for ranges of integers and iterations of SEQUENCE OFs or SET OFs. 

# Chapter 4 Tagging

# (Or: Control it or forget it!)

Summary: Tagging was an important (and difficult!) part of the ASN.1 notation pre-1994. Its importance (and the need to understand it) is much less now, due to three factors: 

the ability to set an AUTOMATIC TAGS environment in the module header as described in Section I Chapter 3; 

• the provision for extensibility without relying on tags to achieve this; 

• the introduction of PER which does not encode tags. 

There are four tag classes: 

• UNIVERSAL 

• APPLICATION 

• PRIVATE 

• context-specific 

and a tag value is a class and a number (zero upwards, unbounded). 

This chapter describes the requirements on use of tags in a legal piece of ASN.1, and gives stylistic advice on the choice of tag class. 

## 1 Review of earlier discussions

We have already discussed the idea of including tags, and have introduced the concepts of implicit tagging and explicit tagging, describing these in terms of their effect on a BER encoding: changing the "T" in the TLV for the type (implicit tagging), or adding a new TLV wrapper (explicit tagging). 

This is clearly not an academically 

Tags were originally closely related to the "T" in the "TLV" of the Basic Encoding Rules (BER), and gave users control over the "T" values used for different elements and choices. This was important if interworking between version 1 and version 2 was to be easy in a BER environment with no explicit extensibility marker. 

satisfactory way of discussing tagging (but might satisfy many readers!), given that the notation is supposed to be independent of the encoding rules, and that there are now other ASN.1 encoding rules that do not use the "TLV" concept. We will therefore introduce below an encoding-ruleindependent, and slightly more abstract (sorry!), description of tags. 

In earlier text we have implied (wrongly!) - but never stated! - that the name-space for tag values is a simple integer. Indeed, we did use a tag "[APPLICATION 1]" in figure 21, which might imply a more complex name-space. We describe below the complete set of available values for tags, and the way these are normally used. 

Finally, we have already briefly mentioned that there are rules about when tags are required to be distinct (broadly, wherever the "T" of a TLV needs to be distinct from that of some other TLV to ensure unambiguity in BER encodings). We give below the actual rules. 

But as a last important reminder: post-1994 you can establish an automatic tagging environment in which you need know nothing about tags, and need never include them in your type definitions. This is the recommended style to adopt for new specifications, and is absolutely the right approach for anybody who gets confused with the text below! 

Let us look at the global level for a moment. Wherever ASN.1 requires or allows type-notation, it is permissible to write: 

tag-notation type-notation 

In other words, tagging is formally defining a new type from an old type, and tag notation can be repeatedly applied to the same type notation. So the following is legal: 

My-type ::= [APPLICATION 1] [3] INTEGER 

but would be rather pointless in an environment of implicit tagging, as the "[3]" is immediately over-ridden! You will rarely see this sort of construction - tag-notation is normally applied to a type-reference or to untagged type-notation. 

Finally, if a type is defined using tag-notation, the tag-notation is ignored for the purposes of value-notation. Value notation for My-type above is still simply "6" (for example). 

## 2 The tag namespace

Staying with BER encodings for the moment: a tag encodes in 7 bits of the "T" part of a BER TLV. 

The remaining bit is nothing to do with tagging, and is set to one if the "V" part is itself a series of TLVs (a constructed encoding such as that used for "SEQUENCE" or "SET"), and 

## Tags

• [UNIVERSAL 29]: do not use UNIVERSAL class tags. 

• [APPLICATION 10]: use for commonly used types or top-level messages. Do not re-use. 

[PRIVATE 0]: Rarely seen. Use to extend a standard with private additions (if you really must!). 

• [3]: Use and re-use in a different context. The most common form of tagging. 

to zero if the "V" part is not composed of further TLVs (a primitive encoding such as that used for "INTEGER" or "BOOLEAN" or "NULL"). 

A tag is specified by giving a class and a tag-value (the latter is indeed a simple positive integer - zero upwards, unbounded). But the class is one of four possibilities: 

UNIVERSAL class APPLICATION class PRIVATE class context-specific class 

<table><tr><td>UNIVERSAL 0</td><td>Reserved for use by the encoding rules</td></tr><tr><td>UNIVERSAL 1</td><td>Boolean type</td></tr><tr><td>UNIVERSAL 2</td><td>Integer type</td></tr><tr><td>UNIVERSAL 3</td><td>Bitstring type</td></tr><tr><td>UNIVERSAL 4</td><td>Octetstring type</td></tr><tr><td>UNIVERSAL 5</td><td>Null type</td></tr><tr><td>UNIVERSAL 6</td><td>Object identifier type</td></tr><tr><td>UNIVERSAL 7</td><td>Object descriptor type</td></tr><tr><td>UNIVERSAL 8</td><td>External type and Instance-of type</td></tr><tr><td>UNIVERSAL 9</td><td>Real type</td></tr><tr><td>UNIVERSAL 10</td><td>Enumerated type</td></tr><tr><td>UNIVERSAL 11</td><td>Embedded-pdv type</td></tr><tr><td>UNIVERSAL 12</td><td>UTF8String type</td></tr><tr><td>UNIVERSAL 13 - 15</td><td>Reserved for future editions of this Recommendation | International Standard</td></tr><tr><td>UNIVERSAL 16</td><td>Sequence and Sequence-of types</td></tr><tr><td>UNIVERSAL 17</td><td>Set and Set-of types</td></tr><tr><td>UNIVERSAL 18-22</td><td>Character string types</td></tr><tr><td>UNIVERSAL 23-24</td><td>Time types</td></tr><tr><td>UNIVERSAL 35-30</td><td>More character string types</td></tr><tr><td>UNIVERSAL 31-...</td><td>Reserved for addenda to this Recommendation | International Standard</td></tr></table>


Figure II-7: Assignment of UNIVERSAL class tags


In the tag notation, a number alone in square brackets denotes the tag-value of a context-specific class tag. For the other classes, the name (all upper-case) of the class appears after the opening square bracket. 

For example: 

```txt
[UNIVERSAL 29] tag-value 29, "universal" class
[APPLICATION 10] tag-value 10, "application" class
[PRIVATE 0] tag-value 0, "private" class
[3] tag-value 3, "context-specific" class 
```

I like to think of the four classes of tag as just different "colours" of tag (red, green, blue, yellow). The actual names do not matter. For most purposes, the "colour" of the tag does not matter either! All that matters is that tags be distinct where so required, and they can differ either in their "colour" (class) or in their tag-value. The colour you choose to use is mainly a matter of style. 

There is only one hard prohibition: users are not allowed to tag types with a UNIVERSAL class tag. This class is (always) used for the "default tag" on a type, and values of such tags can only be assigned within the ASN.1 specification itself. 

Figure II-7 is a copy of a table from X.680/ISO 8824-1 (including all amendments up to September 1998), and gives the UNIVERSAL class tag assigned as the default tag (used unless overridden by implicit tagging) for each of the type notations and constructor mechanisms defined in ASN.1. 

The main reason for forbidding use of UNIVERSAL class tags by users is to avoid problems when future extensions to ASN.1 occur. It is, however, important to note that this is no real hardship, as every tag has equal status with every other tag, no matter what its "colour" (class). 

There have been specifications that conformed to pre-1994 ASN.1, but wanted to use UTF8String (added 1998), and decided to copy the text of the post-1994 definition into their own application specification. This is probably harmless, but is strictly in violation of the specification. As well as being illegal, it is also unnecessary to copy the text and to assign a UNIVERSAL class tag in the copied text - an APPLICATION class tag can be used in the definition of the type, and provided the type is implicitly tagged wherever it is used, the end-result is indistinguishable from an initial assignment with a UNIVERSAL class tag, as later implicit tagging will override either. 

So what about the other three classes of tag? Which one should be used when? To repeat: they are all equivalent. Use PRIVATE class tags absolutely everywhere if you wish! But as a matter of style, most people use context-specific class tags most of the time (they are the easiest to write - just a number in square brackets!). The name "context-specific" implies that they are only unambiguous within some specific context (typically within a single SEQUENCE, SET, or CHOICE), and it is normal to use (and to re-use) these tags (from zero upwards) whenever you need to tag the alternatives of a CHOICE or the elements of a SEQUENCE or SET to conform to the rules requiring distinct tags in particular places (see below). 

It is also common practice (but by no means universal nor required) to use APPLICATION class tags in the following way: 

• An application class tag is only used once in the entire application specification, it is never applied twice. 

If the outer-most type for the application is a CHOICE (it usually is), then each of the alternatives of that choice are tagged (implicitly if possible) with APPLICATION class tags (usually [APPLICATION 0], [APPLICATION 1], [APPLICATION 2], etc). We saw this approach in Figure 21 of Section I Chapter 3. 

If there are some complex types that are defined once and then used in many parts of the application specification, then when they are defined they are given an application class tag (and this tag is never given to anything else), so they can be safely used in a choice (for example) with no danger of a violation of any rules requiring distinct tags (unless the identical type appears again in the CHOICE - presumably with different semantic). 

An example of this might be the types "OutletType" and "Address" in Figures 13 and 14 of Section I Chapters 3 and 4. So in Figure 14 we might write instead: 

$$
\begin{array}{l} \text {OutletType}: := [ \text {APPLICATION 10} ] \text {SEQUENCE} \\ \{\dots . \\ \dots . \\ \dots . \} \\ \text {Address}: := [ \text {APPLICATION 11} ] \text {SEQUENCE} \\ \{\dots . \\ \dots . \\ \dots . \} \end{array}
$$

taking the decision to use application class tags 0 to 9 for top-level messages, and 10 onwards for commonly-used types. 

There is no limit to the magnitude of a tag-value, but when we examine BER in Section III, we will see that a "T" will encode in a single octet provided the tag-value to be encoded is less than or equal to 30, so most application designers usually try to use tag-values below 31 for all their tags. (But there are specifications with tag values in the low hundreds) 

PRIVATE class tags are never used in standardised specifications. They have been used by some multi-nationals that have extended an international standard by adding extra elements at the end of some sequences or sets. The assumption here (as with most jiggery-pokery with tags) is that BER is being used, and the (reasonable) hope is that by adding new elements with PRIVATE class tags, these will not clash with any extension of the base standard in the future. 

## 3 An abstract model of tagging

Note: This material is not present in the ASN.1 specification. It is considered by this author to be a useful model to provide an encoding-ruleindependent description of the meaning of tagging at the notational level, and a means of specifying the behaviour of encoding rules. Most ASN.1 "experts" would probably accept the model, but might argue that it is not needed, and is only one 

We can model tagging as affecting a tag-list associated with every ASN.1 abstract value. Some encoding rules use some or all of the tags in the tag-list as part of the encoding. 

of several possible ways of modelling what the ASN.1 notation is specifying, in order to link it cleanly to encoding rules. (See Figure 999 again!). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/8e5aa554d9f8bbc0a5500031f64ed60a8508594e0621251e2fd952320dbfd62a.jpg)


In order to provide a means of describing the effects of tagging we introduce a model of ASN.1 abstract values (the "things" that are in ASN.1 types) which involves some structure to these values. This is shown in figure II-8. 

In figure II-8 we see that each ASN.1 abstract value is made up of a basic-value (like "integer 1", "boolean true", etc), together with an ordered tag-list consisting of one or more tags (an innermost, closest to the basic-value, and an outermost, furthest away). Each tag consists of, as described earlier, a class and a tag-value. 

When a type is defined using ASN.1 type-notation such as "BOOLEAN" or "INTEGER", or as the result of using notation such as SEQUENCE or SET, all its values are given the same tag-list - a single tag (which is both innermost and outermost) of the UNIVERSAL class. The tag-value for each type notation is specified in the ASN.1 specification, and repeated in figure II-7 above. (We have referred to this as the "default tag" for the type in earlier text). 

There are only two operations that are possible on a tag-list. If a type is implicitly tagged, then the outer-most tag is replaced by the new tag specified in the tagging construction. If a type is explicitly tagged, then a new outer-most tag is added to the tag list. Note that all ASN.1 abstract values always have at least one tag. They acquire additional tags by explicit tagging, and can never have the number of tags reduced. 

With this model of tagging, we can now define our Basic Encoding Rules as encoding a "TLV" for each tag in the tag-list, from the outermost to the innermost tag, where the tag forms the "T", the "L" identifies the length of the remainder of the encoding of the ASN.1 abstract value, and each "V" apart from the last contains (only) the next TLV. The last "V" contains an encoding identifying the basic value. 

The reader will recognise that this gives exactly the same encoding as was obtained when we described explicit tagging as "adding an extra layer of TLV", but the use of the abstract model makes it unnecessary to describe the meaning of the notation in encoding rule terms. We use the concept of a tag-list as a sort of indirection between the notation and the encoding rules. It represents information which an ASN.1 tool will normally need to retain between syntax analysis and other functions. 

Finally, but very importantly, note that for most types, all the values in the type have exactly the same tag-list. If we apply further tagging to the type, we will change the tag-list (add a new tag or replace the outer-level tag) for each and every value in that type. 

Moreover, for many purposes (in particular what tag values are permitted) all that matters is the outer-most tag. It is thus meaningful to talk about "the tag of the type", because every abstract value of that type has the same tag-list (and hence the same outer-level tag). There is, however, one exception to this simple situation. 

The CHOICE constructor is modelled as forming a new type whose values are the union of the set of values in each of the alternatives, with each value retaining its original tag-list. Thus for the choice types, it is not meaningful to talk about "the tag of the type", as different abstract values in the type have different tag-lists. (It is important to remember this if you see text in canonical encoding rules saying "the elements are sorted into tag-order" - look for some qualifying text to cover the case of a choice type!) 

Suppose, however, that a choice type is explicitly tagged (the only form of tagging allowed for choice types). Then whilst the tag-list on different abstract values may (will) still differ, the outermost tag is the same for all abstract values in the type, and the explicitly tagged choice is just like any ordinary type - every abstract value has the same outer-level tag and we can talk about this as "the tag of the type". 

So we can now recognise that most types have a single associated tag (the common outer-level tag for all abstract values of that type), that we can call "the tag of the type", but that an untagged choice type has many tags associated with it (all the outer-level tags of any of its values). If none of the alternatives of this choice are themselves choices, then the number of outer-level tags (all distinct) associated with this choice type will be equal to the number of its alternatives. If, however, some alternatives are themselves choice types, they will each bring to the table multiple (distinct) outer-level tags, and the outer-level choice type will have more (distinct) tags associated with it than it has alternatives. 

For example, if: 

$$
\begin{array}{l} \text {My - choice}:: := \text {CHOICE} \\ \left\{\text {alt1} \quad \text {CHOICE} \right. \\ \left. \begin{array}{l} \left\{\text {alt1 - 1} [ 0 ] \text {INTEGER}, \right. \\ \text {alt1 - 2} [ 1 ] \text {INTEGER} \}, \\ \text {alt2} [ 2 ] \text {EXPLICIT My - choice2} \end{array} \right\} \end{array}
$$

then the tags associated with "My-choice" are context-specific zero, one, and two. Any tags in "My-choice2" are hidden by the explicit tagging. 

With this concept of "the tag of the type", or rather "the tags associated with the type" (which are always distinct), we can go on to discuss the rules for when distinct tags are required. 

# 4 The rules for when tags are required to be distinct

The rule is that distinct tags are required: 

When do we need distinct tags? 

• for the alternatives of a CHOICE; 

• for the elements of a SET; and 

• for consecutive DEFAULT or OPTIONAL elements and any following mandatory element in a SEQUENCE. 

There - its simple really, isn't it? (Skip the rest!) 

The rules given below (and in the ASN.1 specification) are expressed in terms of tag uniqueness, but are most easily remembered if you know that they are the minimum necessary rules to enable a TLV-style of encoding to be unambiguous! Alternatively, just remember the rules and forget the rationale! 

Within a CHOICE constructor, the collection of tags brought to the table by each alternative have all to be distinct. (Remember, each alternative brings just one tag to the table - the common outerlevel tag of the tag-list of its abstract values, unless it is an untagged choice type, when it brings to the table at least one tag for each alternative of the choice type, but these are all distinct.) 

Similarly, within a SET constructor, the tags of all the elements have to be distinct, with any elements that are choice types again potentially contributing several distinct tags to the matching process. 

Within a SEQUENCE constructor, the rules are a little more complicated. In the absence of DEFAULT or OPTIONAL, there are no requirements for distinct tags on the elements of a sequence type. However, in the presence of DEFAULT or OPTIONAL, the situation changes slightly: for any block of successive elements marked DEFAULT or OPTIONAL, together with the next mandatory element, if any, the tags of all elements in that block are required to be distinct. 

You will want to think about that for a moment. Clearly the block of DEFAULT or OPTIONAL elements must all have distinct tags, or (in BER) the receiver won't know which are present and which missing, but equally, if one of those tags matched the next mandatory element there could again be confusion. By requiring that the following mandatory element has a tag distinct from any element of the preceding block, then the appearance of that tag in an encoding gives complete knowledge that the block of OPTIONAL or DEFAULT elements is complete, and processing of the remainder of the sequence elements can proceed in a normal manner. 

There is only one small additional complication if you are trying to control your tags without using automatic tagging. That is an interaction between the extensibility marker and the rules for distinct tags, in circumstances where there are multiple extension markers within a sequence (for example, one on a choice element in the sequence and one at the end of the sequence). The purpose of the rules here is to ensure that if a version 2 specification adds elements, a version 1 system receiving those elements will be in no doubt (with BER – there is never a problem with PER!) about whether the version 2 specification (of which, of course, it has no knowledge!) had extended the choice element or added further elements to the sequence. (This can matter if different exception handling had been specified in version 1 in the two cases.) For details of these additional requirements see the discussion in the next chapter on Extensibility. 

For those of a philosophical bent, you may wish to ponder how much simpler these rules could have been if (in BER, which really dictated the rules) all CHOICE constructions had automatically produced a TLV wrapper with a default tag (say UNIVERSAL 15), in the same way as SEQUENCE! Anybody using this book as an academic text might want to set that question as an exercise for the better students! Please note that whilst PER does not have a TLV philosophy, it does none-the-less have explicit encoding associated with CHOICE, which BER does not. One day some-one will invent the perfect encoding rule philosophy! 

## 5 Automatic tagging

## This clause is solely for implementors!

What tags are applied in an "automatic tagging" environment? First, if anyh piece of SET, SEQUENCE or CHOICE notation contains a textually present tag on any of its outer-level elements or alternatives, automatic tagging is disabled for the outer-level of that notation. Otherwise, tags [0], [1], [2], etc. are successively applied to each element or alternative in an environment of implicit tagging. (So elements/alternatives that are CHOICE types get explicitly tagged and all other elements get implicitly tagged.) 

## 6 Conclusion

Tagging appears complex, but once understood is a relatively simple matter. In early specifications it became common, as a matter of style, to simply tag all elements of SEQUENCEs and SETs and alternatives of CHOICEs with context-specific (implicit) tags from zero upwards (avoiding the word "IMPLICIT" if the type being tagged was itself a CHOICE). 

With the introduction of an "implicit tagging" environment, this became somewhat easier, but if this is desired, it is essentially what automatic tagging provides. 

There are few specifications where the minimum necessary tagging is used. Writers of ASN.1 protocols tend to be more "symmetric" (or lazy?) than a minimalist approach would require. 

It is the firm recommendation of this author that all new modules be produced with automatic tagging, and for tags to be forgotten about! 

# Chapter 5 Extensibility, Exceptions, and Version Brackets

# (Or: There is always more to learn!)

## Summary: This chapter:

describes the "extensibility" concept of interworking between version 1 systems and later version 2 systems; 

explains the need for an "extension marker" to indicate where version 2 additions might occur; 

• describes all the places where an extension marker is permitted; 

• explains the need for defined exception handling when an extension marker is used; 

• describes the notation for "version brackets" to group together elements added in later versions; and 

• describes the interaction between extensibility and the requirements for distinct tags. 

Presence in appropriate places of the extension marker is key to use of the Packed Encoding Rules (PER) which generate encodings approximately 50% the size of those produced by the Basic Encoding Rules (BER). 

Writers of ASN.1-based protocols are very strongly encouraged to include extension markers (with defined exception handling) in their version 1 specifications in order to minimise problems in the future. 

## 1 The extensibility concept

NOTE — In this chapter, the acronyms BER (Basic Encoding Rules) and PER (Packed Encoding Rules) are used without further explanation. 

What is "extensibility"? "Extensibility" refers to a combination of notational support, constraints on encoding rules, and 

You wrote your specification three years ago, there are many fielded implementations - success! But you want to make additions. How do you migrate? What will version 1 systems do with your additions? ASN.1 extensibility gives you control. 

implementation rules. This support enables a protocol specified (and implemented) as version 1 to be upgraded some years later to version 2 in specifically permitted ways. Provided the version 2 extensions are within the permitted set of extensions (and provided the version 1 protocol was marked as "extensible"), then there will be a good interworking capability between the new version 2 systems and the already-deployed and unmodified version 1 systems. 

The keys to extensibility are: 

To ensure that version 2 additions or extensions are "wrapped up" with length counts in encodings, and can be clearly identified by version 1 systems as "foreign material". 

• To provide a clear specification that version 1 systems should process the parts of the encoding that are not "foreign material" in the normal version 1 way, and should take defined and predictable actions with the "foreign material". 

• To avoid unnecessary (and verbose) wrappers and identifications in encodings by using notational "flags" on where version 2 additions or extensions may need to be made. 

For the extensibility concept to be successful, all three of these components must be present. 

A detailed discussion of possible exception handling actions is given in Section I Chapter 7. 

With the BER encoding rules, all fields have a tag and a length associated with them, covering the first point above, but producing the verbosity we want to avoid in the third point. BER itself says nothing about point 2. Some forward-thinking application designers did include text such as: "Within a SEQUENCE or SET, implementations should ignore any TLV which has a tag that is not what is expected in their version", but this was by no means universal, and it was in general not possible to specify different action on "foreign material" in different parts of the protocol. With the PER encoding rules, length wrappers are often missing, and tags are always missing. PER has to be told where to insert length wrappers and to encode presence or absence of version 2 material if extensibility is to be achieved without undue cost. This is the primary purpose of the "extension marker". 

## 2 The extension marker

What does the extension marker look like? We have already encountered it in Figure 21 and Figure 22 of Section I Chapters 3 and 4. It is the ellipsis (three dots) following the "sales" alternative in line 26 of Figure 21, and following the "sales-data" element in Figure 22. 

Look out for the three little dots. Put them in as often as you like, they cost you little on the line. (Zero in BER, one bit in PER). 

If the reader now refers to Figure II-3 in Chapter 3, we see another element being added after the extension marker in the "Wineco-protocol" CHOICE of Figure 21. This is our version 2 addition. 

(Note that an ellipsis is also used following "WITH COMPONENTS {". This is a separate use of three dots, pre-dating the extensibility work, and should not be confused with extensibility.) 

## 3 The exception specification

It is strongly recommended that all uses of extensibility be accompanied by an exception specification, unless the same exception handling is specified for the entire application. 

The exception specification makes clear what implementors of version 1 systems are supposed to 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/3ba760c910562416911ec4e92ce2432e69323649a5a24d10df630d536d241448.jpg)


do with "foreign material" in this position in the message (as in Figures 21 and 22), but this recommendation is not universally followed at this time. 

The syntax of the exception specification (which can appear immediately after any ellipsis which indicates extensibility) is either an integer value, or the name of any ASN.1 type followed by a colon followed by a value of that type. Typical examples would be: 

The first two might be used where there are a list of numbered exception handling procedures, and would identify which to apply in each position of added material. The third might be used where exceptions always give error reports, and the value is just the text for the error report. The final example might be used where "My-Type" has been defined as a SEQUENCE with the first element an enumeration of possible actions (for example, "abort", "returnError", "ignore", "treatAsMaximum" and the second (optional) element as a character string qualifying those actions. Note that "treatAsMaximum" might be an appropriate exception handling procedure for an ellipsis that was within a constraint, whilst "Ignore" is clearly only applicable to added material in a SEQUENCE or SET. For an unexpected CHOICE alternative, "returnError" might be desired. ASN.1 provides the notational tools, but only the application designer can decide how to use them appropriately. (For more discussion, see Section I Chapter 7.) 

## 4 Where can the ellipsis be placed?

In the first ASN.1 extensibility specification, ellipses could be placed (and extensions added serially after them) as follows (illustrations in Figure II-9 give the version 1 text followed by the version 2 text): 

• At the end of any SEQUENCE or SET or CHOICE (see figures 21 and II-3). 

• Wherever there is a constraint (see figure II-9). 

• At the end of the list of enumerations in an ENUMERATED type (see figure II-9). 

```txt
INTEGER (0..255, ... ) or INTEGER (0..255, ... !1)
INTEGER (0..255, ..., 0..65535) INTEGER (0..255, ... !1, 0..65535)
ENUMERATED {red, blue, green, ... }
ENUMERATED {red, blue, green, ..., purple}
Figure II-9: Illustrations of extensibility marker use 
```

An early addendum to the ASN.1 extensibility specification allowed the insertion point for new material in a SEQUENCE, SET or CHOICE (but nowhere else) to be not just at the end, but in the middle. This was flagged by the use of two ellipsis elements as shown in Figure II-10. Again we have included the exception specification to remind implementors that the handling of foreign material at this position is specified in clause 50 of the application specification. 

```txt
SEQUENCE
{field1 TypeA,
    field2 TypeB,
    ... ! PrintableString : "See clause 50",
    -- Version 2 material goes here.
    ...
    field3 TypeC}
Figure II-10: An insertion point between elements 2 and 3 
```

## 5 Version brackets

The same addendum introduced version brackets, with an opening bracket of a pair of "[[" and a closing bracket of "]]". These were introduced to reduce the number of length wrappers needed at any given insertion point to the minimum necessary - one wrapper for each new version, 

Version brackets not only save bits on the line but provide a historical record of the additions that have been made to the protocol. 

and also because application designers felt they would like to be able to identify for historical purposes what was in version 1, version 2, version 3, etc. With extensions for versions 2 and 3, the above sequence could look like figure II-11. 

```txt
SEQUENCE
{field1 TypeA,
    field2 TypeB,
    ... ! PrintableString : "See clause 59",
    -- The following is handled by old systems
    -- as specified in clause 59.
    [[ v2-field1 Type2A,
    v2-field2 Type2B ]],
    [[ v3-field1 Type3A,
    v3-field2 Type3B ]],
    ... ,
    -- The following is version 1 material.
    field3 TypeC}
Figure II-11: An insertion point with two version additions 
```

It should be noted that extensibility can be identified independently for each SEQUENCE, SET and CHOICE, even if these constructs are nested within other extensible constructs. However, within any one such construct there can be at most one insertion point at the outer level of that construct, with material being successively added at the insertion point after any already inserted material. 

Version brackets should normally be employed even if there is only one element added, to provide a clear documentation of the revision history. 

Note also that version brackets can only be inserted in SEQUENCE, SET, and CHOICE constructs, not in ENUMERATED or constraints. 

At the time of writing this book (mid-1999), there are a number of published specifications that have inserted extension markers, and some that contain added material and version brackets. 

## 6 The {...} notation

You will encounter what appears to be an extensible empty "table constraint" (see later) in a number of specifications. This relates to the use of Information Object Classes, and discussion of it is deferred until Chapter 7 of this Section. 

## 7 Interaction between extensibility and tagging

When tagging was discussed in the previous chapter, it was noted that extensibility gave rise to some further requirements on the distinctness of tags. 

These requirements arise because if there are several extension markers in an ASN.1 type, they may have different exception specifications associated with them, and it is therefore important for version 1 systems to be able to unambiguously associate "foreign" material with a specific insertion point and hence exception specification. 

NOTE — Explanations given in this text may be hard to understand without a clear understanding of the BER encoding rules. Readers that are progressing sequentially through this book should either just accept that there are further rules on tagging that are "ad hoc" and curious, or else read the text on BER and return to this section. Sorry! I can do no better! 

It is fortunate (as PER does not encode tags) that there are no problems in this area with a PER encoding. However, with BER, constructions like the following give real problems: 

$$
\begin{array}{l} \text {Example1}: := \text {SEQUENCE} \\ \quad \{\text {field1 CHOICE} \\ \quad \{\text {alt1 INTEGER,} \\ \quad \dots ! 1 \} \text {OPTIONAL,} \\ \quad \dots ! 2 \} \end{array}
$$

or 

Example2 ::= CHOICE {alt2 CHOICE {alt3 INTEGER, ...!3 }, ...!4} 

Now suppose that in version 2 additions are made at the insertion points with exception handling !1 or !2. If "field1" had not been optional it would have been easy - presence of foreign material before the presence of "alt1" is clearly a !1 case, and after it a !2 case. But with field1 being optional, there is no way for version1 systems to determine whether we have new material at !1, or !1 being missing and new material at !2. A similar problem arises with new material at !3 or !4. 

Note that the problem is not with the tag on any added material, the problem is fundamental to the use of extensibility in these constructs. 

Unless BER were to be changed (shrieks of horror - BER long precedes extensibility!) it is necessary to make the two above (and other similar) constructs illegal. How to do that? 

The ASN.1 Specification adopts a slightly curious approach. It says that wherever there is an extension marker, you should add (at the end of any existing extensions) a "conceptual element" whose tag matches that of no other element except other "conceptual element"s. Then you apply rules about when distinct tags are required, and if they are satisfied, you are legal (and there will be no problems for a version 1 system to unambiguously assign foreign material to a single insertion point). 

In the first of the above cases, addition of the conceptual element in the !1 position means that "field1" brings to the table both the INTEGER tag and the tag of the conceptual element. The latter clashes with the tag of the following (mandatory) conceptual element in the !2 position, so the construction is illegal. 

In the second of the above cases, "alt2" brings to the table the tag of the conceptual element (as well as the INTEGER tag), which again clashes with the tag of the conceptual element in the extension !4. So again we have illegality. 

(Please refer to Figure 999 again!) It is important to note here that this is a distinct complexity with extensibility. Having given earlier advice that you should use AUTOMATIC TAGS, and then forget about tagging, I am now saying (and the ASN.1 Specification is saying) that in order to determine whether some extensibility constructions are legal or not requires that you have a fairly sophisticated understanding of tagging. Of course, if you use a tool such as that provided by OSS to check your ASN.1, it will instantly tell you that you have broken the rules, although whether you will understand the error message in these cases is more questionable! 

## So .... we need some simple advice:

• If a CHOICE is OPTIONAL in some SEQUENCE, make sure it is not the last element before an extension marker, or make sure it is not itself extensible. (And don't follow it by another extensible CHOICE!) 

• If a CHOICE is in a SET, make sure that only one of the CHOICE and the SET are extensible. 

• Never put an extensible CHOICE in another extensible CHOICE. 

In summary, treat extensible CHOICEs like radio-active material - keep them well apart, and clearly separated from other extension markers! If you do that, there will never be any problems. 

These rules really are ad hoc, but they are simple to apply, and will eliminate the problems described above. 

Of course, if you break these rules, you are writing de jure illegal ASN.1, and a good tool will tell you so, and probably refuse to encode it! But if you encode it yourself .... well, problems only arise in practice if you have different exception handling on the various extensions. Just keep the above points in mind, and you should be OK. 

## 8 Concluding remarks

We have described the extension marker and its association with the exception specification, and the complications arising from BER, which give rise to the need to produce some complex rules on when apparently innocuous extension markers are illegal. 

Finally, it is important to note that the interworking that extensibility provides between version 1 and version 2 systems is dependent on the extension marker being present in version 1, and in changes being made to the protocol only as permitted by the extensibility provisions (addition of elements, alternatives, enumerations, at the insertion point, and relaxation of constraints). 

If changes are made to a specification that are not covered by the extensibility provisions (such as random insertion of new elements), then the encodings of that new version are likely to produce unpredictable effects if sent to a version 1 system. Similarly, insertion of an extensibility marker in version 2 which was not present in version 1 means that encodings of the version 2 material will produce unpredictable effects if sent to version 1 systems. 

The unpredictability described above may be simply between "Will they abort in some way or will they ignore the apparent error?", but could be "With encodings of some version 2 values version 1 systems will think they are correct encodings of totally unrelated version 1 values" and will act accordingly, which could be very dangerous. So it is generally important to prevent encodings of version 2 types that do not obey the extensibility rules from being sent to version 1 systems. This can, of course, be done in many ways, the most common being some form of version negotiation when a connection is first established. 

Extensibility and exception handling are powerful tools, and enable highly optimised encoding rules to be used. They are safe if the rules governing their use are obeyed. 

It is, however, very important to insert extension markers fairly liberally into version 1 specifications (or to use the EXTENSIBILITY IMPLIED notation). 

# Chapter 6 Information Object Classes, Constraints, and Parameterization

## (Or: Completing the incomplete - with precision)

## Summary:

This chapter: 

• provides a brief description of the concept of "holes" in protocols; 

describes briefly the ROSE (Remote Operations Service Element) protocol in order to provide a specific example of the need to define types with "holes" in them, and the need for notation to support clear specifications in the presence of "holes"; 

provides a clear statement of the Information Object, Information Object Class, and Information Object Set concepts, and the use of those Object Sets to complete a partial protocol specification by constraining "holes" (and the consistency relationships for filling in multiple holes) left in a carrier protocol. 

It goes on to describe: 

the syntax for defining an Information Object Class, Information Objects, and Information Object Sets, using a development of the wineco protocol as examples; 

the means by which defined Information Object Sets can be related to the "holes" that they are intended to constrain, using a simplified version of the ROSE protocol as an example; 

• describes the need for parameterization, and the parameterization syntax of ASN.1 specifications. 

It is supposed to be bad practice to tell a student that "what I am about to say is difficult"! But the information object concepts are among the more conceptually difficult parts of ASN.1, and we will introduce these concepts gently in this chapter and fill in final details in the next chapter. Just skip-read this chapter if it is all too easy! 

# 1 The need for "holes" and notational support for them

## 1.1 OSI Layering

This is probably the first time in this book that Open Systems Interconnection (OSI) has been seriously discussed, although it was within the OSI stable that ASN.1 was first standardised. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/ab65f9c3f11e42a7381c3436c02843a72d5e56689fa6c25ea3cb99bd66840a69.jpg)


OSI was perhaps the first protocol suite specification to take seriously the question of documenting its architecture, with the production of the OSI 7-layer model. Many vendor-specific protocols had some concept of layering, and the TCP/IP work had split off IP from TCP in the late 1970s, but the OSI model was the most complete attempt at describing the concept of layering. 

The 7-layer model was (in 1984) just the latest attempt to try to produce a simplification of the (quite difficult) task of specifying how computers would communicate, by dividing the task into a number of separate pieces of specification with well-defined links between those pieces of specification. 

Although this "architecture" was primarily aimed at making it possible for several groups to work on different parts of the specification simultaneously, an important off-shoot was to provide reusability of pieces of specification. This included re-usability of network specifications to carry many different applications over the same network, or re-usability of application specifications to run over many different network technologies, some of which may not have been invented when the application specification was first written. 

The reader should contrast this with the early so-called "link" protocols (mainly deployed in the military arena, but also in telephony), where a single monolithic specification (document) completely and absolutely defined everything from application semantics to electrical signalling. 

In the International Standards Organization (ISO) 7- layer model, each layer provided a partial specification of messages that were being transmitted, each message having a "hole" in it (called user-data) that carried the bit-patterns of the messages defined by the next higher layer. However, there was a "fan-out" and "fan-in" situation: many possible lower layers (for example, transport or network protocols) could be used to carry any given higher-layer messages, and any given transport (or network) could carry many different higherlayer messages. It was a very flexible many-to-many situation. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/b4138b9fe609cd5a9def681198432579878f7d5284286a6a59dcbe62f098cc36.jpg)


But the basic concept in the original ISO OSI model was that every application layer specification would fill in the final hole - each application layer standard would produce a complete specification for some application. 

It was the CCITT 7-layer model (eventually adopted by ISO) that brought to the table the concept of partial specifications of "useful tools" in the application layer, recognising a potentially infinite set of layers, each filling in a "hole" in the layer beneath, but itself leaving "holes" for other groups to fill in due course. 

As ASN.1 increasingly became the notation of choice for defining application specifications, there clearly became a need for support in ASN.1 for "holes". 

## 1.2 Hole support in ASN.1

Forget about theoretical models for now. It rapidly became clear that people writing application specifications using ASN.1 in 1984 wanted to be able to write a "generic" or "carrier" specification, with "holes" left in their datatypes, with other groups (multiple, independent, groups) providing specifications for what filled the holes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/3d1443e66bcc5b68e9aea1b13de248457a68e9633c2cec888ef90a8d5502dee6.jpg)


At this point it is important to recognise that "leaving some things left undefined, for others to define", can (most obviously) be an undefined part of the format of messages (the user-data in OSI layering), or one of the elements in an ASN.1 sequence, but can also be an undefined part of the procedures for conducting a computer exchange. Both types of "holes" have occurred in real specifications, and notation is needed to identify clearly the presence and nature of any "holes" in a specification, together with notation for "user" specifiers to fill in the "holes". 

There is one other important point: if several different (user) groups provide specifications for applications which fit in the holes of some carrier or generic protocol, it often happens that implementations wish to support several of these user specifications, and need to be able to determine at communication-time precisely which specification has been used to fill in the hole in a given instance of communication. This is rather like the "protocol id" concept in a layered architecture. We recognise the need for holes to carry not just some encoding of information for the user specification, but also an identification of that specification. 

The earliest ASN.1 support for "holes" was with the notation "ANY", which (subject to a lot of controversy!) was withdrawn in 1994, along with the "macro notation" which was an early and largely unsuccessful attempt to relate material defining the contents of a hole (for a particular application) to a specific hole occurrence (in a carrier specification). 

In 1994, the ASN.1 "Information Object Class" and related concepts matured, as the preferred way of handling "holes". In this chapter we next introduce the concepts of ROSE (Remote Operations Service Element), showing how ROSE had the need for notation to let its users complete the holes left in the ROSE protocol. We then briefly describe the nature of the information that has to be supplied when a user of the ROSE specification produces a complete application specification. We then proceed to the concepts associated with ASN.1 "Information Object Classes". 

## 2 The ROSE invocation model

## 2.1 Introduction

One of the earliest users of the ASN.1 notation was the ROSE (Remote Operations Service Element) specification - originally 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/884bc2966c5486dd2e3e45021bf79a680dfc07546052a06d8237ee959f1f6473.jpg)


just called ROS (Remote Operations Service). This still provides one of the easiest to understand examples of the use of the Information Object Class concept, and a little time is taken here to introduce ROSE. 

The reader should, however, note that this treatment of ROSE is NOT complete, and that when tables of information are introduced, the latest version of ROSE has many more columns than are described below. There have been a number of specifications that have written their own version of ROSE, with some simplifications and/or with some extensions, so if you see text using "OPERATION" or "ERROR", check where these names are being imported from. They may be imported from the actual ROSE specification, or they may be a ROSE "look-alike". The definitions in this text are a ROSE "look-alike" - they are a simplification of the actual ROSE definitions. 

A common approach to the specification of protocols by a number of standardization groups (of which the latest is CORBA) is to introduce the concept of one system invoking an operation (or method, or activating an interface) on a remote system. This requires some form of message (defined in ASN.1 in the case of ROSE) to carry details for the operation being invoked, the three most important elements being: 

• some identification of this invocation, so that any returned results or errors can be associated with the invocation; and 

• some identification of the operation to be performed; and 

• the value of some ASN.1 type (specific to that operation) which will carry all the arguments or input parameters for the operation. 

This is called the ROSE INVOKE message (defined as an ASN.1 type called "Invoke"). ROSE introduced the concept of the "invocation identification" because it recognised that multiple instances of (perhaps the same) operation might be launched before the results of earlier ones had come back, and indeed that results might not come back in the same order as the order operations where launched in. 

It is important here to note that the ROSE specification will define the concepts, and the form of the invocation message, but that lots of other groups will independently assign values to identify operations, define the ASN.1 type to carry the arguments or input parameters, and specify the associated semantics. They need a notation to do this, and to be able to link such definitions clearly to the holes left in the ASN.1 definition of the ROSE INVOKE message. 

Used in this context, ASN.1 is being used as what is sometimes called an "Interface Definition Language" (IDL), but it is important to remember that ASN.1 is not restricted to such use and can be applied to protocol definition where there is no concept of remote invocations and return of results. 

The INVOKE message itself is not a complete ASN.1 type definition. It has a "hole" which can carry whatever ASN.1 type is eventually used to carry values of the arguments of an operation. This "hole", and the value of the operation code field in the INVOKE message, clearly have to be filled-in in a consistent manner - that is, the op-code and the type must match. 

## 2.2 Responding to the INVOKE message

The ROSE concept says that an INVOKE message may be responded to by a REJECT message, carrying operation-independent error indications, such as "operation not implemented" (strictly, "invokeunrecognisedOperation"), "system busy" (strictly, 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/7839cf5734f932a021f0b37d2108707a703c4ccd8f7d09586cffaad530086ebb.jpg)


"resourceLimitation"), etc). ROSE has about 40 different error or problem cases that can be notified with a REJECT message. 

If, however, there is no such message, then the operation is successfully invoked and will result in an "intended result" (the RESULT message) or an operation-dependent "error response" (the ERROR message). 


ROSE invocation is illustrated in figure II-12.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/0e2a77f5ec84bbf97569e41efa219f4798c9d8c3111a743af53b96308225da4a.jpg)


This separation of "intended result" and "error response" is not strictly necessary, but simplifies the ASN.1 definition. The assumption here is that any one group will be defining a number of closely-related operations, each of which will have an identification and precisely one ASN.1 type to carry the input arguments in the INVOKE message hole, and precisely one ASN.1 type to carry the output arguments in the RESULT message hole. However, for this complete set of operations, there are likely to be a set of possible error returns, such that any given operation can give rise to a specified subset of these errors. For each error we need an error code, and an ASN.1 type to carry additional information (which ROSE calls parameters) about the error, and of course we need to be able to specify which errors can arise from which operations. 

## 3 The use of tables to complete the user specification

We return here to our wineco protocol, and will first use an informal tabular format to show how we use the ROSE (incomplete) protocol to support our wineco exchanges. We have already specified two main messages using ASN.1, namely 

<table><tr><td>Expressing wineco exchanges as a set of remote operations - you don&#x27;t have to, but it might be simple and convenient.</td></tr></table>

```txt
Order-for-stock and Return-of-sales 
```

We will add, without defining the ASN.1 types themselves, two further wineco messages we might wish to pass with a ROSE INVOKE, namely 

```txt
Query-availability and Request-order-state 
```

The first of these messages queries the availability of items for immediate delivery, and the second asks for an update on the state of an earlier order. 

We will make all four of these messages a ROSE operation, which will either produce a response or an error return. The response to an "Order-for-stock" will be an "Order-confirmed" message. Successful processing of a "Return-of-sales" will result in an ASN.1 NULL being returned. The response to "Query-availability" will be an "Availability-response" and the response to a "Requestorder-state" will be an "Order-status" response. 

We envisage that some or all of these requests (operations) can produce the following errors (in each case with some additional data giving more details of the failure): 

• Security check failure. 

• Unknown branch. 

• Order number unknown. 

• Items unavailable. 

Note that there are other operation-independent errors carried in the ROSE Reject message that are provided for us by ROSE, but we do not need to consider those. Here we are only interested in errors specific to our own operations. 

We need to say all this rather more formally, but we start by doing it in an informal tabular form shown in figures II-13 and II-14. 

In the figures, names such as "asn-val-....." are ASN.1 value reference names of a type defined by ROSE (actually, a CHOICE of INTEGER or OBJECT IDENTIFIER) used to identify operations or errors, and names such as "ASN-type-...." are ASN.1 types that carry more details about each of our possible errors. Note that in the case of the error "Order number unknown", we decide to return no further information, and we have left the corresponding cell of the table empty. We could have decided to return the ASN.1 type NULL in this case, but the element in the ROSE "ReturnError" SEQUENCE type that carries the parameter is OPTIONAL, and by leaving the cell of our table blank, we indicate that that element of the "ReturnError" SEQUENCE is to be omitted in this case. We will see later how we know whether we are allowed to leave a cell of the table empty or not. 

Figure II-13: The wineco ERROR table 

The figure II-13 table has one row for each possible error, and has just two columns: 

• the error codes assigned (as values of the type determined in the ROSE specification); and 

• the corresponding ASN.1 type (defined in our module) to carry parameters of the error. 

We might normally expect a small number of rows for this table for any given application that uses ROSE to define its protocol (in our case we have four rows), and it may be that for some errors there is no additional parameter information to return, and hence no ASN.1 type needed for parameters of that error, as in the case of "asn-val-unknown-order". 

The table in figure II-14 is the other information needed to complete the ROSE protocol for our wineco application. It lists an operation code, which is again a value of the type - as specified by ROSE: 

$$
\begin{array}{l} \text {CHOICE} \left\{\text {local INTEGER}, \right. \\ \text {global OBJECT IDENTIFIER} \end{array}
$$


together with the ASN.1 type that carries the input arguments for the operation, together with the ASN.1 type that carries the result values, together with a list of the errors that the operation can generate.


<table><tr><td>Op Code</td><td>Argument Type</td><td>Result Type</td><td>Errors</td></tr><tr><td>ash-val-order</td><td>Order-for-stock</td><td>Order-confirmed</td><td>security-failure unknown-branch</td></tr><tr><td>asn-val-sales</td><td>Return-of-sales</td><td>NULL</td><td>security-failure unknown-branch</td></tr><tr><td>asn-val-query</td><td>Query-availability</td><td>Availability-Response</td><td>security-failure unknown-branch unavailable</td></tr><tr><td>asn-val-state</td><td>Request-order-state</td><td>Order-status</td><td>security-failure unknown-branch unknown-order</td></tr></table>

In the real ROSE specification, there are additional columns to assign a priority value for operations and for error returns, to identify so-called "linked operations", and to determine whether results are always returned, values of error parameters needed, and so on. Discussion of these details of ROSE would go beyond the scope or the needs of this text, and we have not included these features in the illustration. 

Given then the ROSE concept of messages (ASN.1 datatypes) with "holes" in them, we see 

• The need for a syntax for ROSE to specify the information its users need to supply to complete the ROSE datatypes by the specification of a number of operations and errors (definition of the number and form of the above tables). 

• The need for a strict ASN.1 syntax (machine-readable) for ROSE users to specify the information shown informally in figures II-13 and II-14. 

• The need for notation in ASN.1 to identify "holes" in ASN.1 types, and to link the information shown in figures II-13 and II-14 clearly with the "hole" it is intended to complete. 

## 3.1 From specific to general

In the general case, there may be many different tables needed to complete any given "generic" protocol, and each table will have a number of columns determined by that "generic" protocol. The nature of the information needed for each column of the table (and the column headings to provide a "handle" for each piece of information) will all vary depending on the "generic" protocol in question. 

ROSE is just one example of incomplete (generic) protocols. There are many other examples where specifiers leave it to others to complete the specification, and need to be able to (formally) say what additional information is needed. This is an Information Object Class specification. 

Thus the specifier of a "generic" protocol needs a notation which will provide a clear statement of the form of the tables (the information needed to complete the "generic" protocol). We call the specification of this the specification of Information Object Classes. When a user of the "generic" protocol provides information for a row of a table we say that they are specifying an Information Object of the class associated with that table. The total set of rows of a given table defined to support any one user specification is called an Information Object Set. 

Notation is thus needed in ASN.1 for: 

• The definition of a named Information Object Class (the form of a table). 

• The definition of named Information Objects of a given class (completing the information for one row of the table). 

• Collecting together all the Information Objects (of any given class) defined in a specification into a named Information Object Set (a completed table). 

Linking a named information object set to the "holes" in the carrier protocol that it is designed to complete. 

## 4 From tables to Information Object Classes

The table metaphor is a very useful one in introducing the Information Object Class concepts, but the term "table" is not used in the ASN.1 Standard itself (except in the term "table constraint", discussed later). 

<table><tr><td>Tables are fine for human-to-human communication. For computer processing we use ASN.1 notation to define the form of tables and the contents of those tables.</td></tr></table>

We say that each Information Object has a series of fields, each with a field name. Defining an Information Object Class involves listing all the fields for objects of that class, giving the fieldname for each field, and some properties of that field. The most important property is the nature of the information needed when defining that field. This is most commonly the specification of some ASN.1 type (with the semantics associated with that type), or the specification of an ASN.1 value of some fixed ASN.1 type. We will, however, see later that there are a number of other sorts of fields that can be defined. 

In the case of ROSE, we have two Information Object Classes defined by ROSE, the OPERATION class and the ERROR class. (Names of Information Object Classes are required to be all upper-case). 

All objects of class OPERATION will have four fields containing: 

• A value of type 

$$
\begin{array}{l} \text {CHOICE} \left\{ \begin{array}{l l} \text {local} & \text {INTEGER}, \\ & \text {global} \end{array} \right. \text {OBJECT IDENTIFIER} \end{array}
$$

to identify the operation. 

• An ASN.1 type capable of carrying input values for the operation. 

• An ASN.1 type capable of carrying the result values on successful completion of the operation. 

• A list of information objects of class ERROR, each of which is an error that this particular operation can produce. 

All objects of class ERROR will have two fields containing: 

• A value of type 

CHOICE {local INTEGER, global OBJECT IDENTIFIER} 

to identify the error. 

• An ASN.1 type capable of carrying the values of the parameters of the error. 

To summarise: An Information Object Class definition defines the amount and form of information that is needed to specify an object of that class. An Information Object definition provides that information. The nature of the information needed can be very varied, and we talk about the form of the fields of the Information Object Class according to the information needed for that field when defining an Information Object. 

In the above discussion, we have introduced: 

• type fields: Fields that need an ASN.1 type definition to complete them. 

• fixed type value fields: Fields that need the value of a single (specified) ASN.1 type to complete them. 

object set fields: Fields that need a set of information objects of a single (specified) Information Object Class (in this case the ERROR class) to complete them. 

There are a number of other forms of field that can be specified when defining an Information Object Class, and we shall see more of these later. 

If you see names in all upper case, you can be reasonably sure that you are dealing with Information Object Classes, but another certain way to tell is the presence of names beginning with the & (ampersand) character. In order to avoid confusion with other pieces of ASN.1 notation, the names of fields of Information Object Classes are required to begin with an &. Thus the field of the OPERATION class that contains the object identifier value for some particular operation is called: 

## OPERATION.&operationCode

The field that has to be supplied with a type definition for the arguments of the INVOKE message is called: 

## OPERATION.&ArgumentType

Note that the &operationCode field contains a single ASN.1 value, and after the & we have a lower-case letter (this is a requirement), whilst the &ArgumentType field contains an ASN.1 type, and after the & we have an upper-case letter (again a requirement). Where a field contains a single value (usually - but not always - of some fixed type) or a single information object (of some fixed class) the field-name after the & starts with a lower-case letter. Where a field contains multiple values or multiple information objects (as with the list of errors for an operation), the field-name after the & starts with an upper-case letter. It is important to remember these rules when trying to interpret the meaning of an ASN.1 Information Object Class definition. 

We have already seen that names of Information Object Classes are required to be all upper case. Names given to individual Information Objects are required to start with a lower case letter (similar to value references), and names given to Information Object Sets (collections of Information Objects of a given class) are required to start with an upper case letter. 

There is in general a strong similarity between the concepts of types, values, and sets of values (subtypes), and the concepts of Information Object Classes, Information Objects, and Information Object Sets, and naming conventions in relation to the initial letter of names follow the same rules. 

There is, however, an important difference between types and information object classes. All ASN.1 types start life populated with a set of values, and new types can be produceced as subsets of these values. Information Object Classes have no predefined objects, they merely determine the notation for defining objects of that class, which can later be collected together into information object sets, which are really the equivalent of types. 

When you define a class you provide it with a reference name, and similarly for Information Objects and Information Object Sets. These reference names can then be used in other parts of the ASN.1 notation to reference those classes, objects, and sets, just like type reference and value reference names are assigned to type and value definitions and then used elsewhere. Reference names for classes, objects, and object sets are imported and exported between modules in the IMPORTS and EXPORTS statements just like type and value reference names. 

## 5 The ROSE OPERATION and ERROR Object Class definitions

Figure II-15 shows a simplified form of the definition of the OPERATION and ERROR classes of ROSE, and is the first introduction of the actual ASN.1 syntax for defining Information Object Classes. 

Remember, this syntax is essentially defining the table headings and the information content of the informal tables shown in II-13 and II-14, but it is doing it with a 

At last! We get to see an example of a real Information Object Class definition. Two in fact! The OPERATION class and the ERROR class from ROSE. 

syntax that is similar to ASN.1 type and value definition syntax, and which is fully machineprocessable. 

```txt
OPERATION ::= CLASS
    {&operationCode CHOICE {local INTEGER,
    global OBJECT IDENTIFIER}
    UNIQUE,
    &ArgumentType,
    &ResultType,
    &Errors ERROR OPTIONAL }

ERROR ::= CLASS
    {&errorCode CHOICE {local INTEGER,
    global OBJECT IDENTIFIER}
    UNIQUE,
    &ParameterType OPTIONAL }

Figure II-15: The OPERATION and ERROR class definitions 
```

In figure II-15, we see the definition of four fields for OPERATION and two for ERROR, as expected. Compare that figure with the table headings of figures II-13 and II-14, and let us go through the fields in detail. (Remember, each class definition corresponds to the definition of the form of a table, and each field corresponds to the definition of the form of a column of that table.) 

For the OPERATION class, we have the "&operationCode" field, which is required to be completed with a value of the specified type. (It is called a fixed type value field). This field is also flagged as "UNIQUE". When defining an object of this class, any value (of the specified type) can be inserted in this field, but if a set of such objects are placed together to form an Information Object Set (using notation we will see later), there is a requirement (because of the "UNIQUE") that all values in this field are different for each object in the set. If you regard the object set as representing a completely filled in table, then in database terminology, fields marked "UNIQUE" provide a key or index into the table. More than one field can be marked "UNIQUE" (but this is uncommon), but there is no mechanism in the notation to require that the combination of two fields has to be unique within an information object set. If you needed to specify that, you would have to use comment within the class definition. 

The next two fields, "&ArgumentType" and "&ResultType" have names which begin with a capital letter, and no type definition after them. This means that they have to be completed by the specification of an ASN.1 type (usually, but not necessarily, by giving a type reference rather than an explicit definition of a type). 

The fourth and last field is more interesting. "&Errors" begins with a capital letter, so you complete it with a set of things. But the name following is not an ASN.1 type reference, it is a class reference. So this field requires to be completed with a set of Information Objects of that (the ERROR) class, defined next. This field is also flagged as "OPTIONAL". This means that in the definition of objects of this class, it is not a requirement to define information for this field - it can be left blank. This would imply that the corresponding operation never produced a "ReturnError" response. 

It is left to the reader to examine the definition of the error class, which should now be understandable. 

## 6 Defining the Information Objects

Let us now use the notation for defining objects of a defined class (in this case OPERATION and ERROR). We take the informal definition of operations and errors given in figures II-13 and II-14 and express them in the ASN.1 notation for defining objects. This is shown in figure II-16 (the ERROR objects) and II-17 (the OPERATION objects). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/a0059080-59e4-4cd9-913b-34e7587e39f7/88a3e713d917f81425c00f6df90cef5afbec52d269ccac2ceedfef6245ca2170.jpg)


```lisp
sec-fail ERROR ::=
{&errorCode asn-val-security-failure,
    &ParameterType ASN-type-sec-failure-details}
unknown-branch ERROR ::=
{&errorCode asn-val-unknown-branch,
    &ParameterType ASN-type-branch-fail-details}
unknown-order ERROR ::=
{&errorCode asn-val-unknown-order}
unavailable ERROR ::=
{&errorCode asn-val-unavailable,
    &ParameterType ASN-type-unavailable-details} 
```


Figure II-16: Definition of the wineco ERROR Information Objects


These figures should be fairly understandable, and a line-by-line commentary will not be given, but there are some points to which the reader's attention is drawn. 

Note that the left of the "::=" looks rather like the definition of a value reference - compare: 

which is read as "my-int-val of type INTEGER has the value 3". In a similar way, we read figures II-16 and II-17 as (for example) "sec-fail of class ERROR has the fields ...". Following the "::=" we list (in curly brackets) each of the fields in the class definition, in order, and separated by commas, giving in each case the name of the field and the definition of that field for this particular object. 

Note also that the "unknown-order" ERROR object has no definition for the &ParameterType field - this is permissible only because that field was marked OPTIONAL in the class definition of figure II-15. 

Turning to the "&Errors" field, note that when we want to define a set of errors, we use a list of reference names separated by a vertical bar and enclosed in curly brackets. This may seem less intuitive than if a comma had been used as the list separator, but is in fact a special case of a much more powerful mechanism for grouping objects into sets using set arithmetic (see below). The vertical bar is used for set UNION, so we are producing a set for the "&Error" field of "order" which is the union of "security-failure" and "unknown-branch". 

Finally, note that the names used in the definition of the "&Error" fields are themselves defined as errors in figure II-16. Those definitions would be in the same module as the figure II-17 definitions, or would be imported into that module. 

```txt
order OPERATION ::=
    {&operationCode asn-val-order,
    &ArgumentType Order-for-stock,
    &ResultType Order-confirmed,
    &Errors {security-failure |
    unknown-branch}}
sales OPERATION ::=
    {&operationCode asn-val-sales,
    &ArgumentType Return-of-sales,
    &ResultType NULL,
    &Errors {security-failure |
    unknown-branch}}
query OPERATION ::=
    {&operationCode asn-val-query,
    &ArgumentType Query-availability,
    &ResultType Availability-Response,
    &Errors {security-failure |
    unknown-branch |
    unavailable}}
status OPERATION ::=
    {&operationCode asn-val-state,
    &ArgumentType Request-order-state,
    &ResultType Order-status,
    &Errors {security-failure |
    unknown-branch |
    unknown-order}}
Figure II-17: Definition of the wineco OPERATION Information Objects 
```