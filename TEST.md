## 🧪 Manual Testing

### 📑 Table of Contents

- [✅ Testing Overview](#-testing-overview)
- [🐞 Bugs](#-bugs)
- [✅ Validation](#-validation)
- [📋 Manual Testing by User Story](#-manual-testing-by-user-story)
- [🧪 Additional Testing](#-additional-testing)

### ✅ Testing Overview

This project included a wide range of features, views, and serializer logic, so manual testing was essential at every stage. Testing was done using the Django admin panel and the DRF browsable API. All endpoints were checked to confirm:

- Correct status codes (200, 201, 204, 401, 403, 404)
- Permissions enforced properly
- Serializer fields returning expected values
- Ownership logic working as intended

### 🐞 Bugs

- **🐞 Bug:** Tutorial Feedback not saving correctly

  - **🛠️ Cause:** Incorrect permissions logic for the feedback view
  - **✅ Resolution:** Updated view to ensure only authenticated mentors could create feedback and ensured `is_owner` serializer checks were in place.

- **🐞 Bug:** Artwork comment counts not updating on list view

  - **🛠️ Cause:** Annotated count missing from queryset
  - **✅ Resolution:** Added `annotate()` to view and confirmed accuracy via the browsable API.

- **🐞 Bug:** Follow filtering in `/artworks/` not returning expected data

  - **🛠️ Cause:** Incorrect filterset field name
  - **✅ Resolution:** Updated filterset class to use `owner__followed__owner__profile` and tested via querystring

- **🐞 Bug:** Profiles page returned a 500 error on Heroku after deployment
  - **🛠️ Cause:** `profile_image` was missing from the `ProfileSerializer` field list
  - **✅ Resolution:** Added `profile_image` to the serializer’s `fields` and redeployed — confirmed fixed

✅ All known bugs were resolved during development.

[Back to top ⬆️](#-testing)

---

### ✅ Validation

#### 🐍 Python Code

- Code was validated using the [Code Institute Python Linter](https://pep8ci.herokuapp.com/).
- Most warnings were related to line length; these were reviewed individually.
- Long lines involving queryset logic or serializer fields were left intact to preserve readability and DRY structure.

[Back to top ⬆️](#-testing)

---

### 📋 Manual Testing by User Story

#### 📖 As a **Registered User**, I can:

> **Create:**

- Create a user profile (via registration + `/profiles/` endpoint)
- Upload artworks with and without images
- Create tutorials with cover images
- Add tutorial steps
- Submit a tutorial attempt
- Comment on artworks and tutorials
- Like and favourite artworks and tutorials
- Follow other users

> **Read:**

- View list/detail views of artworks, tutorials, attempts, feedback, and profiles
- See step-by-step tutorials
- View my submitted tutorial attempts and any mentor feedback

> **Update:**

- Edit my profile bio and image
- Edit my own artworks, tutorials, tutorial steps, and tutorial attempts
- Edit my comments on artworks and tutorials

> **Delete:**

- Delete my artworks, tutorials, tutorial steps, comments, likes, favourites, tutorial attempts, and follows

**Result** 🏆: Instances were created successfully
**Verdict** ✅: Test passed.

[Back to top ⬆️](#-testing)

---

#### 📖 As a **Mentor**, I can:

- Create and edit tutorials
- Add tutorial steps
- View tutorial attempts submitted by users
- Submit one feedback item per tutorial attempt
- Edit or delete that feedback if I am the owner

**Result** 🏆: Instances were created successfully
**Verdict** ✅: Test passed.

---

#### 📖 As an **Unregistered User**, I can:

- View public content only
- Access all list and detail views for artworks, tutorials, and profiles
- Receive `401 Unauthorized` or `403 Forbidden` when trying to POST/PUT/DELETE

**Result** 🏆: Instances were created successfully
**Verdict** ✅: Test passed.

[Back to top ⬆️](#-testing)

---

### 🧪 Additional Testing

| Aim                          | Test                                                | Result                                  | Verdict   |
| ---------------------------- | --------------------------------------------------- | --------------------------------------- | --------- |
| Test API routes              | Navigated to each endpoint manually                 | All routes rendered correctly           | ✅ Passed |
| Profile serializer fields    | Checked `is_owner`, `followers_count`, etc.         | Fields populated correctly              | ✅ Passed |
| Artworks filtering           | Tested querystrings for followed users, liked posts | Filtered results returned               | ✅ Passed |
| Tutorials search & ordering  | Searched by title, ordered by like count            | Data returned in expected order         | ✅ Passed |
| Pagination                   | Confirmed page size, next/prev logic                | Results limited and paginated correctly | ✅ Passed |
| Permissions                  | Tested unauthorized users attempting write requests | 401/403 responses shown as expected     | ✅ Passed |
| Tutorial feedback constraint | Verified one feedback per tutorial attempt          | Duplicate feedback blocked              | ✅ Passed |
| Tutorial attempts            | Submitted, edited, deleted attempts                 | All actions worked correctly            | ✅ Passed |
| Image uploads (Cloudinary)   | Uploaded via DRF browsable API and admin            | Images saved and rendered properly      | ✅ Passed |
| `is_owner` logic             | Verified serializers return correct owner context   | Conditional buttons working on frontend | ✅ Passed |

---

This testing log demonstrates that all critical functionality, permissions, and edge cases were accounted for and verified before deployment.

🔙 [Back To README](./README.md) **|** [Back to top ⬆️](#-testing)
