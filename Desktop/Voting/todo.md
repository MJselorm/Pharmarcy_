# UniVote — Organisation & Membership Development Roadmap

## Phase 1: Organisation Foundation

**Objective:** Establish organisation creation, ownership, management, profiles and lifecycle.

### 1. Organisation Creation Requests
- [✅] Allow authenticated users to request organisation creation.
- [✅] Collect organisation information.
- [✅] Store requests with pending approval status.
- [✅] Track organisation request status.

### 2. Platform Super Admin Approval and Rejection
- [✅] Platform Super Admin can review organisation creation requests.
- [✅] Approve organisation creation requests.
- [✅] Reject organisation creation requests.
- [ ] Send an in-app notification when a request is approved.
- [ ] Send an in-app notification when a request is rejected.
- [ ] Send an approval email to the requester.
- [ ] Send a rejection email to the requester, including the reason where available.
- [ ] Ensure notifications are triggered only after successful decisions.

### 3. Direct Organisation Creation by Platform Super Admin
- [✅] Platform Super Admin can create organisations directly.
- [✅] Allow the Super Admin to retain initial management.
- [✅] Allow the Super Admin to designate an initial Organisation Owner.

### 4. Organisation Management Assignment and Handover
- [ ] Assign initial Organisation Owners.
- [ ] Transfer organisation ownership.
- [ ] Hand over organisation management to another administrator.
- [ ] Remove previous organisation-level management permissions after handover.
- [ ] Preserve Platform Super Admin oversight and intervention authority.
- [ ] Maintain ownership and handover history.

### 5. Organisation Profiles and Settings
- [ ] Organisation name and description.
- [ ] Organisation logo and branding.
- [ ] Organisation type and classification.
- [ ] Organisation contact information.
- [ ] Organisation-specific settings.
- [ ] Public and private organisation profiles.
- [ ] Membership configuration settings.

### 6. Organisation Status and Lifecycle
- [ ] Define organisation lifecycle statuses: Pending, Active, Suspended, Rejected and Archived.
- [ ] Allow authorised administrators to suspend organisations.
- [ ] Allow authorised administrators to reinstate organisations.
- [ ] Restrict organisation operations based on status.
- [ ] Preserve historical organisation records.
- [ ] Maintain organisation status change history.

---

## Phase 2: Membership Management

**Objective:** Allow users to discover organisations, join them, verify their identity and manage multiple organisation memberships.

### 1. Organisation Discovery Tab
- [✅] Display available organisations.
- [✅] Allow users to discover organisations.
- [✅] Allow users to view organisation information.

### 2. Join Requests
- [✅] Allow users to request to join organisations.
- [✅] Collect required joining information.
- [✅] Track pending join requests.
- [✅] Allow administrators to review requests.
- [✅] Support membership approval and rejection.

### 3. Invitation Links and Email Invitations
- [ ] Allow organisation administrators to generate invitation links.
- [ ] Support invitation expiration dates.
- [ ] Allow administrators to revoke invitations.
- [ ] Send organisation invitation emails.
- [ ] Allow existing UniVote users to accept invitations.
- [ ] Allow new users to register before accepting invitations.
- [ ] Track invitation status: Pending, Accepted, Expired and Revoked.
- [ ] Notify administrators when invitations are accepted.

### 4. Configurable Membership Policies
- [ ] Open membership.
- [ ] Request-to-join with administrator approval.
- [ ] Institutional verification-based membership.
- [ ] Invitation-only membership.
- [ ] Administrator-issued invitations.
- [ ] Allow organisations to configure compatible joining methods.

### 5. Identity and Institutional Verification
- [ ] Collect institutional identifiers such as student ID or staff ID.
- [ ] Verify submitted information against official institutional records.
- [ ] Support administrator-assisted verification.
- [ ] Track verification status.
- [ ] Handle successful, failed and pending verification attempts.
- [ ] Restrict protected organisation access until required verification is completed.

### 6. Membership Attributes Retrieved from Official Records
- [ ] Retrieve student or staff identification details.
- [ ] Retrieve faculty information.
- [ ] Retrieve department information.
- [ ] Retrieve programme information.
- [ ] Retrieve academic level where applicable.
- [ ] Retrieve institutional membership status.
- [ ] Preserve the source and verification status of retrieved attributes.
- [ ] Support updates when official records change.

### 7. Multiple Organisation Memberships
- [ ] Allow one user account to belong to multiple organisations.
- [ ] Maintain separate membership records for each organisation.
- [ ] Allow users to switch between organisations.
- [ ] Maintain separate roles and permissions per organisation.
- [ ] Enforce organisation-specific data isolation.
- [ ] Evaluate election and poll eligibility within the relevant organisation.

