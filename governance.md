# Draft Governance for Kwaai pAI-OS Open Source Community

## 1. Introduction

Welcome to the governance document for the Kwaai pAI-OS project.
This document outlines the structure, roles, and processes that will guide our community as we continue to grow and evolve.
Our goal is to empower the current do-ocracy, recognize contributions, and establish a framework for future leadership and governance.

The purpose of a governance document is primarily two-fold:

1. Clarify for contributors how decisions are made.
1. Inform newcomers how decisions are made.

## 2. Community Principles

1. **Open Source** : Any content we create is released under an Open Work license.
Content includes but is not limited to all software, documentations, configuration files, data, and training materials.
"All software" includes the code necessary to operate software, AKA operational code.
1. **Welcoming and respectful** : We intend to be an open, welcoming, and inclusive community.
Diversity is our strength.
We have and follow a Code of Conduct.
1. **Open Design** : We follow a transparent and open process for planning and designing any content, services, and features of pAI-OS.
Ideas and contributions are accepted according to their technical merit and alignment with project objectives, scope, and design principles.
1. **Open Work** : Two of our core tools for successful community building are transparency and accessibility.
To support that, work and collaboration must be done in public to the greatest degree possible.
1. **Sustainable Open Community** : The best way to build a sustainable open source community is to ensure the community cohesion is through openness and transparency, ensuring all the voices are heard and anyone can rise to leadership positions.
The more diversity of voices at the decision table, the better our ability to improve conditions such as inclusion and equity.
Sustainable comes through continuous improvement of those areas, such as through centering the agenda of those people most marginalized and at risk in each given context (which results in things being more accessible for everyone.)

### 2.1 Practices to Support Community Principles

1. **Transparency** : All decision-making processes will be open and transparent.
1. **Inclusivity** : We encourage participation from all community members and value diverse perspectives.
1. **Meritocracy** : Contributions are valued based on merit and effort, recognizing the work done by contributors.
1. **Collaboration** : We foster a collaborative environment where members work together towards common goals.
1. **Respect** : All interactions within the community should be respectful and considerate.

