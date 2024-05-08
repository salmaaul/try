def konfigurasi_elektron(nomor_atom):
    konfigurasi = ""
    elektron = nomor_atom
    shell = 1
    while elektron > 0:
        max_elektron_shell = 2 * shell ** 2
        if elektron >= max_elektron_shell:
            konfigurasi += "{}{} ".format(shell, "s" if shell == 1 else "p")
            elektron -= max_elektron_shell
        else:
            subshell = elektron // (shell ** 2)
            remainder = elektron % (shell ** 2)
            if subshell > 0:
                konfigurasi += "{}{}{} ".format(shell, "s" if shell == 1 else "p", subshell)
            if remainder > 0:
                konfigurasi += "{}{}{} ".format(shell, "s" if shell == 1 else "p", subshell + 1)
            elektron = 0
        shell += 1
    return konfigurasi.strip()

nomor_atom = int(input("Masukkan nomor atom: "))
print("Konfigurasi elektron untuk atom dengan nomor atom", nomor_atom, "adalah:", konfigurasi_elektron(nomor_atom))
