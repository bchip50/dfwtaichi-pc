URL Patterns for DFW TaiChi site
==========================================================
https://www.dfwtaichi.com/ - Base
https://dfwtaichi.com/ redirects to https://www.dfwtaichi.com/
http://www.dfwtaichi.com/ - redirects to https://www.dfwtaichi.com/
http://dfwtaichi.com/ - redirects to https://www.dfwtaichi.com/

" " - home page with introduction and menu that allows login
or selection of a style to view.
Login is not required for this page,
but is required for any detail pages.

style application URL's
------------------------------
**"style/<slug:style>/"** - detail landing page for one style.
if the user has a selected preferred style,
then this is the landing page.
Contains a list of series associated with this style.

Additional menu lists:

- Resources: List of resources for this style
- Leaders: List of Instructors or club leaders for this style

**"style/<slug:style>/series/<slug:series>/"** detail landing page
for one series. Contains a list of locations for this series.

Additional menu lists:

- Meetings: List of upcoming meetings.
- Membership: List of series members.
