# Section 9 - Artifacts Under CIM Management

## Overview

Artifacts under CIM Management consist of: 1) model artifacts (CIM Artifacts); 2) draft standards; 3) CIM Schemas; 4) CIM Management documents and records; and 5) tool customizations. These artifacts are described in this section.

### Draft Standards Artifacts

As IEC standards, the CIM standards must go through the IEC standards development process to be published (see Section 8.1). This process results in the creation of several draft standard artifacts as intermediate work products. The types IEC draft standard artifacts under CIM management are listed below. The description of each type of draft standard is provided in Section 8.1.

1.  New Work Item Proposal (NWIP)

2.  Working Draft & Committee Draft (CD)

3.  Committee Draft for Vote (CDV)

4.  Final Draft International Standard FDIS)

## CIM Artifacts

CIM Artifacts are model artifacts that are maintained in the Sparx Systems Enterprise Architect modeling tool. CIM Artifacts are stored in four (4) file formats: 1) as an EA project file in the native EA file format (\*.eap or \*.eapx); 2) in the ZIP compressed file format (\*.zip); 3) in the XML Metadata Interchange file format (\*.xmi); and 4) as a collection of web pages in HyperText Markup Language file format (\*.html). The EA project file is also exported and maintained as a Web Ontology Language project file (\*.owl). The CIM Artifacts under CIM Management are listed and described in Table 9‑1.

| **CIM Artifact**                    | **Artifact Description**                                                                                                                                                                                                             |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CIM UML                             | The CIM UML is the semantic common information model expressed in UML.                                                                                                                                                               |
| CIM Interface Reference Model (IRM) | The IRM is contained in the same EA project file as the CIM UML as a separate root model. The IRM is stored in the same four (4) file formats as the CIM UML.                                                                        |
| Schema Composer Profile Artifacts   | Schema Composer profile artifacts are contained in the same EA project file as the CIM UML as a separate top level package within the CIM UML. Schema profile artifacts are stored in the same four (4) file formats as the CIM UML. |

<span id="_Ref22120330" class="anchor"></span>Table 9‑1. CIM Artifacts Under CIM Management

## Model Documents

Model documents are CIM standards that are derived from the CIM UML using the CIM document generation tool jCleanCim. Draft versions of the CIM standard model documents under CIM Management are listed and described in Table 9‑2.

| **Model Document** | **Model Document Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IEC 61968-11       | This part of IEC 61968 specifies the distribution extensions of the common information model (CIM) specified in IEC 61970-301. It defines a standard set of extensions of common information model (CIM), which support message definitions in IEC 61968-3 to IEC 61968-9, IEC 61968-13 and IEC 61968-142. The scope of this standard is the information model that extends the base CIM for the needs of distribution networks, as well as for integration with enterprise-wide information systems typically used within electrical utilities.                                                                                                                                                                                                        |
| IEC 61970-301      | This document specifies a Base set of packages which provide a logical view of the functional aspects of Energy Management System (EMS) and power system modelling information within the electric utility enterprise that is shared between all applications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| IEC 61970-303      | This proposed specification IEC 61970-303 extends the Common Information Model (CIM) with information describing how network model data is organised and administrated. A specific network model not only describe its equipment but also include additional data about the network model itself as its origin, responsible organisation, author, when it was created, version, the time (e.g. past, current, future) when the model is valid, usage (e.g. operation, operation planning, extension planning), purpose for its creation (e.g. commissioning of new equipment, test of network changes/extensions), relation to neighbouring networks etc. IEC 61970-303 extends the basic CIM (IEC 61970-301 and IEC 61970-302) with this kind of data. |
| IEC 62325-301      | This international standard specifies a set of packages which provide a logical view of the functional aspects of market management within an electricity market that is shared between a market management system and other systems concerned with different aspects of market management, such as capacity allocation, day-ahead management, balancing, settlement, etc. This international standard includes support for demand-side resource communication with a wholesale market and support for environmental (weather) forecast, observation, phenomena, and alerts data.                                                                                                                                                                       |

<span id="_Ref22125995" class="anchor"></span>Table 9‑2. Model Documents Under CIM Management

## CIM Profiles

