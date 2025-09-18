namespace CriptBB84 {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Arrays;
    open Microsoft.Quantum.Diagnostics;

    /// # Summary
    /// Gera um bit aleatório usando 1 qubit e medição.
    operation RandomBit() : Int {
        use q = Qubit();           // 'use' substitui 'using'
        H(q);                      // Hadamard
        let result = MResetZ(q);   // Mede e reseta o qubit
        return result == One ? 1 | 0;
    }

    /// Imprime um vetor de inteiros como string.
    operation PrintVetorInt(v : Int[], n : Int) : Unit {
        mutable str = "";
        for i in 0 .. n - 1 {
            set str = str + " " + IntAsString(v[i]);
        }
        Message(str);
    }

    operation ConvertResultinIntArray(v : Result[]) : Int[] {
        return ForEach(result => result == One ? 1 | 0, v);
    }

    // Operações de Aplicação de Base e Medidas
    operation AliceApply(qubits : Qubit[], AliceBits : Int[], AliceBase : Int[]) : Unit {
        for i in IndexRange(qubits) {
            if AliceBits[i] == 1 { X(qubits[i]); } // Se o bit é 1, o qubit passará a ser |1>
            if AliceBase[i] == 1 { H(qubits[i]); } // Aplica H aleatoriamente seguindo o vetor de bits
        }
    }

    operation BobRead(qubits : Qubit[], BobBase : Int[]) : Result[] {
        // Bob recebe a transmissão e aplica aleatoriamente H
        // Caso os dois tenham aplicado a H nos mesmos qubits, terão as mesmas medidas
        // Caso contrário os valores serão diferentes
        mutable MeasureBob = new Result[Length(qubits)];
        for i in IndexRange(qubits) {
            if BobBase[i] == 1 { H(qubits[i]); }
            set MeasureBob w/= i <- M(qubits[i]);
        }
        return MeasureBob;
    }

    // Operação do Protocolo BB84
    operation KeyBB84(AliceBits : Int[], AliceBase : Int[], BobBase : Int[]) : Int[] {
        // Operação principal que gera uma chave entre Alice e Bob
        let n = Length(AliceBits);
        use qubits = Qubit[n]; // Aloca n qubits em |0>
        
        // Alice aplica X para setar seus Bits
        // E aplica H de acordo com a base aleatoriamente
        AliceApply(qubits, AliceBits, AliceBase);

        // TRANSMISSÃO DOS QUBITS PARA BOB ... (Ex: Fótons por Fibra Ótica em condições ideais)

        // Bob recebe os qubits e aplica a H aleatoriamente e faz a medida
        let BobM = BobRead(qubits, BobBase);
        let BobBits = ConvertResultinIntArray(BobM); //operação apenas para trocar o tipo Result em Inteiros (0 ou 1)

        // Reconciliacão de bases
        // Bob envia a Alice somente os seus bits de Base (por meio público), idem para Alice.
        // Assim, tanto Alice quanto Bob, podem comparar as bases de cada um, e usar como chave 
        // os Bits de Mensagem cujos bits de base utilizados são iguais, logo Alice e Bob terão uma chave idêntica.

        // Alice separa os bits de chave, comparando sua base com a gerada por Bob, idem para Bob
        mutable key = new Int[0];
        for i in 0 .. n - 1 {
            if AliceBase[i] == BobBase[i] {
                set key += [AliceBits[i]];
            }
        }

        ResetAll(qubits);
        return key; // Retorna a chave compartilhada

        // OBS:
        // Caso Eva interceptasse os qubits, qualquer tentativa de captura da informação, por parte
        // de Eva, implica em mudanças nesta informação, segundo a Teoria da Medida.

        // Existe um próximo passo que é a verificação se houve interceptação, onde Bob envia a Alice parte 
        // de sua chave, caso os valores sejam diferentes indica que ou houve espionagem ou erros nos instrumentos
        // invalidando a chave gerada e repetindo o processo.
    }
}