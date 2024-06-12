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
        # Diagonal dari atas kiri ke bawah kanan
        diag1 = [(board[i][i+l], i, i+l) for i in range(max(-l, 0), min(n, m-l)) if 0 <= i+l < m]
        # Diagonal dari atas kanan ke bawah kiri
        diag2 = [(board[i][l+n-i-1], i, l+n-i-1) for i in range(max(l, 0), min(n, m+l-n)) if 0 <= l+n-i-1 < m]
        
        if diag1:
            diags.append((''.join([x[0] for x in diag1]).lower(), [(x[1], x[2]) for x in diag1]))
        if diag2:
            diags.append((''.join([x[0] for x in diag2]).lower(), [(x[1], x[2]) for x in diag2]))

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
                    row_answers.append([word,[i, ans]])

        else:
            for word in words:
                # Berhenti jika kata lebih panjang dari baris
                if (len(word)>len(rows[i])):
                    break
                # Searching BM
                ans = bmSearch(word,rows[i])
                if ans != -1:
                    row_answers.append([word,[i, ans]])


    print(GREEN + f"\nJawaban Pada sisi ROWS ({len(row_answers)}) : "  + RESET)
    row_answers = sorted(row_answers, key=lambda x: len(x[0]), reverse=True)
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
                    col_answers.append([word,[ans,i]])

        else:
            for word in words:
                # Berhenti jika kata lebih panjang dari baris
                if (len(word)>len(cols[i])):
                    break
                # Searching BM
                ans = bmSearch(word,cols[i])
                if ans != -1:
                    col_answers.append([word,[ans,i]])

    print(GREEN  + f"\nJawaban Pada sisi COLUMNS ({len(col_answers)}) : " + RESET)
    col_answers = sorted(col_answers, key=lambda x: len(x[0]), reverse=True)
    for col in col_answers:
        print(col)
    
    # Searching diagonal
    diag = extract_diagonals(board)
    for diag_data in diag:
        diag_string, positions = diag_data  # Harus selalu menerima tuple dengan dua elemen
        for word in words:
            if len(word) <= len(diag_string):
                ans = kmpSearch(word, diag_string) if mode.lower() == "kmp" else bmSearch(word, diag_string)
                if ans != -1:
                    diag_answers.append([word, positions[ans]])

    print(GREEN + f"\nJawaban Pada sisi DIAGONAL ({len(diag_answers)}) : " + RESET)
    diag_answers = sorted(diag_answers, key=lambda x: len(x[0]), reverse=True)
    for dia in diag_answers:
        print(dia)

    #  Set timer
    end = time.time()
    print(YELLOW + f"\nWaktu eksekusi program : {end - start} detik" +RESET)
    