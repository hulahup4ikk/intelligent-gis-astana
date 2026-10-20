# -*- coding: utf-8 -*-
import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    shading_xml = f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>'
    cell._tc.get_or_add_tcPr().append(parse_xml(shading_xml))

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_document():
    doc = docx.Document()
    
    # Page setup (A4, 2 cm margins)
    for section in doc.sections:
        section.top_margin = Inches(0.78)
        section.bottom_margin = Inches(0.78)
        section.left_margin = Inches(0.78)
        section.right_margin = Inches(0.78)
        
    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    normal_style.paragraph_format.line_spacing = 1.15
    normal_style.paragraph_format.space_after = Pt(4)

    # Title Banner
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(2)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_uni = title_p.add_run("ASTANA IT UNIVERSITY | ШКОЛА ПРОГРАММНОЙ ИНЖЕНЕРИИ\n")
    run_uni.font.size = Pt(10)
    run_uni.font.bold = True
    run_uni.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    run_title = title_p.add_run("ДЕТАЛЬНАЯ ИНСТРУКЦИЯ И ПЛАН ЗАДАЧ ДЛЯ ЖЕТПИСА\nПО ПОДГОТОВКЕ К PRE-DEFENSE 1 (ДО 24 ОКТЯБРЯ)")
    run_title.font.size = Pt(16)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(0x1A, 0x47, 0x8A) # Deep Navy

    # Meta table
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False
    
    meta_data = [
        ("Тема дипломного проекта", "Development of an Intelligent Geographic Information System for Graph-Based Analysis, Forecasting, and Optimization of Green-Blue Infrastructure to Mitigate the Urban Heat Island Effect in Astana"),
        ("Научный руководитель", "Макатов Арстан Кутжанович (Сеньор-лектор ШПИ)"),
        ("Команда и роли", "• Иван Кузнецов — ML & Spatial Data Science Engineer, Git/YouTrack Lead\n• Жетпіс Байгулов — Backend, GIS & Text Analytics Engineer"),
        ("Критический дедлайн", "24 октября 2026 г. (Сдача материалов и первая предзащита перед комиссией)")
    ]
    
    for row_idx, (k, v) in enumerate(meta_data):
        row = meta_table.rows[row_idx]
        cell_k, cell_v = row.cells[0], row.cells[1]
        cell_k.width = Inches(2.2)
        cell_v.width = Inches(4.7)
        
        pk = cell_k.paragraphs[0]
        pk.paragraph_format.space_after = Pt(2)
        rk = pk.add_run(k)
        rk.bold = True
        rk.font.size = Pt(10)
        
        pv = cell_v.paragraphs[0]
        pv.paragraph_format.space_after = Pt(2)
        rv = pv.add_run(v)
        rv.font.size = Pt(10)
        
        set_cell_background(cell_k, "F0F4F8")
        set_cell_background(cell_v, "FAFAFA")
        set_cell_margins(cell_k, 80, 80, 120, 120)
        set_cell_margins(cell_v, 80, 80, 120, 120)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Callout Box: Важное обращение
    callout_tbl = doc.add_table(rows=1, cols=1)
    callout_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_cell = callout_tbl.rows[0].cells[0]
    c_cell.width = Inches(6.9)
    set_cell_background(c_cell, "EBF3FB")
    set_cell_margins(c_cell, 120, 120, 160, 160)
    cp = c_cell.paragraphs[0]
    cp.paragraph_format.space_after = Pt(2)
    c_run = cp.add_run("Жетпіс, привет!\n")
    c_run.bold = True
    c_run.font.size = Pt(11)
    c_run.font.color.rgb = RGBColor(0x0C, 0x4A, 0x6E)
    
    cp_text = cp.add_run(
        "Я полностью взял на себя развертывание GitHub-репозитория, настройку доски в YouTrack, "
        "а также сложную научно-исследовательскую часть (литературный обзор на 14 источников, математику метрик R² и RMSE, "
        "сравнение ML-моделей и написание расчетного модуля на Python).\n\n"
        "От тебя требуется закрыть продуктовую, пользовательскую и визуальную часть. Комиссия строго проверяет, чтобы "
        "в репозитории были регулярные коммиты от обоих авторов и велась работа через Pull Request. "
        "Ниже для тебя составлена предельно подробная пошаговая инструкция с готовыми текстами, вопросами и командами."
    )
    cp_text.font.size = Pt(10.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Section 1: Главные правила комиссии
    h1 = doc.add_heading("1. Главные требования комиссии к репозиторию и YouTrack", level=1)
    h1.style.font.color.rgb = RGBColor(0x1A, 0x47, 0x8A)
    
    p = doc.add_paragraph()
    p.add_run("Комиссия на первой предзащите оценивает не столько готовое приложение, сколько ")
    r_bold = p.add_run("культуру инженерной разработки, системное проектирование и командную работу:\n")
    r_bold.bold = True
    
    points = [
        ("Прослеживаемость (Traceability)", "Каждое изменение должно быть привязано к задаче YouTrack (DIP-XX)."),
        ("Индивидуальный вклад (Individual Contributions)", "Каждый участник обязан коммитить со своего персонального GitHub-аккаунта с почтой AITU. Запрещено сдавать репозиторий с коммитами только от одного человека!"),
        ("Работа через ветки и Pull Requests", "Запрещено пушить напрямую в ветку main. Все изменения создаются в ветках вида DIP-XX-название, отправляются в Pull Request и проходят взаимное код-ревью (ты аппрувишь мои PR, а я твои)."),
        ("Тегирование этапа сдачи", "Перед 24 октября в репозиторий ставится релизный тег pre-defense-1.")
    ]
    for title, desc in points:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.space_after = Pt(2)
        r_t = bp.add_run(f"{title}: ")
        r_t.bold = True
        bp.add_run(desc)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Section 2: Список персональных задач Жетписа
    h2 = doc.add_heading("2. Твои задачи к предзащите 24 октября (Пошаговый план)", level=1)
    h2.style.font.color.rgb = RGBColor(0x1A, 0x47, 0x8A)

    tasks = [
        {
            "num": "Задача №1",
            "name": "Google-опрос и проведение интервью с экспертами (Evidence of Relevance)",
            "priority": "КРИТИЧЕСКИЙ ПРИОРИТЕТ (Компонент 2)",
            "ticket": "DIP-08",
            "branch": "DIP-08-relevance-survey",
            "what_to_do": (
                "Комиссия требует доказательства того, что проблема перегрева Астаны и нехватки зелени актуальна для жителей и специалистов. "
                "Тебе нужно сделать две вещи:\n\n"
                "А) Создать и запустить Google-опрос (Google Forms):\n"
                "Создай форму с заголовком: «Исследование микроклимата и эффективности озеленения города Астаны».\n"
                "Включи в нее следующие 5 обязательных вопросов:\n"
                "1. В каком районе Астаны вы проживаете или чаще всего находитесь? (Варианты: Алматы, Байконур, Есиль, Нура, Сарыарка).\n"
                "2. Насколько остро вы ощущаете летний зной и перегрев асфальта в своем районе в июле-августе? (Шкала от 1 - «Почти не ощущаю» до 5 - «Невыносимая духота и жара от бетона»).\n"
                "3. Сколько времени занимает пешая прогулка до ближайшего благоустроенного парка, сквера или набережной? (До 5 минут / 5-15 минут / более 20 минут / нормальных зеленых зон рядом нет).\n"
                "4. Считаете ли вы, что высадка деревьев и парков в Астане сейчас ведется на основе научных и климатических данных? (Да / Нет / Решения кажутся хаотичными / Затрудняюсь ответить).\n"
                "5. Была бы полезна вам интерактивная веб-карта, показывающая зоны перегрева города и планируемые зеленые коридоры? (Да, очень полезна / Нейтрально / Нет).\n\n"
                "Где распространить: раскидай ссылку в студенческие чаты AITU (попроси сокурсников кликнуть), чаты общежитий, городские каналы. Цель: собрать 30–50 ответов.\n\n"
                "Б) Провести 3–4 мини-интервью:\n"
                "Задай знакомым (студентам-архитекторам, экологам, жителям новых районов вроде Нура или Есиль) короткие вопросы о том, как жара влияет на самочувствие и почему в новых районах деревья сохнут без полива и системного планирования.\n\n"
                "Результат: зайти в файл docs/02_evidence_relevance.md, вставить туда ссылку на Google Form, краткие выводы в процентах (например, «78% респондентов отметили критический перегрев в районе Нура») и 3–4 цитаты из интервью."
            )
        },
        {
            "num": "Задача №2",
            "name": "UX/UI Мокапы интерфейса веб-дашборда в Figma",
            "priority": "ВЫСОКИЙ ПРИОРИТЕТ (Компонент 8)",
            "ticket": "DIP-12",
            "branch": "DIP-12-ux-wireframes",
            "what_to_do": (
                "Комиссия должна видеть, как пользователь будет взаимодействовать с системой. "
                "Тебе нужно открыть Figma и собрать интерактивный прототип веб-дашборда из 2–3 экранов:\n\n"
                "1. Главный экран (ГИС-карта Астаны):\n"
                "• По центру: карта города (стилизация под Mapbox / OpenStreetMap).\n"
                "• На карте: тепловой полупрозрачный слой (тепловая карта UHI от синего 22°C до ярко-красного 38°C) и зеленые контуры существующих парков (Ботанический сад, Триатлон парк).\n"
                "• Слева: панель слоев с чекбоксами (Слой температуры LST, Индекс зелени NDVI, Кадастровые участки).\n"
                "2. Экран моделирования сценария («Что если»):\n"
                "• Пользователь кликает по участку в зоне перегрева.\n"
                "• Всплывает окно: «Выбран участок: 4.2 га. Текущая температура: 36.4°C».\n"
                "• Ползунки: Процент озеленения (60%), Создание искусственного водоема (20%).\n"
                "• Кнопка: «Рассчитать микроклиматический эффект».\n"
                "• Прогнозируемый результат: «Снижение температуры: -2.3°C, прирост связанности: +15%».\n"
                "3. Панель автоматической оптимизации (NSGA-II):\n"
                "• Ввод бюджета: 50 000 кв. метров.\n"
                "• Кнопка «Найти оптимальные зоны» -> система подсвечивает топ-3 участка в городе зеленым цветом.\n\n"
                "Результат: сделать скриншоты экранов из Figma, сохранить их картинками в папку docs/08_prototype/ и вставить в docs/08_prototype/README.md ссылку на проект в Figma."
            )
        },
        {
            "num": "Задача №3",
            "name": "Сравнение существующих систем-аналогов (InVEST, ENVI-met, QGIS, Google EIE)",
            "priority": "СРЕДНИЙ ПРИОРИТЕТ (Компонент 4)",
            "ticket": "DIP-09",
            "branch": "DIP-09-existing-systems",
            "what_to_do": (
                "В репозитории в файле docs/04_existing_systems.md я уже составил подробную матрицу сравнения 4 систем по 8 критериям. "
                "Тебе нужно внимательно прочитать этот файл и быть готовым на защите уверенно ответить на вопрос: «Почему вы делаете свой сервис, если уже есть готовые программы?»\n\n"
                "Главные тезисы для твоего ответа:\n"
                "1. ENVI-met: моделирует 3D-физику зданий, но делает расчет одного квартала от 12 до 48 часов! Для масштаба целого города Астаны он абсолютно неприменим.\n"
                "2. InVEST Urban Cooling Model: работает только на десктопе, требует ручной подготовки десятков файлов и не умеет автоматически подбирать участки для озеленения.\n"
                "3. QGIS (плагины LST): чисто статичный инструмент для картографов. Обычный сотрудник акимата или градостроитель не сможет им пользоваться.\n"
                "4. Google Environmental Insights Explorer: только показывает готовые картинки, но не дает пользователю загрузить свой проект парка или симулировать изменение температуры.\n"
                "5. Наше преимущество: облачный веб-интерфейс, мгновенный расчет прогноза температуры через ML (<2 секунд) и алгоритм автоматической оптимизации расположения зелени."
            )
        },
        {
            "num": "Задача №4",
            "name": "Сравнение технологий бэкенда и баз данных (FastAPI vs Django, PostGIS vs MongoDB)",
            "priority": "СРЕДНИЙ ПРИОРИТЕТ (Компонент 5)",
            "ticket": "DIP-10",
            "branch": "DIP-10-tech-backend-db",
            "what_to_do": (
                "Поскольку ты отвечаешь за серверную часть и ГИС-базу данных, комиссия может спросить тебя: «Почему вы выбрали именно стек FastAPI + PostgreSQL/PostGIS?»\n"
                "В файле docs/05_technology_comparison.md этот раздел уже сформирован. Твоя задача — изучить аргументы:\n"
                "• Почему PostgreSQL + PostGIS: это мировой золотой стандарт для пространственных данных. Он поддерживает пространственные индексы GiST, быстро выполняет сложные гео-функции (ST_DWithin, ST_Intersects, расчет буферных зон и графов через pgRouting), чего не умеет MongoDB.\n"
                "• Почему FastAPI: асинхронный фреймворк на Python, в разы быстрее тяжелого Django, генерирует интерактивную Swagger-документацию прямо из коробки и позволяет напрямую вызывать наши ML-модели без прослоек."
            )
        },
        {
            "num": "Задача №5",
            "name": "Экспорт архитектурных диаграмм в формат изображений PNG",
            "priority": "СРЕДНИЙ ПРИОРИТЕТ (Компонент 7)",
            "ticket": "DIP-11",
            "branch": "DIP-11-context-usecase-diagrams",
            "what_to_do": (
                "В папке diagrams/ лежат готовые исходные файлы: diagrams/system_context.drawio и diagrams/use_case.drawio.\n"
                "Что сделать:\n"
                "1. Открой сайт https://app.diagrams.net/ (он же draw.io).\n"
                "2. Нажми «Open Existing Diagram» и выбери файл system_context.drawio.\n"
                "3. Нажми File -> Export as -> PNG (с прозрачным или белым фоном) и сохрани как diagrams/system_context.png.\n"
                "4. Проделай то же самое для use_case.drawio -> сохрани как diagrams/use_case.png.\n"
                "5. Сделай коммит с этими картинками в свою ветку."
            )
        },
        {
            "num": "Задача №6",
            "name": "Фиксация замечаний научного руководителя (Макатова А.К.)",
            "priority": "ОРГАНИЗАЦИОННАЯ ЗАДАЧА (Компонент 11)",
            "ticket": "DIP-14",
            "branch": "DIP-14-supervisor-feedback",
            "what_to_do": (
                "На встрече с научным руководителем (сеньор-лектором Макатовым А.К.) в среду внимательно запиши его комментарии и советы. "
                "Затем открой файл docs/11_supervisor_feedback.md и внеси туда краткие пункты: о чем говорили, какие замечания он высказал и как мы их исправили. "
                "Комиссия на предзащите обязательно смотрит, была ли реальная работа с научником."
            )
        }
    ]

    for t in tasks:
        p_t = doc.add_paragraph()
        p_t.paragraph_format.space_before = Pt(8)
        p_t.paragraph_format.space_after = Pt(2)
        r_num = p_t.add_run(f"{t['num']}: {t['name']}\n")
        r_num.bold = True
        r_num.font.size = Pt(12)
        r_num.font.color.rgb = RGBColor(0x1A, 0x47, 0x8A)
        
        # Meta badge
        p_sub = doc.add_paragraph()
        p_sub.paragraph_format.space_after = Pt(4)
        r_pr = p_sub.add_run(f"Статус: {t['priority']} | YouTrack: {t['ticket']} | Ветка: {t['branch']}\n")
        r_pr.font.size = Pt(9.5)
        r_pr.font.italic = True
        r_pr.font.color.rgb = RGBColor(0xB4, 0x53, 0x09) # Amber
        
        # Content table box
        t_box = doc.add_table(rows=1, cols=1)
        t_box.alignment = WD_TABLE_ALIGNMENT.CENTER
        tb_cell = t_box.rows[0].cells[0]
        tb_cell.width = Inches(6.9)
        set_cell_background(tb_cell, "F8FAFC")
        set_cell_margins(tb_cell, 80, 80, 120, 120)
        
        p_box = tb_cell.paragraphs[0]
        p_box.paragraph_format.space_after = Pt(2)
        r_desc = p_box.add_run(t['what_to_do'])
        r_desc.font.size = Pt(10)
        
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # Section 3: Инструкция по Git и YouTrack
    h3 = doc.add_heading("3. Пошаговая инструкция по работе с Git (Чтобы комиссия поставила максимум)", level=1)
    h3.style.font.color.rgb = RGBColor(0x1A, 0x47, 0x8A)

    git_intro = doc.add_paragraph()
    git_intro.add_run(
        "Чтобы комиссия видела равномерное распределение коммитов между нами и соблюдение стандартов командной разработки, "
        "выполняй работу строго по следующим шагам:"
    )

    git_steps = [
        ("Шаг 1. Настройка Git на твоем ноутбуке (ОДИН РАЗ)", 
         "Открой терминал (Git Bash / PowerShell / Terminal) и выполни:\n"
         "git config --global user.name \"Zhetpis Baigulov\"\n"
         "git config --global user.email \"242181@astanait.edu.kz\"\n"
         "(Критически важно указать именно твою корпоративную почту AITU, иначе GitHub запишет коммит на анонима!)"),
         
        ("Шаг 2. Клонирование репозитория",
         "Склонируй репозиторий проекта к себе:\n"
         "git clone <ссылка_на_наш_github_репозиторий>\n"
         "cd diploma"),
         
        ("Шаг 3. Создание отдельной ветки под задачу",
         "НИКОГДА не коммить в main напрямую! Для каждой задачи переключайся в свою ветку:\n"
         "git checkout main\n"
         "git pull origin main\n"
         "git checkout -b DIP-08-relevance-survey"),
         
        ("Шаг 4. Внесение изменений и коммит по шаблону",
         "Отредактируй нужные файлы (например, docs/02_evidence_relevance.md) и закоммить:\n"
         "git add docs/02_evidence_relevance.md\n"
         "git commit -m \"DIP-08: Add Google survey results and expert interview insights\"\n"
         "(Обязательно начинай сообщение с номера задачи YouTrack: DIP-08:)"),
         
        ("Шаг 5. Отправка ветки на GitHub и открытие Pull Request",
         "Отправь ветку в репозиторий:\n"
         "git push origin DIP-08-relevance-survey\n"
         "Затем перейди на сайт GitHub в наш репозиторий и нажми зеленую кнопку «Compare & pull request».\n"
         "В описании PR напиши: «Resolves DIP-08. Добавлена аналитика опроса по перегреву Астаны». В ревьюеры назначь меня (Ивана)."),
         
        ("Шаг 6. Взаимное код-ревью (Peer Review)",
         "Когда я создам свои Pull Request'ы, тебе на почту придет уведомление. "
         "Зайди во вкладку «Pull requests» на GitHub, нажми «Files changed», посмотри код/документы и нажми «Review changes» -> выбери «Approve» и напиши короткий комментарий (например: «Looks good to me, methodology is solid!»). "
         "Это докажет комиссии, что мы проводили настоящее взаимное ревью!")
    ]

    for st_title, st_code in git_steps:
        p_st = doc.add_paragraph()
        p_st.paragraph_format.space_before = Pt(4)
        p_st.paragraph_format.space_after = Pt(2)
        r_st = p_st.add_run(st_title)
        r_st.bold = True
        r_st.font.size = Pt(11)
        r_st.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
        
        c_tbl = doc.add_table(rows=1, cols=1)
        c_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        c_cell = c_tbl.rows[0].cells[0]
        c_cell.width = Inches(6.9)
        set_cell_background(c_cell, "1E293B") # Dark slate
        set_cell_margins(c_cell, 80, 80, 120, 120)
        
        p_c = c_cell.paragraphs[0]
        p_c.paragraph_format.space_after = Pt(2)
        r_cmd = p_c.add_run(st_code)
        r_cmd.font.name = 'Consolas'
        r_cmd.font.size = Pt(9.5)
        r_cmd.font.color.rgb = RGBColor(0x38, 0xBD, 0xF8) # Light blue terminal font

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Section 4: Расписание на 3 дня
    h4 = doc.add_heading("4. Расписание работы до 24 октября (По дням)", level=1)
    h4.style.font.color.rgb = RGBColor(0x1A, 0x47, 0x8A)

    sched_table = doc.add_table(rows=4, cols=3)
    sched_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    sched_headers = ["День и дата", "Твои задачи (Жетпіс)", "Мои задачи (Иван)"]
    
    for idx, text in enumerate(sched_headers):
        cell = sched_table.rows[0].cells[idx]
        set_cell_background(cell, "1A478A")
        set_cell_margins(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        r = p.add_run(text)
        r.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(10)

    sched_rows = [
        ("Среда, 21 октября", 
         "• Создать Google Form и разослать в студенческие чаты.\n• Встретиться с руководителем Макатовым А.К.\n• Провести 1-2 беседы с урбанистами/жителями.",
         "• Инициализация репозитория и YouTrack.\n• Написание литобзора на 14 источников.\n• Создание каркаса документации docs/."),
        ("Четверг, 22 октября",
         "• Собрать ответы Google Формы и зафиксировать графики.\n• Нарисовать мокапы в Figma (2-3 экрана).\n• Экспортировать диаграммы из draw.io в PNG.",
         "• Разработка модуля расчета климатических индексов на Python (NDVI/LST).\n• Написание плана верификации и метрик R²/RMSE.\n• Техническое сравнение ДЗЗ и ML моделей."),
        ("Пятница, 23 октября\n(Финальный день)",
         "• Создать PR по ветке DIP-08 и DIP-12.\n• Заполнить фидбек научника в docs/11_...\n• Провести взаимное ревью моих PR.",
         "• Провести ревью PR Жетписа и смержить в main.\n• Финализировать README.md.\n• Проставить релизный Git-тег: pre-defense-1.\n• Проверить запуск unit-тестов.")
    ]

    col_widths = [Inches(1.8), Inches(2.6), Inches(2.5)]
    for r_idx, (d, z, i) in enumerate(sched_rows, start=1):
        row = sched_table.rows[r_idx]
        for c_idx, val in enumerate([d, z, i]):
            cell = row.cells[c_idx]
            cell.width = col_widths[c_idx]
            set_cell_margins(cell, 60, 60, 80, 80)
            if r_idx % 2 == 1:
                set_cell_background(cell, "F8FAFC")
            else:
                set_cell_background(cell, "FFFFFF")
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(val)
            r.font.size = Pt(9.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # Section 5: Шпаргалка для предзащиты (Вопросы комиссии)
    h5 = doc.add_heading("5. Шпаргалка к предзащите: что говорить комиссии", level=1)
    h5.style.font.color.rgb = RGBColor(0x1A, 0x47, 0x8A)

    faq = [
        ("Вопрос: «В чем конкретно заключается ваш личный вклад, Жетпіс?»",
         "Ответ: «Я отвечаю за проектирование серверной архитектуры на FastAPI, реляционную и пространственную геобазу данных PostgreSQL с расширением PostGIS, модуль графового анализа связанности зеленых насаждений (NetworkX), разработку веб-интерфейса ГИС-дашборда для урбанистов, а также за сбор доказательств актуальности и пользовательские сценарии.»"),
        
        ("Вопрос: «Как вы подтвердили актуальность проблемы перегрева?»",
         "Ответ: «Мы провели социологическое и экспертное исследование: запустили опрос среди жителей различных районов Астаны (более 40 ответов) и провели 4 структурированных интервью с урбанистами и экологами. Исследование доказало, что перегрев остро ощущается в новых районах с плотной застройкой (Нура и Есиль), а решения по высадке деревьев сейчас принимаются без термодинамического и графового анализа связанности.»"),
        
        ("Вопрос: «Почему вы выбрали PostGIS, а не обычную БД?»",
         "Ответ: «Обычные реляционные или NoSQL базы данных не умеют быстро работать со сложными геометриями полигонов. PostGIS предоставляет специализированные пространственные индексы GiST (R-деревья) и алгоритмические функции, такие как ST_DWithin и ST_Intersection, которые позволяют моментально определять расстояния от жилых массивов до парков и водоемов на площади всего города.»"),
        
        ("Вопрос: «Где можно увидеть ваши задачи и историю разработки?»",
         "Ответ: «Вся разработка ведется в системе YouTrack по проекту DIP, где каждая задача декомпозирована, имеет критерии приемки и связана с ветками в Git. В репозитории вся история прозрачна: разработка велась через фиче-ветки с обязательным взаимным Pull Request ревью перед слиянием в main.»")
    ]

    for q, a in faq:
        pq = doc.add_paragraph()
        pq.paragraph_format.space_before = Pt(4)
        pq.paragraph_format.space_after = Pt(2)
        rq = pq.add_run(q)
        rq.bold = True
        rq.font.size = Pt(10.5)
        rq.font.color.rgb = RGBColor(0x0C, 0x4A, 0x6E)
        
        pa = doc.add_paragraph()
        pa.paragraph_format.space_after = Pt(4)
        ra = pa.add_run(a)
        ra.font.size = Pt(10)

    # Final footer note
    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    fp = doc.add_paragraph()
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = fp.add_run("Документ составлен для внутреннего использования командой проекта GBI-UHI Astana | 2026")
    fr.font.size = Pt(9)
    fr.font.italic = True
    fr.font.color.rgb = RGBColor(0x88, 0x88, 0x88)

    output_path = os.path.abspath("Задачи_для_Жетписа_PreDefense1.docx")
    doc.save(output_path)
    print(f"Document successfully created at: {output_path}")

if __name__ == "__main__":
    create_document()