A CIM Profile is a subset of the full CIM UML that is derived to define data exchanges required between systems. Each profile is a collection of classes, attributes and references along with additional restrictions such as making attributes mandatory or restricting the cardinalities on associations. Draft versions of CIM standard profiles are artifacts under CIM Management. Also included as a CIM Profile is 61968-1 which is not a subset of the CIM UML; it is a reference to be used in the development of CIM Profiles. The CIM Profiles under CIM Management are listed and described in Table 9‑3.

<span id="_Ref25434542" class="anchor"></span>Table 9‑3. CIM Profiles Under CIM Management

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>CIM Profile</strong></th>
<th><strong>CIM Profile Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IEC 61968-1</td>
<td>This Part of the IEC 61968 International Standard identifies and establishes recommendations for standard interfaces based on an Interface Reference Model (IRM). Subsequent clauses of this standard are based on each interface identified in the IRM. This set of standards is limited to the definition of interfaces. They provide for interoperability among different computer systems, platforms, and languages. Methods and technologies used to implement functionality conforming to these interfaces are recommended in IEC 61968-100.</td>
</tr>
<tr class="even">
<td>IEC 61968-3</td>
<td>This part of the IEC 61968 International Standard specifies the information content of a set of message types that can be used to supervise main substation topology (breaker and switch state) and control equipment status. It also provides the means for handling network connectivity and loading conditions. Finally, it makes it possible for utilities to locate customer telephone complaints and supervise the location of field crews.</td>
</tr>
<tr class="odd">
<td>IEC 61968-4</td>
<td>This Part of IEC 61968 International Standard specifies the information content of a set of message types that can be used to support many of the business functions related to records and asset management.</td>
</tr>
<tr class="even">
<td>IEC 61968-5</td>
<td>This Part of IEC 61968 International Standard specifies a set of functions that are needed for enterprise integration of DERMS functions. These exchanges are most likely between a DERMS and a DMS. However, an enterprise integration standard leveraging IEC 61968-100:2013 for application integration, there are no technical limitation for systems with which a DERMS might exchange information.</td>
</tr>
<tr class="odd">
<td>IEC 61968-6</td>
<td>This Part of IEC 61968 International Standard specifies the information content of a set of message types that can be used to support business functions related to Maintenance and Construction. Typical uses of the message types defined in Part 6 include planned maintenance, unplanned maintenance, conditional maintenance, and work management</td>
</tr>
<tr class="even">
<td>IEC 61968-7</td>
<td>This Part of IEC 61968 International Standard specifies the information content of a set of message types that can be used to support business functions related to engineering design.</td>
</tr>
<tr class="odd">
<td>IEC 61968-8</td>
<td>This Part of IEC 61968 International Standard specifies the information content of a set of message types that can be used to support many of the business functions related to customer support.</td>
</tr>
<tr class="even">
<td>IEC 61968-9</td>
<td>This Part of IEC 61968 International Standard specifies the information content of a set of message types that can be used to support many of the business functions related to meter reading and control.</td>
</tr>
<tr class="odd">
<td>IEC 61968-13</td>
<td>This part of IEC 61968 specifies profiles that can be used to exchange Network Models in a Utility or between a Utility and external applications to the utility. This standard provides a list of profiles which allow to model balanced and unbalanced distribution networks in order to conduct network analysis (Power flow calculation).</td>
</tr>
<tr class="even">
<td>IEC 61968-100</td>
<td>This document specifies an implementation profile for the application of the other parts of IEC 61968 using common integration technologies, including JMS and web services. This International Standard also provides guidance with respect to the use of Enterprise Service Bus (ESB) technologies.</td>
</tr>
<tr class="odd">
<td>IEC 61970-452</td>
<td>This document contains a subset of classes, class attributes, and associations from the CIM UML necessary to describe a static transmission network model. This document defines a Core Equipment Profile, an Operation Profile, and a Short Circuit Profile.</td>
</tr>
<tr class="even">
<td>IEC 61970-453</td>
<td>This document contains a subset of classes, class attributes, and associations from the CIM UML necessary to exchange schematic information between systems. This document defines a Diagram Layout Profile.</td>
</tr>
<tr class="odd">
<td>IEC 61970-456</td>
<td>This document contains a subset of classes, class attributes, and associations from the CIM UML necessary to describe the steady state of a power system network. This document defines a State Variables Profile and a Topology Profile.</td>
</tr>
<tr class="even">
<td>IEC 61970-457</td>
<td><p>This international standard specifies a standard interface for exchanging dynamic model information needed to support the analysis of the steady state stability (small-signal stability) and/or transient stability of a power system or parts of it. The schema(s) for expressing the dynamic model information shall be derived directly from the CIM.</p>
<p>The scope of this standard includes only the dynamic model information that needs to be exchanged as part of a dynamic study, namely the type, description and parameters of each control equipment associated with a piece of power system equipment included in the steady state solution of a complete power system network model.</p></td>
</tr>
<tr class="odd">
<td>IEC 61970-458</td>
<td>This international standard specifies a standard interface to support the models and objects required for power generation information exchanges. The scope of information exchange includes all generation processes such as bulk and distributed resources, including processes generating by-products such as heat or steam. The scope of information exchange is focused on Generation specific applications such as scheduling, optimization, operation and maintenance of the Generation resources.</td>
</tr>
<tr class="even">
<td>IEC 61970-459</td>
<td>This international standard specifies a framework for network model exchange including description of network model parts, boundaries between network model parts, complete power flow cases and responsible authorities. The boundaries act as a frame where network model parts fit. A network model part, boundary or power flow case is described by additional meta-data such as source, author, study time, description, development of time (audit trail) etc. This additional meta-data is described in the framework information model and will be part of the IEC 61970 300 series documents.</td>
</tr>
<tr class="odd">
<td>IEC 61970-460</td>
<td><p>This international standard specifies a standard interface for exchanging incremental network models of proposed changes to IEC 61970 network models used for network analysis. These incremental network models of proposed changes are called IEC 61970 Projects, or in this document, simply ‘Projects’.</p>
<p>The scope of this document shall include models for all types of changes that impact IEC 61970 network model datasets. The initial version of this specification, however, focuses on Projects that define plans for new construction activity in the power grid.</p>
<p>The exchanges which are in scope here, (i.e. the proposed change) are datasets of long-term interest which are a fundamental component used by various parties in the construction of network analysis cases for many different purposes.</p></td>
</tr>
<tr class="even">
<td>IEC 62325-351</td>
<td>This part of IEC 62325 provides the European style market profile specifications that support the European style design electricity markets. These electricity markets are based on the European regulations, and on the concepts of third-party access and zonal market.</td>
</tr>
<tr class="odd">
<td>IEC 62325-450</td>
<td>This document provides the modelling rules necessary to ensure that Contextual Models derived from the CIM for information exchanges between electricity market actors participating in various market business processes are in conformity with the CIM model.</td>
</tr>
<tr class="even">
<td>IEC 62325-451-1</td>
<td>This document provides for the European style market profile the generic technical and application acknowledgement document that can be used in all European style market processes.</td>
</tr>
<tr class="odd">
<td>IEC 62325-451-2</td>
<td>This document provides for the European style market profile the time-based scheduling process. These market processes are based on the European regulations, and on the concepts of third-party access and zonal market.</td>
</tr>
<tr class="even">
<td>IEC 62325-451-3</td>
<td>This document provides for the European style market profile the transmission capacity allocation business process based on either explicit or implicit auction that can be used throughout a European style market.</td>
</tr>
<tr class="odd">
<td>IEC 62325-451-4</td>
<td>This document provides for the European style market profile the settlement and reconciliation business process that can be used throughout a European style market.</td>
</tr>
<tr class="even">
<td>IEC 62325-451-5</td>
<td>This document provides for the European style market profile the problem statement and status request business processes that can be used throughout a European style market.</td>
</tr>
<tr class="odd">
<td>IEC 62325-451-6</td>
<td>This document provides for the European style market profile the publication (or transparency) information exchanges to submit either to a data aggregator or to an electronic publication platform the necessary information to be published about the electricity market.</td>
</tr>
<tr class="even">
<td>IEC 62325-451-7</td>
<td>This document provides, for the European style market profile, the necessary information to be exchanged between Balancing Service Providers, Transmission System Operators and a Common Merit Order List about the Electricity Balancing market.</td>
</tr>
<tr class="odd">
<td>IEC 62325-451-8</td>
<td>Based on the European style market profile, IEC 62325-351, this document specifies a package for the HVDC Scheduling business processes and the associated document’s contextual models, assembly models and XML schema for use within European style markets.</td>
</tr>
<tr class="even">
<td>IEC 62325-451-10</td>
<td>Based on the European style market contextual model (IEC 62325-351), this particular part of IEC 62325 series specifies a UML package for the Energy Consumption Data business process and its associated document contextual model, assembly model and XML schema for use within the European style electricity markets.</td>
</tr>
</tbody>
</table>

