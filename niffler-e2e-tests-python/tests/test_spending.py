from marks import Pages, TestData
from pages.main_page import MainPage


@Pages.main_page
def test_spending_title_exists():
    main_page = MainPage()
    main_page.main_content_should_have_text('History of spendings')


TEST_CATEGORY = "school"


@Pages.main_page
@TestData.category(TEST_CATEGORY)
@TestData.spends({
        "amount": "108.51",
        "description": "QA.GURU Python Advanced 1",
        "category": TEST_CATEGORY,
        "spendDate": "2024-08-08T18:39:27.955Z",
        "currency": "RUB"
    })
def test_spending_should_be_deleted_after_table_action(category, spends):
    main_page = MainPage()

    main_page.table_should_have_text('QA.GURU Python Advanced 1')
    main_page.click_on_select_all_checkbox()
    main_page.click_on_delete_selected_button()
    main_page.spending_content_should_have_text("No spendings provided yet!")

