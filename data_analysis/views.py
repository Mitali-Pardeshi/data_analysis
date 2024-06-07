import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import UploadForm
from .models import Upload

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save()
            file_path = os.path.join(settings.MEDIA_ROOT, upload.file.name)
            return redirect('data_analysis:analyze_file', file_path=file_path)
    else:
        form = UploadForm()
    return render(request, 'data_analysis/upload.html', {'form': form})

def analyze_file(request, file_path):
    data = pd.read_csv(file_path)

    # Basic Data Analysis
    head = data.head().to_html()
    description = data.describe().to_html()

    # Handle missing values
    missing_values = data.isnull().sum()
    missing_values_df = missing_values.to_frame(name='Missing Values').reset_index()
    missing_values_html = missing_values_df.to_html(index=False)

    # Visualizations
    plt.figure(figsize=(10, 6))
    data.hist(bins=30, figsize=(20, 15), layout=(4, 4))
    plt.tight_layout()
    hist_path = os.path.join(settings.MEDIA_ROOT, 'histogram.png')
    plt.savefig(hist_path)
    plt.close()

    return render(request, 'data_analysis/analyze.html', {
        'head': head,
        'description': description,
        'missing_values': missing_values_html,
        'hist_path': hist_path,
    })