**Table 9‑3. CIM Profiles Under CIM Management (Cont’d)**

## CIM Schemas

### Background

XML, the eXtensible Markup Language, is a “universal format for structured documents and data” which is quickly becoming the standard for storing machine-readable data in a structured, extensible format that is accessible over the Internet. XML uses *tags* to denote the elements within XML documents.

While XML itself has no set tag-syntax or semantics, *schemas* can be defined for expressing almost any kind of data using XML notation. An application interpreting XML data must be given this knowledge of the syntax and semantics used; otherwise it will have trouble interpreting it. This requires the tag-syntax and semantics of the XML to be expressed as a schema, which provides constraints on the structure and contents of an XML document.

CIM Schemas provide the constraints on the structure and contents of CIM based XML data exchanges. The types of CIM Schemas under CIM Management are: 1) RDF Schemas (RDFS – used for exchange of network model information); 2) XML Schemas (XSDs – used for message exchanges between applications); and 3) CIM based schemas that contain RDFS and XSD elements, and non-XML elements. The later are referred to as “Hybrid Schemas”.

The following subsections list and describe the CIM Schemas under CIM Management. Some of the CIM Schemas are IEC International Standards and some are schemas derived from CIM Profiles.

### RDF Schemas

The RDF schemas under CIM management are listed and described in Table 9‑4.

