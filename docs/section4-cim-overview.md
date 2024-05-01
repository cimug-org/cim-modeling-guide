# Section 4 - CIM Modeling Overview

## Section 4.1 Business Context

### Section 4.1.1 Business Motivation

Since international deregulation of energy markets began in the 1990’s, the need for electric utility companies to exchange data externally on a regular basis, and internally between software applications, has steadily increased. The exponential growth in integration complexity due to the large number of proprietary application interfaces created a significant risk to the reliable operation of an interconnected electric power grid owned and operated by different electric utility companies. In addition, there is a greater demand for higher quality data within a utility enterprise and in power markets. The increase in operational complexity of the interconnected power grid has made grid operations dramatically more dependent on complex computer-based analytically-intensive operating practices.

These business drivers have led to the need for transformation of the traditional electric power grid into a “smart” grid. A Smart Grid is an interconnected electric power grid (system) that incorporates information technology to deliver electricity efficiently, reliably, sustainably, and securely. A Smart Grid system architecture at its core has a high degree of interoperability between its distributed components to handle the significant increase in the operational complexity of the system.

In order to achieve a high degree of system interoperability electric utility companies need a standard way to exchange information with each other, ISOs and energy markets. Specifically, electric utility companies need: 

1. a common power system model, 

2. a common information exchange format, 

3. and common data naming and typing in order to achieve a high degree of interoperability.


### Section 4.1.2 Smart Grid Conceptual Model

The NIST Smart Grid Conceptual Model diagram (shown in Figure 4.1) is a high-level view of Smart Grid conceptual domains and their overall interconnectivity. Each domain represents the types of services, interactions, and stakeholders that make decisions and exchange information.

![](images/media/conceptual-model.png)

Figure 4-1. NIST Smart Grid Conceptual Model

### Section 4.1.3 Smart Grid Conceptual Reference Model

The NIST Conceptual Reference Model (shown in Figure 4-2) is a refinement of the NIST Conceptual Model. It depicts Smart Grid communication pathways. It is intended to aid in identifying potential intra- and inter-domain interactions and potential applications and capabilities enabled by these interactions. 

![](images/media/nist-smart-grid-conceptual-reference-model.png)

Figure 4-2. NIST Smart Grid Conceptual Reference Model



## Section 4.2 Business Solution Overview

### Section 4.2.1 Transformation Approach

A systematic, model-driven, standards-based approach is being used to transform traditional electric power grids into Smart Grids. In the United States the National Institute of Standards and Technology (NIST) within the U.S. Department of Commerce has developed and maintains the NIST Framework and Roadmap for Smart Grid Interoperability Standards. In Europe the European Network of Transmission System Operators for Electricity (ENTSO-E) is responsible for carrying out the legally mandated task of development and implementation of standards, network codes, platforms and tools to ensure secure system and market operation as well as integration of renewable energy.

### Section 4.2.2 The GWAC Stack and the NIST Smart Grid Model

The GridWise Architecture Council (GWAC) was formed by the U.S. Department of Energy to promote and enable interoperability among the many entities that interact with the nation's electric power system. To that end the GWAC developed the GWAC Interoperability Framework, commonly known as the “GWAC Stack.” The intent of the interoperability framework is to provide the context for identifying and debating interoperability issues to advance actions that make integration within this complex system easier. The framework recognizes that system interoperability is only achieved when agreement is reached across overarching interdependent layers of concern and cross-cutting interoperability issues. These layers of concern are described in the framework as “layered interoperability categories” and are organized into technical, informational, and organizational groups.

The GWAC Stack grouped interoperability categories along with the NIST Conceptual Reference Model are shown in Figure 4-3. The GWAC Stack interoperability categories and their cross-cutting interoperability issues are shown in Figure 4-4.

![] (images/media/gwac-layers-of-concern.png)

Figure 4-3. GWAC Layers of Concern and NIST Conceptual Reference Model

![](images/media/gwac-cross-cutting-issues.png)

Figure 4-4. GWAC Stack Interoperability Categories and Cross-Cutting Interoperability Issues

## Section 4.3 CIM Overview

