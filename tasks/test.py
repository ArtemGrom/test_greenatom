from bs4 import BeautifulSoup as BS

from tasks.task_3 import count_all_tag, count_tag_with_attrs
from tasks.task_5 import compare_versions


def test_task_3():
    test_html = (
        """
        <html>
            <head>
                <link rel="stylesheet" type="text/css" href="style.css"/>
            </head>
            <body>
                <nav class='navbar navbar-dark bg-dark'>
                    <div class='ms-auto'></div>
                </nav>
                <div class="my class"></div>
            </body>
        </html>
        """
    )
    test_html = BS(test_html, 'html.parser')
    test_html = test_html.find('html')

    assert count_all_tag(test_html) == 6
    assert count_tag_with_attrs(test_html) == 4


def test_task_5():
    assert compare_versions('0.0001.0002', '0.0001.02') == -1
    assert compare_versions('1.1.', '1.10') == -1
    assert compare_versions('1.2.3', '1.2.3') == 0
    assert compare_versions('2.3.7', '2.3.5') == 1
    assert compare_versions('5.6.4.', '5.6.4.5') == -1
    assert compare_versions('5.6.4', '5.6') == 1
    assert compare_versions('5.6.0', '5.6') == 0
    assert compare_versions('5.6', '5.6.0') == 0
    assert compare_versions('0.0.1', '1.0') == -1
    assert compare_versions('7.3.5', '8.0.10') == -1
    assert compare_versions('8.0.10', '7.3.5') == 1
    assert compare_versions('0.26784.1', '0.238.2') == 1
    assert compare_versions('0.1', '0.01') == 1
    assert compare_versions('1.1', '1.01') == 1
    assert compare_versions('5.5.1.006', '5.5.1.006') == 0
    assert compare_versions('0.03', '0.0003.2') == 1
    assert compare_versions('03', '3') == 0
    assert compare_versions('03.007', '3.007') == 0
    assert compare_versions('03.007', '3.007000') == -1
    assert compare_versions('22', '4') == 1