<span id="_Ref25431641" class="anchor"></span>Table 9‑4. RDF Schemas Under CIM Management

| **RDF Schema** | **RDF Schema Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IEC 61970-501  | This part of the IEC 61970 series specifies the mapping between the semantic information model (in the UML) specified in IEC 61970-301 and the machine-readable Extensible Markup Language (XML) representation of that model using the Resource Description Framework (RDF) Schema specification language.                                                                                                                                                                           |
| IEC 61970-552  | This part of the IEC 61970 series specifies how the CIM RDF schema specified in IEC 61970-501 is used to exchange power system models using XML (referred to as CIMXML) defined in the 61970-45x series of profile standards, such as the CIM Transmission Network Model Exchange Profile described in IEC 61970-452.                                                                                                                                                                 |
| IEC 61970-556  | This part of the IEC 61970 series specifies how the CIM RDF schema specified in IEC 61970-501 is used to exchange CIM based graphic objects; and how to display an object using XML defined in the 61970-453. This standard defines a format (CIM/G) to facilitate efficient graphic data transfer, which will support on-line remote diagram browsing and exchanging, and off-line exchange of graphic displays. It includes graphic file structure and graphic element definitions. |
| IEC 62325-503  | The purpose of this part of the 62325 series is to provide the guidelines to exchange European style market messages specified in IEC 62325-451-x. The common information model (CIM UML) specifies the basis for the semantics for the message exchange. The European style market profile specifications that support the European style design electricity markets are defined in IEC 62325 part 351.                                                                              |

**Table 9‑4. RDF Schemas Under CIM Management (Cont’d)**

### XML Schemas

The XML schemas under CIM management are listed and described in Table 9‑5.

