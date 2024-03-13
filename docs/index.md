<img src="images/media/image1.png" style="width:3.02526in;height:1.41679in" />

**UCAIug**

**CIM Modeling Guide**

**Version 1.1**

**13-February-2021**


!!! Note

    When referencing an offline PDF version of this guide note that it may not corresponds to the latest publicly available guide. To reference the latest visit [https://cim-mg.ucaiug.io](https://cim-mg.ucaiug.io).


**UCA International Users Group**


> **RIGHT TO DISTRIBUTE AND CREDIT NOTICE**
>
> This material was created by the UCA International Users Group CIM Model Managers and is available for public use and distribution. Please include credit in the following manner, “UCAIug CIM Modeling Guide, Version 1.1, © November 2021. All rights reserved by the UCA International Users Group”.

DISCLAIMER OF WARRANTIES AND LIMITATION OF LIABILITIES

> THIS DOCUMENT is a work product of THE UCA International Users Group. it was prepared by the CIM Model Managers and approved by the UCA International Users Group leadership. NEITHER the CIM Model Managers, the UCA International Users Group leadership, the CIM users group, NOR ANY PERSON ACTING ON BEHALF OF ANY OF THEM:
>
> \(A\) MAKES ANY WARRANTY OR REPRESENTATION WHATSOEVER, EXPRESS OR IMPLIED, (I) WITH RESPECT TO THE USE OF ANY INFORMATION, APPARATUS, METHOD, PROCESS, OR SIMILAR ITEM DISCLOSED IN THIS DOCUMENT, INCLUDING MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE, OR (II) THAT SUCH USE DOES NOT INFRINGE ON OR INTERFERE WITH PRIVATELY OWNED RIGHTS, INCLUDING ANY PARTY'S INTELLECTUAL PROPERTY, OR (III) THAT THIS DOCUMENT IS SUITABLE TO ANY PARTICULAR USER'S CIRCUMSTANCE; OR
>
> \(B\) ASSUMES RESPONSIBILITY FOR ANY DAMAGES OR OTHER LIABILITY WHATSOEVER (INCLUDING ANY CONSEQUENTIAL DAMAGES, EVEN IF the UCA International Users Group OR ANY UCA International Users Group REPRESENTATIVE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES) RESULTING FROM YOUR SELECTION OR USE OF THIS DOCUMENT OR ANY INFORMATION, APPARATUS, METHOD, PROCESS, OR SIMILAR ITEM DISCLOSED IN THIS DOCUMENT.
>
> \(C\) Reference herein to any specific commercial process, or service by its trade name, trademark, manufacturer, or otherwise, does not necessarily constitute or imply its endorsement, recommendation, or favoring by the UCA International Users Group.

THIRD PARTY INTELLECTUAL PROPERTY

> The CIM standards are a set of International Electrotechnical Committee (IEC) standards and are the Intellectual Property of the IEC. the UCA International Users Group has a liaison d relationship with the iec that provides access rights to the cim standards for software development. the common information model (CIM) is Open Source and is rendered in the Unified Modeling Language.

# Acknowledgements

In preparing this specification, the UCAIug recognizes the special contributions of the following CIM Subcommittee and their organizations.

- Becky Iverson - *Siemens*

- Eric G. Stephan - *Pacific Northwest National Laboratory*

- Henry B. Dotson, III - *Mandla Solutions, Inc.*

- Kendall Demaree - *Ahlstrom*

- Kurt Hunter - *Siemens*

- Margaret Goodrich - *Project Consultants, LLC*

- Martin Miller - *ABB*

- Tatjana Kostic - *ABB*

##  

# *Abstract*

> *This document specifies the rules and recommendations on how to use the UML to create and maintain a standardized Common Information Model (CIM) of the electric grid and other related business domains. Such models are called Domain Models. The primary goal of this document is to facilitate communication and understanding among people working with the CIM domain models. The primary goal of the rules is to specify the structure and modeling constraints applied to the CIM. The primary goal of the recommendations is to provide guidelines on how to extend the CIM as more of the model is elaborated by working groups within the International Electrotechnical Commission (IEC) and by the CIM user community. The intent of the recommendations is to facilitate the incorporation of new model elements into the CIM.*


# Foreword

Exchanging power systems data between utility companies is always problematic when proprietary formats are used. In the past a company would traditionally use a single software system, whether it is a custom in-house solution, or purchased from a large software company, and there would be a single proprietary data standard and format used. With the deregulation of the power industry and the emergence of smarter grids, there is now a greater need to be able to share such power system data between companies and systems.

The increase in choice provided by the number of power system software vendors and the different software packages and architectures available add to the challenge of data exchange. These issues point to a requirement for a single, open standard for describing power system data and to aid the interoperability between software packages and exchange of information both within one company and between companies.

The Common Information Model (CIM) is an open standard for representing power system components originally developed by the Electric Power Research Institute (EPRI) in North America. The CIM provides the basis of a series of standards developed under the auspices of the International Electrotechnical Commission (IEC). The CIM standard was started as part of the Control Centre Application Programming Interface (CCAPI) project at EPRI with the aim of defining a common definition for the components in power systems for use the Energy Management System (EMS) Application Programming Interface (API). The EMS API is now maintained by IEC Technical Committee 57 Working Group 13 as IEC 61970-301. The format has been adopted by the major EMS vendors to allow the exchange of data between their applications, independent of their internal software architecture or operating platform.[^1]

# About the UCA International CIM Users Group

The UCA International Users Group (UCAIug) is a not-for-profit corporation focused on assisting users and vendors in the deployment of standards for real-time applications for several industries with related requirements. The UCAIug does not write standards, however it works closely with those bodies that have primary responsibility for the completion of standards (notably IEC TC 57: *Power Systems Management and Associated Information Exchange*).

The UCAIug as well as its member groups (the CIM Users Group (CIMug), Open Smart Grid, and IEC61850) draws its membership from utility user and supplier companies. The mission of the UCAIug is to enable integration through the deployment of open standards by providing a forum in which the various stakeholders in the energy and utility industry can work cooperatively together as members of a common organization to:

- Influence, select, and/or endorse open and public standards appropriate to the energy and utility market based upon the needs of the membership.

- Specify, develop and/or accredit product/system-testing programs that facilitate the field interoperability of products and systems based upon these standards.

- Implement educational and promotional activities that increase awareness and deployment of these standards in the energy and utility industry.

- Influence and promote the adoption of standards and technologies specific to the ever-increasing Smart Grid initiatives worldwide.

This document is a work product produced by the CIM Subcommittee with the intent to help accomplish the UCAIug mission.

[^1]: "Common Information Model Primer: Eighth Edition”; EPRI, Palo Alto, CA: 2022 [EPRI 3002001040](https://www.epri.com/research/products/000000003002024188)
