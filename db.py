import pandas as pd
import sqlite3

gene_df = pd.read_csv('genotyping_data/genstudio.csv', index_col=0)
connection = sqlite3.connect('genes.db')

query = '''CREATE TABLE genstudio(
            genstudio_id INTEGER PRIMARY KEY,
            SNP_Name TEXT,
            SNP_Index INTEGER,
            SNP_Aux INTEGER,
            Sample_ID TEXT,
            SNP TEXT,
            Allele1_Top TEXT,
            Allele2_Top TEXT,
            Allele1_Forward TEXT,
            Allele2_Forward TEXT,
            Allele1_AB TEXT,
            Allele2_AB TEXT,
            Chr TEXT,
            Position TEXT,
            GC_Score REAL,
            GT_Score REAL,
            Theta REAL,
            R REAL,
            B_Allele_Freq REAL,
            Log_R_Ratio REAL
            )'''

connection.execute(query)
connection.commit()
connection.close()

inserion_query = '''
                INSERT INTO
                genstudio(SNP_Name, SNP_Index, SNP_Aux, Sample_ID, SNP,
                Allele1_Top, Allele2_Top, Allele1_Forward, Allele2_Forward,
                Allele1_AB, Allele2_AB, Chr, Position, GC_Score,
                GT_Score, Theta, R, B_Allele_Freq, Log_R_Ratio)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                        ?, ?, ?, ?, ?, ?, ?, ?, ?)
                '''

connection = sqlite3.connect('genes.db')
connection.executemany(inserion_query, gene_df.to_numpy())
connection.commit()
connection.close()

connection = sqlite3.connect('genes.db')

# Проверим, что все работает:
select_query = '''
                SELECT SNP_Name, SNP, Position
                FROM genstudio
                '''
result = connection.execute(select_query).fetchall()

for i, (name, SNP, pos) in enumerate(result):
    print(name, SNP, pos)
    if i == 10:
        break
