{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "<center><font size=\"6\"><b>Комп'ютерний практикум 6.\n",
        "\n",
        "<center><b> Створення дашборду за допомогою Streamlit </font>\n"
      ],
      "metadata": {
        "id": "GzG85jXXkg_S"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "<center><img src=\"https://www.dataquest.io/wp-content/uploads/2024/02/Why-Should-You-Learn-Streamlit-in-2024.png.webp\" width=\"600\"></center>\n",
        "\n"
      ],
      "metadata": {
        "id": "nkSp72R80cGt"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# __Streamlit__\n",
        "__Streamlit__ - це безкоштовна і відкрита бібліотека Python для створення і розповсюдження веб-додатків для машинного навчання та аналізу даних. Streamlit дає  змогу перетворити свої скрипти з даними на інтерактивні веб-додатки за кілька хвилин.\n",
        "\n",
        "### Можливості Streamlit:\n",
        "\n",
        "*   Створити привабливий і функціональний інтерфейс для алгоритмів, моделей, візуалізацій, дашбордів та інших продуктів з даними.\n",
        "*   Робити експерименти та ітерації з даними і кодом, використовуючи  простий API, який автоматично оновлює ваш застосунок під час збереження вихідного файлу.\n",
        "*   Додавати взаємодію з вашими даними і додатком, використовуючи різні віджети, такі як слайдери, кнопки, чекбокси, радіокнопки, випадаючі списки та інші.\n",
        "* Ділитися своїми додатками з колегами, клієнтами, спільнотою або всім світом, використовуючи  платформу Community Cloud або свій власний сервер.\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "Bg_hTWNExzvt"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Завантажимо Streamlit (не додавати в .py файл додатку)\n",
        "!pip install streamlit"
      ],
      "metadata": {
        "id": "S6rL2H1vAgNf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Python-бібліотеки**, які можуть використовуються у створеному Streamlit-додатку:\n",
        "\n",
        "| Бібліотека            | Призначення                                                                 |\n",
        "|-----------------------|------------------------------------------------------------------------------|\n",
        "| **`streamlit`**       | Основна бібліотека для створення **інтерактивного вебдодатку**. Створює інтерфейс, фільтри, графіки, карту. |\n",
        "| **`pandas`**          |  Робота з табличними даними (DataFrame) — читання, фільтрація, обчислення нових змінних. |\n",
        "| **`matplotlib.pyplot`** |  Побудова класичних графіків (гістограми, scatter, лінійні графіки, heatmap). |\n",
        "| **`seaborn`**         |  Стилізовані графіки на основі matplotlib — barplot, boxplot, heatmap з анотаціями. |\n",
        "|**`altair`**|Декларативна система побудови інтерактивних графіків, яка працює особливо добре в Streamlit. Підходить для побудови інтерактивних діаграм, фільтрації та дослідження взаємозв’язків у даних|\n",
        "| **`numpy`**           |  Математичні операції, генерація випадкових чисел для симуляцій (Монте-Карло). |\n",
        "| **`plotly.express`**  |  Інтерактивні графіки: scatter з підказками, інтерактивні осі, кольори, розміри. |\n",
        "| **`sklearn.linear_model`** | Лінійна регресія — побудова моделі для оцінки залежності ROI від AdBudget. |\n",
        "| **`sklearn.cluster`** |  Кластеризація (алгоритм KMeans) для групування компаній за економічними показниками. |\n",
        "\n"
      ],
      "metadata": {
        "id": "hwSuTm52_5hY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import altair as alt\n",
        "import numpy as np\n",
        "import plotly.express as px\n",
        "from sklearn.linear_model import LinearRegression\n",
        "from sklearn.cluster import KMeans"
      ],
      "metadata": {
        "id": "w7Ntq5ZW3DAp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "__Завантажимо дані__\n",
        "\n",
        "Маємо датасет **`streamlit_dataset.xlsx`**:\n",
        "\n",
        "| Назва змінної        | Тип             | Опис |\n",
        "|----------------------|------------------|------|\n",
        "| **Company**          | `str`            | Назва компанії (`Company_1`, `Company_2`, ...). Унікальний ідентифікатор суб’єкта аналізу. |\n",
        "| **Year**             | `int`            | Рік, за який наведені фінансові показники (2022, 2023, 2024). |\n",
        "| **Region**           | `str`            | Географічний регіон діяльності компанії: `North`, `South`, `East`, `West`. |\n",
        "| **Industry**         | `str`            | Галузь економіки: `Finance`, `Tech`, `Retail`, `Manufacturing`. |\n",
        "| **Revenue**          | `int`            | Загальний дохід компанії за відповідний рік. |\n",
        "| **Expenses**         | `int`            | Загальні витрати компанії за відповідний рік. |\n",
        "| **Investment**       | `int`            | Обсяг інвестицій у розвиток або рекламу. |\n",
        "| **Customers**        | `int`            | Кількість клієнтів, яких обслуговувала компанія. |\n",
        "| **ConversionRate**   | `float`          | Частка клієнтів, які здійснили цільову дію (наприклад, купівлю). Є пропущені значення. |\n",
        "| **Profit**           | `int`            | Прибуток компанії = Revenue − Expenses. |\n",
        "| **ROI**              | `float`          | Рентабельність інвестицій = Profit / Investment. |\n",
        "| **RevenuePerCustomer** | `float`        | Дохід на одного клієнта = Revenue / Customers. |\n",
        "| **Latitude**         | `float`          | Географічна широта для відображення компанії на мапі. |\n",
        "| **Longitude**        | `float`          | Географічна довгота для мапи. |\n",
        "| **Scenario**         | `str`            | Бізнес-сценарій, в рамках якого оцінюються показники: `Baseline`, `Optimistic`, `Pessimistic`. |\n",
        "| **MarketGrowth**     | `float`          | Темп зростання ринку (в %) — умовна макроекономічна змінна для моделювання. |\n",
        "| **AdBudget**         | `float`          | Бюджет на рекламу або маркетинг. Використовується для аналізу ефективності. |\n",
        "\n",
        "\n",
        "\n",
        "___Застосування змінних:___\n",
        "\n",
        "- **Кількісні змінні** (`Revenue`, `Expenses`, `Profit`, `ROI`, `Customers`, `AdBudget`) — підходять для графіків, регресій, кластеризацій.\n",
        "- **Категоріальні змінні** (`Region`, `Industry`, `Scenario`) — для групування, фільтрації, аналізу розподілів.\n",
        "- **Просторові змінні** (`Latitude`, `Longitude`) — для інтерактивної карти.\n",
        "- **ConversionRate** — підходить для демонстрації роботи з пропущеними даними.\n"
      ],
      "metadata": {
        "id": "Br-KK_Sw6pYm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv('streamlit_dataset.csv')"
      ],
      "metadata": {
        "id": "jMCCFys3x6K-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## __Розвідувальний аналіз даних (EDA)__\n",
        "Для якісної роботи з даними та їх представленням, використанням для моделювання, їх необхідно попередньо опрацювати. Тому етап препроцесінгу та розвідувального аналізу є ключовим в підготовці даних."
      ],
      "metadata": {
        "id": "E1HNr8pEBLpI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "id": "gAD0FTB13udb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.describe()"
      ],
      "metadata": {
        "id": "WGwtma2B460L"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "missing_data = df.isnull()\n",
        "for column in missing_data.columns.values.tolist():\n",
        "    print(column)\n",
        "    print (missing_data[column].value_counts())\n",
        "    print(\"\")"
      ],
      "metadata": {
        "id": "I2RIfHwU5EYh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## __Конфігурація сторінки__\n",
        "\n",
        "\n",
        "Визначимо налаштування програми, надавши їй заголовок сторінки та значок, які відображаються в браузері. Це також визначає вміст сторінки, який буде відображатися в широкому макеті, який вписується в ширину сторінки, а також відображає бічну панель у розгорнутому стані.\n",
        "\n",
        "`st.set_page_config(...)` у Streamlit — задає загальні параметри зовнішнього вигляду сторінки Streamlit-додатку. Її потрібно викликати одразу після імпорту `streamlit`, до будь-якого іншого коду Streamlit.\n",
        "\n",
        "___Синтаксис:___\n",
        "\n",
        "```python\n",
        "st.set_page_config(\n",
        "    page_title=None,\n",
        "    page_icon=None,\n",
        "    layout=\"centered\",\n",
        "    initial_sidebar_state=\"auto\",\n",
        "    menu_items=None\n",
        ")\n",
        "```\n",
        "\n",
        "| Параметр                | Тип      | Опис |\n",
        "|-------------------------|----------|------|\n",
        "| `page_title`            | `str`    | Назва сторінки (відображається у вкладці браузера) |\n",
        "| `page_icon`             | `str` або `Image` | Емодзі або шлях до файлу з іконкою (favicon) |\n",
        "| `layout`                | `str`    | `'centered'` (стандарт) або `'wide'` (повна ширина) |\n",
        "| `initial_sidebar_state` | `str`    | `'auto'`, `'expanded'`, `'collapsed'` — як відкривається бокове меню |\n",
        "| `menu_items`            | `dict`   | Налаштування меню у правому верхньому куті: `{ 'Get Help', 'Report a bug', 'About' }` |\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "liQNKZPD9OkD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "st.set_page_config(\n",
        "    page_title=\"Економічний дашборд\",\n",
        "    page_icon=\"📊\",\n",
        "    layout=\"wide\",\n",
        "    initial_sidebar_state=\"expanded\",\n",
        "    menu_items={\n",
        "        'Get Help': 'https://docs.streamlit.io/',\n",
        "        'Report a bug': 'https://github.com/streamlit/streamlit/issues',\n",
        "        'About': 'Інтерактивна панель для економічного аналізу підприємств'\n",
        "    }\n",
        ")"
      ],
      "metadata": {
        "id": "bq3kYYSJFRqA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## __Бічна панель (**`st.sidebar`**)__\n",
        "\n",
        "у Streamlit — це окрема область інтерфейсу, яка розташовується ліворуч і використовується для фільтрів, параметрів, налаштувань, навігації.\n",
        "\n",
        "Вона дозволяє розділити логіку:\n",
        "- зліва — керування\n",
        "- справа — результати, графіки, аналітика\n",
        "\n",
        "\n",
        "| Компонент   `sidebar`            | Опис                                              |\n",
        "|-------------------------|---------------------------------------------------|\n",
        "| `st.sidebar.title()`    | Заголовок                                         |\n",
        "| `st.sidebar.markdown()` | Текстовий опис / інструкції                       |\n",
        "| `st.sidebar.selectbox()`| Один вибір зі списку                              |\n",
        "| `st.sidebar.multiselect()`| Кілька виборів                                   |\n",
        "| `st.sidebar.slider()`   | Слайдер для чисел або дат                         |\n",
        "| `st.sidebar.radio()`    | Вибір одного варіанту з декількох (радіо-кнопки)  |\n",
        "| `st.sidebar.checkbox()` | Прапорець                                |\n",
        "| `st.sidebar.file_uploader()` | Завантаження CSV, Excel, зображень             |\n",
        "| `st.sidebar.button()`   | Кнопка, яка реагує на клік                        |\n",
        "| `st.sidebar.info()` / `warning()` | Інформаційні повідомлення         |\n",
        "\n"
      ],
      "metadata": {
        "id": "5cgjLc2Wey0b"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## __Створимо наступну бічну панель (`st.sidebar`):__\n",
        "\n",
        "```python\n",
        "st.sidebar.title(\"Панель фільтрації\")\n",
        "```\n",
        "> Створює заголовок в лівій боковій панелі\n",
        "\n",
        "***Фільтри:***\n",
        "\n",
        "```python\n",
        "st.sidebar.selectbox(\"Рік\", sorted(df[\"Year\"].unique()))\n",
        "```\n",
        "> Випадаючий список із доступних років  \n",
        "Користувач обирає один рік для фільтрації.\n",
        "\n",
        "\n",
        "```python\n",
        "st.sidebar.multiselect(\"Регіон\", df[\"Region\"].unique(), default=df[\"Region\"].unique())\n",
        "```\n",
        "> Список із можливістю вибору декількох регіонів. По замовчуванню обрані всі регіони.\n",
        "\n",
        "\n",
        "```python\n",
        "st.sidebar.multiselect(\"Галузь\", df[\"Industry\"].unique(), default=df[\"Industry\"].unique())\n",
        "```\n",
        "> Вибір однієї або кількох галузей. По замовчуванню обрані всі галузі.\n",
        "\n",
        "\n",
        "```python\n",
        "st.sidebar.radio(\"Сценарій\", df[\"Scenario\"].unique())\n",
        "```\n",
        "> Вибір одного варіанту зі сценаріїв розвитку подій (наприклад: Optimistic, Baseline, Pessimistic)\n",
        "\n",
        "\n",
        "```python\n",
        "st.sidebar.slider(\n",
        "    \"Максимальний рекламний бюджет\",\n",
        "    min_value=int(df[\"AdBudget\"].min()),\n",
        "    max_value=int(df[\"AdBudget\"].max()),\n",
        "    value=int(df[\"AdBudget\"].max()),\n",
        "    step=1000\n",
        ")\n",
        "```\n",
        "> Слайдер, який дозволяє обмежити максимальний рекламний бюджет\n",
        "\n",
        "\n",
        "***Чекбокс***\n",
        "\n",
        "```python\n",
        "show_map = st.sidebar.checkbox(\"🗺 Показати мапу компаній\")\n",
        "```\n",
        "> Дозволяє увімкнути або вимкнути мапу на головній панелі.\n",
        "\n",
        "\n",
        "\n",
        "***Перемикач типу графіка***\n",
        "\n",
        "```python\n",
        "chart_option = st.sidebar.radio(\n",
        "    \"Оберіть графік для перегляду:\",\n",
        "    [...]\n",
        ")\n",
        "```\n",
        "\n",
        "Користувач може обрати один із шести графіків:\n",
        "\n",
        "| Варіант                                      | Що показує                                  |\n",
        "|----------------------------------------------|----------------------------------------------|\n",
        "| `Доходи на клієнта vs Витрати`               | Scatter-графік між `Expenses` і `RevenuePerCustomer` |\n",
        "| `Boxplot прибутку по галузях`                | Розподіл прибутку в різних галузях           |\n",
        "| `Scatter: Прибуток vs Інвестиції`            | Залежність прибутку від інвестицій           |\n",
        "| `Гістограма конверсії по галузях`            | Середній рівень `ConversionRate` у галузях   |\n",
        "|`Теплова карта кореляцій`|Візуалізує кореляції між числовими змінними у відфільтрованій таблиці|\n",
        "|`Кластеризація компаній (KMeans)`|Кластеризація за `ROI` та `Investment`|\n",
        "\n",
        "\n",
        "\n",
        "***Інформаційний блок***\n",
        "\n",
        "```python\n",
        "st.sidebar.markdown(\" **Інструкція**: ...\")\n",
        "```\n",
        "> Виводить просту текстову інструкцію, яка допомагає користувачу зрозуміти, як користуватись фільтрами і навігацією. Використовується мова розмітки markdown\n",
        "\n",
        "---\n",
        "\n",
        "\n",
        "Ця бокова панель забезпечує:\n",
        "\n",
        "|  Компонент         | Призначення                        |\n",
        "|----------------------|-------------------------------------|\n",
        "|  Selectbox         | Обрати 1 рік                       |\n",
        "|  Multiselect        | Обрати кілька регіонів/галузей     |\n",
        "|  Radio             | Обрати сценарій і тип графіка      |\n",
        "|  Слайдер           | Обмежити за рекламним бюджетом     |\n",
        "|  Checkbox          | Показати/приховати карту           |\n",
        "|  Markdown          | Надати інструкцію користувачу      |\n"
      ],
      "metadata": {
        "id": "_wviotgMolHt"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Бічна панель / SIDEBAR\n",
        "st.sidebar.title(\"Панель фільтрації\")\n",
        "\n",
        "# Фільтри\n",
        "selected_year = st.sidebar.selectbox(\"Рік\", sorted(df[\"Year\"].unique()))\n",
        "selected_region = st.sidebar.multiselect(\"Регіон\", df[\"Region\"].unique(), default=df[\"Region\"].unique())\n",
        "selected_industry = st.sidebar.multiselect(\"Галузь\", df[\"Industry\"].unique(), default=df[\"Industry\"].unique())\n",
        "selected_scenario = st.sidebar.radio(\"Сценарій\", df[\"Scenario\"].unique())\n",
        "\n",
        "selected_max_adbudget = st.sidebar.slider(\n",
        "    \"Максимальний рекламний бюджет\",\n",
        "    min_value=int(df[\"AdBudget\"].min()),\n",
        "    max_value=int(df[\"AdBudget\"].max()),\n",
        "    value=int(df[\"AdBudget\"].max()),\n",
        "    step=1000\n",
        ")\n",
        "\n",
        "# Чекбокси для відображення\n",
        "show_map = st.sidebar.checkbox(\"🗺 Показати карту компаній\")\n",
        "\n",
        "# Перемикач графіків\n",
        "chart_option = st.sidebar.radio(\n",
        "    \"📈 Оберіть графік для перегляду:\",\n",
        "    [\n",
        "        \"Доходи на клієнта vs Витрати\",\n",
        "        \"Boxplot прибутку по галузях\",\n",
        "        \"Scatter: Прибуток vs Інвестиції\",\n",
        "        \"Гістограма конверсії по галузях\",\n",
        "        \"Теплова карта кореляцій\",\n",
        "        \"Кластеризація компаній (KMeans)\"\n",
        "    ]\n",
        ")\n",
        "\n",
        "# Інформаційний блок\n",
        "st.sidebar.markdown(\"---\")\n",
        "st.sidebar.markdown(\" **Інструкція**: \\nФільтруйте дані за параметрами і переглядайте графіки та таблиці на панелі праворуч.\")\n",
        "st.sidebar.markdown(\" **Автор**: Lazar_Iryna\")"
      ],
      "metadata": {
        "id": "0-MXdvZxGzP4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## __Фільтрація__\n",
        "\n",
        "\n",
        "Цей блок фільтрує основний DataFrame `df` відповідно до вибору користувача в бічній панелі (`sidebar`). Результат зберігається у змінну `df_filtered`, яка використовується далі для побудови таблиці, графіків, завантаження CSV тощо.\n",
        "\n",
        " `df[...]`  \n",
        "Це підмножина початкового датафрейму — тут передається логічна маска, що вибирає лише ті рядки, які відповідають критеріям.\n",
        "\n",
        "`(df[\"Year\"] == selected_year)`  \n",
        "Фільтрує лише ті записи, у яких значення в колонці `Year` дорівнює вибраному року.\n",
        "\n",
        "`(df[\"Region\"].isin(selected_region))`  \n",
        "Залишає лише ті рядки, де `Region` міститься у списку вибраних регіонів.  \n",
        "Функція `.isin()` перевіряє, чи є значення у списку.\n",
        "\n",
        "`(df[\"Industry\"].isin(selected_industry))`  \n",
        "Залишає лише ті записи, де `Industry` відповідає вибраним галузям.\n",
        "\n",
        "`(df[\"Scenario\"] == selected_scenario)`  \n",
        "Фільтрує за вибраним сценарієм.\n",
        "\n",
        "`(df[\"AdBudget\"] <= selected_max_adbudget)`  \n",
        "Обмежує вибір рядків лише тими, де рекламний бюджет не перевищує вказане максимальне значення зі слайдера.\n"
      ],
      "metadata": {
        "id": "IoLsxIdlqbE_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Фільтрація\n",
        "\n",
        "df_filtered = df[\n",
        "    (df[\"Year\"] == selected_year) &\n",
        "    (df[\"Region\"].isin(selected_region)) &\n",
        "    (df[\"Industry\"].isin(selected_industry)) &\n",
        "    (df[\"Scenario\"] == selected_scenario) &\n",
        "    (df[\"AdBudget\"] <= selected_max_adbudget)\n",
        "]\n"
      ],
      "metadata": {
        "id": "DiK8iJwmqart"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## __Побудова моделі лінійної регресії__\n",
        "\n",
        "\n",
        "***Блок регресії в бічній панелі***\n",
        "\n",
        "`numeric_columns`: отримує список усіх числових стовпців з відфільтрованого DataFrame `df_filtered`, тому цей блок треба писати після створення відфільтрованого `df_filtered`.\n",
        "\n",
        "`reg_x` та `reg_y`: дозволяють користувачу вибрати незалежну (X) та залежну (Y) змінні для побудови регресії.\n",
        "\n",
        "`show_regression`: чекбокс, який визначає, чи слід відображати регресійну модель.\n",
        "\n"
      ],
      "metadata": {
        "id": "d5BlygixBZaJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Блок регресії\n",
        "st.sidebar.markdown(\"Побудова регресії\")\n",
        "numeric_columns = df_filtered.select_dtypes(include=np.number).columns.tolist()\n",
        "\n",
        "reg_x = st.sidebar.selectbox(\"Оберіть змінну X\", numeric_columns, index=0)\n",
        "reg_y = st.sidebar.selectbox(\"Оберіть змінну Y\", numeric_columns, index=1)\n",
        "show_regression = st.sidebar.checkbox(\"Показати регресійну модель\")"
      ],
      "metadata": {
        "id": "3tKY-O6dKATm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## __Основна панель Streamlit-додатку__\n",
        "\n",
        "Основна панель Streamlit-додатку формує фінальний вигляд і поведінку сторінки після фільтрації\n",
        "\n",
        "\n",
        "***Заголовок і кількість компаній***\n",
        "\n",
        "```python\n",
        "st.title(\"📊 Економічний дашборд компаній\")\n",
        "st.subheader(f\"🔍 Відфільтровано {df_filtered.shape[0]} компаній\")\n",
        "```\n",
        "\n",
        "`st.title(...)` — основний заголовок сторінки.\n",
        "\n",
        "`st.subheader(...)` — повідомляє користувачу, скільки компаній залишилось після застосування фільтрів.\n",
        "\n",
        "`df_filtered.shape[0]` — кількість рядків (компаній) у відфільтрованому DataFrame.\n",
        "\n",
        "\n",
        "___Кнопка завантаження CSV___\n",
        "\n",
        "```python\n",
        "csv = df_filtered.to_csv(index=False).encode(\"utf-8\")\n",
        "st.download_button(\n",
        "    label=\"⬇️ Завантажити CSV\",\n",
        "    data=csv,\n",
        "    file_name=\"filtered_companies.csv\",\n",
        "    mime=\"text/csv\"\n",
        ")\n",
        "```\n",
        "\n",
        "> Конвертує таблицю в CSV і кодує її для завантаження.\n",
        "\n",
        "`st.download_button(...)` — додає інтерактивну кнопку, щоб користувач міг завантажити дані.\n",
        "\n",
        "___Таблиця результатів___\n",
        "\n",
        "\n",
        "> Виводить повну таблицю результатів у вигляді інтерактивної таблиці з прокруткою, сортуванням тощо.\n",
        "\n",
        "**`all_columns`**: отримує список усіх стовпців у відфільтрованому DataFrame `df_filtered`.\n",
        "\n",
        "**`default_columns`**: визначає список стовпців, які будуть вибрані за замовчуванням, якщо вони присутні в `df_filtered`.\n",
        "\n",
        "**`st.multiselect`**: створює віджет для вибору кількох стовпців, дозволяючи користувачам обрати, які стовпці відображати.\n",
        "\n",
        "**`st.dataframe`**: відображає таблицю з обраними стовпцями.\n",
        "\n",
        "**`st.info`**: виводить повідомлення, якщо не вибрано жодного стовпця.\n",
        "\n",
        "\n",
        "___🗺 Карта компаній___\n",
        "\n",
        "```python\n",
        "if show_map:\n",
        "    st.subheader(\"🗺 Географія компаній\")\n",
        "\n",
        "    map_data = df_filtered[[\"Latitude\", \"Longitude\"]].dropna().rename(\n",
        "        columns={\"Latitude\": \"latitude\", \"Longitude\": \"longitude\"}\n",
        "    )\n",
        "\n",
        "    if not map_data.empty:\n",
        "        st.map(map_data)\n",
        "    else:\n",
        "        st.warning(\"Немає доступних координат для побудови карти.\")\n",
        "```\n",
        "\n",
        "`show_map` — логічна змінна (встановлюється через чекбокс у sidebar).\n",
        "\n",
        "`dropna()` — виключає компанії без координат.\n",
        "\n",
        "`rename(...)` — перетворює назви колонок у формат, який вимагає `st.map()` (все маленькими).\n",
        "\n",
        "`st.map(...)` — будує інтерактивну карту.\n",
        "\n",
        "___Графіки за вибором користувача___\n",
        "\n",
        "> Залежно від `chart_option`, виводиться певний графік (визначається через `radio` у sidebar):\n",
        "\n",
        "1. __Доходи на клієнта vs Витрати (Altair)__\n",
        "\n",
        "> компанія, вісь X: `Expenses`, Y: `RevenuePerCustomer`.\n",
        "\n",
        "2. __Boxplot прибутку по галузях (Seaborn)__\n",
        "\n",
        "> Дозволяє виявити галузі з високою/низькою волатильністю.\n",
        "\n",
        "3. __Scatter-графік: Прибуток vs Інвестиції (Altair)__\n",
        "\n",
        "> Візуалізує залежність між розміром інвестицій та прибутком.\n",
        "\n",
        "4. __Гістограма конверсії по галузях (Seaborn)__\n",
        "\n",
        "> Стовпчиковий графік із середнім `ConversionRate` для кожної галузі.\n",
        "\n",
        "5. __Теплова карта кореляцій (Seaborn Heatmap)__\n",
        "\n",
        "```python\n",
        "numeric_cols = df_filtered.select_dtypes(include=[np.number])\n",
        "corr = numeric_cols.corr()\n",
        "```\n",
        "\n",
        "> Обчислює кореляцію між усіма числовими змінними. Показує, які показники мають сильну/слабку кореляцію.\n",
        "\n",
        "6. __Кластеризація компаній (KMeans)__\n",
        "\n",
        "```python\n",
        "cluster_data = df_filtered[[\"ROI\", \"Investment\"]].dropna()\n",
        "kmeans = KMeans(n_clusters=3).fit(...)\n",
        "```\n",
        "\n",
        "> Використовується KMeans для розбиття компаній на 3 кластери за ознаками `ROI` та `Investment`. Кожна точка має колір відповідно до кластера.\n",
        "\n",
        "_Працює лише якщо є мінімум 3 компанії з непорожніми значеннями._\n",
        "\n"
      ],
      "metadata": {
        "id": "NWi-bae6ze9S"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Основна панель\n",
        "st.title(\"📊 Економічний дашборд компаній\")\n",
        "st.subheader(f\"🔍 Відфільтровано {df_filtered.shape[0]} компаній\")\n",
        "\n",
        "# Кнопка завантаження CSV\n",
        "csv = df_filtered.to_csv(index=False).encode(\"utf-8\")\n",
        "st.download_button(\n",
        "    label=\"⬇️ Завантажити CSV\",\n",
        "    data=csv,\n",
        "    file_name=\"filtered_companies.csv\",\n",
        "    mime=\"text/csv\"\n",
        ")\n",
        "\n",
        "# Інтерактивна таблиця результатів\n",
        "st.subheader(\"Оберіть, які стовпці таблиці відображати\")\n",
        "\n",
        "all_columns = df_filtered.columns.tolist()\n",
        "default_columns = [\"Company\", \"Region\", \"Industry\", \"Profit\", \"ROI\"]\n",
        "\n",
        "selected_columns = st.multiselect(\n",
        "    \"Оберіть стовпці для перегляду\",\n",
        "    options=all_columns,\n",
        "    default=[col for col in default_columns if col in all_columns]\n",
        ")\n",
        "\n",
        "if selected_columns:\n",
        "    st.dataframe(df_filtered[selected_columns])\n",
        "else:\n",
        "    st.info(\"Оберіть хоча б один стовпець, щоб побачити таблицю.\")\n",
        "\n",
        "# Карта компаній\n",
        "if show_map:\n",
        "    st.subheader(\"🗺 Географія компаній\")\n",
        "\n",
        "    map_data = df_filtered[[\"Latitude\", \"Longitude\"]].dropna().rename(\n",
        "        columns={\"Latitude\": \"latitude\", \"Longitude\": \"longitude\"}\n",
        "    )\n",
        "\n",
        "    if not map_data.empty:\n",
        "        st.map(map_data)\n",
        "    else:\n",
        "        st.warning(\"Немає доступних координат для побудови карти.\")\n",
        "\n",
        "# Відображення обраного графіка\n",
        "if chart_option == \"Доходи на клієнта vs Витрати\":\n",
        "    st.subheader(\"📊 Доходи на клієнта vs Витрати\")\n",
        "    chart = alt.Chart(df_filtered).mark_circle(size=60).encode(\n",
        "        x=\"Expenses:Q\",\n",
        "        y=\"RevenuePerCustomer:Q\",\n",
        "        color=\"Industry:N\",\n",
        "        tooltip=[\"Company\", \"Expenses\", \"RevenuePerCustomer\", \"Industry\"]\n",
        "    ).interactive().properties(title=\"Дохід на клієнта vs Витрати\")\n",
        "    st.altair_chart(chart, use_container_width=True)\n",
        "\n",
        "elif chart_option == \"Boxplot прибутку по галузях\":\n",
        "    st.subheader(\"📊 Boxplot прибутку по галузях\")\n",
        "    fig, ax = plt.subplots(figsize=(10, 5))\n",
        "    sns.boxplot(data=df_filtered, x=\"Industry\", y=\"Profit\", ax=ax)\n",
        "    ax.set_title(\"Розподіл прибутку по галузях\")\n",
        "    st.pyplot(fig)\n",
        "\n",
        "elif chart_option == \"Scatter: Прибуток vs Інвестиції\":\n",
        "    st.subheader(\"📊 Scatter: Прибуток vs Інвестиції\")\n",
        "    chart = alt.Chart(df_filtered).mark_circle(size=60).encode(\n",
        "        x=\"Investment:Q\",\n",
        "        y=\"Profit:Q\",\n",
        "        color=\"Industry:N\",\n",
        "        tooltip=[\"Company\", \"Investment\", \"Profit\"]\n",
        "    ).interactive().properties(title=\"Прибуток vs Інвестиції\")\n",
        "    st.altair_chart(chart, use_container_width=True)\n",
        "\n",
        "elif chart_option == \"Гістограма конверсії по галузях\":\n",
        "    st.subheader(\"📊 Гістограма конверсії по галузях\")\n",
        "    fig, ax = plt.subplots(figsize=(10, 5))\n",
        "    sns.barplot(\n",
        "        data=df_filtered,\n",
        "        x=\"Industry\",\n",
        "        y=\"ConversionRate\",\n",
        "        estimator=\"mean\",\n",
        "        ax=ax\n",
        "    )\n",
        "    ax.set_title(\"Середній Conversion Rate по галузях\")\n",
        "    st.pyplot(fig)\n",
        "\n",
        "elif chart_option == \"Теплова карта кореляцій\":\n",
        "    st.subheader(\"📊 Теплова карта кореляцій\")\n",
        "    numeric_cols = df_filtered.select_dtypes(include=[np.number])\n",
        "    corr = numeric_cols.corr()\n",
        "    fig, ax = plt.subplots(figsize=(10, 6))\n",
        "    sns.heatmap(corr, annot=True, cmap=\"coolwarm\", fmt=\".2f\", ax=ax)\n",
        "    ax.set_title(\"Кореляційна матриця числових показників\")\n",
        "    st.pyplot(fig)\n",
        "\n",
        "elif chart_option == \"Кластеризація компаній (KMeans)\":\n",
        "    st.subheader(\"📊 Кластеризація компаній на основі ROI та Investment\")\n",
        "    cluster_data = df_filtered[[\"ROI\", \"Investment\"]].dropna().copy()\n",
        "\n",
        "    if cluster_data.shape[0] >= 3:\n",
        "        kmeans = KMeans(n_clusters=3, random_state=0)\n",
        "        cluster_data[\"Cluster\"] = kmeans.fit_predict(cluster_data)\n",
        "\n",
        "        chart = alt.Chart(cluster_data).mark_circle(size=60).encode(\n",
        "            x=\"Investment:Q\",\n",
        "            y=\"ROI:Q\",\n",
        "            color=\"Cluster:N\",\n",
        "            tooltip=[\"ROI\", \"Investment\", \"Cluster\"]\n",
        "        ).interactive().properties(title=\"Кластеризація за ROI та Investment\")\n",
        "        st.altair_chart(chart, use_container_width=True)\n",
        "    else:\n",
        "        st.warning(\"Недостатньо даних для кластеризації (потрібно ≥ 3 рядки).\")"
      ],
      "metadata": {
        "id": "hjUurC4Ynx-S"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## __Реалізація моделі лінійної регресії__\n",
        "\n",
        "- Перевіряється, чи активовано чекбокс `show_regression`.\n",
        "- Створюється новий DataFrame `df_reg`, що містить лише вибрані змінні X та Y, з видаленими пропущеними значеннями.\n",
        "- Якщо в `df_reg` є принаймні 2 рядки, будується лінійна регресійна модель за допомогою `LinearRegression` з бібліотеки `scikit-learn`.\n",
        "- Виводяться коефіцієнт нахилу $\\beta$, зсув `intercept` та коефіцієнт детермінації $R^2$.\n",
        "- Будується графік розсіювання з лінією регресії.\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "ltXufxdx1nsm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Побудова регресійної моделі\n",
        "if show_regression:\n",
        "    st.subheader(f\"📈 Лінійна регресія: {reg_y} ~ {reg_x}\")\n",
        "\n",
        "    df_reg = df_filtered[[reg_x, reg_y]].dropna()\n",
        "\n",
        "    if df_reg.shape[0] >= 2:\n",
        "        model = LinearRegression()\n",
        "        model.fit(df_reg[[reg_x]], df_reg[reg_y])\n",
        "        y_pred = model.predict(df_reg[[reg_x]])\n",
        "\n",
        "        coef = model.coef_[0]\n",
        "        intercept = model.intercept_\n",
        "        r2 = model.score(df_reg[[reg_x]], df_reg[reg_y])\n",
        "\n",
        "        st.markdown(f\"**Коефіцієнт нахилу (β):** {coef:.4f}\")\n",
        "        st.markdown(f\"**Зсув (intercept):** {intercept:.4f}\")\n",
        "        st.markdown(f\"**R²:** {r2:.4f}\")\n",
        "\n",
        "        fig, ax = plt.subplots(figsize=(8, 5))\n",
        "        sns.scatterplot(data=df_reg, x=reg_x, y=reg_y, ax=ax)\n",
        "        sns.lineplot(x=df_reg[reg_x], y=y_pred, color='red', ax=ax)\n",
        "        ax.set_title(f\"Регресія {reg_y} ~ {reg_x}\")\n",
        "        st.pyplot(fig)\n",
        "    else:\n",
        "        st.warning(\"Недостатньо даних для побудови регресії.\")"
      ],
      "metadata": {
        "id": "4KbgaUsQJ0wp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##<center>__Самостійні завдання__</center>\n",
        "\n",
        "> Скопіювати блок самостійних завдань в окремий файл ***LastName_DA6.py***\n",
        "\n",
        "> Інсталюйте необхідні пакети бібліотек Python збережіть у файл `requirements.txt`\n",
        "\n",
        "> завантажте файл зі статистичного банку даних, з яким будете працювати `data.csv`"
      ],
      "metadata": {
        "id": "huHRYPaK36l0"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Завдання\n",
        "\n",
        "1. Створіть dashboard, як додаток у **Streamlit Community Cloud**\n",
        "2. Додаток має містити: панель фільтрації з елементами\n",
        "- Заголовок      \n",
        "- Текстовий опис / інструкції                       \n",
        "- Один вибір зі списку                              \n",
        "- Кілька виборів                                   \n",
        "- Вибір одного варіанту з декількох (радіо-кнопки)  \n",
        "- Прапорець        \n",
        "3. В головній частині: таблиця, як результат фільтрів з можливістю вибору колонок\n",
        "4. Графічне представлення (мінімум 3 типи графіки)\n",
        "5. Реалізація регресійної моделі або інших (кластеризації/класифікації)                        \n",
        "6. Створені файли мають бути розміщені в репрозиторії GitHub, та імплементуватися в Streamlit Community Cloud"
      ],
      "metadata": {
        "id": "jDnw9G5y4Glz"
      }
    }
  ]
}