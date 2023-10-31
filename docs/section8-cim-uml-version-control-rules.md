# Section 8 - CIM UML Version Control Rules

## 8.1 Overview

After the top-level CIM packages have been synchronized and deployed as the complete CIM UML for use by either working groups or into the public domain, profiles will naturally be developed that have dependencies on it. When the need arises to make changes to the CIM UML, an impact assessment needs to be made to determine:

- Whether the changes will negatively impact existing (and potentially future) CIM Profiles

- How changes that will or will not impact CIM Profiles should be implemented and communicated.

These issues result in the need for versioning. How versioning is implemented and communicated is specified in a **Version Control Strategy**. The Version Control Strategy must answer the following questions:

- What exactly constitutes a new version of the CIM UML?

- What is the difference between a major and a minor version?

- What do the parts of a version number indicate?

- Will the new version of the CIM UML still work with existing profiles that were designed for the old CIM UML version?

- Will the current version of the CIM UML work with new profiles that have different data exchange requirements?

- What is the best way to add changes to the CIM UML while minimizing the impact on profiles?

The remaining subsections of this overview address these questions and provide a set of options for solving common versioning problems.

### 8.1.1 The Scope of a Version

We have established that the CIM UML is partitioned into three top-level packages that must be merged and synchronized before being deployed for use. So, when a new version of the CIM UML is created, exactly what is being referring to must be defined.

### 8.1.2 Versioning and Compatibility

The number one concern when developing and deploying a new version of the CIM UML is the impact it will have on users that will develop CIM Profiles that have dependencies on it. The measure of impact is directly related to how compatible the new CIM UML is with the old version(s) of the CIM UML.

This subsection establishes the fundamental types of compatibility that relate to the content of new CIM UML versions and also tie into the goals and limitations of different versioning strategies covered in section 8.2. The different types of compatibility are listed and described in Table 8‑1.

| **Compatibility Type**      | **Compatibility Type Description**                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Backwards Compatibility** | A new version of the CIM UML continues to support CIM Profiles designed to work with the old version is considered *backwards-compatible*.                                                                                                                                                                                                                                                                           |
| **Forwards Compatibility**  | When a new version of the CIM UML can support a range of future CIM Profiles it is considered to have an extent of forwards compatibility. A new version of the CIM UML will support future CIM Profiles by definition. The extent of forwards compatibility is defined by the number of new use case interactions that can be supported with the new CIM UML.                                                       |
| **Compatible Changes**      | When the changes incorporated in a new version of the CIM UML do not negatively affect existing CIM Profiles, then the change itself is considered a *compatible change*. Common compatible changes include adding an enumeration literal, and changes to a UML element description for clarification.                                                                                                               |
| **Incompatible Changes**    | If after a change the CIM UML is no longer compatible with existing CIM Profiles, then the CIM UML is considered to have received an *incompatible change.* The term “Incompatible change” indicates an absence of backwards compatibility. Common incompatibility changes include changing the multiplicity of an association end from “0..”, changing an association role name, and deleting enumeration literals. |

<span id="_Ref22373775" class="anchor"></span>Table 8‑1. Compatibility Types

### 8.1.3 Version Identifiers

Version identifiers always follow some version identification pattern. The version identification pattern used must not only express the version number at the CIM UML level, but right down to the lowest level changeable element or element property. The version identification patterns for the CIM UML are specified in section 8.2.3, Version Identification.

### 8.1.4 Versioning Strategies

There is no one versioning strategy that is right for everyone. Because versioning represents a governance-related phase in the overall lifecycle of the CIM UML, it is a practice that is subject to conventions, preferences, and requirements that are distinct to CIM Management.

Even though there is no de facto versioning strategy for UML models, a number of advocated versioning strategies have emerged, each with its own benefits and tradeoffs. This sub-section will cover the three known versioning strategies considered for the CIM UML.

#### 8.1.4.1 The Strict Strategy

The Strict Strategy is the simplest approach to CIM UML versioning. Any compatible or incompatible changes result in a new version of the CIM UML. This approach is commonly implemented by changing the target namespace value. In effect, namespaces are used for version identification instead of a version attribute because changing the namespace value automatically forces a change in all CIM Profiles that need to access the new version of the CIM UML.

This “super-strict” approach is not really practical, but it is the safest and sometimes warranted when there are significant implications to CIM UML changes. Because both compatible and incompatible changes will result in a new CIM UML version, this strategy does not support backwards or forwards compatibility.

***Pros and Cons***

The benefit of this strategy is having full control over the evolution of the CIM UML, and because backwards and forwards compatibility are intentionally disregarded, it is not necessary to be concerned with the impact of any change in particular (because all changes will effectively break existing CIM Profiles).

