from bs4 import BeautifulSoup
import cv2
import numpy as np
from airflow.decorators import task

@task(task_id='resizing')
def resize(img, width, height):
    img = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized


@task(task_id='normalization')
def normalize(img):
    img = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    normalized_img = np.zeros((800, 800))
    return cv2.normalize(img, normalized_img, 0, 255, cv2.NORM_MINMAX)