## 3. Membership and Roles
We are borrowing and adapting role descriptions from the [Kubernetes community group definitions](https://github.com/kubernetes/community/blob/master/community-membership.md) as a good place to start from.

This section outlines the various responsibilities of contributor roles in the pAI-OS community.

A contribution can take many, many forms, such as: documentation, code, best-practices content, marketing materials, running a meeting, helping a user in chat, operating a cluster, responding to a `help wanted` flag, reviewing and commenting on contributions of all these types when in a proposed-state (a _pull request_ or _PR_), giving a talk at a conference, staffing a booth at a conference, and so forth.

For a longer list, refer to this chapter, "[What Is A Contribution?](https://www.theopensourceway.org/the_open_source_way-guidebook-2.0.html#_what_is_a_contribution)", which includes these definitions:

> An open source **Contribution**
  >
> Any original, intentional, and substantive object given freely to an open source community, under the licensing of that community.
> A contribution can come from an individual or a community.
> 
> An open source **Contributor**
> 
> Any individual person involved in making Contributions to the community.
> Communities are interpersonal by their nature.
> They consist of humans, not organizations.
> Organizations can send their members, staff, leaders, and so forth out to make contributions to a community as a contributor.

One reason this project runs so many processes through a git workflow is to raise the visibility on all types of contributions and contributor roles.
These interactions by a contributor help qualify and quantify their activities.
It is never a full picture of one's activities, but it is a useful and helpful one.

### 3.1 Roles and Responsibilities
This is our _aspirational_ set of roles and responsibilities.
The project should be expanding to hold roles in this model, or make changes to this governance document to reflect the way roles and responsibilities end up occurring.

| Role             | Responsibilities                              | Requirements                                                                     | Defined by                                          |
| ---------------- | --------------------------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------- |
| Member           | Active contributor in the community           | Sponsored by 2 reviewers and multiple contributions to the project               | pAI-OS GitHub org member                             |
| Reviewer         | Review contributions from other members       | History of review and authorship                               | [OWNERS] file reviewer entry                        |
| Approver         | Contributions acceptance approval             | Highly experienced active reviewer and contributor             | [OWNERS] file approver entry                        |
| Subproject owner | Set direction and priorities for a subproject | Demonstrated responsibility and excellent technical judgement for the subproject | [sigs.yaml] subproject [OWNERS] file _owners_ entry |

### 3.2 Contributors

A _contributor_ is anyone who contributes to the project, including code, documentation, design, and community engagement.

### 3.3 Maintainers

A _maintainer_ is a contributor who has demonstrated sustained contributions and has been given write access to the repository. Maintainers are responsible for reviewing and merging pull requests, as well as guiding the direction of the project.

### 3.4 Leadership Body

As the project grows, a self-appointed leadership body will be established, composed of maintainers and key contributors.
This body will handle strategic decisions and oversight.

The need for forming this body typically arises organically out of repeated requests by contributors to create a formal leadership body. The discussion should be seeded by one of the maintainers within six months of the adoption of this initial governance.

As best practice of Open Source projects, the technical decision making process shall be kept separate from the governance (political) decision process and bodies.

## 4. Decision Making

### 4.1 Consensus Decision Making

We use consensus decision-making, where "a proposal passes if there are no outright blocks to it.
A proposal is blocked if any member states a clear objection and asks that the decision not proceed.
Blocking should be used only if there is a fundamental objection. 
Silence is considered consent."

A full definition of the decision making model is in Appendix A.

##### 4.2 Lazy Consensus

Most decisions are made using lazy consensus, where if no one objects within a specified period, the proposal is accepted.
Seventy two (72) hours is a recommended minimum for lazy consensus, to give the best chance for anyone globally to be able to read about the change.

Ultimately it is up to the person who is making the change and asking for lazy consent to specify the period of time until lazy consensus is recognized.
Thus if the matter is timely or truly minor, it is not unreasonable to give only 24 or even 12 hours notice for lazy consent.

In fact, some forms of lazy consent come in the form of making a change and _afterward_ offering to reverse the change if someone raises a concern within a period of time (72 or more hours.)
If a contributor does this too often, typically social pressure will curtail the habit.

##### 4.3 Full Consensus

For significant decisions, such as changes to this governance document or major project directions, the full consensus decision process will be used.
Maintainers and active contributors can vote +1, 0, or -1.
Three (3) +1 votes and zero (0) -1 votes is the minimum requirement for achieving consensus and a decision to passing, as long as at least seventy two (72) hours has passed for the voting process.

A full definition of consensus decision making is in Appendix B.

#### 5. Evolving Governance

Until the formation of a self-appointing leadership body to manage governance updates, this is how we will handle any updates to this document:

1. Changes to `governance.md` are created as a pull request (PR).
1. The PR author is responsible for publicizing the suggestions into established communication channels.
1. The PR needs to follow either the lazy consensus or full consensus decision process.
	1. Use _lazy consensus_ for small matters, such as punctuation fixes or any non-meaningful change.
	1. Use _full consensus_ when the change is substantive, such as creating or changing a rule about decision making.
1. Once consensus is achieved, a separate person should approve the PR than the one who authored it.

##### 5.1 Establishing a Leadership Body

We will eventually transition to a self-appointed leadership body composed of maintainers and key contributors.
This body will be responsible for strategic decisions and oversight.

- **Formation**: Current maintainers and key contributors will form the initial leadership body.
- **Roles**: The leadership body will include a Chair, Secretary, and other roles as needed.
- **Responsibilities**: Setting strategic direction, resolving conflicts, and ensuring the project's health and sustainability.
- **Separating Technical Decisions**: As a best practice, as we establish a leadership body, we will deliberately separate out the project technical decision bodies from the project governance decision body.

##### 5.2 Transition to an Elected Leadership

The next step will be to establish an elected leadership method to ensure democratic participation and representation.

- **Election Process**:
  - **Nomination**: Any contributor can nominate themselves or be nominated by others.
  - **Voting**: All active contributors can vote.
Voting will be conducted online, ensuring accessibility and transparency.
  - **Terms**: Elected leaders will serve fixed terms, after which new elections will be held.

#### 6. Code of Conduct

To maintain a welcoming and inclusive environment, all community members are expected to adhere to our [Code of Conduct](https://github.com/pAI-OS/paios/blob/main/CODE_OF_CONDUCT.md). **TBD**

#### 7. Amendments

This governance document is a living document and can be amended through a proposal and consensus-voting process.
Major and substantive changes require a full consensus decision process from the maintainers and active contributors.

#### 8. Conclusion

We believe that this governance structure will empower our community, recognize the efforts of our contributors, and provide a clear path for growth and sustainability.
Together, we can ensure the success of the Kwaai pAI-OS project.

---

For any questions or suggestions regarding this governance document, please reach out to the maintainers through the project's communication channels.

# Appendix A:  Decision making model

While the project is in the early stages, we are favoring a balance of including all voices and keeping a rapid pace of progress.
To accomplish this balance, we are using a _consensus decision model_ that gives time and space for everyone to voice concerns with the proposal.

There are two types of consensus models we use, the lightweight and the full:

- **Lightweight consensus** occurs when a decision does not have wide or sweeping effects and is considered approved if no one raises any blocking objections after several days.
  In practice, a proposal email with sufficient detail is sent to a SIG or main community list, and if no one raises an objection after three working days (i.e., Saturdays and Sundays are not counted), the proposal passes.
- **Full consensus** decisions require 3 yes votes (+1) and no objections (-1’s) and votes should be left open for at least 72 hours (not counting weekend days) to ensure all voices are heard.
  72 hours is a minimum and should be increased for decisions with a likely broad impact, that involve contentious issues, or for any other reason that increases fairness in reaching consensus.
  Specifically, these rules must **not** be used to intentionally or accidentally disenfranchise contributors.
  For example, if a 72 hour window goes over a weekend and means a significant decision closes on a Monday, it may disenfranchise contributors who cannot watch the project daily.
  In such cases, a full calendar week is a fair minimum window for decision making, balancing the needs to give people enough time and to keep the process moving along.
  All -1s votes require reason/ explanation, -1’s with no substantiation may be overturned.
  Thus a single -1 vote can block achieving consensus, so it forces the group to take care of the blocking person rather than outvoting.

SIGs decide by consensus within themselves whatever they are doing, and which model is used for a particular decisions.

Anything needing wider discussion and approval goes to mailing list for either group or SIG roll-up consensus.

When we are ready, we use this power to form a technical and/or overall steering committee, with corresponding election system.

# Appendix B: Consensus decision making defined

One practice of meritocracy is the consensus-based decision model.
From <http://en.wikipedia.org/wiki/Consensus_decision-making>, “Consensus decision-making is a group decision making process that seeks the consent of all participants.”
In practice, it is different from a majority-vote-wins approach.
In the Op1st project a discussion toward a decision follows this process:

1. A proposal is put forth and a check for consensus is made.
   1. Consensus is signified through a +1 vote.
1. A check is made for any dissent on the proposal.
   1. Reservations? State reservation, sometimes with a ‘-1’ signifier
      1. Reservations about the proposal are worked through, seeking consensus to resolve the reservations.
      2. A reservation is not a vote against the proposal, but may turn into a vote against if unresolved.
         It is often expressed with an initial -1 vote to indicate reservations and concerns.
         This indicates there is still discussion to be had.
   1. Stand aside?
      No comment, or state concerns without a -1 reservation; sometimes the ‘-0’ signifier is used.
      1. This option allows a member to have issues with the proposal without choosing to block the proposal, by instead standing aside with a +/-0 vote.
      1. The stated concerns may influence other people to have or release reservations.
   1. Block?
      Vote ‘-1’ with reasons for the block.
   1. This is a complete block on a proposal, refusing to let it pass.
      A block is a -1 vote and must be accompanied with substantive arguments that are rooted in the merit criteria of the Project – protecting the community, the upstream, technical reasons, and so forth.
