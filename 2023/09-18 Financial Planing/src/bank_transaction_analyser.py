import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

class BankTransactionAnalyser:

    schema = {
        'Date': np.dtype('<M8[ns]'),
        'Description': np.dtype('O'),
        'Type': np.dtype('O'),
        'Money In (£)': np.dtype('float64'),
        'Money Out (£)': np.dtype('float64'),
        'Balance (£)': np.dtype('float64')
        }
    
    category = [
        ('MARKS&SPENCER PLC|TESCO|SAINSBURYS|CO-OP GROUP','Food & Grocery'),
        ('STGCOACH|TRAINLINE','Transport'),
        ('COSTA COFFEE|PRET A MANGER','Cafe'),
        ('STEPHEN GIBSON|UKVISA|IMM HEALTH','Rent & Essential'),
        ('A MEDIUM CORPORATI|EXETER CITY COUNCI|PAYPAL *NETFLIX|APPLE|AO-OPTICALSERVICES|Amazon Prime*HT247|PAYPAL \*LEBARA 150','Subscri & Apple'),
        ('JOHN LEWIS|TED BAKER','Cloth & Shopping')
        ]
    
    # Seaborn graphic config
    sns.set_style("whitegrid")
    plot_params = {'color': '0.75',
    'style': '.-',
    'markeredgecolor': '0.25',
    'markerfacecolor': '0.25',
    'legend': False}

    plt.style.use('seaborn-whitegrid')
    plt.rc(
        "figure",
        autolayout=True,
        figsize=(11, 4),
        titlesize=18,
        titleweight='bold',
    )
    plt.rc(
        "axes",
        labelweight="bold",
        labelsize="large",
        titleweight="bold",
        titlesize=16,
        titlepad=10,
    )
    # %config InlineBackend.figure_format = 'retina'

    # Plotly Graph Settings
    
    

    def __init__(self, data, darkmode=False) -> None:
        self.data = data
        self\
            .__clean_check()\
            .__add_columns()
        self.darkmode = darkmode # initialise dark mode as true
    def __px_bgcolor(self):
        return '#17202A' if self.darkmode else '#F0F3F4'
        
    def __px_txcolor(self):
        return '#AEB6BF' if self.darkmode else '#1C2833'
    
    @staticmethod
    def __px_update_fig(fig):
        fig.update_xaxes(
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey'
        )
        fig.update_yaxes(
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey'
        )
        return fig
    def __clean_check(self):
        schema2test=self.data.dtypes.to_dict()
        validity=[]
        for key in self.schema:
            test = schema2test[key]==self.schema[key]
            validity += [test]
        if(all(validity)):
            print('data is valid') 
        else:
            # this is actually super risky because
            self.__clean()
        print('initialized')
        return self
    
    def __clean(self):
        # Create Two Funcions to Clean Numeric Date Time
        def clean_numbers(df, col):
            df[col] = df[col].apply(
                lambda x: x.str.replace(',', '').str.replace('blank','0')
            ).astype(float)
            return(df)
        def parse_datetime(df, col):
            df[col] = pd.to_datetime(df[col], format='%d %b %y')
            return(df)
        (self.data
            .pipe(clean_numbers, ['Money In (£)', 'Money Out (£)', 'Balance (£)'])
            .pipe(parse_datetime, 'Date'))
        print('cleaning complete.')
        return self
    
    def update_data(self, data):
        self.data =data
        self.__add_columns()
        return self

    @staticmethod
    def which_category(x, category):
        for match_key, content in category:
            if re.match(match_key, x):
                return(content)
            else:
                return('Other')
                
    def __add_columns(self):
        def which_cateogry(x):
            # label_category = [
            #     # This directory defines what to map, what to look for, 
            #     # Order matters, you should order them based on how confident you are.
            #     ('MARKS&SPENCER PLC|TESCO|SAINSBURYS|CO-OP GROUP','Food & Grocery'),
            #     ('STGCOACH','Transport'),
            #     ('COSTA COFFEE|PRET A MANGER','Cafe'),
            #     ('STEPHEN GIBSON|UKVISA|\*IMM HEALTH','Rent & Essential')
            # ]
            label_category=self.category
            for match_key, content in label_category:
                if re.match(match_key, x):
                    return(content)
            return('Other')
        
        self.data = (
            self.data.assign(
                Category = lambda df: df['Description'].map(which_cateogry),
                Month = lambda df: df.Date.dt.to_period('M'),
                Week = lambda df: df.Date.dt.to_period('W')
            )
        )
        return self
    def drop_columns(self):
        self.data.drop(
            columns=['Category','Month','Week']
        )
        print('columns has been droped, use __add_columns to add them back')
        return self
    
    def by_spending_period(self, p='Week'):
        '''Aggregation'''
        spending_periodic_breakdown = (
            self.data
            .groupby(['Category'] + [p])
            .agg({
                'Money Out (£)':sum,
                'Description':lambda x: x.value_counts().to_json()
                })
            # .drop('Rent & Essential', axis = 0)
        )
        return spending_periodic_breakdown
    def plot_spending_period(self, p='Week'):
        
        visBase = self.by_spending_period(p)
        # Register for ploting to use 
        ax = plt.gca() # Get Current Plotting
        pd.plotting.register_matplotlib_converters()
        ax.xaxis.freq = visBase.index.levels[1].freq
        plt.xticks(rotation=45)

        # Two Layer Plot
        sns.lineplot(
            data = visBase.reset_index(),
            x = p,
            y = 'Money Out (£)',
            hue = 'Category',
            palette = 'Set2',
            legend = False # Remove the first plot so ledgend don't overlay
        )
        sns.pointplot(
            data = visBase.reset_index(),
            x = p,
            y = 'Money Out (£)',
            hue = 'Category',
            palette = 'Set2'
        )
        sns.move_legend(
            plt.gca(), loc='center right', frameon=False, bbox_to_anchor=(1.2, .5)
        )
    def plotly_spending_period(
            self,p='Week',type='line'
            ):
        visBase=self.by_spending_period(p)
        visBase=visBase.reset_index()
        visBase[p]=visBase[p].dt.to_timestamp()
        pal = px.colors.qualitative.Vivid

        bgcolor=self.__px_bgcolor()
        txtcolor=self.__px_txcolor()

        if p=='Month':
            income_level=2199.5
        elif p=='Week':
            income_level=2199.5/4


        if(type=='line'):
            fig = px.line(
                visBase, 
                x=p, 
                y='Money Out (£)',
                color='Category',
                markers=True,
                color_discrete_sequence=pal
            )
        elif(type=='bar'):
            fig = px.bar(
                visBase, 
                x=p, 
                y='Money Out (£)',
                color='Category',
                color_discrete_sequence=pal
            )
        fig.add_hline(y=income_level)
        fig.update_layout(
            font=dict(
                color=txtcolor
            ), 
            plot_bgcolor=bgcolor,
            paper_bgcolor=bgcolor,
            legend_title_text='',
            legend=dict(
                orientation="h",
                entrywidth=100,
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ))
        fig.update_xaxes(
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black',
            # gridcolor='lightgrey'
        )
        fig.update_yaxes(
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black',
            gridcolor='lightgrey'
        )
        # fig.show(config=config) # don't ever do this! it will open up a new window
        return fig
    def plot_balance(self):
        p = sns.scatterplot(
            data = self.data,
            x = 'Date',
            y = 'Balance (£)'
        )
        p.set_title('Blance Level')
    def plotly_balance(self):
        safty=3700
        safty_color="#e63e06"

        fig = go.Figure(go.Scatter(
            mode='markers',
            x=self.data['Date'],
            y=self.data['Balance (£)'],
            marker=dict(
                color='#000080',
                line=dict(#line configure border color
                    color='#FFFFFF',
                    width=1
                )
            )
        ))
        fig.add_hline(
            y=safty,
            line=dict(
                color=safty_color,
                width=2,
                dash="dot"
            ),
            label=dict(# Lable property add annotation directly on the marker.
                text='SAFTY FIRST:)', 
                font=dict(color=safty_color), 
                textposition='end',yanchor='top'
                )
        )
        fig.update_layout(
            font=dict(
                color=self.__px_txcolor(),
            ),
            plot_bgcolor=self.__px_bgcolor(),
            paper_bgcolor=self.__px_bgcolor(),
        )
        self.__px_update_fig(fig)
        return fig
        


            
        
    