### Section 4.3.1 What Is the CIM?

The CIM is a framework that provides a systematic, model-driven methodology for creating standardized system interfaces based on a common electric utility semantic information model. Deriving system interfaces from a common semantic information model results in a system with a high degree of interoperability. The CIM framework includes:

1. an open-source electric utility semantic information model expressed in the Unified Modeling Language (the CIM UML);

2. a method for developing additional CIM UML model elements;

3. a method for maintaining the CIM UML as a well-formed, consistent semantic information model;

4. a method for deriving implementation models (CIM Profiles) from the CIM UML;

5. CIM Profiles used to create serialized CIM-compliant files and messages;

6. a method for developing extensions to the CIM UML to create a user-defined enterprise information model (EIM).

### Section 4.3.2 Role of the CIM in Smart Grid Architecture

The GWAC Stack is used along with the NIST Conceptual Reference Model to identify where the CIM framework artifacts are located within the Smart Grid Architecture. Figure 4 5 shows where the CIM framework artifacts fit within the GWAC Stack.

![](images/media/cim-and-gwac.png)

Figure 4-5. Location of CIM Framework artifacts within the GWAC Stack

### Section 4.3.3 CIM Standards

CIM Standards are standards published by the International Electrotechnical Commission (IEC) to enable electric power systems integration and data exchange that are based on the CIM UML. The IEC is the governing standards development organization (SDO) used by the electric utility industry to publish its international standards.
IEC Technical Committee 57 (TC 57) was established in 1965 to develop standards for “Power systems management and associated information exchange.” TC 57 oversees the development of power systems modeling standards. TC 57 has four (4) Working Groups that develop CIM Standards.
There are two types of CIM Standards, both derived from the CIM UML – Informational standards and Syntactic standards, based on the GWAC Stack. Informational standards specify:

1. UML model elements that represent real-world power system objects and how they are related to each other;

2. UML model elements that represent electric utility industry information concepts and how they are related to each other;

3. normalized names for UML model elements representing real-world objects and information concepts and their attributes;

4. and common data typing of UML class attributes.

CIM Informational standards are sometimes referred to as “CIM Data Standards.”

CIM Syntactic standards specify the data structure in information exchanged between systems. Syntactic standards are identified in the CIM Framework as “CIM Profiles.”

<ins>It is important to note that the CIM UML is not a standard, nor is it the intellectual property of the IEC. The CIM UML is copyrighted under an Apache 2.0 open-source license held by the UCA International Users Group. The Apache 2.0 license makes the CIM UML open-source and free to use.</ins>

## Section 4.4 Scope of the CIM UML

The scope of the information contained in the CIM UML is established by the scope of work performed by each TC 57 Working Group. The scope of work for each TC 57 working group is described their respective mission statements and is provided in Table 4-1.

Table 4-1. IEC TC57 CIM Working Group Mission Statements

| **Group ID** | **Mission Statement**                                                                                                                       |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| WG13         | Define standards for information exchange among systems supporting business functions directly involved with operation and planning of the overall interconnected electric grid. These functions rely on power system network models to analyse the behaviour of the grid. These business functions cover the entire interconnected grid at all voltage levels, and they often involve interactions between systems at various different participants in the grid (e.g. RTO, TSO, DSO, microgrid, generator, consumer). |
| WG14         | Define standards for information exchange among systems supporting business functions that support power system operations, maintenance and customer support. This includes major business functions such as asset management, work management, meter data management, customer information, geographic information systems and engineering design. Also included is interoperating with assets and business capabilities governed by interconnection agreements with customers. |
| WG16         | Define standards which facilitate the integration of electricity market application software developed independently by different vendors into a market management system, between market management systems and market participant systems. This is accomplished by defining message exchanges to enable these applications or systems access to public data and exchange information independent of how such information is represented internally. |
| WG21         | Define standards for system interfaces, communication protocols and profiles in consideration of:<br><br><un><li>Interconnecting a large number of geographically distributed systems (aggregator, (utility, QSE, SC) to end customer)<li>Domain specific protocols for industrial, home and building automation<li>Domain specific protocols for retail markets, real time pricing, and traditional non-market load management<li>State-of-the-art wireless and wired communication<li>Efficient installation, commissioning and maintenance</ul> |

