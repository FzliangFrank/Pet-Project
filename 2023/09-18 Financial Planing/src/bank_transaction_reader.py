import pandas as pd
import re
import PyPDF2

class BankTransactionReader:
    '''Cleaning, Transaction and Cleaning'''
    def __init__(self):
        pass

    def read(pdf_file_path, processor=None):
        """
        Read bankstatement on the fly. This is considered as interface 
        for bank statement read. 
        
        Processor arugment should let you swap engines in case your statment or
        function is different.
        """
        
        if processor is None:
            processor = BankTransactionProcesser()
        else:
            processor = processor()
        
        if isinstance(pdf_file_path, (list)):

            for file in pdf_file_path:
                processor.read(file, reset=False)

            df = processor.get_concatenated_dataframe()
        else:   
            df = processor.read(pdf_file_path)
        return df
        

class BankTransactionProcesser:
    def __init__(self, 
                 rowsep = r'(?!\d)\.(?<!\d)'
                 ):
        self.data_dict = {}  # Initialize an empty dictionary
        self.dfs = []  # Initialize an empty list to store parsed DataFrames
        self.rowsep = rowsep

    def _parse_transaction(self, transaction):
        transaction = transaction.strip('\n')
        parts = transaction.split('\n', 1)
        
        if len(parts) == 2:
            key, value = parts
            key = key.strip()
            value = value.strip()
            
            if key == 'Column':
                self.current_column = value
                self.data_dict[self.current_column] = []
            else:
                self.current_column = key
                self.data_dict[self.current_column].append(value)

    def read(self, pdf_file_path, reset = True):
        '''This method will save every read into dfs'''

        # clean cached dataframe fragment
        self.dfs = [] if reset else self.dfs 

        pdf_text = self.extract_text_from_pdf(pdf_file_path)
        transaction_blocks = self.extract_transaction_blocks(pdf_text)
        self.process_transactions(transaction_blocks)
        concatenated_df = self.get_concatenated_dataframe()
        if reset: 
            return(concatenated_df)
        else: 
            print(f'Read additional {len(transaction_blocks)} tables.Total {len(self.dfs)} tables populated.')
    
    def extract_text_from_pdf(self, pdf_file_path):
        text = ""
        with open(pdf_file_path, 'rb') as readerOBJ:
            pdfReader = PyPDF2.PdfReader(readerOBJ)
            for page in pdfReader.pages:
                text += page.extract_text() + "\n"
        return text

    def extract_transaction_blocks(self, text):
        # Use the provided regular expression pattern to extract 'transaction_blocks' from the input 'text'
        pattern = r'(?<=Your Transactions\n)(.*?)(?=\(Continued on next page\)|Transaction types)'
        transaction_blocks = re.findall(pattern, text, re.DOTALL)
        return transaction_blocks

    def process_transactions(self, transaction_blocks):
        for transaction_block in transaction_blocks:
            transaction_block = transaction_block.strip('\n')
            transaction_list = re.split(self.rowsep, transaction_block)

            for transaction in transaction_list:
                self._parse_transaction(transaction)

            df = pd.DataFrame(self.data_dict)
            self.dfs.append(df)
            self.data_dict = {}  # Reset data_dict for the next chunk

    def get_concatenated_dataframe(self):
        if not self.dfs:
            raise ValueError("No dataframes have been processed. Call process_transactions() first.")
        
        return pd.concat(self.dfs, ignore_index=True)
    
