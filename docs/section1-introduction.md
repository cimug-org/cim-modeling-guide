# Section 1 - Introduction

## 1.1 Document Overview

The CIM has been growing and more groups are extending it with new functionality. Currently the following IEC TC57 working groups are working with the CIM:

- WG13

- WG14

- WG16

  Initially only WG13 and WG14 were working with the CIM. Each group worked with a local copy of the UML model file and the two copies were synchronised as needed. With three working groups the synchronisation process becomes more complex. This document describes how to manage CIM across multiple working groups and provides best practices for applications wanting to extend the CIM.

### 1.1.1 Document Purpose

The purpose of this document is to provide guidance to individuals working with the CIM UML on how to modify the CIM in accordance with the CIM modeling rules and CIM change management. The rules and process are maintained and enforced by the CIM model managers.

The goals of this document are to: 1) facilitate communication and understanding among individuals working with CIM domain models; and 2) streamline the incorporation of new content into the CIM UML.

### 1.1.2 Document Scope

The scope of this document includes providing:

1)  A description of the items under CIM Management;

2)  A description of the CIM Management processes;

3)  Rules and recommendations for CIM UML modeling

4)  Rules and recommendations for CIM UML extension;

5)  Rules and recommendations for transforming CIM UML into a canonical model in preparation to create CIM Profiles;

6)  A description of the process for submitting CIM UML extensions, UML used in the user-defined profiles for incorporation into the CIM UML and the IEC CIM standards, respectively;

7)  A description of the UML tool (Sparx EA) used for CIM Management.

### 1.1.3 What this Document Does Not Cover

*This Document Does Not Cover All UML Concepts*

The CIM UML uses a subset of the UML concepts. This document only covers the UML concepts relevant to the CIM UML.

*This Document Does Not Cover How the CIM UML Rules Evolved*

The CIM UML rules have evolved over time and it is not the intent of this document to discuss the history of their evolution. The intent of this document is to specify the CIM UML rules in clear unambiguous language. It is the goal of this document to communicate the rules in such a way that the rationale for each rule is self-evident. The exception is the discussion of CIM UML version control in section 8.

*This Document Does Not Cover How Each Working Group Develops Additional CIM UML Content*

The methodologies and practices used by each IEC working group to develop additional CIM UML content is not in the purview of CIM Management. The output of the working groups do trigger some of the CIM Management processes, and these triggers are identified in this document.

*This Document Does Not Cover Detailed Tool Procedures Used To Accomplish CIM Management Tasks*

The detailed tool procedures used to accomplish CIM Management tasks are not in the purview of CIM modeling. This document does identify what tool is used to accomplish each CIM Management process activity. This document does provide the step by step procedures for exporting and importing the CIM model in XMI format. CIM Management tasks are discussed in the CIM Management Process and Procedures document.

*This Document Does Not Cover Tools Used To Create CIM Profiles*

The tools used to create CIM Profiles are not in the purview of CIM Management. This document does provide rules and recommendations for transforming the CIM UML (a semantic information model) into a canoncial data model that can then be used as input to a tool to create CIM Profiles.

### 1.1.4 Who this Document Is For

This document has the following intended audience:

**Target Audience**

- CIM Model Managers in order to have documented rules and recommendations for CIM UML modeling, and extensions,

- IEC Working Group leads who need to understand how their CIM UML development processes relate to and interact with CIM Management processes;

- IEC Working Group members who need to know CIM UML modeling rules and recommendations in order to properly incorporate additional information into the CIM UML;

- IEC CIM users who need to know how to create their own CIM compliant Enterprise Information Model which contains their user defined CIM UML extensions that can be readily submitted for addition to the base CIM UML;

- IEC CIM users who need to know how to create their own CIM profiles that can be readily submitted for addition to the IEC CIM standards;

- Utility companies who need to know the process for submitting their user-defined CIM UML extensions and CIM profiles for addition to the CIM UML and the IEC CIM standard documents, respectively;

**Secondary Audience**

- Utility companies interested in learning more about the CIM UML;

- Vendors interested in developing CIM compliant products;

- Researchers interested in learning about the CIM UML and conducting CIM UML research.

## 1.2 How this Document Is Organized

This document begins with Sections 1, 2, and 3 providing introductory content, references, and definitions, respectively.

Section 4 is an overview of CIM Management. This section provides the business context for CIM Management within the UCAIug organizational structure (the “Where” of CIM Management), and the roles and responsibilities (the “Who” and “What”) of CIM Management. The section also provides an overview of the CIM Management processes (the “How” of CIM Management) performed by CIM model managers, and how the CIM Management processes integrate with the IEC standards development process.

Section 5 specifies CIM UML modeling rules and recommendations. This section covers rules and recommendations for the model structure, packages, classes, attributes, associations, enumerations, inheritance, diagrams, element descriptions, stereotypes, namespaces, and documentation (the “How To” of CIM UML development within the working groups).

Section 6 specifies CIM extension rules and recommendations. This section contains general extension rules and covers rules and recommendations for package extension, class extension, attribute extension, association extension, and enumeration extension (the “How To” of CIM extension).

Section 7 specifies CIM UML transformation rules. This section contains general schema profiling rules and rules for RDFS and XSD profiling.

Section 8 describes CIM UML version control. This section provides an overview of version control and the CIM UML version control strategy.

Section 9 identifies and describes the artifacts under CIM Management. This includes CIM UML artifacts, CIM Profiles, draft standards, CIM Management process artifacts, and CIM Management tool customizations.

Section 10 discusses the tools used for CIM UML model management. Tools include Enterprise Architect, jCleanCIM, and the CIMug Website.

## 1.3 Symbols, Figures, and Style Conventions

**Conventions**

This document uses the following conventions.

- Rules and recommendations are similar to requirements. As such, this document uses the terms defined in RFC 2119 of the Internet Engineering Task Force (IETF) in the specification of the rules and recommendations.

- Specifically, the terms “Shall”, “Must”, “Shall not”, “Must not”, and “May” are used to specify rules, and the terms “Should” and “Should not” are used to provide recommendations.

- All rules and recommendations have a unique identifier that is formatted as: “RuleXXX”. The distinction between rules and recommendations is based on the use of the RFC 2119 terms in the descriptive text.

**Symbol Legend**

This document contains a series of diagrams that are referred to as figures. The primary symbols used throughout all figures are individually described in the following symbol legend:

UML Notation

The Unified Modeling Language is used

**Text Formats**

1.  **Bold text** is used to identify a term that can be found in the glossary. The term will be in bold text the first time it is used in the document. All subsequent uses of the term will be in normal text.

2.  Square brackets (\[ \]) are used as delimiters for referenced works cited in this document.

## 1.4 Document Control

This document will be reviewed periodically by the CIM Model Managers and updated as needed. Lessons learned will be captured with each CIM UML update and used to improve this document. If the document is written in an older format, the document should be revised into the latest CIM Users Group template format.

This document contains a revision history log. When changes occur, the version number will be updated to the next increment and the date, author making the change, and change description will be recorded in the revision history log of the document.
