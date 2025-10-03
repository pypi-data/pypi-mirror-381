from ccinput.exceptions import InvalidParameter
from ccinput.tests.testing_utilities import InputTests


class QChemTests(InputTests):
    def test_sp_SE(self):
        params = {
            "type": "Single-Point Energy",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "AM1",
            "charge": "-1",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = sp
        method = am1
        semi_empirical = true
        mem_total = 1000
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_sp_HF(self):
        params = {
            "mem": "2000MB",
            "type": "Single-Point Energy",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "HF",
            "basis_set": "3-21G",
            "charge": "-1",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = sp
        method = hf
        basis = 3-21g
        mem_total = 2000
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_sp_HF_SMD(self):
        params = {
            "mem": "2000MB",
            "type": "Single-Point Energy",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "HF",
            "basis_set": "3-21G",
            "charge": "-1",
            "solvent": "Chloroform",
            "solvation_model": "SMD",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = sp
        method = hf
        basis = 3-21g
        mem_total = 2000
        solvent_method = smd
        $end

        $smx
        solvent trichloromethane
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_sp_HF_SMD_lowercase(self):
        params = {
            "mem": "2000MB",
            "type": "Single-Point Energy",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "HF",
            "basis_set": "3-21G",
            "charge": "-1",
            "solvent": "Chloroform",
            "solvation_model": "smd",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = sp
        method = hf
        basis = 3-21g
        mem_total = 2000
        solvent_method = smd
        $end

        $smx
        solvent trichloromethane
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_sp_HF_SMD18(self):
    #     params = {
    #         "type": "Single-Point Energy",
    #         "file": "I.xyz",
    #         "software": "QChem",
    #         "method": "HF",
    #         "basis_set": "3-21G",
    #         "charge": "-1",
    #         "solvent": "Chloroform",
    #         "solvation_model": "SMD",
    #         "solvation_radii": "SMD18",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !SP HF 3-21G
    #     *xyz -1 1
    #     I 0.0 0.0 0.0
    #     *
    #     %pal
    #     nprocs 8
    #     end
    #     %cpcm
    #     smd true
    #     SMDsolvent "chloroform"
    #     radius[53] 2.74
    #     radius[35] 2.60
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_sp_HF_SMD18_lowercase(self):
    #     params = {
    #         "type": "Single-Point Energy",
    #         "file": "I.xyz",
    #         "software": "QChem",
    #         "method": "HF",
    #         "basis_set": "3-21G",
    #         "charge": "-1",
    #         "solvent": "Chloroform",
    #         "solvation_model": "smd",
    #         "solvation_radii": "smd18",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !SP HF 3-21G
    #     *xyz -1 1
    #     I 0.0 0.0 0.0
    #     *
    #     %pal
    #     nprocs 8
    #     end
    #     %cpcm
    #     smd true
    #     SMDsolvent "chloroform"
    #     radius[53] 2.74
    #     radius[35] 2.60
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_solvation_octanol_smd(self):
        params = {
            "mem": "2000MB",
            "type": "Single-Point Energy",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "HF",
            "basis_set": "3-21G",
            "charge": "-1",
            "solvent": "octanol",
            "solvation_model": "SMD",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = sp
        method = hf
        basis = 3-21g
        mem_total = 2000
        solvent_method = smd
        $end

        $smx
        solvent 1-octanol
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_sp_HF_CPCM(self):
        params = {
            "type": "Single-Point Energy",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "HF",
            "basis_set": "3-21G",
            "charge": "-1",
            "solvent": "Chloroform",
            "solvation_model": "CPCM",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = sp
        method = hf
        basis = 3-21g
        mem_total = 1000
        solvent_method = pcm
        $end

        $pcm
        theory cpcm
        $end

        $solvent
        solventname trichloromethane
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_solvent_synonym(self):
        params = {
            "mem": "2000MB",
            "type": "Single-Point Energy",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "HF",
            "basis_set": "3-21G",
            "charge": "-1",
            "solvent": "CHCL3",
            "solvation_model": "SMD",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = sp
        method = hf
        basis = 3-21g
        mem_total = 2000
        solvent_method = smd
        $end

        $smx
        solvent trichloromethane
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_solvation_octanol_cpcm1(self):
        params = {
            "type": "Single-Point Energy",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "HF",
            "basis_set": "3-21G",
            "charge": "-1",
            "solvent": "octanol",
            "solvation_model": "CPCM",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = sp
        method = hf
        basis = 3-21g
        mem_total = 1000
        solvent_method = pcm
        $end

        $pcm
        theory cpcm
        $end

        $solvent
        solventname octanol
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_solvation_octanol_cpcm2(self):
        params = {
            "type": "Single-Point Energy",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "HF",
            "basis_set": "3-21G",
            "charge": "-1",
            "solvent": "1-octanol",
            "solvation_model": "CPCM",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = sp
        method = hf
        basis = 3-21g
        mem_total = 1000
        solvent_method = pcm
        $end

        $pcm
        theory cpcm
        $end

        $solvent
        solventname octanol
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_invalid_solvation(self):
        params = {
            "mem": "2000MB",
            "type": "Single-Point Energy",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "HF",
            "basis_set": "3-21G",
            "charge": "-1",
            "solvent": "Chloroform",
            "solvation_model": "ABC",
        }

        # TODO raise specific exception?
        with self.assertRaises(Exception):
            self.generate_calculation(**params)

    def test_sp_DFT(self):
        params = {
            "mem": "1200MB",
            "type": "Single-Point Energy",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "M06-2X",
            "basis_set": "Def2-SVP",
            "charge": "-1",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = sp
        method = m06-2x
        basis = def2-svp
        mem_total = 1200
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_sp_DFT_specifications(self):
    #     params = {
    #         "type": "Single-Point Energy",
    #         "file": "Cl.xyz",
    #         "software": "QChem",
    #         "method": "M06-2X",
    #         "basis_set": "Def2-SVP",
    #         "charge": "-1",
    #         "specifications": "TightSCF",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !SP M062X Def2-SVP tightscf
    #     *xyz -1 1
    #     Cl 0.0 0.0 0.0
    #     *
    #     %pal
    #     nprocs 8
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_sp_DFT_multiple_specifications(self):
    #     params = {
    #         "type": "Single-Point Energy",
    #         "file": "Cl.xyz",
    #         "software": "QChem",
    #         "method": "M06-2X",
    #         "basis_set": "Def2-SVP",
    #         "charge": "-1",
    #         "specifications": "TightSCF GRID6",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !SP M062X Def2-SVP tightscf grid6
    #     *xyz -1 1
    #     Cl 0.0 0.0 0.0
    #     *
    #     %pal
    #     nprocs 8
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_sp_DFT_duplicate_specifications(self):
    #     params = {
    #         "type": "Single-Point Energy",
    #         "file": "Cl.xyz",
    #         "software": "QChem",
    #         "method": "M06-2X",
    #         "basis_set": "Def2-SVP",
    #         "charge": "-1",
    #         "specifications": "tightscf TightSCF GRID6",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !SP M062X Def2-SVP tightscf grid6
    #     *xyz -1 1
    #     Cl 0.0 0.0 0.0
    #     *
    #     %pal
    #     nprocs 8
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_sp_MP2(self):
    #     params = {
    #         "mem": "2000MB",
    #         "type": "Single-Point Energy",
    #         "file": "Cl.xyz",
    #         "software": "QChem",
    #         "method": "RI-MP2",
    #         "basis_set": "cc-pVTZ",
    #         "charge": "-1",
    #         # "specifications": "cc-pVTZ/C",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     $comment
    #     File created by ccinput
    #     $end

    #     $molecule
    #     -1 1
    #     Cl 0.0 0.0 0.0
    #     $end

    #     $rem
    #     jobtype = sp
    #     method = ri-mp2
    #     basis = cc-pvtz
    #     aux_basis = rimp2-cc-pvtz
    #     mem_total = 2000
    #     $end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_opt_SE(self):
        params = {
            "type": "Geometrical Optimisation",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "AM1",
            "charge": "-1",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = opt
        method = am1
        semi_empirical = true
        mem_total = 1000
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_opt_HF(self):
        params = {
            "mem": "2000MB",
            "type": "Geometrical Optimisation",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "HF",
            "basis_set": "3-21G",
            "charge": "-1",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = opt
        method = hf
        basis = 3-21g
        mem_total = 2000
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_opt_DFT(self):
        params = {
            "mem": "2000MB",
            "type": "Geometrical Optimisation",
            "file": "Cl.xyz",
            "software": "QChem",
            "charge": "-1",
            "method": "B3LYP",
            "basis_set": "6-31+G(d,p)",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = opt
        method = b3lyp
        basis = 6-31+g(d,p)
        mem_total = 2000
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_freq_SE(self):
        params = {
            "type": "Frequency Calculation",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "AM1",
            "charge": "-1",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = freq
        method = am1
        semi_empirical = true
        mem_total = 1000
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_freq_HF(self):
        params = {
            "mem": "2000MB",
            "type": "Frequency Calculation",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "HF",
            "basis_set": "3-21G",
            "charge": "-1",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = freq
        method = hf
        basis = 3-21g
        mem_total = 2000
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_freq_DFT(self):
        params = {
            "mem": "2000MB",
            "type": "Frequency Calculation",
            "file": "Cl.xyz",
            "software": "QChem",
            "charge": "-1",
            "method": "B3LYP",
            "basis_set": "6-31+G(d,p)",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = freq
        method = b3lyp
        basis = 6-31+g(d,p)
        mem_total = 2000
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # opt mod SE and HF

    # def test_scan_bond_DFT(self):
    #     params = {
    #         "type": "Constrained Optimisation",
    #         "file": "ethanol.xyz",
    #         "software": "QChem",
    #         "charge": "0",
    #         "method": "B3LYP",
    #         "basis_set": "6-31+G(d,p)",
    #         "constraints": "Scan_9_1.4_10/1_2;",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !OPT B3LYP 6-31+G(d,p)
    #     *xyz 0 1
    #     C         -1.31970       -0.64380        0.00000
    #     H         -0.96310       -1.65260        0.00000
    #     H         -0.96310       -0.13940       -0.87370
    #     H         -2.38970       -0.64380        0.00000
    #     C         -0.80640        0.08220        1.25740
    #     H         -1.16150        1.09160        1.25640
    #     H         -1.16470       -0.42110        2.13110
    #     O          0.62360        0.07990        1.25870
    #     H          0.94410        0.53240        2.04240
    #     *
    #     %geom Scan
    #     B 0 1 = 9.00, 1.40, 10
    #     end
    #     end
    #     %pal
    #     nprocs 8
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_invalid_opt_mod(self):
    #     params = {
    #         "type": "Constrained Optimisation",
    #         "file": "ethanol.xyz",
    #         "software": "QChem",
    #         "charge": "0",
    #         "method": "B3LYP",
    #         "basis_set": "6-31+G(d,p)",
    #         "constraints": "",
    #     }

    #     with self.assertRaises(Exception):
    #         self.generate_calculation(**params)

    # def test_no_method(self):
    #     params = {
    #         "mem": "2000MB",
    #         "type": "Constrained Optimisation",
    #         "file": "ethanol.xyz",
    #         "software": "QChem",
    #         "charge": "0",
    #         "method": "",
    #         "basis_set": "6-31+G(d,p)",
    #         "constraints": "",
    #     }

    #     # TODO raise specific exception?
    #     with self.assertRaises(Exception):
    #         self.generate_calculation(**params)

    # def test_scan_angle_DFT(self):
    #     params = {
    #         "type": "Constrained Optimisation",
    #         "file": "ethanol.xyz",
    #         "software": "QChem",
    #         "charge": "0",
    #         "method": "B3LYP",
    #         "basis_set": "6-31+G(d,p)",
    #         "constraints": "Scan_9_90_10/2_1_3;",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !OPT B3LYP 6-31+G(d,p)
    #     *xyz 0 1
    #     C         -1.31970       -0.64380        0.00000
    #     H         -0.96310       -1.65260        0.00000
    #     H         -0.96310       -0.13940       -0.87370
    #     H         -2.38970       -0.64380        0.00000
    #     C         -0.80640        0.08220        1.25740
    #     H         -1.16150        1.09160        1.25640
    #     H         -1.16470       -0.42110        2.13110
    #     O          0.62360        0.07990        1.25870
    #     H          0.94410        0.53240        2.04240
    #     *
    #     %geom Scan
    #     A 1 0 2 = 9.00, 90.00, 10
    #     end
    #     end
    #     %pal
    #     nprocs 8
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_scan_dihedral_DFT(self):
    #     params = {
    #         "type": "Constrained Optimisation",
    #         "file": "ethanol.xyz",
    #         "software": "QChem",
    #         "charge": "0",
    #         "method": "B3LYP",
    #         "basis_set": "6-31+G(d,p)",
    #         "constraints": "Scan_9_1_10/4_1_5_8;",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !OPT B3LYP 6-31+G(d,p)
    #     *xyz 0 1
    #     C         -1.31970       -0.64380        0.00000
    #     H         -0.96310       -1.65260        0.00000
    #     H         -0.96310       -0.13940       -0.87370
    #     H         -2.38970       -0.64380        0.00000
    #     C         -0.80640        0.08220        1.25740
    #     H         -1.16150        1.09160        1.25640
    #     H         -1.16470       -0.42110        2.13110
    #     O          0.62360        0.07990        1.25870
    #     H          0.94410        0.53240        2.04240
    #     *
    #     %geom Scan
    #     D 3 0 4 7 = 9.00, 1.00, 10
    #     end
    #     end
    #     %pal
    #     nprocs 8
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # # def test_scan_no_constraint(self):
    # #     params = {
    #         "type": "Constrained Optimisation",
    #         "file": "ethanol.xyz",
    #         "software": "QChem",
    #         "charge": "0",
    #         "method": "B3LYP",
    #         "basis_set": "6-31+G(d,p)",
    #     }

    #     with self.assertRaises(InvalidParameter):
    #         self.generate_calculation(**params)

    # def test_freeze_bond_DFT(self):
    #     params = {
    #         "type": "Constrained Optimisation",
    #         "file": "ethanol.xyz",
    #         "software": "QChem",
    #         "charge": "0",
    #         "method": "B3LYP",
    #         "basis_set": "6-31+G(d,p)",
    #         "constraints": "Freeze/1_2;",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !OPT B3LYP 6-31+G(d,p)
    #     *xyz 0 1
    #     C         -1.31970       -0.64380        0.00000
    #     H         -0.96310       -1.65260        0.00000
    #     H         -0.96310       -0.13940       -0.87370
    #     H         -2.38970       -0.64380        0.00000
    #     C         -0.80640        0.08220        1.25740
    #     H         -1.16150        1.09160        1.25640
    #     H         -1.16470       -0.42110        2.13110
    #     O          0.62360        0.07990        1.25870
    #     H          0.94410        0.53240        2.04240
    #     *
    #     %geom Constraints
    #     { B 0 1 C }
    #     end
    #     end
    #     %pal
    #     nprocs 8
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_freeze_angle_DFT(self):
    #     params = {
    #         "type": "Constrained Optimisation",
    #         "file": "ethanol.xyz",
    #         "software": "QChem",
    #         "charge": "0",
    #         "method": "B3LYP",
    #         "basis_set": "6-31+G(d,p)",
    #         "constraints": "Freeze/2_1_3;",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !OPT B3LYP 6-31+G(d,p)
    #     *xyz 0 1
    #     C         -1.31970       -0.64380        0.00000
    #     H         -0.96310       -1.65260        0.00000
    #     H         -0.96310       -0.13940       -0.87370
    #     H         -2.38970       -0.64380        0.00000
    #     C         -0.80640        0.08220        1.25740
    #     H         -1.16150        1.09160        1.25640
    #     H         -1.16470       -0.42110        2.13110
    #     O          0.62360        0.07990        1.25870
    #     H          0.94410        0.53240        2.04240
    #     *
    #     %geom Constraints
    #     { A 1 0 2 C }
    #     end
    #     end
    #     %pal
    #     nprocs 8
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_freeze_dihedral_DFT(self):
    #     params = {
    #         "type": "Constrained Optimisation",
    #         "file": "ethanol.xyz",
    #         "software": "QChem",
    #         "charge": "0",
    #         "method": "B3LYP",
    #         "basis_set": "6-31+G(d,p)",
    #         "constraints": "Freeze/4_1_5_8;",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !OPT B3LYP 6-31+G(d,p)
    #     *xyz 0 1
    #     C         -1.31970       -0.64380        0.00000
    #     H         -0.96310       -1.65260        0.00000
    #     H         -0.96310       -0.13940       -0.87370
    #     H         -2.38970       -0.64380        0.00000
    #     C         -0.80640        0.08220        1.25740
    #     H         -1.16150        1.09160        1.25640
    #     H         -1.16470       -0.42110        2.13110
    #     O          0.62360        0.07990        1.25870
    #     H          0.94410        0.53240        2.04240
    #     *
    #     %geom Constraints
    #     { D 3 0 4 7 C }
    #     end
    #     end
    #     %pal
    #     nprocs 8
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_nmr_DFT(self):
        params = {
            "mem": "2000MB",
            "type": "NMR Prediction",
            "file": "Cl.xyz",
            "software": "QChem",
            "charge": "-1",
            "method": "B3LYP",
            "basis_set": "6-31+G(d,p)",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = sp
        moprop = nmr
        method = b3lyp
        basis = 6-31+g(d,p)
        mem_total = 2000
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_irrelevant_gen_bs(self):
        params = {
            "type": "NMR Prediction",
            "file": "Cl.xyz",
            "software": "QChem",
            "charge": "-1",
            "method": "B3LYP",
            "basis_set": "6-31+G(d,p)",
            "custom_basis_sets": "N=Def2-SVP;",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl   0.00000000   0.00000000   0.00000000
        $end

        $rem
        jobtype = sp
        moprop = nmr
        method = b3lyp
        basis = 6-31+g(d,p)
        mem_total = 1000
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_ts_DFT(self):
        params = {
            "mem": "2000MB",
            "type": "TS Optimisation",
            "file": "mini_ts.xyz",
            "software": "QChem",
            "charge": "0",
            "method": "B3LYP",
            "basis_set": "6-31+G(d,p)",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        0 1
        N   1.08764072053386     -0.33994563112543     -0.00972525479568
        H   1.99826836912112      0.05502842705407      0.00651240826058
        H   0.59453997172323     -0.48560162159600      0.83949232123172
        H   0.66998093862168     -0.58930117433261     -0.87511947469677
        $end

        $rem
        jobtype = ts
        method = b3lyp
        basis = 6-31+g(d,p)
        mem_total = 2000
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

        # combination tests

    # def test_ts_DFT_custom_bs(self):
    #     params = {
    #         "type": "TS Optimisation",
    #         "file": "mini_ts.xyz",
    #         "software": "QChem",
    #         "charge": "0",
    #         "method": "B3LYP",
    #         "basis_set": "6-31+G(d,p)",
    #         "custom_basis_sets": "N=Def2-SVP;",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !OPTTS B3LYP 6-31+G(d,p)
    #     *xyz 0 1
    #     N   1.08764072053386     -0.33994563112543     -0.00972525479568
    #     H   1.99826836912112      0.05502842705407      0.00651240826058
    #     H   0.59453997172323     -0.48560162159600      0.83949232123172
    #     H   0.66998093862168     -0.58930117433261     -0.87511947469677
    #     *
    #     %basis
    #     newgto N
    #     S   5
    #     1      1712.8415853             -0.53934125305E-02
    #     2       257.64812677            -0.40221581118E-01
    #     3        58.458245853           -0.17931144990
    #     4        16.198367905           -0.46376317823
    #     5         5.0052600809          -0.44171422662
    #     S   1
    #     1         0.58731856571          1.0000000
    #     S   1
    #     1         0.18764592253          1.0000000
    #     P   3
    #     1        13.571470233           -0.40072398852E-01
    #     2         2.9257372874          -0.21807045028
    #     3         0.79927750754         -0.51294466049
    #     P   1
    #     1         0.21954348034          1.0000000
    #     D   1
    #     1         1.0000000              1.0000000
    #     end
    #     end
    #     %pal
    #     nprocs 8
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_opt_DFT_custom_bs_ecp(self):
    #     params = {
    #         "type": "Geometrical Optimisation",
    #         "file": "Ph2I_cation.xyz",
    #         "software": "QChem",
    #         "charge": "+1",
    #         "method": "B3LYP",
    #         "basis_set": "6-31+G(d,p)",
    #         "custom_basis_sets": "I=Def2-TZVPD;",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     $comment
    #     File created by ccinput
    #     $end

    #     $molecule
    #     1 1
    #     C         -3.06870       -2.28540        0.00000
    #     C         -1.67350       -2.28540        0.00000
    #     C         -0.97600       -1.07770        0.00000
    #     C         -1.67360        0.13090       -0.00120
    #     C         -3.06850        0.13080       -0.00170
    #     C         -3.76610       -1.07740       -0.00070
    #     H         -3.61840       -3.23770        0.00040
    #     H         -1.12400       -3.23790        0.00130
    #     H          0.12370       -1.07760        0.00060
    #     H         -1.12340        1.08300       -0.00130
    #     H         -4.86570       -1.07720       -0.00090
    #     I         -4.11890        1.94920       -0.00350
    #     C         -4.64360        2.85690       -1.82310
    #     C         -3.77180        3.76300       -2.42740
    #     C         -5.86360        2.55380       -2.42750
    #     C         -4.12020        4.36650       -3.63560
    #     H         -2.81040        4.00240       -1.95030
    #     C         -6.21180        3.15650       -3.63650
    #     H         -6.55070        1.83950       -1.95140
    #     C         -5.34050        4.06290       -4.24060
    #     H         -3.43340        5.08120       -4.11170
    #     H         -7.17360        2.91710       -4.11310
    #     H         -5.61500        4.53870       -5.19320
    #     $end

    #     $rem
    #     jobtype = opt
    #     method = b3lyp
    #     basis
    #     mem_total = 1000
    #     $end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_NEB(self):
    #     params = {
    #         "type": "Minimum Energy Path",
    #         "file": "elimination_substrate.xyz",
    #         "auxiliary_file": "elimination_product.xyz",
    #         "software": "QChem",
    #         "charge": -1,
    #         "method": "HF",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     $comment
    #     File created by ccinput
    #     $end

    #     $molecule
    #     -1 1
    #     C         -0.74277        0.14309        0.12635
    #     C          0.71308       -0.12855       -0.16358
    #     Cl         0.90703       -0.47793       -1.61303
    #     H         -0.84928        0.38704        1.20767
    #     H         -1.36298       -0.72675       -0.06978
    #     H         -1.11617        0.99405       -0.43583
    #     H          1.06397       -0.95639        0.44985
    #     H          1.30839        0.75217        0.07028
    #     O         -0.91651        0.74066        3.00993
    #     H         -1.82448        0.94856        3.28105
    #     ****
    #     C         -0.89816        0.30949        0.13095
    #     C          0.41712        0.14751        0.20321
    #     Cl         1.32706       -0.97006       -2.40987
    #     H         -1.14270        0.57588        2.51484
    #     H         -1.57182       -0.52496        0.20609
    #     H         -1.34211        1.27553       -0.03286
    #     H          0.86001       -0.81888        0.34553
    #     H          1.09447        0.97622        0.10901
    #     O         -1.18361        0.65508        3.47337
    #     H         -1.98467        1.14237        3.68042
    #     $end

    #     $rem
    #     jobtype = fsm
    #     method = hf
    #     basis = 3-21g
    #     mem_total = 1000
    #     $end
    #     """
    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_NEB2(self):
    #     params = {
    #         "type": "Minimum Energy Path",
    #         "file": "elimination_substrate.xyz",
    #         "auxiliary_file": "elimination_product.xyz",
    #         "software": "QChem",
    #         "specifications": "--nimages 12",
    #         "charge": -1,
    #         "method": "gfn2-xtb",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """!NEB xtb2
    #     *xyz -1 1
    #     C         -0.74277        0.14309        0.12635
    #     C          0.71308       -0.12855       -0.16358
    #     Cl         0.90703       -0.47793       -1.61303
    #     H         -0.84928        0.38704        1.20767
    #     H         -1.36298       -0.72675       -0.06978
    #     H         -1.11617        0.99405       -0.43583
    #     H          1.06397       -0.95639        0.44985
    #     H          1.30839        0.75217        0.07028
    #     O         -0.91651        0.74066        3.00993
    #     H         -1.82448        0.94856        3.28105
    #     *
    #     %neb
    #     product "calc2.xyz"
    #     nimages 12
    #     end
    #     %pal
    #     nprocs 8
    #     end

    #     """
    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_NEB_aux_name(self):
    #     params = {
    #         "type": "Minimum Energy Path",
    #         "file": "elimination_substrate.xyz",
    #         "auxiliary_file": "elimination_product.xyz",
    #         "software": "QChem",
    #         "specifications": "--nimages 12",
    #         "charge": -1,
    #         "method": "gfn2-xtb",
    #         "aux_name": "product",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """!NEB xtb2
    #     *xyz -1 1
    #     C         -0.74277        0.14309        0.12635
    #     C          0.71308       -0.12855       -0.16358
    #     Cl         0.90703       -0.47793       -1.61303
    #     H         -0.84928        0.38704        1.20767
    #     H         -1.36298       -0.72675       -0.06978
    #     H         -1.11617        0.99405       -0.43583
    #     H          1.06397       -0.95639        0.44985
    #     H          1.30839        0.75217        0.07028
    #     O         -0.91651        0.74066        3.00993
    #     H         -1.82448        0.94856        3.28105
    #     *
    #     %neb
    #     product "product.xyz"
    #     nimages 12
    #     end
    #     %pal
    #     nprocs 8
    #     end

    #     """
    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_hirshfeld_pop(self):
        params = {
            "type": "Single-Point Energy",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "M06-2X",
            "basis_set": "Def2-SVP",
            "charge": "-1",
            "specifications": "--phirshfeld",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = sp
        method = m06-2x
        basis = def2-svp
        mem_total = 1000
        hirshfeld = true
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_mo(self):
    #     params = {
    #         "type": "MO Calculation",
    #         "file": "Ph2I_cation.xyz",
    #         "software": "QChem",
    #         "charge": "+1",
    #         "method": "B3LYP",
    #         "basis_set": "def2tzvp",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !SP B3LYP Def2-TZVP
    #     *xyz 1 1
    #     C         -3.06870       -2.28540        0.00000
    #     C         -1.67350       -2.28540        0.00000
    #     C         -0.97600       -1.07770        0.00000
    #     C         -1.67360        0.13090       -0.00120
    #     C         -3.06850        0.13080       -0.00170
    #     C         -3.76610       -1.07740       -0.00070
    #     H         -3.61840       -3.23770        0.00040
    #     H         -1.12400       -3.23790        0.00130
    #     H          0.12370       -1.07760        0.00060
    #     H         -1.12340        1.08300       -0.00130
    #     H         -4.86570       -1.07720       -0.00090
    #     I         -4.11890        1.94920       -0.00350
    #     C         -4.64360        2.85690       -1.82310
    #     C         -3.77180        3.76300       -2.42740
    #     C         -5.86360        2.55380       -2.42750
    #     C         -4.12020        4.36650       -3.63560
    #     H         -2.81040        4.00240       -1.95030
    #     C         -6.21180        3.15650       -3.63650
    #     H         -6.55070        1.83950       -1.95140
    #     C         -5.34050        4.06290       -4.24060
    #     H         -3.43340        5.08120       -4.11170
    #     H         -7.17360        2.91710       -4.11310
    #     H         -5.61500        4.53870       -5.19320
    #     *
    #     %plots
    #     dim1 45
    #     dim2 45
    #     dim3 45
    #     min1 0
    #     max1 0
    #     min2 0
    #     max2 0
    #     min3 0
    #     max3 0
    #     Format Gaussian_Cube
    #     MO("in-HOMO.cube",66,0);
    #     MO("in-LUMO.cube",67,0);
    #     MO("in-LUMOA.cube",68,0);
    #     MO("in-LUMOB.cube",69,0);
    #     end

    #     %pal
    #     nprocs 8
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_opt_freq(self):
    #     params = {
    #         "type": "opt+freq",
    #         "file": "Cl.xyz",
    #         "software": "QChem",
    #         "method": "AM1",
    #         "charge": "-1",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !OPT FREQ AM1
    #     *xyz -1 1
    #     Cl 0.0 0.0 0.0
    #     *
    #     %pal
    #     nprocs 1
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_d3(self):
        params = {
            "type": "opt",
            "file": "Cl.xyz",
            "software": "QChem",
            "basis_set": "Def2TZVP",
            "method": "M062X",
            "charge": "-1",
            "d3": True,
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = opt
        method = m06-2x
        basis = def2-tzvp
        mem_total = 1000
        dft_d = d3_zero
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_d3bj(self):
        params = {
            "type": "opt",
            "file": "Cl.xyz",
            "software": "QChem",
            "basis_set": "Def2TZVP",
            "method": "PBE0",
            "charge": "-1",
            "d3bj": True,
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = opt
        method = pbe0
        basis = def2-tzvp
        mem_total = 1000
        dft_d = d3_bj
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_d3_d3bj_crash(self):
        params = {
            "type": "opt",
            "file": "Cl.xyz",
            "software": "QChem",
            "basis_set": "Def2TZVP",
            "method": "PBE0",
            "charge": "-1",
            "d3": True,
            "d3bj": True,
        }

        with self.assertRaises(InvalidParameter):
            self.generate_calculation(**params)

    # def test_SMD_custom_radius(self):
    #     params = {
    #         "type": "Single-Point Energy",
    #         "file": "Cl.xyz",
    #         "software": "QChem",
    #         "method": "HF",
    #         "basis_set": "3-21G",
    #         "charge": "-1",
    #         "solvent": "Chloroform",
    #         "solvation_model": "SMD",
    #         "custom_solvation_radii": "Cl=1.00;",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !SP HF 3-21G
    #     *xyz -1 1
    #     Cl 0.0 0.0 0.0
    #     *
    #     %pal
    #     nprocs 8
    #     end
    #     %cpcm
    #     smd true
    #     SMDsolvent "chloroform"
    #     radius[17] 1.00
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_SMD_custom_radii(self):
    #     params = {
    #         "type": "Single-Point Energy",
    #         "file": "Cl.xyz",
    #         "software": "QChem",
    #         "method": "HF",
    #         "basis_set": "3-21G",
    #         "charge": "-1",
    #         "solvent": "Chloroform",
    #         "solvation_model": "SMD",
    #         "custom_solvation_radii": "Cl=1.00;Br=2.00;",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !SP HF 3-21G
    #     *xyz -1 1
    #     Cl 0.0 0.0 0.0
    #     *
    #     %pal
    #     nprocs 8
    #     end
    #     %cpcm
    #     smd true
    #     SMDsolvent "chloroform"
    #     radius[17] 1.00
    #     radius[35] 2.00
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_SMD_custom_radius_and_SMD18(self):
    #     params = {
    #         "type": "Single-Point Energy",
    #         "file": "Cl.xyz",
    #         "software": "QChem",
    #         "method": "HF",
    #         "basis_set": "3-21G",
    #         "charge": "-1",
    #         "solvent": "Chloroform",
    #         "solvation_model": "SMD",
    #         "solvation_radii": "SMD18",
    #         "custom_solvation_radii": "Cl=1.00;",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !SP HF 3-21G
    #     *xyz -1 1
    #     Cl 0.0 0.0 0.0
    #     *
    #     %pal
    #     nprocs 8
    #     end
    #     %cpcm
    #     smd true
    #     SMDsolvent "chloroform"
    #     radius[17] 1.00
    #     radius[53] 2.74
    #     radius[35] 2.60
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    # def test_SMD_custom_radius_and_SMD18_clash(self):
    #     params = {
    #         "type": "Single-Point Energy",
    #         "file": "Cl.xyz",
    #         "software": "QChem",
    #         "method": "HF",
    #         "basis_set": "3-21G",
    #         "charge": "-1",
    #         "solvent": "Chloroform",
    #         "solvation_model": "SMD",
    #         "solvation_radii": "SMD18",
    #         "custom_solvation_radii": "I=3.00;",
    #     }

    #     inp = self.generate_calculation(**params)

    #     REF = """
    #     !SP HF 3-21G
    #     *xyz -1 1
    #     Cl 0.0 0.0 0.0
    #     *
    #     %pal
    #     nprocs 8
    #     end
    #     %cpcm
    #     smd true
    #     SMDsolvent "chloroform"
    #     radius[53] 3.00
    #     radius[35] 2.60
    #     end
    #     """

    #     self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_CPCM_custom_radius(self):
        params = {
            "type": "Single-Point Energy",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "HF",
            "basis_set": "3-21G",
            "charge": "-1",
            "solvent": "Chloroform",
            "solvation_model": "CPCM",
            "custom_solvation_radii": "Cl=1.00;",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = sp
        method = hf
        basis = 3-21g
        mem_total = 1000
        solvent_method = pcm
        $end

        $pcm
        theory cpcm
        radii read
        $end

        $solvent
        solventname trichloromethane
        $end

        $van_der_waals
        1
        17 1.00
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))

    def test_CPCM_custom_radii(self):
        params = {
            "type": "Single-Point Energy",
            "file": "Cl.xyz",
            "software": "QChem",
            "method": "HF",
            "basis_set": "3-21G",
            "charge": "-1",
            "solvent": "Chloroform",
            "solvation_model": "CPCM",
            "custom_solvation_radii": "Cl=1.00;Br=2.00;",
        }

        inp = self.generate_calculation(**params)

        REF = """
        $comment
        File created by ccinput
        $end

        $molecule
        -1 1
        Cl 0.0 0.0 0.0
        $end

        $rem
        jobtype = sp
        method = hf
        basis = 3-21g
        mem_total = 1000
        solvent_method = pcm
        $end

        $pcm
        theory cpcm
        radii read
        $end

        $solvent
        solventname trichloromethane
        $end

        $van_der_waals
        1
        17 1.00
        35 2.00
        $end
        """

        self.assertTrue(self.is_equivalent(REF, inp.input_file))
