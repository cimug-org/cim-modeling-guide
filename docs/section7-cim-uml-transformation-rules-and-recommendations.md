# Section 7 - CIM UML Transformation Rules and Recommendations

## 7.1 Overview

The CIM UML is a semantic information model (also referred to as a conceptual data model). It is a conceptual model of utility objects and their relationships with each other. It is application independent, but defines all the concepts needed for any application. It essentially provides the vocabulary (sometimes referred to as a data dictionary) to be used when utility domain data is exchanged between systems.

Since the CIM UML is a conceptual model, it cannot be used as is for data exchange. A subset of CIM elements needs to be selected and constrained for a specific business context for use in a data exchange between systems. This is analogous to the need for the grammatical structure of words and phrases to create coherent sentences in a given language. The CIM UML subset must therefore be transformed from a semantic information model into a contextual data model (also referred to as a canonical data model). The contextual data model is called a “CIM Profile”. The resultant CIM Profile is the syntax of a data exchange between utility domain systems.

This section specifies the rules and recommendations for transforming a subset of the CIM UML into a contextual data model. The contextual data model can then be used to derive implementation models which define the data and the structure of the data required to exchange information between two systems to execute a single interaction in a System Use Case.

## 7.2 General Transformation Rules and Recommendations

| **RuleID** | **Description**                                                                                                                                                                     |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rule207    | A contextual data model derived from the CIM UML shall not contain any classes, attributes, or associations that are not part of the CIM UML, with the exception of CIM extensions. |
| Rule208    | In instances where CIM extensions have been added to the CIM UML, the extensions may be part of a contextual data model derived from the CIM UML.                                   |
| Rule209    | A class diagram that contains all candidate classes and associations should be created, which may be used as a reference diagram, for each contextual data model.                   |

## 7.3 Package Transformation Rules and Recommendations

| **RuleID** | **Description**                                                                                                                                                                                                              |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rule210    | Transformation of all CIM UML packages shall not be required to create a contextual data model (i.e. entire packages may be left out of a contextual data models if they are not needed).                                    |
| Rule211    | Transformation of an entire package shall not be required to create a contextual data model (i.e. classes, attributes, and associations within a package may be left out of a contextual data model if they are not needed). |
| Rule212    | A single top-level package for contextual data models that exists outside of the TC57CIM package should be created at the root level of the CIM.                                                                             |

## 7.4 Class Transformation Rules and Recommendations

| **RuleID** | **Description**                                                    |
|------------|--------------------------------------------------------------------|
| Rule213    | A contextual data model shall contain at least one concrete class. |
| Rule214    | A contextual data model may contain abstract classes.              |

## 7.5 Attribute Transformation Rules and Recommendations

| **RuleID** | **Description**                                                                                                                                                              |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rule215    | A contextual data model should contain at least one mandatory attribute.                                                                                                     |
| Rule216    | Mandatory attributes in the CIM UML shall be mandatory when included in a contextual data model.                                                                             |
| Rule217    | Optional attributes in the CIM UML may be restricted to be mandatory when included in a contextual data model.                                                               |
| Rule218    | A contextual data model should contain the attributes necessary to execute a System use case interaction.                                                                    |
| Rule219    | A contextual data model should not contain attributes not used in a System use case interaction (i.e. not all class attributes must be included in a contextual data model). |

## 7.6 Association Transformation Rules and Recommendations

| **RuleID** | **Description**                                                                                                                                                                  |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rule220    | A contextual data model should contain the associations necessary to execute a System use case interaction.                                                                      |
| Rule221    | A contextual data model should not contain associations not used in a System use case interaction (i.e. not all class associations must be included in a contextual data model). |
| Rule222    | Mandatory association roles in the CIM UML shall be mandatory when included in a contextual data model.                                                                          |
| Rule223    | Optional association roles in the CIM UML may be restricted to be mandatory when included in a contextual data model.                                                            |
| Rule224    | Association roles in the CIM UML with unspecified maximum multiplicity may be restricted to a maximum multiplicity when included in a contextual data model.                     |
