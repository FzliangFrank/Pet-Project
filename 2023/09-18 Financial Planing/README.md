Yep. 


You have it. Ready your pdf bank statement into pandas dataframe. 
Read bank-statement from a list of files. 

**on-the-fly read**

```py
from bank_transaction_reader import BankTransactionReader as btr

# having a list of pdf files in place.
files = [
    'bank-statement/Statement_2023_8.pdf',
    'bank-statement/Statement_2023_9.pdf'
]

# et voila!
df = btr.read(files)
```

It is possible some bank statement don't extract the same imformation from pdf files. In that case you have to modify break tokens (details will be introduced below).

**redefine processor**

```py
from bank_transaction_reader import BankTransactionProcesser

# reserved this ability of using 
my_pattern = r'(?!\d)\.(?<!\d)'
processor = BankTransactionProcesser(my_pattern)


file_loc = 'bank-statement/Statement_2023_9.pdf'
df = btr.read(file_loc, processor) # this is the idea way, haven't tested yet.
## Interally this calls processor.read
df = processor.read(file_loc)

text = processor.extract_text_from_pdf(file_loc) # the extracted text
tran_bloc=processor.extract_transaction_blocks(text)  # sections where tables are printed
processor.process_transactions(tran_bloc) # extract dataframe for each secions and store it into processor.dfs. This can be viewed. 
```

The `r'(?!\d)\.(?<!\d)'` looks for seperator used to break the key values. Pairs. 


**rational**

This is based off the 
```

```