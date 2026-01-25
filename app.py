<<<<<<< HEAD
import streamlit as st
import pickle
import numpy as np
import os

# Set page config
st.set_page_config(page_title="Book Recommender", layout="wide")

# Relative Paths for easier deployment
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model.pkl')
PIVOT_PATH = os.path.join(BASE_DIR, 'models', 'book_pivot.pkl')
BOOKS_PATH = os.path.join(BASE_DIR, 'models', 'books.pkl')

# Custom CSS for Modern LOOK
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Open+Sans:wght@400;600&display=swap');
    
    /* Main container background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Open Sans', sans-serif;
    }

    /* Header styling */
    .main-header {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .stTitle {
        color: #1a1a1a;
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        letter-spacing: -0.5px;
    }

    /* Recommendation Card Styling */
    .book-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: all 0.3s ease-in-out;
        text-align: center;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        margin-bottom: 1rem;
    }

    .book-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 12px 20px rgba(0,0,0,0.1);
        border: 2px solid #ff9900; /* Kindle Orange */
    }

    .book-title {
        font-size: 0.9rem;
        font-weight: 600;
        color: #333;
        margin-top: 10px;
        line-height: 1.2;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
    }

    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        background-color: transparent;
        border-radius: 10px;
        color: #666;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff9900 !important;
        color: white !important;
    }

    /* Button styling */
    .stButton>button {
        background-color: #ff9900;
        color: white;
        border-radius: 10px;
        padding: 10px 30px;
        border: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #e68a00;
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_data():
    try:
        # Check if files exist
        if not all([os.path.exists(MODEL_PATH), os.path.exists(PIVOT_PATH), os.path.exists(BOOKS_PATH)]):
             return None, None, None
             
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        with open(PIVOT_PATH, 'rb') as f:
            book_pivot = pickle.load(f)
        with open(BOOKS_PATH, 'rb') as f:
            books_metadata = pickle.load(f)
        return model, book_pivot, books_metadata
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None, None

model, book_pivot, books_metadata = load_data()

# Layout for Logo and Title
col_logo, col_title = st.columns([1, 5])
with col_logo:
    logo_path = os.path.join(BASE_DIR, 'logo.png')
    if os.path.exists(logo_path):
        st.image(logo_path, width=100)
with col_title:
    st.title("Kindle Book Recommendation System")

tab1, tab2 = st.tabs(["🎯 Recommendations", "📊 Data Insights"])

with tab1:
    st.markdown("Enter a book you like, and we'll suggest similar ones!")
    if model is None or book_pivot is None:
        st.error(f"Model files not found at {MODEL_PATH}. Please make sure the 'models' folder is in the same directory as this app.")
    else:
        book_list = book_pivot.index.values
        selected_book = st.selectbox(
            "Type or select a book from the dropdown",
            book_list
        )

        if st.button('🚀 Get Recommendations'):
            with st.spinner('Curating books for you...'):
                query_index = np.where(book_pivot.index == selected_book)[0][0]
                distances, indices = model.kneighbors(book_pivot.iloc[query_index,:].values.reshape(1, -1), n_neighbors=6)
                
                st.markdown("### ✨ Top Recommendations")
                cols = st.columns(5)
                for i in range(1, 6):
                    idx = indices.flatten()[i]
                    recommended_book_title = book_pivot.index[idx]
                    meta = books_metadata[books_metadata['title'] == recommended_book_title]
                    poster_url = meta.iloc[0]['image_url'] if not meta.empty else "https://via.placeholder.com/150"
                    
                    with cols[i-1]:
                        st.markdown(f"""
                        <div class="book-card">
                            <img src="{poster_url}" style="width: 100%; border-radius: 10px;">
                            <div class="book-title">{recommended_book_title}</div>
                        </div>
                        """, unsafe_allow_html=True)

with tab2:
    st.header("Insights from Kindle Book Data")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top Authors")
        if books_metadata is not None:
            top_authors = books_metadata['author'].value_counts().head(10)
            st.bar_chart(top_authors)
    with col2:
        st.subheader("Top Publishers")
        if books_metadata is not None:
            top_publishers = books_metadata['publisher'].value_counts().head(10)
            st.bar_chart(top_publishers)

    st.divider()
    st.subheader("Statistical Findings")
    st.markdown("""
    - **Age vs Region**: No significant difference in average reader age between US and Canada.
    - **Popularity Bias**: Highly rated books tend to have a higher volume of ratings.
    """)
=======
import streamlit as st
import pickle
import numpy as np
import os

# Set page config
st.set_page_config(page_title="Book Recommender", layout="wide")

# Relative Paths for easier deployment
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model.pkl')
PIVOT_PATH = os.path.join(BASE_DIR, 'models', 'book_pivot.pkl')
BOOKS_PATH = os.path.join(BASE_DIR, 'models', 'books.pkl')

# Custom CSS for Modern LOOK
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Open+Sans:wght@400;600&display=swap');
    
    /* Main container background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Open Sans', sans-serif;
    }

    /* Header styling */
    .main-header {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .stTitle {
        color: #1a1a1a;
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        letter-spacing: -0.5px;
    }

    /* Recommendation Card Styling */
    .book-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: all 0.3s ease-in-out;
        text-align: center;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        margin-bottom: 1rem;
    }

    .book-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 12px 20px rgba(0,0,0,0.1);
        border: 2px solid #ff9900; /* Kindle Orange */
    }

    .book-title {
        font-size: 0.9rem;
        font-weight: 600;
        color: #333;
        margin-top: 10px;
        line-height: 1.2;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
    }

    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        background-color: transparent;
        border-radius: 10px;
        color: #666;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff9900 !important;
        color: white !important;
    }

    /* Button styling */
    .stButton>button {
        background-color: #ff9900;
        color: white;
        border-radius: 10px;
        padding: 10px 30px;
        border: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #e68a00;
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_data():
    try:
        # Check if files exist
        if not all([os.path.exists(MODEL_PATH), os.path.exists(PIVOT_PATH), os.path.exists(BOOKS_PATH)]):
             return None, None, None
             
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        with open(PIVOT_PATH, 'rb') as f:
            book_pivot = pickle.load(f)
        with open(BOOKS_PATH, 'rb') as f:
            books_metadata = pickle.load(f)
        return model, book_pivot, books_metadata
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None, None

model, book_pivot, books_metadata = load_data()

# Layout for Logo and Title
col_logo, col_title = st.columns([1, 5])
with col_logo:
    logo_path = os.path.join(BASE_DIR, 'logo.png')
    if os.path.exists(logo_path):
        st.image(logo_path, width=100)
with col_title:
    st.title("Kindle Book Recommendation System")

tab1, tab2 = st.tabs(["🎯 Recommendations", "📊 Data Insights"])

with tab1:
    st.markdown("Enter a book you like, and we'll suggest similar ones!")
    if model is None or book_pivot is None:
        st.error(f"Model files not found at {MODEL_PATH}. Please make sure the 'models' folder is in the same directory as this app.")
    else:
        book_list = book_pivot.index.values
        selected_book = st.selectbox(
            "Type or select a book from the dropdown",
            book_list
        )

        if st.button('🚀 Get Recommendations'):
            with st.spinner('Curating books for you...'):
                query_index = np.where(book_pivot.index == selected_book)[0][0]
                distances, indices = model.kneighbors(book_pivot.iloc[query_index,:].values.reshape(1, -1), n_neighbors=6)
                
                st.markdown("### ✨ Top Recommendations")
                cols = st.columns(5)
                for i in range(1, 6):
                    idx = indices.flatten()[i]
                    recommended_book_title = book_pivot.index[idx]
                    meta = books_metadata[books_metadata['title'] == recommended_book_title]
                    poster_url = meta.iloc[0]['image_url'] if not meta.empty else "https://via.placeholder.com/150"
                    
                    with cols[i-1]:
                        st.markdown(f"""
                        <div class="book-card">
                            <img src="{poster_url}" style="width: 100%; border-radius: 10px;">
                            <div class="book-title">{recommended_book_title}</div>
                        </div>
                        """, unsafe_allow_html=True)

with tab2:
    st.header("Insights from Kindle Book Data")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top Authors")
        if books_metadata is not None:
            top_authors = books_metadata['author'].value_counts().head(10)
            st.bar_chart(top_authors)
    with col2:
        st.subheader("Top Publishers")
        if books_metadata is not None:
            top_publishers = books_metadata['publisher'].value_counts().head(10)
            st.bar_chart(top_publishers)

    st.divider()
    st.subheader("Statistical Findings")
    st.markdown("""
    - **Age vs Region**: No significant difference in average reader age between US and Canada.
    - **Popularity Bias**: Highly rated books tend to have a higher volume of ratings.
    """)
>>>>>>> 26c380b (Initial commit: Streamlit app and trained model artifacts)