In summary, the CIM UML contains all of the information required to produce the IEC CIM data standards. Specifically, the CIM UML contains all of the information required to produce IEC Standards IEC61970-301, IEC61968-11, and IEC62325-301. The IEC TC57 CIM information exchange standards (CIM Profiles) are derived from the CIM UML. (Note: WG21 uses IEC62325-301 as the basis for its CIM-based Profiles and therefore does not have a separate IEC CIM data standard).

## Section 4.5	CIM UML Model Structure

The CIM UML uses UML packages to logically organize utility domain information. The CIM UML contains a single high-level (root) package (TC57CIM) and four (4) top-level packages The purpose of top-level packages in the CIM UML is primarily to organize utility domain information logically according to the mission of each IEC TC57 CIM working group. They are also used to define the areas of responsibility for each UCA and TC 57 working group and CIM Model Manager. The CIM UML high-level and top-level package hierarchy is shown in Figure 4-6. The CIM UML is maintained in Sparx Systems' Enterprise Architect (EA) modeling tool as an EA project file.



<span id="_Ref21669616" class="anchor"></span>Table 4‑1. IEC TC57 CIM Working Group Mission Statements

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Group ID</strong></th>
<th><strong>Mission Statement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WG13</td>
<td>Define standards for information exchange among systems supporting business functions directly involved with operation and planning of the overall interconnected electric grid. These functions rely on power system network models to analyse the behaviour of the grid. These business functions cover the entire interconnected grid at all voltage levels, and they often involve interactions between systems at various different participants in the grid (e.g. RTO, TSO, DSO, microgrid, generator, consumer).</td>
</tr>
<tr class="even">
<td>WG14</td>
<td>Define standards for information exchange among systems supporting business functions that support power system operations, maintenance and customer support. This includes major business functions such as asset management, work management, meter data management, customer information, geographic information systems and engineering design. Also included is interoperating with assets and business capabilities governed by interconnection agreements with customers.</td>
</tr>
<tr class="odd">
<td>WG16</td>
<td>Define standards which facilitate the integration of electricity market application software developed independently by different vendors into a market management system, between market management systems and market participant systems. This is accomplished by defining message exchanges to enable these applications or systems access to public data and exchange information independent of how such information is represented internally.</td>
</tr>
<tr class="even">
<td>WG21</td>
<td><p>Define standards for system interfaces, communication protocols and profiles in consideration of:</p>
<ul>
<li><p>Interconnecting a large number of geographically distributed systems (aggregator, (utility, QSE, SC) to end customer)</p></li>
<li><p>Domain specific protocols for industrial, home and building automation</p></li>
<li><p>Domain specific protocols for retail markets, real time pricing, and traditional non-market load management</p></li>
<li><p>State-of-the-art wireless and wired communication</p></li>
<li><p>Efficient installation, commissioning and maintenance</p></li>
</ul></td>
</tr>
</tbody>
</table>

## 4.2 CIM Management Business Context

CIM Management is a business function performed by the CIM Subcommittee of the UCAIug Technical Oversight Committee (see Figure 4‑1).

<img src="/images/media/image2.jpeg" style="width:4.47551in;height:3.02727in" alt="http://www.ucaiug.org/aboutucaiug/ucaiugorg.jpg" />

<span id="_Ref529901341" class="anchor"></span>Figure 4‑1. UCA International Users Group Organization Chart

The CIM Technical Subcommittee is responsible for handling all technical and maintenance issues concerning the CIM and related standards. Responsibilities of the CIM Subcommittee related to CIM Management include:

1.  **Chair Modeling Meetings**

    - Review model updates submitted by working groups with working group representative(s)

2.  **Manage the CIM Issues Process**

    - Compile and categorize issues

    - Develop proposed resolutions

    - Obtain agreement on resolutions from CIM Technical Subcommittee and IEC TC57 WG13, WG14, WG16 and WG21.

3.  **Manage Versions of CIM Artifacts**

    - Provide version management of the CIM UML model

    - Provide version management of derived files in other formats (e.g., XML, RDF, etc.)

