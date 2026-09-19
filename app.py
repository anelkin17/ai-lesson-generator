import streamlit as st
from lesson_generator import generate_lesson


st.set_page_config(
    page_title="AI Teacher Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Teacher Assistant")
st.write("Создавайте планы уроков, задания и тесты с помощью искусственного интеллекта.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    subject = st.text_input(
        "📚 Предмет",
        placeholder="Например: Информатика"
    )

    grade = st.selectbox(
        "🎓 Класс / курс",
        ["5", "6", "7", "8", "9", "10", "11", "1 курс", "2 курс", "3 курс", "4 курс"]
    )

    topic = st.text_input(
        "📝 Тема урока",
        placeholder="Например: Логические операции"
    )

with col2:
    language = st.selectbox(
        "🌐 Язык",
        ["Қазақша", "Русский", "English"]
    )

    lesson_type = st.selectbox(
        "📖 Тип материала",
        [
            "План урока",
            "Тест",
            "Практическое задание",
            "Домашнее задание",
            "Критерии оценивания"
        ]
    )

    difficulty = st.selectbox(
        "⚡ Уровень сложности",
        ["Базовый", "Средний", "Продвинутый"]
    )

st.divider()

if st.button("✨ Создать с помощью AI", type="primary", use_container_width=True):

    if not subject or not topic:
        st.warning("Пожалуйста, укажите предмет и тему урока.")
    else:
        with st.spinner("AI готовит материал..."):
            try:
                result = generate_lesson(
                    subject=subject,
                    grade=grade,
                    topic=topic,
                    language=language,
                    lesson_type=lesson_type,
                    difficulty=difficulty
                )

                st.success("Материал успешно создан!")

                st.markdown("## 📄 Результат")
                st.markdown(result)

                st.download_button(
                    label="📥 Скачать результат",
                    data=result,
                    file_name="ai_lesson.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Произошла ошибка: {e}")

st.divider()

st.caption("AI Teacher Assistant • HackAlem AI 2026")
