# first_script.py
# Liest eine FASTA-Datei ein und zeigt die häufigsten Aminosäuren.
from collections import Counter


def read_fasta(path):
    """Liest eine FASTA-Datei und gibt Kopfzeile und Sequenz zurück."""
    header = ""
    seq_parts = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                header = line[1:]
            else:
                seq_parts.append(line)
    return header, "".join(seq_parts)


header, seq = read_fasta("insulin.fasta")

print("Protein:", header)
print("Länge:", len(seq), "Aminosäuren")
print()
print("Die fünf häufigsten Aminosäuren:")

counts = Counter(seq)
for aa, n in counts.most_common(5):
    print(f"  {aa}: {n} ({n / len(seq) * 100:.1f} %)")