4.  **Maintain Oversight of CIM Support Tools**

    - Maintain oversight of which version of Sparx Enterprise Architect is used to maintain the CIM UML.

    - Maintain oversight of the jCleanCIM tool used for validation of the CIM UML model.

5.  **Maintain CIM Repositories**

    - Maintain repositories for artifacts produced by individual projects implementing the CIM and related standards, such as:

      - submitted CIM extensions;

      - message payload definitions;

      - tools, and;

      - training materials.

      - Maintain repositories for sample CIM/XML/RDF power system model files

## 4.3 CIM Management Functions

### 4.3.1 Model Change Management

Model change management (MCM) is the ongoing process of identifying and managing CIM UML change requests. A model change management plan (MCMP) is developed to define, document and track the information required to effectively manage change requests throughout the CIM UML development life cycle.

### 4.3.2 Model Change Validation

Model change validation (MCV) is the ongoing process of ensuring proposed CIM UML changes are in compliance with CIM modeling rules.

### 4.3.3 Model Change Implementation

Model change implementation (MCI) is the ongoing process of making changes to an existing CIM UML baseline to create a new CIM UML baseline.

### 4.3.4 Configuration Management

Configuration management (CM) is the ongoing process of identifying and managing changes to the CIM UML and other work products. A configuration management plan (CM Plan) is developed to define, document, control, implement, account for, and audit changes to the various CIM configuration items. The CM Plan provides information on the requirements and procedures necessary for CMP activities and establishes the methodology for configuration identification and control of releases and changes to configuration items. It also describes the process for maintaining status accounting and verifying the completeness and correctness of configuration items throughout the CIM UML development life cycle.

### 4.3.5 Model Distribution

Model distribution (MD) is the ongoing process of distributing CIM UML baselines to official repositories and authorized consumers of the CIM UML.

### 4.3.6 Continuous Process Improvement

Continuous process improvement (CPI) is the ongoing process of improving the CIM management processes through incremental and breakthrough improvements. The goal of CPI is to improve the quality of the CIM UML or the efficiency of the CIM management processes.

### 4.3.7 CIM Management Function Mappings

Mapping of the CIM management functions includes two (2) mappings of the CIM management functions. The first shows the mapping between CIM management functions and CIM management responsibilities assigned to the CIM Subcommittee with the UCAIug. The second shows the mapping between CIM management functions and the CIM management processes that realize those functions. The first mapping is shown in Figure 4‑2. The second mapping is discussed in Section 4.4 and shown in Figure 4‑9


<img src="/images/media/image3.png" style="width:5.53416in;height:3.21783in" />

<span id="_Ref1988984" class="anchor"></span>Figure 4‑2. CIM Management Functions-to-UCA CIM Responsibilities Mapping

## 4.4 CIM Management Processes

CIM management processes are the realization of CIM management functions. There are five (5) CIM management processes. The CIM management processes are shown in Figure 4‑3. A list of the processes and their descriptions are provided in Table 4‑2.

![](images/media/image4.png)

<span id="_Ref22556726" class="anchor"></span>Figure 4‑3. CIM Management Processes

<span id="_Ref22556968" class="anchor"></span>Table 4‑2. CIM Management Processes

| **Process**  | **Process Description**  |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Model Development | The model development process is the core CIM UML process. It is executed to extend the CIM UML and create a new baseline of the CIM UML. This process is triggered by any one of the roles that is responsible for model development. The model development process flow is shown in Figure 4‑4. CIM Management is performed as part of the “Verify Extended Model” subprocess. |
| Change Management | The Change Management Process establishes an orderly and effective procedure for tracking the submission, coordination, review, evaluation, categorization of change requests, and approval for release of changes to CIM UML baselines. The Change Management Process is shown in Figure 4‑5. Changes can either be modifications to existing model elements or the creation of new model elements.  |
| Document Generation | The document generation process involves the creation of the document artifacts associated with the CIM. The CIM UML is used to create these documents as exemplified in Figure 4‑6. CIM Profiles (including RDF and XML schemas) are generated by the IEC working groups. CIM Model Managers may assist working groups in creating RDF and XML schemas. All other artifacts under CIM Management are generated by CIM Model Managers. |
| Artifact Distribution | The artifact distribution process ensures comprehensive distribution of artifacts under CIM management (see Section 8 for details) to CIMug repositories and other subscribers of those artifacts. The artifact distribution process flow is shown in Figure 4‑7. |
| Continuous Process Improvement | The continuous process improvement process establishes a sequence of activities for incremental improvement of the change request and model distribution processes with the goal of improving the quality of the CIM UML or the efficiency of the CIM management processes. The continuous process improvement process is shown in Figure 4‑8. |

