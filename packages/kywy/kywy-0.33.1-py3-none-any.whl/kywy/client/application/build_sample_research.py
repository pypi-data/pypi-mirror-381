import pandas as pd

from ...client.kawa_client import KawaClient as K
from datetime import datetime, date, timedelta
import numpy as np
from faker import Faker


def kawa():
    k = K(kawa_api_url='http://localhost:8080')
    k.set_api_key(api_key_file='/Users/emmanuel/doc/local-pristine/.key')
    k.set_active_workspace_id(workspace_id='108')
    return k

research = kawa().research('Net Profit Analysis by State')

# Register the data models
orders_model = research.register_model(model_id='3650')
events_model = research.register_model(model_id='3651')

## PHASE 1: Model building

# Create relationship to get event costs per state
events_relationship = orders_model.create_relationship(
    name='Events by State',
    description='Linking orders to events to calculate total event costs per state',
    target_model=events_model,
    link={'State': 'event state'}
)

events_relationship.add_column(
    name='event cost',
    aggregation='SUM',
    new_column_name='Total Event Cost'
)

# Create metric for net profit
orders_model.create_metric(
    name='Net Profit',
    formula='"Profit" - "Total Event Cost"'
)

research.publish_models()

## PHASE 2: Model querying and analysis

df = (orders_model.select(
    K.col('State').first(),
    K.col('Profit').sum().alias('Total Profit'),
    K.col('Total Event Cost').sum().alias('Total Event Cost'),
    K.col('Net Profit').sum().alias('Net Profit')
)
.group_by('State')
.order_by('Net Profit', ascending=False)
.limit(10000)
.collect())

response_model = research.publish_results(
    title='Net Profit by State',
    df=df
)

## PHASE 3: Explain your reasoning

report = research.report()

report.header1('State with the Most Net Profit')

report.paragraph("""
The objective is to identify which state has the highest net profit, where net profit is calculated as the sum of all profits from orders minus the sum of all event costs in that state.
""")

report.header2('Approach used')

report.paragraph("""
To answer this question, I created a relationship between the Orders model and the Events model by linking them on the State field. This relationship allows us to aggregate all event costs per state and add them as a new column to the Orders model. I then created a Net Profit metric that subtracts the total event cost from the profit for each order.
""")

report.paragraph(f"""
Using this enriched model, I queried the data grouping by State to calculate the total profit, total event cost, and net profit for each state. The query returned {len(df)} states. By sorting the results in descending order by net profit, I identified the state with the highest net profit value of ${df.iloc[0]['Net Profit']:,.2f}, which is {df.iloc[0]['State']}.
""")

report.header2('Data model(s)')

report.header3('Orders')

report.table(
    title='Orders Model with Event Costs',
    source=orders_model,
    column_names=['State', 'Profit', 'Total Event Cost', 'Net Profit']
)

report.paragraph("""
I added a relationship to the Events model to bring in the total event costs per state, and created a Net Profit metric that calculates the difference between Profit and Total Event Cost.
""")

report.code("""
  Orders → Events (via State = event state)
""")

report.header2('Final result')

report.paragraph("""
After aggregating all orders and event costs by state, I calculated the net profit for each state and sorted the results to find the state with the highest value.
""")

report.table(
    title='Net Profit by State',
    source=response_model,
    column_names=['State', 'Total Profit', 'Total Event Cost', 'Net Profit']
)

report.paragraph(f"""
The state with the most net profit is {df.iloc[0]['State']} with a net profit of ${df.iloc[0]['Net Profit']:,.2f}. This was calculated by taking the total profit of ${df.iloc[0]['Total Profit']:,.2f} and subtracting the total event cost of ${df.iloc[0]['Total Event Cost']:,.2f}.
""")

print(report.publish())