On the downside, by forcing a new namespace upon the CIM UML with each change, it is guaranteed that all existing CIM Profiles will not longer be compatible with any new version of the CIM UML. CIM Profiles will only be able to continue to enable data exchanges while the old version of the CIM UML remains available along side the new version or until the CIM Profiles themselves are updated to conform to the new CIM UML.

Therefore, this strategy will increase the governance burden on users of the CIM UML and will require careful transitioning strategies. Having two or more version of the CIM UML at the same time can become a common requirement for which a supporting infrastructure will need to be prepared.

#### 8.1.4.2 The Flexible Strategy

A common strategy used to balance practical considerations with an attempt at minimizing the impact of changes to the CIM UML is to allow compatible changes to occur without forcing a new CIM UML version, while not attempting to support forwards compatibility at all.

This means that any backwards-compatible change is considered safe in that it ends up extending or augmenting the existing CIM UML without affecting any of the existing CIM Profiles. A common example of this is changing the description of UML element which results in no material change to the model.

As with the Strict strategy, any change that breaks existing CIM Profiles does result in a new version of the CIM UML, usually implemented by changing the target namespace value of the CIM UML.

***Pros and Cons***

The primary advantage to this strategy is that it can be used to accommodate a variety of changes while consistently retaining the CIM UML’s backwards compatibility.

However, when compatibility changes are made, these changes become permanent and cannot be reversed without introducing an incompatible change. Therefore, a governance process is required during which each proposed change is evaluated to ensure CIM Profiles do not become overly bloated or convoluted.

#### 8.1.4.3 The Loose Strategy

As with the previous two strategies, this strategy requires that incompatible changes result in a new version of the CIM UML. The difference is the changes are modeled in the CIM UML to be intrinsically extensible so that the CIM UML remains able to support a broad range of future, unknown data exchange requirements. Since the CIM UML is, by definition, a semantic information model, it is structured to be intrinsically extensible.

***Pros and Cons***

The fact that all attributes are optional and most associations have an undefined upper range provides a constant opportunity to further expand the CIM UML. On the other hand, there is a governance process required during which each proposed change is evaluated to ensure CIM Profiles do not become overly bloated or convoluted.

#### 8.1.4.4 Summary Table

Table 8‑2 broadly summarizes how the three strategies compare based on three fundamental characteristics.

The three characteristics used in this table to form the basis of this comparison are as follows:

- Strictness – The rigidity of the CIM UML versioning options. The Strict strategy is clearly the most rigid in its versioning rules, while the Loos strategy provides the broadest range of versioning options.

- Governance Impact – The amount of governance burden imposed by a strategy. Both Strict and Loose strategies increase governance burden impact but for different reasons. The Strict strategy requires the issuance of more CIM UML versions which impacts CIM Profiles and infrastructure, while the Loose strategy introduces the need to accommodate large message sets through custom programming of the consuming application.

- Complexity – The overall complexity of the versioning strategy. The Loose strategy has the highest complexity potential, while the straight-forward rules that form the basis of the Strict strategy make it the simplest option.

|                       | **Strategy** |              |           |
|-----------------------|--------------|--------------|-----------|
|                       | **Strict**   | **Flexible** | **Loose** |
| **Rigidity**          | High         | Medium       | Low       |
| **Governance Impact** | High         | Medium       | High      |
| **Complexity**        | Low          | Medium       | High      |

<span id="_Ref22387240" class="anchor"></span>Table 8‑2. A general comparison of the three versioning strategies.

## 8.2 Version Control Strategy

The version control strategy is expressed as a set of rules that address version scope, version compatibility, and version identification. The following sub-sections address each area, respectively.

**NOTE**: The versioning strategy presented here is still under discussion amongst the CIM managers and is subject to change once discussions are completed. The versioning strategy will then be updated to reflect any changes.

### 8.2.1 Version Scope

| **RuleID** | **Description** 
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rule225    | A new version of a top-level package shall be created when the contents of the top-level package (which includes any of its normative sub-packages) has been changed, and the change has been verified by the appropriate CIM model manager. |
| Rule226    | A new version of the CIM UML shall be created when a new version of a top-level package has been created. |

### 8.2.2 Version Compatibility

| **RuleID** | **Description**  |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rule227 | A new version of the CIM UML shall be considered backwards-compatible if it continues to support CIM Profiles designed to work with the old version of the CIM UML (i.e. the changes incorporated in the new version of the CIM UML are compatible changes). |
| Rule228 | A new version of the CIM UML shall be considered not backwards-compatible if it does not support CIM Profiles designed to work with the old version of the CIM UML. |

### 8.2.3 Version Identification

Version identification rules are based on the needs of the CIM UML users. There are two types of CIM UML users: 1) working group members involved in the development of standards; and 2) the broader CIM community (end users). Each type of user has different requirements for version identification.

