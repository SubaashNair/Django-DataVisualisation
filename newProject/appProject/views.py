from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
# Create your views here.


def indexPage(request):

    df = pd.read_csv(
        'https://raw.githubusercontent.com/SubaashNair/Django-DataVisualisation/main/covid_19.csv'
    )
    new_df = df[['Country/Region', 'Deaths']].sort_values(by='Deaths',
                                                          ascending=False)
    grouped_df = new_df.groupby('Country/Region').sum().sort_values(
        by="Deaths", ascending=False)
    filtered_df = grouped_df[grouped_df['Deaths'] > 15000]
    countryList = filtered_df.index.tolist()
    countryValueList = filtered_df.values.tolist()
    context = {
        'countryList': countryList,
        'countryValueList': countryValueList
    }
    return render(request, 'index.html', context)
    #return render(request, 'index.html', {})
