# Section A1 – Manual Test Suite 

Application: Sauce Demo – https://www.saucedemo.com/

Use Case: Shop and Check Out

Objective: Validate that a registered customer can log in, browse and sort products, manage the shopping cart, complete checkout and place an order successfully.

## 1. Questions for the Product Owner and Assumptions

| No. | Question for Product Owner | Assumption to Be Tested |

| --- | --- | --- |

| 1 | Is the postal code validated against a specific country or format? | The postal code is mandatory. The application should reject an empty value. |

| 2 | How should the application behave when two products have the same price? | Products with equal prices should still appear in a valid sorted order and if possible gives priority based on ratings |

| 3 | Is there a maximum number of products that can be added to the cart? | No maximum limit is assumed for this test unless the application specifies one. |

| 4 | Which browsers and screen sizes are officially supported? | The application should work on commonly used browsers and desktop and mobile-sized screens. |

| 5 | Should users be able to navigate the complete shopping flow using only a keyboard? | All important interactive elements should be keyboard accessible. |

## 2. Manual Test Cases – Refer Harvee_Functional_Test_Cases_A0.xlsx sheet

| ID | Area | Type | Title | Pre-conditions | Steps | Test data | Expected result | Priority | Automate? and why |

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| TC01 | Login | Positive | Standard user logs in successfully | On login page | Enter valid username and password; click Login | standard_user credentials | User should be redirected to the Products page. | P1 | Yes – critical smoke test. |

| TC02 | Login | Negative | Locked-out user cannot log in | On login page | Enter locked-out username and valid password; click Login | locked_out_user credentials | Appropriate locked-out error should be displayed and login should fail. | P1 | Yes – important negative test. |

| TC03 | Login | Negative | Invalid password is rejected | On login page | Enter valid username and incorrect password; click Login | standard_user and wrong password | Error message should be displayed and user should remain on login page. | P1 | Yes – validates authentication. |

| TC04 | Login | Boundary | Login with empty credentials | On login page | Leave both fields empty; click Login | Blank username and password | Required-field validation message should appear. | P1 | Yes – repeatable validation test. |

| TC05 | Products | Positive | Products are displayed after login | Logged in as standard user | Observe the Products page | standard_user | Product names, images, prices and Add to Cart buttons should be displayed. | P1 | Yes – verifies core product listing. |

| TC06 | Products | Positive | Sort products by name A to Z | Logged in as standard user | Select Name (A to Z); verify the complete product list | Name A to Z | All product names should be in ascending alphabetical order. | P1 | Yes – deterministic sorting test. |

| TC07 | Products | Positive | Sort products by name Z to A | Logged in as standard user | Select Name (Z to A); verify the complete product list | Name Z to A | All product names should be in descending alphabetical order. | P2 | Yes – validates reverse sorting. |

| TC08 | Products | Positive | Sort products by price low to high | Logged in as standard user | Select Price (low to high); verify every product price | Price low to high | All product prices should be in ascending order. | P1 | Yes – important business functionality. |

| TC09 | Products | Positive | Sort products by price high to low | Logged in as standard user | Select Price (high to low); verify every product price | Price high to low | All product prices should be in descending order. | P1 | Yes – validates reverse price sorting. |

| TC10 | Cart | Positive | Add one product to cart | Logged in as standard user | Click Add to Cart for one product; observe cart badge | standard user cart products | Cart badge should display 1 and the product button should change to Remove. | P1 | Yes – core cart functionality. |

| TC11 | Cart | Positive | Add two products and remove one | Logged in as standard user | Add two different products; open cart; remove one | standard user cart products | Cart badge and cart contents should show exactly one remaining product. | P1 | Yes – validates cart updates. |

| TC12 | Cart | Positive | Remove product from products page | Logged in and one product added | Click Remove for the added product | standard user cart products | Product should be removed and cart badge should update accordingly. | P1 | Yes – validates removal from listing. |

| TC13 | Cart | Boundary | Verify cart with no products | Logged in as standard user | Open cart without adding any products | Empty cart | Cart should display no products and should not permit placing an order. | P2 | Yes – useful boundary test. |

| TC14 | Cart | Positive | Verify cart details match selected products | At least two products added | Open cart; compare product names, prices and quantities | Backpack and Bike Light | Cart should display the correct selected products and details. | P1 | Yes – validates data consistency. |

| TC15 | Checkout | Positive | Complete checkout with valid information | One or more products in cart | Click Checkout; enter all required fields; click Continue | Manoj / Kumar / 642001 | User should reach the checkout overview page. | P1 | Yes – critical checkout flow. |

