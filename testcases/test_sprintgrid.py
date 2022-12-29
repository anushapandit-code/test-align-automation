import pytest
from pages.sprintgrid_page import SprintGridPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestSprintGridApp():
    log = Utils.custom_logger()

# Create an instance of class
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.sp = SprintGridPage(self.driver, self.action)  # sp is an instance of SprintGridPage class
        self.ut = Utils()  # ut is an instance of Utils class

    """2. User can create new task by clicking Plus “+” button and filling the name of new task."""
    @pytest.mark.parametrize("task", [("Task 4"), ("Task 5"), ("Task 6")])
    def test_add_task(self, task):
        # click on add task button +
        self.sp.do_click(self.sp.ADD_TASK_BUTTON)
        # Give Task name in the input field
        self.sp.do_send_keys(self.sp.SEND_TASK_NAME, task)
        # double click on Add button to add the task
        self.sp.do_double_click(self.sp.ADD_OPTION_TASK)
        # click on close task button x
        self.sp.do_click(self.sp.CLOSE_TASK_BUTTON)
        assert self.sp.assert_element(self.sp.IS_TASK_DISPLAYED) == task, "Task has not added"
        self.log.info(task+" row added")

    """3.User can create new Date (column) by clicking Plus “+” button and
     filling the date (using datepicker or keyboard)."""
    def test_add_date(self):
        # click on add date button +
        self.sp.do_click(self.sp.ADD_DATE_BUTTON)
        # //click on calender icon
        self.sp.do_click(self.sp.CALENDER_ICON)
        # //click on dates on the calender
        self.sp.do_click(self.sp.DATE_ON_CALENDER)
        # // click on Add (date Add option)
        self.sp.do_double_click(self.sp.ADD_OPTION_DATE)
        # click on close date button
        self.log.info("Date column added")

    """4.User can assign statuses by clicking to the cell of the table. Then the table expends, 
        and the nearest input is autofocused and is getting active."""
    @pytest.mark.parametrize("status", [("To do"), ("In progress"), ("In Testing"), ("Blocked"), ("Done")])
    def test_status_assignment(self, status):
        # click on the cell of the status
        self.sp.do_click(self.sp.STATUS_CELL)
        # clear the status field
        self.sp.do_clear(self.sp.STATUS_FIELD)
        # enter the status
        self.sp.do_send_keys(self.sp.STATUS_FIELD, status)
        self.log.info(status+" Status assigned")

    """ 7. User can remove rows by hovering over the task name and clicking to remove button (red cross)"""
    def test_remove_rows(self):
        # move to web element and hover over and click
        self.sp.do_move_to_element(self.sp.REMOVE_TASK_ROW)
        self.log.info("Row removed")

    """ 8. User can remove columns by hovering over the date and clicking to remove button (red cross)"""
    def test_remove_columns(self):
        # move to web element and hover over and click
        self.sp.do_move_to_element(self.sp.REMOVE_DATE_COLUMN)
        self.log.info("Column removed")





