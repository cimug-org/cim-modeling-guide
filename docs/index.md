<img src="images/media/image1.png" style="width:3.02526in;height:1.41679in" />

**UCAIug**

**CIM Modeling Guide**

**Version 2.0.1**

**12-December-2023**


!!! Note

    When referencing an offline PDF version of this guide it is recommended to confirm it corresponds to the latest publicly available guide at [https://cim-mg.ucaiug.io](https://cim-mg.ucaiug.io).


**UCA International Users Group**


> **RIGHT TO DISTRIBUTE AND CREDIT NOTICE**
>
> THIS MATERIAL WAS CREATED BY THE UCA INTERNATIONAL USERS GROUP AND IS AVAILABLE FOR PUBLIC USE AND DISTRIBUTION.  PLEASE INCLUDE CREDIT IN THE FOLLOWING MANNER, “UCAIUG CIM MODELING GUIDE, VERSION 2.0.2, © DECEMBER 2023. ALL RIGHTS RESERVED BY THE UCA INTERNATIONAL USERS GROUP”.

DISCLAIMER OF WARRANTIES AND LIMITATION OF LIABILITIES

> THIS DOCUMENT IS A WORK PRODUCT OF THE UCA INTERNATIONAL USERS GROUP CIM MODEL MANAGERS AND APPROVED BY THE UCA INTERNATIONAL USERS GROUP LEADERSHIP. NEITHER THE CIM MODEL MANAGERS, THE UCA INTERNATIONAL USERS GROUP LEADERSHIP, THE CIM USERS GROUP, NOR ANY PERSON ACTING ON BEHALF OF ANY OF THEM:
>
> \(A\) MAKES ANY WARRANTY OR REPRESENTATION WHATSOEVER, EXPRESS OR IMPLIED, (I) WITH RESPECT TO THE USE OF ANY INFORMATION, APPARATUS, METHOD, PROCESS, OR SIMILAR ITEM DISCLOSED IN THIS DOCUMENT, INCLUDING MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE, OR (II) THAT SUCH USE DOES NOT INFRINGE ON OR INTERFERE WITH PRIVATELY OWNED RIGHTS, INCLUDING ANY PARTY'S INTELLECTUAL PROPERTY, OR (III) THAT THIS DOCUMENT IS SUITABLE TO ANY PARTICULAR USER'S CIRCUMSTANCE; OR
>
> \(B\) ASSUMES RESPONSIBILITY FOR ANY DAMAGES OR OTHER LIABILITY WHATSOEVER (INCLUDING ANY CONSEQUENTIAL DAMAGES, EVEN IF THE UCA INTERNATIONAL USERS GROUP OR ANY UCA INTERNATIONAL USERS GROUP REPRESENTATIVE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES) RESULTING FROM YOUR SELECTION OR USE OF THIS DOCUMENT OR ANY INFORMATION, APPARATUS, METHOD, PROCESS, OR SIMILAR ITEM DISCLOSED IN THIS DOCUMENT.
>
> \(C\) REFERENCE HEREIN TO ANY SPECIFIC COMMERCIAL PROCESS, OR SERVICE BY ITS TRADE NAME, TRADEMARK, MANUFACTURER, OR OTHERWISE, DOES NOT NECESSARILY CONSTITUTE OR IMPLY ITS ENDORSEMENT, RECOMMENDATION, OR FAVORING BY THE UCA INTERNATIONAL USERS GROUP.

THIRD PARTY INTELLECTUAL PROPERTY

> THE CIM STANDARDS ARE A SET OF INTERNATIONAL ELECTROTECHNICAL COMMITTEE (IEC) STANDARDS AND ARE THE INTELLECTUAL PROPERTY OF THE IEC. THE UCA INTERNATIONAL USERS GROUP HAS A LIAISON D RELATIONSHIP WITH THE IEC THAT PROVIDES ACCESS RIGHTS TO THE CIM STANDARDS FOR SOFTWARE DEVELOPMENT.
>
>THE COMMON INFORMATION MODEL (CIM) IS RENDERED IN THE UNIFIED MODELING LANGUAGE (CIM UML). THE CIM UML IS COPYRIGHTED UNDER AN APACHE 2.0 OPEN-SOURCE LICENSE HELD BY THE UCA INTERNATIONAL USERS GROUP. MAJOR PORTIONS OF THIS LICENSE ARE OWNED BY THE ELECTRIC POWER RESEARCH INSTITUTE (EPRI) AND THE REMAINING PORTIONS ARE PROVIDED BY OTHER CONTRIBUTORS.

# Acknowledgements

In preparing this specification, the UCAIug recognizes the special contributions of the following CIM Subcommittee and their organizations.

- Becky Iverson - *Siemens*

- Eric G. Stephan - *Pacific Northwest National Labs*

- Henry B. Dotson, III - *Mandla Solutions, Inc.*

- Kendall Demaree - *Ahlstrom*

- Kurt Hunter - *Siemens*

- Margaret Goodrich - *Project Consultants, LLC*

- Martin Miller - *ABB*

- Tatjana Kostic - *ABB*

- Todd Viegut - *AspenTech*

##  

# *Abstract*

> *This document specifies the rules and recommendations on how to evolve and maintain the Common Information Model (CIM) of the electric power grid and information from supporting business domains. This model is referred to as the CIM UML. The primary purpose of the rules is to specify how to evolve and maintain the CIM UML as a well-formed, consistent semantic information model using a standard methodology. The primary purpose of the recommendations is to provide guidelines on how to extend the CIM UML with additional information to create a user-defined CIM-compliant enterprise information model (EIM). The intent of this document is to facilitate and guide the incorporation of new information into the CIM UML and its extension.*


# Foreword

Exchanging power systems data between utility companies is always problematic when proprietary formats are used. In the past a company would traditionally use a single software system, whether it is a custom in-house solution, or purchased from a large software company, and there would be a single proprietary data standard and format used. With the deregulation of the power industry and the emergence of smarter grids, there is now a greater need to be able to share such power system data between companies and systems.

The increase in choice provided by the number of power system software vendors and the different software packages and architectures available add to the challenge of data exchange. These issues point to a requirement for a single, open standard for describing power system data and to aid the interoperability between software packages and exchange of information both within one company and between companies.

The Common Information Model (CIM) is an open standard for representing power system components originally developed by the Electric Power Research Institute (EPRI) in North America. The CIM provides the basis of a series of standards developed under the auspices of the International Electrotechnical Commission (IEC). 

The CIM standard was started as part of the Control Centre Application Programming Interface (CCAPI) project at EPRI with the aim of defining a common definition for the components in power systems for use the Energy Management System (EMS) Application Programming Interface (API). The EMS API is now maintained by IEC Technical Committee 57 Working Group 13 as IEC 61970-301. The format has been adopted by the major EMS vendors to allow the exchange of data between their applications, independent of their internal software architecture or operating platform.[^1]

# About the UCA International CIM Users Group

The UCA International Users Group (UCAIug) is a not-for-profit corporation focused on assisting users and vendors in the deployment of standards for real-time applications for several industries with related requirements. The UCAIug does not write standards, however it works closely with those bodies that have primary responsibility for the completion of standards (notably IEC TC 57: *Power Systems Management and Associated Information Exchange*).

The UCAIug as well as its member groups (the CIM Users Group (CIMug), Open Field Message Bus (OpenFMB), and  IEC61850) draws its membership from utility user and supplier companies. The mission of the UCAIug is to enable integration through the deployment of open standards by providing a forum in which the various stakeholders in the energy and utility industry can work cooperatively together as members of a common organization to:

- Influence, select, and/or endorse open and public standards appropriate to the energy and utility market based upon the needs of the membership.

- Specify, develop and/or accredit product/system-testing programs that facilitate the field interoperability of products and systems based upon these standards.

- Implement educational and promotional activities that increase awareness and deployment of these standards in the energy and utility industry.

- Influence and promote the adoption of standards and technologies specific to the ever-increasing Smart Grid initiatives worldwide.

This document is a work product produced by the CIM Subcommittee with the intent to help accomplish the UCAIug mission.

[^1]: "Common Information Model Primer: Eighth Edition”; EPRI, Palo Alto, CA: 2022 [EPRI 3002001040](https://www.epri.com/research/products/000000003002024188)

# Revision History

| **Rev #**    | **Rev Date**             | **Author**         | **Description**                                                      |
|--------------|--------------------------|--------------------|----------------------------------------------------------------------|
| 1.0          | 25-Nov-2019              | H. Dotson          | Initial Release                                                      |
| 1.1          | 13-Feb-2021              | H. Dotson          | Update to Rule 197                                                   |
| 2.0          | 31-Aug-2022              | H. Dotson          | Added CIM Modeling Overview, CIM Processes, CIM Extension Rules,<br>CIM Extension Rules, and Version Control Rules |
| 2.0.1        | 30-Jan-2023              | H. Dotson          | Removed all information related to CIM Model Management procedures.<br>The overview in Section 4 was updated<br>Inserted a new methodology section after section 4 and then revised<br>and adjusted the number on subsequent sections. |
| 2.0.2        | 12-Dec-2023              | T. Viegut          | Added missing definitions for ISO and Enterprise Information Model (EIM) in Section 3. |