![](images/media/image5.png)

<span id="_Ref2079526" class="anchor"></span>Figure 4‑4. Model Development Process Flow

<img src="/images/media/image6.png" style="width:7.78294in;height:2.33488in" />

<span id="_Ref1985784" class="anchor"></span>Figure 4‑5. Change Management Process

![](images/media/image7.png)

<span id="_Ref22563694" class="anchor"></span>Figure 4‑6. Document generation from CIM UML

![](images/media/image8.png)

<span id="_Ref2158379" class="anchor"></span>Figure 4‑7. Artifacts Distribution Process Flow

![](images/media/image9.png)

<span id="_Ref1995527" class="anchor"></span>Figure 4‑8. Continuous Process Improvement Process Flow

### 4.4.1 CIM Management Process Mappings

The mapping between CIM management functions and the CIM management processes are shown in Figure 4‑9.

<img src="/images/media/image10.png" style="width:7in;height:3.33194in" />

<span id="_Ref1994217" class="anchor"></span>Figure 4‑9. CIM Management Process-to-CIM Management Functions Mapping

The CIM Model Managers perform most of the tasks within the CIM management processes. There are however, other roles within the CIMug and IEC working groups that also perform CIM management tasks. The following table provides a description of each role and its mapping to CIM management processes.

| **Role** | **Role Description** | **MDP** | **CMP** | **DGP** | **ADP** | **CPIP** |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|---------|---------|---------|----------|
| CIMug Focus Community | This group role consists of individual CIMug members and IEC CIM Working Group members dedicated to developing CIM extensions that deal with a specific area of focus. |  <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> |         |         |         |          |
| CIMug Project Team | This group role consists of individual CIMug members and IEC CIM Working Group members working on projects that are jointly funded by participating utilities or vendor companies. | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> |         |         |         |          |
| CIMug Working Group | This group role consists of individual CIMug members working on issues of common interest to CIM Users. | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> |         |         |         |          |
| IEC CIM Working Group | This group role consists of individuals appointed by their respective IEC National Committee (technical experts) that take part in the drafting of IEC standard working documents. | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> |         | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> |         |          |
| IEC Working Group Project Leader | This individual role performed by an IEC Working Group member has overall responsibility for leading the development of a new edition of an international standard from the IEC proposal stage through to the IEC publication stage. | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> |         | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> |         |          |
| IEC Working Group Convener | This individual role performed by an IEC Working Group member is responsible for arranging and leading face-to-face IEC Working Group meetings and providing working group oversight.  |         | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> |         |         | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> |
| Model Manager | This individual role performed by an individual that is a member of both the CIMug and an IEC Working Group has overall responsibility for artifacts under CIM management. | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> |

<span id="_Toc25586011" class="anchor"></span>Table 4‑3. Role-to-CIM Management Process Mapping

## 4.5 CIM Management Process Integration with the IEC Standards Process

### 4.5.1 IEC Standards Development Process

As IEC standards, the CIM standards must go through the IEC international standards development process to be published. An IEC International Standard is the result of an agreement between the National Committees of the IEC. The IEC standard development process and the documents created in the process are shown in Figure 4‑10. A description of the IEC stages is provided in Table 4‑4.

![](images/media/image11.png)

<span id="_Ref22425787" class="anchor"></span>Figure 4‑10. IEC International Standard Development Process