<span id="_Ref25431767" class="anchor"></span>Table 9‑5. XML Schemas Under CIM Management

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>XML Schema</strong></th>
<th><strong>XML Schema Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>61968-3 Schemas</td>
<td>IEC61968 Part 3 XSDs specify the message payloads for system interactions in network operations support use cases.</td>
</tr>
<tr class="even">
<td>61968-4 Schemas</td>
<td>IEC61968 Part 4 XSDs specify the message payloads for system interactions in asset management use cases.</td>
</tr>
<tr class="odd">
<td>61968-5 Schemas</td>
<td>IEC61968 Part 5 XSDs specify the message payloads for system interactions in Distributed Energy Resources and DERMS use cases.</td>
</tr>
<tr class="even">
<td>61968-6 Schemas</td>
<td>IEC61968 Part 6 XSDs specify the message payloads for system interactions in work management use cases.</td>
</tr>
<tr class="odd">
<td>61968-7 Schemas</td>
<td>IEC61968 Part 7 XSDs specify the message payloads for system interactions in engineering design use cases.</td>
</tr>
<tr class="even">
<td>61968-8 Schemas</td>
<td>IEC61968 Part 8 XSDs specify the message payloads for system interactions in customer support use cases.</td>
</tr>
<tr class="odd">
<td>61968-9 Schemas</td>
<td>IEC61968 Part 9 XSDs specify the message payloads for system interactions in meter reading and control use cases.</td>
</tr>
<tr class="even">
<td>61968-100 Schemas</td>
<td>IEC61968 Part 100 XSDs specify the message headers for CIM message payloads.</td>
</tr>
<tr class="odd">
<td>IEC 62325-504</td>
<td><p>This part of the 32325 series defines the services needed to support the electronic data interchanges between different actors on the European Energy Market for Electricity (EME) in a fast (near-real time), and secure way. At the same time, this Technical Specification can also be applied to integration problems outside the scope of IEC 62325-451, such as to the integration of gas market systems or general enterprise integration</p>
<p>Web Services (in WSDL) will be specified for the defined services, applying the Basic Web Service Pattern implementation profile from IEC 61968-100.</p></td>
</tr>
</tbody>
</table>

**Table 9‑5. XML Schemas Under CIM Management (Cont’d)**

### Hybrid Schemas

The Hybrid schemas under CIM management are listed and described in Table 9‑6.

<span id="_Ref25432000" class="anchor"></span>Table 9‑6. Hybrid Schemas Under CIM Management

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Hybrid Schema</strong></th>
<th><strong>Hybrid Schema Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IEC 61970-555</td>
<td><p>This international standard specifies the translation of the CIM UML into a CIM based machine-readable format named the "Efficient Model Exchange Format"(CIM/E). The CIM/E, which is in use in China, is an alternative to 61970-552 (CIM/XML) for serializing CIM data exchanges. A CIM/E formatted exchange document will contain some symbols with semantic meaning that are not compliant with the XML standard.</p>
<p>IEC 61970-555 specifies how the CIM/E schema is used to support power system models or particular application data models exchange requirements, especially for real-time or online applications. Similar to CIM/XML, CIM/E is an efficient serialization format to describe CIM objects. The power system model described by CIM/E can be converted bi-directionally with consistent result.</p></td>
</tr>
</tbody>
</table>

## CIM Management Documents and Records

CIM management documents are electronic or paper objects that contain instructions for tasks, requirements for how and when to perform a task or function, and logs the task execution and decisions. CIM management documents can communicate and share information and knowledge. Examples of CIM management documents include procedures, protocols, methods, and specifications.

CIM records are a subset of CIM management documents that provide evidence that actions were taken and decisions were made in keeping with procedures; they can serve as evidence of the Working Group’s activity and compliance with IEC processes and procedures.

### CIM Management Documents

Table 9‑7 is a list and description of CIM Management Documents maintained by CIM model managers.

<span id="_Ref25435542" class="anchor"></span>Table 9‑7. CIM Management Documents

| **Document**                                | **Document Description**                                                                                                                                                                                                                                                       |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Action Item List**                        | The action item list is a list of actions that have been assigned to one of the model managers to complete. The action item list is used to identify and track the activity of the model managers.                                                                             |
| **CIM Management Processes and Procedures** | The purpose of this document is to provide a detailed description of the processes and procedures that are involved in CIM Model Management. This document is written by CIM model managers for CIM model managers and anyone who is considering becoming a CIM model manager. |
| **CIM Modeling Guide**                      | The purpose of this document is to provide guidance to individuals working with the CIM UML on how to modify the CIM in accordance with the CIM modeling rules and CIM change management. The rules and process are maintained and enforced by the CIM model managers.         |
| **Combined Issues List**                    | The combined issues list is a collection of issues concerning the CIM UML that need to be resolved by a joint effort of more than working group.                                                                                                                               |
| **Model Manager Checklist**                 | The Model Manager Checklist is a list of tasks that need to be completed as a matter of course in implementing a model change request. Currently there is a Model Manager Checklist maintained for each working group.                                                         |
| **Working Group Issues List**               | The working group issues list is a collection of issues raised by a working group concerning the CIM UML contained in their respective top-level CIM package. The issues on these lists can be resolved without involving other working groups.                                |

