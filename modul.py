import main
while True:
    main.tampilan()
    main.pengaplikasian()
    print('\n')
    lanjut = input('APAKAH ANDA INGIN MELANJUTKAN PROGRAM ? [Y/T] : ').upper()
    if lanjut == 'T':
        print('======= PROGRAM TERHENTI😉 =======')
        break