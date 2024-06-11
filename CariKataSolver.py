from BM import *
from KMP import *
import time

# Color
RED = '\033[31m'  # Red text
GREEN = '\033[32m'  # Green text
YELLOW = '\033[33m'  # Yellow text
RESET = '\033[0m'

def extract_diagonals(board):
    n, m = len(board), len(board[0])
    diags = []
    for l in range(1-n, m):
        diag1 = [board[i][i+l] for i in range(max(-l, 0), min(n, m-l))]
        diag2 = [board[i][l+n-i-1] for i in range(max(l, 0), min(n, m+l-n))]
        if diag1:
            diags.append((''.join(diag1)).lower())
        if diag2:
            diags.append(''.join(diag2).lower())
    return diags

def extract_rows(board):
    return [(''.join(row)).lower() for row in board]

def extract_columns(board):
    return  [(''.join(col)).lower() for col in zip(*board)]
# Contoh penggunaan



def readWordFile(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            array_of_strings = [line.strip() for line in lines]
        return array_of_strings
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
        return []
    except Exception as e:
        print(f"Terjadi error saat membaca file: {e}")
        return []

def readMatrixFile(filename):
    try:
        matrix = []
        with open(filename, 'r') as file:
            for line in file:
                # Convert each line to a list of integers
                row = list(map(str, line.split()))
                matrix.append(row)
        return matrix
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
        return []


while(True):
    words = readWordFile("words.txt")
    row_answers = []
    col_answers = []
    diag_answers = []

    board_file = input("Masukkan nama file papan kata yang akan di cari jawabannya : ")
    board = readMatrixFile(board_file)
    while board == []:
        board_file = input("Masukkan nama file papan kata yang akan di cari jawabannya : ")
        board = readMatrixFile(board_file)

    mode = input("Masukkan mode pencarian (KMP/BM) : ")
    while mode not in ["KMP", "BM","kmp","bm"]:
        mode = input("Masukkan mode pencarian (KMP/BM) : ")    
    
    #  Set timer
    start = time.time()

    # Searching horizontal
    rows = extract_rows(board)
    for i in range(len(rows)):
        ans = 0 # insiasi
        if mode == "KMP" or mode == "kmp":
            for word in words:
                # Berhenti jika kata lebih panjang dari baris
                if (len(word)>len(rows[i])):
                    break
                # Searching KMP
                ans = kmpSearch(word,rows[i])
                if ans != -1:
                    row_answers.append([word,[i+1, ans+1]])

        else:
            for word in words:
                # Berhenti jika kata lebih panjang dari baris
                if (len(word)>len(rows[i])):
                    break
                # Searching BM
                ans = bmSearch(word,rows[i])
                if ans != -1:
                    row_answers.append([word,[i+1, ans+1]])


    print(GREEN + "\nJawaban Pada sisi ROWS :" + RESET)
    for row in row_answers:
        print(row)

    # Searching vertical
    cols = extract_columns(board)
    for i in range(len(cols)):
        ans = 0 # insiasi

        if mode == "KMP" or mode == "kmp":
            for word in words:
                # Berhenti jika kata lebih panjang dari baris
                if (len(word)>len(cols[i])):
                    break
                # Searching KMP
                ans = kmpSearch(word,cols[i])
                if ans != -1:
                    col_answers.append([word,[i+1, ans+1]])

        else:
            for word in words:
                # Berhenti jika kata lebih panjang dari baris
                if (len(word)>len(cols[i])):
                    break
                # Searching BM
                ans = bmSearch(word,cols[i])
                if ans != -1:
                    col_answers.append([word,[i+1, ans+1]])

    print(GREEN  + "\nJawaban Pada sisi COLUMNS :" + RESET)
    for col in col_answers:
        print(col)
    
    # Searching diagonal
    diag = extract_diagonals(board)
    for i in range(len(diag)):
        ans = 0 # insiasi

        if mode == "KMP" or mode == "kmp":
            for word in words:
                # Berhenti jika kata lebih panjang dari baris
                if (len(word)>len(diag[i])):
                    break
                # Searching KMP
                ans = kmpSearch(word,diag[i])
                if ans != -1:
                    diag_answers.append([word,[i+1, ans+1]])

        else:
            for word in words:
                # Berhenti jika kata lebih panjang dari baris
                if (len(word)>len(diag[i])):
                    break
                # Searching BM
                ans = bmSearch(word,diag[i])
                if ans != -1:
                    diag_answers.append([word,[len(rows)-i, ans+1]])

    print(GREEN + "\nJawaban Pada sisi DIAGONAL :" + RESET)
    for dia in diag_answers:
        print(dia)

    #  Set timer
    end = time.time()
    print(YELLOW + f"\nWaktu eksekusi program : {end - start} detik" +RESET)
    