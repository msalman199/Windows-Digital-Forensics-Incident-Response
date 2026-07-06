# 🔍 Parse NTFS Master File Table (MFT) with MFTECmd

<div align="center">

# 🛡️ Windows Digital Forensics Lab

## **Parse NTFS Master File Table (MFT) with MFTECmd**

*Learn how to extract, parse, analyze, and investigate NTFS Master File Table artifacts for digital forensic investigations.*

---

![Windows](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)
![Linux](https://img.shields.io/badge/Platform-Linux-FCC624?style=for-the-badge&logo=linux)
![NTFS](https://img.shields.io/badge/FileSystem-NTFS-blue?style=for-the-badge)
![MFTECmd](https://img.shields.io/badge/Tool-MFTECmd-success?style=for-the-badge)
![DFIR](https://img.shields.io/badge/Domain-Digital%20Forensics-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)
![Bash](https://img.shields.io/badge/Bash-Scripting-black?style=for-the-badge&logo=gnubash)
![CSV](https://img.shields.io/badge/Data-CSV-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-success?style=for-the-badge)

</div>

---

# 📖 Lab Overview

The **NTFS Master File Table (MFT)** is the heart of every NTFS file system. Every file and directory stored on an NTFS volume has a corresponding record inside the MFT, making it one of the most valuable forensic artifacts available during an investigation.

In this lab, you will learn how to use **MFTECmd** to extract, parse, and analyze MFT records from an NTFS disk image. You will investigate timestamps, metadata, deleted files, Alternate Data Streams (ADS), and other forensic artifacts commonly used during Windows Digital Forensics and Incident Response (DFIR).

---

# 🎯 Learning Objectives

By completing this lab, you will be able to:

- ✅ Understand the structure of the NTFS Master File Table (MFT)
- ✅ Install and configure MFTECmd
- ✅ Create a sample NTFS image for forensic analysis
- ✅ Extract MFT data from a disk image
- ✅ Parse MFT records using MFTECmd
- ✅ Analyze file metadata and timestamps
- ✅ Investigate deleted file records
- ✅ Identify Alternate Data Streams (ADS)
- ✅ Generate forensic reports from CSV output
- ✅ Build forensic timelines for investigations

---

# 🧠 Skills You'll Gain

- 🔍 NTFS Forensics
- 📂 MFT Record Analysis
- 🗃 File Metadata Investigation
- 🕒 Timeline Analysis
- 📊 CSV Data Analysis
- 💻 Linux Command Line
- 🐍 Python Automation Concepts
- 📄 Digital Evidence Interpretation
- 🛡 Incident Response Techniques

---

# 🛠 Technologies Used

| Category | Tools |
|----------|------|
| Operating System | Ubuntu Linux |
| File System | NTFS |
| Parser | MFTECmd |
| Runtime | .NET 6 |
| Disk Utilities | dd, ntfs-3g |
| CSV Analysis | csvkit |
| Shell | Bash |
| Hex Analysis | hexdump |

---

# 📚 Prerequisites

Before starting this lab, ensure you have:

- Basic Linux command-line knowledge
- Understanding of NTFS file systems
- Familiarity with Digital Forensics concepts
- Basic knowledge of CSV files
- Understanding of Windows file metadata

---

# 🖥️ Lab Environment

This lab uses an **Al Nafi Linux Cloud Machine**.

The virtual machine starts as a clean Linux installation without forensic tools, allowing students to perform the complete installation and configuration process.

---

# 📂 Lab Workflow

```text
Create NTFS Image
        │
        ▼
Extract MFT
        │
        ▼
Parse with MFTECmd
        │
        ▼
Analyze CSV Output
        │
        ▼
Investigate Metadata
        │
        ▼
Generate Timeline
        │
        ▼
Produce Forensic Report
```

---

# 🚀 Task 1 — Install and Configure MFTECmd

## 🎯 Objective

Prepare the forensic environment and install MFTECmd.

### ✔ Activities

- Update Linux packages
- Install .NET Runtime
- Download MFTECmd
- Extract binaries
- Configure permissions

### 🏆 Outcome

✔ Fully functional MFTECmd environment ready for forensic analysis.

---

# 💾 Task 2 — Create Sample NTFS Image

## 🎯 Objective

Build a forensic disk image for analysis.

### ✔ Activities

- Create NTFS image
- Format image
- Mount filesystem
- Create sample files
- Create folders
- Preserve timestamps
- Unmount safely

### 🏆 Outcome

✔ A complete NTFS image containing forensic artifacts.

---

# 🔎 Task 3 — Extract the Master File Table

## 🎯 Objective

Extract the MFT for analysis.

### ✔ Activities

- Locate MFT
- Extract MFT using `dd`
- Verify MFT signature
- Validate extracted data

### 🏆 Outcome

✔ Binary MFT file ready for parsing.

---

# 📑 Task 4 — Parse the MFT Using MFTECmd

## 🎯 Objective

Convert raw MFT data into readable forensic information.

### ✔ Activities

- Parse MFT
- Export CSV
- Generate verbose output
- Validate parsing results

### 🏆 Outcome

✔ Structured CSV containing all NTFS records.

---

# 📊 Task 5 — Analyze File Records

## 🎯 Objective

Examine MFT entries.

### ✔ Investigate

- File names
- Directories
- Entry numbers
- Parent records
- File attributes
- File sizes
- Extensions

### 🏆 Outcome

✔ Understanding of NTFS record structure.

---

# 🕒 Task 6 — Analyze Timestamps

## 🎯 Objective

Investigate Windows file timestamps.

### Examine

- Created Time
- Modified Time
- Accessed Time
- Entry Modified Time

### Learn

- Standard Information (0x10)
- File Name Attribute (0x30)

### 🏆 Outcome

✔ Complete timeline of filesystem activity.

---

# 📁 Task 7 — Investigate Deleted Files

## 🎯 Objective

Recover deleted file evidence.

### Activities

- Locate unused records
- Identify deleted files
- Recover metadata
- Analyze deletion artifacts

### 🏆 Outcome

✔ Discovery of deleted forensic evidence.

---

# 🛡️ Task 8 — Examine Advanced MFT Attributes

## 🎯 Objective

Investigate advanced forensic artifacts.

### Analyze

- Alternate Data Streams (ADS)
- Resident files
- Non-resident files
- System files
- Hidden files

### 🏆 Outcome

✔ Identification of suspicious artifacts.

---

# 📈 Task 9 — Generate Forensic Reports

## 🎯 Objective

Produce professional forensic documentation.

### Reports Include

- File statistics
- Largest files
- File extensions
- Timeline
- Recently created files
- Deleted records

### 🏆 Outcome

✔ Investigation-ready forensic report.

---

# ✔ Verification

Validate your forensic investigation by:

- ✅ Checking CSV integrity
- ✅ Reviewing parsed records
- ✅ Generating statistics
- ✅ Building timelines
- ✅ Confirming timestamp accuracy

---

# 📂 Expected Directory Structure

```text
Parse-NTFS-MFT-MFTECmd/
│
├── README.md
├── sample_ntfs.img
├── extracted_mft.bin
├── timeline.csv
├── mft_analysis.sh
│
├── output/
│   ├── mft_analysis.csv
│   ├── detailed_mft.csv
│   └── report.txt
│
├── scripts/
│
├── screenshots/
│
└── resources/
```

---

# 🧰 Tools Used

| Tool | Purpose |
|------|----------|
| MFTECmd | Parse NTFS MFT |
| dd | Disk extraction |
| hexdump | Binary inspection |
| csvkit | CSV analysis |
| ntfs-3g | NTFS support |
| Bash | Automation |
| .NET Runtime | Execute MFTECmd |

---

# 🧪 Forensic Artifacts Investigated

- 📂 Master File Table (MFT)
- 📄 File Records
- 🕒 MACB Timestamps
- 📑 Standard Information Attribute
- 📁 File Name Attribute
- 📦 Resident Attributes
- 💾 Non-Resident Attributes
- 🗑 Deleted File Records
- 📡 Alternate Data Streams
- 📂 Directory Records

---

# 🎓 Learning Outcomes

After completing this lab you will confidently be able to:

- ✔ Extract NTFS Master File Table data
- ✔ Parse MFT using MFTECmd
- ✔ Interpret NTFS metadata
- ✔ Analyze Windows timestamps
- ✔ Identify deleted files
- ✔ Investigate Alternate Data Streams
- ✔ Build forensic timelines
- ✔ Produce professional forensic reports
- ✔ Apply NTFS artifact analysis in DFIR investigations

---

# 🌟 Key Takeaways

- 🛡 MFT is the most important NTFS forensic artifact.
- 🔍 Every file and directory has an MFT record.
- 🕒 MFT timestamps reveal user activity.
- 📂 Deleted files often remain recoverable within the MFT.
- 📊 CSV exports simplify large-scale forensic analysis.
- ⚡ MFTECmd is one of the industry's leading NTFS forensic tools.

---

# 📖 Recommended Next Labs

- 🔹 Windows Registry Forensics
- 🔹 USN Journal Analysis
- 🔹 Windows Event Log Analysis
- 🔹 Prefetch Analysis
- 🔹 Amcache Investigation
- 🔹 Shimcache Analysis
- 🔹 SRUM Database Analysis
- 🔹 Windows Memory Forensics
- 🔹 Timeline Analysis with Plaso
- 🔹 Full Windows Incident Response

---

# 📜 License

This lab is intended **for educational purposes, authorized digital forensic investigations, and incident response training only**.

Always obtain proper authorization before examining systems or digital evidence.

---

<div align="center">

# ⭐ If this lab helped you learn Windows Digital Forensics, consider giving the repository a Star!

### 🔍 Extract • Parse • Analyze • Investigate • Report

**Happy Investigating! 🛡️💻**

</div>