### CIM Records

Table 9‑8 is a list and description of CIM Records managed by CIM model managers.

<span id="_Ref25435667" class="anchor"></span>Table 9‑8. CIM Records

| **Record**                      | **Record Description**                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Country Comment Responses**   | Country Comment Responses are tracked by CIM Model Management and are used as part of a check and balance to ensure CIM UML changes are included in new versions of the CIM UML to address the responses as intended.                                                                                                                                                                                                                          |
| **Lessons Learned**             | Lessons learned are records that capture experience-based learning at the completion of a major milestone in a CIM Management process or at the completion of a CIM Management process. The lessons are used as input to planning process improvements.                                                                                                                                                                                        |
| **Meeting Agendas**             | Meeting agendas are documents that capture what is planned to be covered during a Model Manager led meeting. The purpose of the agenda is twofold: 1) To be used as a guide during the meeting to make sure everything intended to be covered is known; and 2) To be used as part of a meeting invite to help ensure individuals who should or want to be in attendance are aware of what topics will be covered so they can plan accordingly. |
| **Meeting Minutes**             | Meeting minutes are records of what took place during a Model Manager led meeting.                                                                                                                                                                                                                                                                                                                                                             |
| **Model Change Request**        | A model change request is the document used to identify and track changes to the CIM UML.                                                                                                                                                                                                                                                                                                                                                      |
| **Model Managers Report**       | The Model Managers report is a Model Management status report delivered at face-to-face CIMug and IEC CIM working group meetings. A Model Managers report is prepared for each working group and presented by the working group’s model manager.                                                                                                                                                                                               |
| **Model Release/Change Report** | The Model Release/Change Report is a document that describes changes implemented in a particular release and version of the CIM UML. Each working group prepares its own report.                                                                                                                                                                                                                                                               |
| **Model Validation Report**     | The Model Validation Report is the output of CIM UML validation checking that is used as input to the process step that creates the Model Release/Change Report.                                                                                                                                                                                                                                                                               |
| **Process Metrics**             | Process metrics are records of key performance indicators used to identify under-performing CIM Management processes and to make decisions about changes necessary to improve CIM Management processes.                                                                                                                                                                                                                                        |

**Table 9‑8. CIM Records (Cont’d)**

## Tool Customizations

Tool customizations are artifacts that facilitate or help automate tasks performed by CIM Model Mangers in conjunction with a software tool. Table 9‑9 is a list and description of Tool customizations managed by CIM Model Managers.

<span id="_Ref25435838" class="anchor"></span>Table 9‑9. Tool Customizations

| **Document**                            | **Document Description**                                                                                                                                                                                                                            |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Automation Scripts**                  | Automation scripts are used in Enterprise Architect to automate workflows or perform modeling tasks. An automation script can be written, for example, to perform Model Validation.                                                                 |
| **Model Management Document Templates** | Model management document templates are used in the auto generation of CIM Documents. Document templates are used with jCleanCim and can be used with Word and Enterprise Architect.                                                                |
| **User-Defined Add-ins**                | User-defined add-ins (also referred to as plug-ins) are developed software that is designed to be procedurally added to a tool to extend the base functionality of a tool. User-defined add-ins can be developed for Enterprise Architect.          |
| **User-Defined Configuration Files**    | User-defined configuration files are used to setup an automated tool activity. User-defined configuration files are used with jCleanCim and can be used with Enterprise Architect.                                                                  |
| **User-Defined Model Searches**         | User-defined model searches are used in Enterprise Architect to query the in-memory database of the open Enterprise Architect project.                                                                                                              |
| **Vendor Add-ins**                      | Vendor add-ins (also referred to as plug-ins) are vendor supplied software that is designed to be procedurally added to a tool to extend the base functionality of a tool. Vendor supplied add-ins are available for Word and Enterprise Architect. |

Table 9‑9. Tool Customizations (Cont’d)