<span id="_Ref22426512" class="anchor"></span>**Table 4‑4. Description of IEC Standard Development Stages.**

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Stage</strong></th>
<th><strong>Stage Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Preliminary Stage</td>
<td>The preliminary stage is applied for work items where no target dates can be established. This stage can be used for the elaboration of a new work item proposal and the development of an initial draft. These work items are subject to approval in accordance with the normal procedures before progressing to the preparatory stage.</td>
</tr>
<tr class="even">
<td>Proposal Stage</td>
<td>The proposal stage is the first step in creating a new standard. During this stage a working group generates a proposal for new work. The output of this stage is a New Work Item Proposal (NWIP). The NWIP is submitted via a National Committee to the IEC and communicated to the members of the appropriate IEC CIM working group.</td>
</tr>
<tr class="odd">
<td>Preparatory Stage</td>
<td><p>During this stage a Working Draft (WD) is prepared, generally by a project leader within a project team. The availability of working draft (if not supplied with the proposal) is 6 months.</p>
<p>The preparatory stage ends when a working draft is available for circulation to the members of the technical committee or subcommittee as a first committee draft (CD) and is registered by the office of the CEO.</p></td>
</tr>
<tr class="even">
<td>Committee Stage</td>
<td>The committee stage is the principal stage at which comments from National Committees are taken into consideration, with a view to reaching consensus on the technical content.</td>
</tr>
<tr class="odd">
<td>Enquiry Stage</td>
<td>After addressing the comments received from national committees about the CD the working group then prepares an updated version of the standard that is issued as a Committee Draft for Vote (CDV). This is circulated to member countries for a five-month voting period and is considered approved if two thirds of the votes cast are in favor and the number of negative votes does not exceed 25% of the votes cast. At this stage countries may still submit comments along with their vote.</td>
</tr>
<tr class="even">
<td>Approval Stage</td>
<td><p>The working group, once again, addresses any comments that have been received and prepares a Final Draft International Standard (FDIS). This is submitted to the IEC Central Office and circulated to the national committees for a two-month voting period. At this stage a country may only make an explicit vote: positive, negative or abstention.</p>
<p>The FDIS is approved if two thirds of the votes cast are in favor and the number of negative votes cast does not exceed 25% of the votes cast. If approved, the document is published however if the conditions are not met it is referred back to the working group to be revised. Final publication is the responsibility of the IEC Central Office and leads to the publication of an international standard. This normally takes place within two months of the approval of the FDIS.</p></td>
</tr>
<tr class="odd">
<td>Publication Stage</td>
<td><p>This stage is entirely the responsibility of the Central Office and leads to publication of the International Standard, normally within 6 weeks of approval of the FDIS.</p>
<p>Once a final draft International Standard has been approved, only minor editorial changes are introduced into the final text. The International Standard is published within 6 weeks of approval of the FDIS.</p></td>
</tr>
</tbody>
</table>

### 4.5.2 Process Integration Points

The CIM management processes integrate with the IEC standards development process because the CIM UML provides the basis for IEC CIM standards. There are two types of integration points between the two processes: 1) draft standards preparation; and 2) draft standards submission.

A mapping between the applicable IEC standards development stages and the CIM Management processes are provided in Table 4‑5.

<span id="_Ref22569302" class="anchor"></span>Table 4‑5. CIM Management Processes-to-IEC Standard Development Stage Mappings

| | Proposal Stage | Preparatory Stage | Committee Stage | Enquiry Stage | Approval Stage | Publication Stage |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Model Development Process | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | |
| Change Management Process | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | |
| Document Generation Process | | | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | |
| Artifact Distribution Process | | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> | <img src="/images/media/image12.png" style="width:0.15518in;height:0.17674in" alt="Image result for check mark" /> |

#### 4.5.2.1 Draft Standards Preparation

The intermediate draft standards submitted to the IEC are produced during the execution of the Model Development process and the Document Generation process. CIM UML changes are incorporated to form the basis of the draft standards. Therefore, the Change Management process is also part of draft standards preparation.

#### 4.5.2.2 Draft Standards Submission

The submission of the draft standards to the IEC takes place during the Artifact Distribution process. The IEC is considered one of the subscribers for the draft standards in the process.