### 8. Approval Workflows
- [ ] Support configurable membership approval workflows.
- [ ] Allow designated administrators to review applications.
- [ ] Support automatic approval where configured.
- [ ] Support multiple approval stages where required.
- [ ] Record approval and rejection decisions.
- [ ] Notify users when membership is approved.
- [ ] Notify users when membership is rejected, including reasons where available.

### 9. Membership Lifecycle Management
- [ ] Allow administrators to suspend memberships.
- [ ] Allow administrators to remove members.
- [ ] Allow administrators to reinstate memberships.
- [ ] Allow users to leave organisations.
- [ ] Revoke organisation access when membership is suspended or removed.
- [ ] Preserve membership history.
- [ ] Notify affected users of membership status changes.

---

## Phase 3: Internal Organisational Structure

**Objective:** Allow organisations to define their internal hierarchy, manage organisational units and assign scoped administrative permissions.

### 1. Organisational Units
- [ ] Faculties.
- [ ] Schools.
- [ ] Departments.
- [ ] Clubs.
- [ ] Teams.
- [ ] Academic levels.
- [ ] Other configurable organisational units.

### 2. Organisational Hierarchy
- [ ] Allow organisations to create and manage internal units.
- [ ] Support parent-child relationships.
- [ ] Allow departments to belong to faculties or schools.
- [ ] Allow clubs and teams to exist independently or under parent units.
- [ ] Support configurable hierarchy depth.
- [ ] Preserve historical organisational assignments.

### 3. Scoped Administrative Permissions
- [ ] Organisation Administrator.
- [ ] Faculty Administrator.
- [ ] Department Administrator.
- [ ] Club Administrator.
- [ ] Team Administrator.
- [ ] Configure permissions for each administrative scope.
- [ ] Restrict administrators to their assigned organisational units.
- [ ] Prevent access to unrelated organisational units.
- [ ] Preserve Platform Super Admin platform-wide oversight.

### 4. Unit Membership Assignment
- [ ] Assign members to faculties.
- [ ] Assign members to departments.
- [ ] Assign members to clubs and teams.
- [ ] Support multiple unit memberships where appropriate.
- [ ] Allow authorised administrators to manage unit membership.
- [ ] Synchronise assignments with verified institutional records where available.

---

## Cross-Phase Requirements: Email and Notifications

These requirements support all three phases. They are not a separate development phase.

### Account Email Verification
- [ ] Send verification email during registration.
- [ ] Provide a secure verification link.
- [ ] Support resending verification emails.
- [ ] Handle expired verification links.
- [ ] Track verified and unverified email addresses.
- [ ] Restrict protected features until email verification is complete.

### Organisation Notifications
- [ ] Organisation request approval notification.
- [ ] Organisation request rejection notification.
- [ ] Ownership assignment notification.
- [ ] Management handover notification.
- [ ] Organisation suspension and reinstatement notifications.

### Membership Notifications
- [ ] Join request confirmation.
- [ ] Membership approval notification.
- [ ] Membership rejection notification.
- [ ] Institutional verification result notification.
- [ ] Membership suspension notification.
- [ ] Membership reinstatement notification.
- [ ] Membership removal notification.
- [ ] Membership invitation notification.

### Notification Infrastructure
- [ ] Use a centralised transactional email service.
- [ ] Maintain consistent email templates and branding.
- [ ] Support in-app notifications.
- [ ] Handle email delivery failures.
- [ ] Prevent duplicate notifications.
- [ ] Track notification status where supported.
- [ ] Keep sensitive institutional information out of email content.

**Important distinction:**
- Email verification confirms ownership of an email address.
- Institutional verification confirms a user's identity or institutional status.
- Membership approval grants permission to join an organisation.

These are separate processes.

---
### EXTRA TODOS
1.  PROFILE PICTURE THING

## Implementation Rules

1. Inspect existing functionality before implementing anything.
2. Reuse existing authentication, APIs, database clients and services.
3. Do not introduce duplicate database tables or APIs.
4. Keep universal user accounts separate from organisation memberships.
5. Keep platform-level roles separate from organisation-level roles.
6. Enforce permissions on the backend.
7. Preserve existing functionality.
8. Test features before marking them completed.
9. Update this checklist whenever implementation status changes.
10. Never mark a feature completed merely because its frontend interface exists.

**Status convention:**
- `[x]` Completed and tested.
- `[ ]` Not completed.
- `[~]` Partially implemented or awaiting verification.

Only use `[x]` when the feature has been implemented and its expected behaviour has been tested.