| TC16 | Checkout | Negative | Checkout with missing first name | Product available in cart | Open checkout; leave first name blank; enter remaining details; click Continue | Blank / Kumar / 642001 | Validation message should indicate that first name is required. | P1 | Yes – parameterized validation. |

| TC17 | Checkout | Negative | Checkout with missing last name | Product available in cart | Open checkout; enter first name; leave last name blank; enter postal code; click Continue | Manoj / Blank / 642001 | Validation message should indicate that last name is required. | P1 | Yes – parameterized validation. |

| TC18 | Checkout | Negative | Checkout with missing postal code | Product available in cart | Open checkout; enter first and last names; leave postal code blank; click Continue | Manoj / Kumar / Blank | Validation message should indicate that postal code is required. | P1 | Yes – parameterized validation. |

| TC19 | Checkout | Positive | Verify subtotal, tax and total | At least two products in cart | Continue to overview; compare item prices, subtotal, tax and total | standard user cart products | Subtotal should equal item-price sum and total should equal subtotal plus tax. | P1 | Yes – financial calculation validation. |

| TC20 | Checkout | Positive | Finish order successfully | Valid checkout overview displayed | Click Finish | Valid checkout information | Order confirmation should be displayed and cart should be empty after completion. | P1 | Yes – critical end-to-end test. |

| TC21 | Checkout | Negative | Cancel checkout without placing order | Checkout overview displayed | Click Cancel | Existing cart items | User should return to the previous shopping flow without placing an order. | P2 | Yes – validates cancellation flow. |

| TC22 | Security | Negative | Access products page after logout | User is logged in | Log out; directly enter the inventory page URL | /inventory.html | User should not be allowed to access the protected page and should be redirected to login or an appropriate access-denied page. | P1 | Yes – security regression test. |

| TC23 | Usability | Usability | Verify error messages and navigation clarity | On login and checkout pages | Trigger validation errors; inspect messages and navigation controls | Invalid login and blank checkout fields | Error messages should be understandable, visible and associated with the relevant fields. Navigation should be clear. | P2 | No – manual usability assessment. |

| TC24 | Compatibility | Browser / Screen Size | Verify application on different browsers and screen sizes | Application accessible | Open the application in Chrome and Firefox; repeat at desktop and mobile-sized viewports | Desktop 1920x1080 and mobile 375x812 | Layout should remain usable, with no overlapping, hidden or inaccessible important controls. | P2 | Partially – viewport checks can be automated; cross-browser visual checks should include manual review. |

| TC25 | Accessibility | Accessibility | Verify keyboard navigation and accessible controls | On login and products pages | Navigate using Tab and Shift+Tab; activate controls using Enter or Space; inspect focus indicators and labels | Keyboard only | Important controls should be keyboard accessible, focus should be visible and form fields should have meaningful labels. | P2 | Partially – keyboard checks can be automated; accessibility review should include manual validation. |

## 3. Fifteen-Minute Exploratory Testing Charter

Charter Title: Explore shopping and checkout behavior using a user with known performance issues.

Test User: performance_glitch_user

Password: secret_sauce

Duration: 15 minutes

Objective: Identify performance delays, inconsistent UI behavior and unexpected failures while completing the shopping and checkout journey.

Exploratory Activities:

| Time | Activity | What to Observe |

| --- | --- | --- |

| 0–3 minutes | Log in to the application | Login response time, loading delays and error messages. |

| 3–6 minutes | Browse the Products page | Product loading, images, prices and responsiveness. |

| 6–9 minutes | Try all sorting options | Sorting accuracy, delays and UI consistency. |

| 9–12 minutes | Add and remove products | Cart badge updates, product removal and cart consistency. |

| 12–15 minutes | Complete checkout | Form responsiveness, calculation accuracy, confirmation and unexpected errors. |

Expected Evidence:

Screenshots of unexpected behavior.

Steps to reproduce identified issues.

Approximate response times for slow operations.

Actual versus expected behavior.

Browser console errors, where applicable.

Known Problem Consideration: The performance_glitch_user is intended to expose performance-related behavior. Slow responses should be recorded separately from functional failures. Do not automatically classify every delay as a defect without checking the expected behavior.

## 4. Test Strategy

I would automate critical and repeatable UI scenarios such as login, locked-out login, product sorting, cart operations, checkout validation, price calculations and order completion using Python, Playwright and Pytest. These tests would run as part of regression testing on every build.

If API access is available, I would validate authentication, product data, cart operations, checkout calculations and order creation at the API layer. Unit tests should cover tax calculations, sorting logic and input validation.

Manual testing would focus on usability, accessibility, cross-browser and responsive behavior, exploratory testing and visual consistency.

The biggest remaining risk is inconsistent checkout behavior under real-world conditions, especially performance-related delays and incorrect order or payment processing. I would recommend investigating these risks before release.
