# Cloud Resume Site

A static resume website for Chaska Ananiev, built with HTML, CSS, and JavaScript for Azure hosting as part of the Cloud Resume Challenge. It includes a live total visitor counter.

### See the website live [here](https://resume.voyous.dev)

## Website and API tests

The tests in `tests/test_api.py` run against the deployed visitor-counter API and website. They check that:

- A `GET` request to `/api/get_visits` returns HTTP 200 and an integer visitor count.
- A `POST` request to `/api/visits` increments the visitor count by one.
- Reloading the website increments the displayed visitor count by one.

### Set up the test environment

Create and activate a virtual environment, then install the project requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate the environment with `.venv\Scripts\activate` instead.

Install Playwright's browser and system dependencies:

```bash
playwright install
playwright install-deps
```

Run the tests from the project root:

```bash
pytest
```
