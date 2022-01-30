dna_input=list(input("DNA please: "))
def transcription():
	rna_output=list()
	for i in dna_input:
		match i: 
			case ('A' | 'a'):
				rna_output.append('U')
			case ('T' | 't'):
				rna_output.append('A')
			case ('G' | 'g'):
				rna_output.append('C')
			case ('C' | 'c'):
				rna_output.append('G')
	return rna_output
def translation(rna_input=transcription()):
	protein_output=list()
	rna_input = [rna_input[i:i+3] for i in range(0,len(rna_input),3)]
	for i in rna_input:
		match rna_input:
			case("GCU" | "GCC" | "GCA" | "GCG"):
				protein_output.append("A")
			case("" | "" | "" | ""):
				pass
			case("" | "" | "" | ""):
				pass
			case("" | "" | "" | ""):
				pass
			case("" | "" | "" | ""):
				pass
			case("" | "" | "" | ""):
				pass
			case("" | "" | "" | ""):
				pass
			case("" | "" | "" | ""):
				pass
	return protein_output
print(translation())
