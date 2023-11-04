import streamlit as st
from celery import Celery

# Create a Celery instance
celery = Celery('myapp', broker='redis://localhost:6379/0')

@celery.task
def background_task():
    # Your background task logic here
    return "Task completed!"

# Streamlit app
st.title("Streamlit with Celery")

if st.button("Run Background Task"):
    result = background_task.delay()
    st.spinner("Running task...")
    st.text(result.get())
