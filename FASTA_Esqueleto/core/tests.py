import unittest
from sequences import Sequence
from transformations import RenameDuplicatedSequencesTransformation

class TestRenameDuplicatedSequencesTransformation(unittest.TestCase):

    def test_no_duplicates(self):
        seqs = [Sequence("S1", "ACTG"), Sequence("S2", "GGTA")]
        transformer = RenameDuplicatedSequencesTransformation()
        result = transformer.transform(seqs)
        # En este caso, los identificadores no se deben modificar
        expected = [Sequence("S1", "ACTG"), Sequence("S2", "GGTA")]
        
        result_stripped = [str(seq).strip() for seq in result]
        expected_stripped = [str(seq).strip() for seq in expected]
    
        self.assertEqual(result_stripped, expected_stripped)

    def test_two_duplicates(self):
        seqs = [Sequence("S1", "ACTG"), Sequence("S1", "GGTA")]
        transformer = RenameDuplicatedSequencesTransformation()
        result = transformer.transform(seqs)
        # Aquí "S1" debe ser renombrado a "S1.1" y "S1.2"
        expected = [Sequence("S1.1", "ACTG"), Sequence("S1.2", "GGTA")]
        
        result_stripped = [str(seq).strip() for seq in result]
        expected_stripped = [str(seq).strip() for seq in expected]
    
        self.assertEqual(result_stripped, expected_stripped)
        
    def test_multiple_duplicates(self):
        seqs = [
            Sequence("S1", "AAA"),
            Sequence("S1", "CCC"),
            Sequence("S1", "GGG"),
        ]
        transformer = RenameDuplicatedSequencesTransformation()
        result = transformer.transform(seqs)
        # Tres duplicados, deben ser renombrados a "S1.1", "S1.2", "S1.3"
        expected = [
            Sequence("S1.1", "AAA"),
            Sequence("S1.2", "CCC"),
            Sequence("S1.3", "GGG"),
        ]

        result_stripped = [str(seq).strip() for seq in result]
        expected_stripped = [str(seq).strip() for seq in expected]
    
        self.assertEqual(result_stripped, expected_stripped)
        
    def test_interleaved_duplicates(self):
        seqs = [
            Sequence("S1", "AAA"),
            Sequence("S2", "CCC"),
            Sequence("S1", "GGG"),
            Sequence("S2", "TTT"),
        ]
        transformer = RenameDuplicatedSequencesTransformation()
        result = transformer.transform(seqs)
        # "S1" y "S2" están intercalados, pero deben ser renombrados correctamente
        expected = [
            Sequence("S1.1", "AAA"),
            Sequence("S2.1", "CCC"),
            Sequence("S1.2", "GGG"),
            Sequence("S2.2", "TTT"),
        ]

        result_stripped = [str(seq).strip() for seq in result]
        expected_stripped = [str(seq).strip() for seq in expected]
    
        self.assertEqual(result_stripped, expected_stripped)
        
    def test_single_entry(self):
        seqs = [Sequence("S1", "AAA")]
        transformer = RenameDuplicatedSequencesTransformation()
        result = transformer.transform(seqs)
        # Un solo identificador, no se renombra
        expected = [Sequence("S1", "AAA")]

        result_stripped = [str(seq).strip() for seq in result]
        expected_stripped = [str(seq).strip() for seq in expected]
    
        self.assertEqual(result_stripped, expected_stripped)
        
if __name__ == '__main__':
    unittest.main()
