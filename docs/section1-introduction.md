# Section 1 - Introduction

## 1.1 Document Overview

### 1.1.1 Document Purpose

The Common Information Model (CIM) is an open-source semantic information model for an interconnected electric power grid expressed in the Unified Modeling Language (referred to as the CIM UML). The purpose of this document is to provide guidance to individuals working with the CIM UML on how to modify the model in accordance with the CIM modeling rules and the UCA Model Change Management Process.

The goals of this document are to: 

1. facilitate communication and understanding among individuals working with CIM domain models;

2. and streamline the incorporation of new content into the CIM UML.

### 1.1.2 Document Scope

The scope of this document includes providing:

1. An overview of CIM Modeling;

2. A description of the processes and procedures used to evolve, maintain, and extend the CIM UML;

3. Rules and recommendations for CIM UML modeling

4. CIM UML version control rules;

5. Recommendations for extending the CIM UML to create a user-defined CIM-compliant enterprise information model that will facilitate submitting user-defined model elemnents for incorporation into the CIM UML.

6. A description of the process for submitting CIM UML extensions for incorporation into the CIM UML.

7. A description of the UML tool (Sparx EA) used for CIM Management.


### 1.1.3 What this Document Does Not Cover

*This Document Does Not Cover All UML Concepts and Constructs*

The CIM UML uses a subset of the UML concepts and constructs. This document only covers the UML concepts and constructs relevant to the CIM UML.

*This Document Does Not Cover How the CIM UML Modeling Rules Evolved*

The CIM UML modeling rules have evolved over time and it is not the intent of this document to discuss the history of their evolution. The intent of this document is to specify the CIM UML modeling rules in clear unambiguous language. It is the goal of this document to communicate the rules in such a way that the rationale for each rule is self-evident. The exception is the discussion of CIM UML version control in Clause 7.1.

*This Document Does Not Cover how each UCA or IEC TC 57 Working Group operates to develop additional CIM UML Content*

How each Working Group conducts its business to develop additional CIM UML content is not in the purview of this guide. This document covers what needs to be done, but not how. The output of the working groups do trigger CIM modeling and maintenance processes covered in Section 5, of this document.

*This Document Does Not Cover All Detailed Tool Procedures Used To Accomplish CIM Modeling and Maintenance Tasks*

All detailed tool procedures used to accomplish CIM Model Management tasks are not in the purview of CIM modeling. This document does identify what tools are used to accomplish CIM modeling andmaintenance. This document also covers step-by-step tool procedures to ensure rules are adhered to in the Appendicies.

*This Document Does Not Cover the method for deriving CIM Profiles from the CIM UML*

Creating CIM Profiles are not in the purview of this document. How to create CIM Profiles is covered in the “Common Information Model Primer,” Eighth Edition, EPRI document 3002024188, and other CIM Users Guide material created by UCA. This document does identify CIM Model Management tools that are used to create CIM Profiles in Appendix F.

### 1.1.4 Who this Document Is For

This document has the following intended audience:

**Target Audience**

- UCA and IEC Working Group members who need to know CIM UML modeling rules and recommendations in order to properly incorporate additional information into the CIM UML;

- CIM users who need to know how to create their own CIM compliant Enterprise Information Model which contains their user defined CIM UML extensions that can be readily submitted for addition to the base CIM UML;

- Utility companies who need to know the process for submitting their user-defined CIM UML extensions and CIM profiles for addition to the CIM UML and the IEC CIM standard documents, respectively;

- UCA and IEC Working Group leads who need to understand their role in the Model Change Management process;

- CIM Model Managers in order to have documented rules and recommendations for CIM UML modeling, and extensions,


**Secondary Audience**

- Utility companies interested in learning more about the CIM UML;

- Vendors interested in developing CIM compliant products;

- Researchers interested in learning about the CIM UML and conducting CIM UML research.

## 1.2 How this Document Is Organized

This document begins with Sections 1, 2, and 3 providing introductory content, references, and definitions, respectively.

Section 4 is an overview of CIM Modeling. This section provides the business context for CIM Management within the UCAIug organizational structure (the “Where” of CIM Management), and the roles and responsibilities (the “Who” and “What”) of CIM Management. The section also provides an overview of the CIM Management processes (the “How” of CIM Management) performed by CIM model managers, and how the CIM Management processes integrate with the IEC standards development process.

Section 5 discusses the CIM Framework Methodology. This section covers the system of methods used to: 

1. update and maintain the CIM UML, 

2. derive CIM Profiles from the CIM UML, and 

3. develop extensions to the CIM UML to create a CIM-compliant user-defined enterprise information model. Each method specifies the processes, procedures, rules, and tools used to produce a work product or result.  

Section 6 specifies CIM UML modeling rules and recommendations. This section covers rules and recommendations for the model structure, packages, classes, attributes, associations, enumerations, inheritance, diagrams, element descriptions, stereotypes, namespaces, and documentation.

Section 7 describes CIM UML version control. This section provides an overview of version control and the CIM UML version control strategy.

Section 8 specifies CIM extension rules and recommendations. This section contains general extension rules and covers rules and recommendations for package, class, attribute, association, and enumeration extension.

The Appendices describe the step-by-step tool procedures that ensure CIM modeling and maintenance is performed according to CIM modeling and maintenance rules.

## 1.3 Symbols, Figures, and Style Conventions

**Conventions**

This document uses the following conventions.

- Rules and recommendations are similar to requirements. As such, this document uses the terms defined in RFC 2119 of the Internet Engineering Task Force (IETF) in the specification of the rules and recommendations.

- The term “rules” is used to refer to both rules and recommendations. The distinction between rules and recommendations is made by how the RFC 2119 terms are used in specification text. Specifically, the terms “Shall”, “Must”, “Shall not”, “Must not”, and “May” are used to specify rules, and the terms “Should” and “Should not” are used to specify recommendations.

- All rules and recommendations have a unique identifier that is formatted as: “RuleXXX”.


**Symbol Legend**

This document contains a series of diagrams that are referred to as figures and tables. The primary symbols used throughout this document are individually described in the following symbol legend:

| **Symbol**                                             | **What the symbol represents**   |
|--------------------------------------------------------|----------------------------------|
| ![](images/media/cim-framework-process.png)             | CIM Framework Process           |
| ![](images/media/cim-framework-procedure.png)           | CIM Framework Procedure         |
| ![](images/media/cim-modeling-rules.png)                | CIM Modeling Rules              |
| ![](images/media/cim-modeling-or-maintenance.tool.png)  | CIM Modeling or Maitenance Tool |

**UML**

The Unified Modeling Language is used in figures containing CIM UML model elements.

**BPMN**

Business Process Modeling Notation is used in figures depicting CIM Framework processes.

**Text Formats**

1. **Bold text** is used to identify a term that can be found in the glossary. The term will be in bold text the first time it is used in the document. All subsequent uses of the term will be in normal text.

2. Square brackets (\[ \]) are used as delimiters for referenced works cited in this document.

## 1.4 Document Control

This document will be reviewed periodically by the CIM Model Managers and updated as needed. Lessons learned will be captured with each CIM UML update and used to improve this document. If the document is written in an older format, the document should be revised into the latest CIM Users Group template format.

This document contains a revision history log. When changes occur, the version number will be updated to the next increment and the date, author making the change, and change description will be recorded in the revision history log of the document.

