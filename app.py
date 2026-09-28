import streamlit as st

from course_data import BEGINNER_TRACK, LESSONS, PROJECTS, QUIZZES

st.set_page_config(
    page_title="MIS Python Learning Hub",
    page_icon="📊",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(180deg, #f5f8ff 0%, #eef5ff 100%);
    }
    h1, h2, h3 {
        color: #123d7a;
    }
    .stAlert {
        border-radius: 12px;
    }
    .presentation-slide {
        background: white;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        min-height: 600px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("MIS Python Learning Hub")
st.caption("A beginner-friendly Python education service for MIS major students")

with st.sidebar:
    st.header("Navigation")
    page = st.radio(
        "Choose a section",
        ["Overview", "Lessons", "Practice", "Quizzes", "MIS Projects", "🎤 Presentation Mode"]
    )

if page == "Overview":
    st.subheader("Why this service matters")
    st.info(
        "This learning hub is designed for MIS students who are new to programming. It focuses on business-friendly examples, beginner skills, and practical use cases in management information systems."
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Goal", "Learn Python")
    with col2:
        st.metric("Audience", "MIS beginners")
    with col3:
        st.metric("Focus", "Business automation")

    st.subheader("Beginner track")
    for step in BEGINNER_TRACK:
        st.write(f"- {step}")

    st.subheader("What students will practice")
    st.markdown(
        """
        - Variables and basic data types
        - Lists and dictionaries
        - Conditions and logic
        - Loops and functions
        - CSV and Excel workflow basics
        - Small business reporting and decision support tasks
        """
    )

elif page == "Lessons":
    st.subheader("Structured learning modules")
    for lesson in LESSONS:
        with st.expander(f"{lesson['id']}. {lesson['title']} ({lesson['level']})"):
            st.write(f"Duration: {lesson['duration']}")
            st.write("Objectives:")
            for objective in lesson["objectives"]:
                st.write(f"- {objective}")
            st.write(lesson["content"])
            st.code(lesson["example"], language="python")
            st.write("Practice idea:")
            st.write(lesson["practice"])

elif page == "Practice":
    st.subheader("Mini practice tasks")
    practice_tasks = [
        "Create a variable for a product's price and quantity.",
        "Use a dictionary to store customer order information.",
        "Write an if statement to check if stock is low.",
        "Write a loop that prints each employee name from a list.",
        "Build a simple function that calculates total revenue.",
        "Read a CSV file and print the total of one column."
    ]

    for idx, task in enumerate(practice_tasks, start=1):
        st.write(f"{idx}. {task}")

    st.markdown("---")
    st.write("Suggested daily plan:")
    st.write("- Step 1: Read one lesson")
    st.write("- Step 2: Complete one mini task")
    st.write("- Step 3: Review the quiz")

elif page == "Quizzes":
    st.subheader("Quick Knowledge Check")
    score = 0
    for index, question in enumerate(QUIZZES, start=1):
        st.write(f"### Q{index}: {question['question']}")
        selected = st.radio(
            "Choose an answer:",
            question["options"],
            key=f"q{index}",
            index=None,
            horizontal=False,
        )

        if selected:
            if selected == question["answer"]:
                score += 1
                st.success("Correct! " + question["explanation"])
            else:
                st.warning("Not quite. " + question["explanation"])

    st.markdown("---")
    if score > 0:
        st.subheader(f"Your score: {score}/{len(QUIZZES)}")
    else:
        st.subheader("Start answering questions to see your score.")

elif page == "MIS Projects":
    st.subheader("Project ideas for MIS students")
    for project in PROJECTS:
        with st.container():
            st.markdown(f"### {project['title']}")
            st.write(project["goal"])
            st.write(project["description"])
            st.write("Skills:")
            for skill in project["skills"]:
                st.write(f"- {skill}")
            st.markdown("---")

elif page == "🎤 Presentation Mode":
    st.subheader("🎤 Presentation Mode - Easy Demo for Stakeholders")
    
    presentation_slides = [
        {
            "title": "MIS Python Learning Hub",
            "subtitle": "A Beginner-Friendly Education Service",
            "content": """
            ### 소개
            - **목표**: MIS 전공 학생들을 위한 Python 교육 서비스
            - **대상**: 프로그래밍 초보자
            - **특징**: 경영정보시스템 실무 중심의 학습
            """
        },
        {
            "title": "Why This Service?",
            "subtitle": "Business Problem We're Solving",
            "content": """
            ### 문제점
            1. MIS 학생들이 Python을 어렵게 느낌
            2. 이론만 배우고 실무 적용 못함
            3. 학습 모티베이션 부족
            
            ### 해결책
            - 비즈니스 예제 중심 학습
            - 단계적 커리큘럼
            - 실제 MIS 프로젝트 경험
            """
        },
        {
            "title": "Service Features",
            "subtitle": "What Students Get",
            "content": """
            ### 주요 기능
            1. **8개의 구조화된 수업 모듈**
               - Python 기초부터 실무 프로젝트까지
               
            2. **실습 과제** (6가지)
               - 매일 작은 과제로 꾸준한 학습
               
            3. **퀴즈** (5개)
               - 학습 이해도 확인
               
            4. **MIS 프로젝트** (3가지)
               - 출석 관리 시스템
               - 재고 모니터링
               - 매출 리포트 생성
            """
        },
        {
            "title": "Learning Path",
            "subtitle": "Curriculum Overview",
            "content": """
            ### 단계별 학습 로드맵
            
            **1단계: 기초 (Lessons 1-2)**
            - Python 소개 및 변수/데이터 타입
            
            **2단계: 데이터 구조 (Lessons 3-4)**
            - 리스트, 딕셔너리, 조건문
            
            **3단계: 프로그래밍 기법 (Lessons 5-6)**
            - 반복문, 함수
            
            **4단계: 실무 응용 (Lessons 7-8)**
            - CSV/Excel 파일 처리 및 미니 프로젝트
            """
        },
        {
            "title": "Sample Lesson: Variables",
            "subtitle": "Lesson 2 - Python Basics",
            "content": """
            ### 변수와 데이터 타입
            
            **개념**
            변수는 데이터를 저장하는 상자입니다.
            
            **코드 예제**
            ```
            product_name = 'Laptop'
            price = 950.50
            in_stock = True
            ```
            
            **비즈니스 예제**
            - 상품명, 가격, 재고 상태 저장
            - 고객 정보 관리
            - 판매 데이터 기록
            """
        },
        {
            "title": "Sample Project: Sales Summary",
            "subtitle": "Real-World MIS Application",
            "content": """
            ### 판매 요약 애플리케이션
            
            **목표**
            - 상품 데이터 수집
            - 총 판매액 계산
            - 베스트셀러 식별
            - 월별 수익 예측
            
            **사용 기술**
            - Lists & Dictionaries
            - Loops & Functions
            - File Handling (CSV)
            
            **학습 효과**
            실제 회사에서 사용하는 비즈니스 로직 경험
            """
        },
        {
            "title": "Why Web-Based?",
            "subtitle": "Technology Benefits",
            "content": """
            ### 웹 기반 서비스의 장점
            
            **1. 설치 불필요**
            - 브라우저만 있으면 즉시 사용 가능
            - 어디서나 학습 가능
            
            **2. 상호작용적**
            - 실시간 코드 예제 실행
            - 즉시 결과 확인
            - 인터랙티브 퀴즈
            
            **3. 확장 용이**
            - 새 강의 추가 쉬움
            - 프로젝트 추가 간단
            - 기능 개선 가능
            
            **4. 접근성**
            - 모바일 친화적
            - 모든 OS 지원
            """
        },
        {
            "title": "Success Metrics",
            "subtitle": "How We Measure Impact",
            "content": """
            ### 성공 지표
            
            **학습 효과**
            - 퀴즈 평균 점수: 80% 이상
            - 모든 수업 완료율
            - 프로젝트 완성율
            
            **학생 만족도**
            - 서비스 사용도
            - 학생 피드백
            - 재사용 의향
            
            **비즈니스 임팩트**
            - MIS 전공 학생의 Python 능력 향상
            - 졸업 후 취업 경쟁력 강화
            - 실무 자동화 능력 보유
            """
        },
        {
            "title": "Roadmap & Features",
            "subtitle": "Future Enhancements",
            "content": """
            ### 향후 계획
            
            **단기 (1-2개월)**
            - 한국어 완전 지원
            - 더 많은 수업 콘텐츠
            - 학습 진도 저장 기능
            
            **중기 (3-6개월)**
            - 회원가입 및 로그인
            - 학생 성적 관리
            - 관리자 대시보드
            - 커뮤니티 기능
            
            **장기 (6개월 이상)**
            - AI 기반 개인화 학습
            - 고급 Python 과정
            - 데이터 분석 특화 과정
            - 기업 인턴십 연계
            """
        },
        {
            "title": "Get Started Today",
            "subtitle": "Quick Start Guide",
            "content": """
            ### 지금 바로 시작하기
            
            **온라인 접속**
            ```
            streamlit run app.py
            ```
            
            **학습 방법**
            1. Overview에서 소개 읽기
            2. Lessons 탭에서 수업 학습
            3. Practice로 실습 문제 해결
            4. Quizzes로 이해도 확인
            5. MIS Projects로 실프로젝트 도전
            
            **문의 및 피드백**
            - GitHub Issues로 제안 올리기
            - 질문 환영합니다!
            """
        }
    ]
    
    # Presentation controls
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col1:
        if st.button("⬅️ Previous"):
            st.session_state.slide = max(0, st.session_state.slide - 1)
    
    with col3:
        if st.button("Next ➡️"):
            st.session_state.slide = min(len(presentation_slides) - 1, st.session_state.slide + 1)
    
    with col2:
        slide_number = st.session_state.get('slide', 0)
        st.selectbox(
            "Select slide:",
            range(len(presentation_slides)),
            index=slide_number,
            key="slide_select",
            on_change=lambda: st.session_state.update({'slide': st.session_state.slide_select})
        )
    
    # Display current slide
    slide = presentation_slides[st.session_state.get('slide', 0)]
    
    st.markdown(f"""
    <div class="presentation-slide">
        <h1 style="color: #123d7a; text-align: center;">{slide['title']}</h1>
        <h3 style="color: #666; text-align: center; margin-bottom: 40px;">{slide['subtitle']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(slide['content'])
    
    # Slide counter
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.write(f"**Slide {st.session_state.get('slide', 0) + 1} of {len(presentation_slides)}**")

st.markdown("---")
st.caption("Built for beginner MIS learners who want a practical and approachable introduction to Python.")