Working group members need interim versions of the CIM UML in order to work with a synchronized model while developing new model content and creating CIM Profiles. Some of these interim versions may not ever be released to the end users. Therefore, the version identifier for working group members needs to communicate which versions of the top-level CIM packages have been merged and synchronized to create the interim version of the CIM UML.

End users need to be able to distinguish one version of the CIM UML from another, and know which versions of the top-level CIM packages are included in each version. It would be helpful, but not necessary, to be able to determine version compatibility from the version identifier.

The version identification rules specify version naming conventions and how version identification will be communicated.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>RuleID</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Rule229</td>
<td>There shall be one and only one class in the PackageDependencies package that contains date and version information about the combined CIM (hereinafter referred to as the “CIM Version Class”).</td>
</tr>
<tr class="even">
<td>Rule230</td>
<td>The name of the CIM Version Class shall be “PackageDependenciesCIMVersion”.</td>
</tr>
<tr class="odd">
<td>Rule231</td>
<td>The CIM Version Class shall contain two (2) and only two mandatory read only attributes: “date” and “version”.</td>
</tr>
<tr class="even">
<td>Rule232</td>
<td>The value of the “date” attribute of the CIM Version Class shall be the effective date of the CIM UML.</td>
</tr>
<tr class="odd">
<td>Rule233</td>
<td><p>The value of the “version” attribute of the CIM Version Class shall comply with the following version identification pattern when the CIM UML is deployed for public use:</p>
<p>“CIM&lt;XX&gt;.&lt;YY&gt;”</p>
<p>where “XX” stands for the CIM UML major version number and “YY” stands for the minor version number.</p></td>
</tr>
<tr class="even">
<td>Rule234</td>
<td>The CIM UML major version number for versions deployed for public use shall be incremented when either: 1) a significant amount of new model content has been added; or 2) the new version is not backwards compatible.</td>
</tr>
<tr class="odd">
<td>Rule235</td>
<td>The CIM UML minor version number for versions deployed for public use shall be incremented when minor compatible changes have been incorporated into the old version of the CIM UML.</td>
</tr>
<tr class="even">
<td>Rule236</td>
<td>Each working group and its respective model manager shall determine what is a “significant” amount of new model content and what constitutes “minor” compatible changes in order to specify a new CIM UML version number.</td>
</tr>
<tr class="odd">
<td>Rule237</td>
<td>The initial value for the CIM UML minor version number for versions deployed for public use shall be “0” (e.g. “CIM100.0”).</td>
</tr>
<tr class="even">
<td>Rule238</td>
<td><p>The value of the “version” attribute of the CIM Version Class shall comply with the following version identification pattern when the CIM UML is deployed for working group use:</p>
<p>“CIM&lt;XX1&gt;.&lt;YY1&gt;.&lt;XX2&gt;.&lt;YY2&gt;.&lt;XX3&gt;.&lt;YY3&gt;”</p>
<p>Where</p>
<p>“XX1” stands for the IEC61970CIM major version number</p>
<p>“YY1” stands for the IEC61970CIM minor version number</p>
<p>“XX2” stands for the IEC61968CIM major version number</p>
<p>“YY2” stands for the IEC61968CIM minor version number</p>
<p>“XX3” stands for the IEC62325CIM major version number</p>
<p>“YY3” stands for the IEC62325CIM minor version number.</p>
<p>Example: CIM17.34.13.12.03.17a</p></td>
</tr>
<tr class="odd">
<td>Rule239</td>
<td>Each top-level package shall contain one and only one class (referred to as the “IEC Version Class”) that contains date and version information about the CIM UML for the working group.</td>
</tr>
<tr class="even">
<td>Rule240</td>
<td><p>The name of the IEC Version Class shall comply with the following version identification pattern:</p>
<p>“&lt;top-level package name&gt;CIMVersion&gt;”.</p></td>
</tr>
<tr class="odd">
<td>Rule241</td>
<td>The IEC Version Class shall contain two (2) and only two mandatory read only attributes: “date” and “version”.</td>
</tr>
<tr class="even">
<td>Rule242</td>
<td>The value of the “date” attribute of the IEC Version Class shall be the effective date of the CIM UML contained in the top-level package.</td>
</tr>
<tr class="odd">
<td>Rule243</td>
<td><p>The value of the “version” attribute of the IEC Version Class shall comply with the following version identification pattern:</p>
<p>“&lt;top-level-package-name&gt;CIM&lt;XX&gt;v&lt;YY&gt;”</p>
<p>where “XX” stands for the top-level CIM package release number (major version), “YY” stands for the top-level CIM package minor version (update). The release corresponds to a major change in the model while a version is used to keep track of work in progress changes.</p></td>
</tr>
</tbody>
</table>
