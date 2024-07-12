
## Network Security Assessment Guide (AAS 2024)

### Overview
This guide will walk you through a series of exercises to help you understand and practice various aspects of network security assessment, including scanning, enumeration, and exploitation. You will use the provided Docker Compose setup to explore a simulated network environment.

### Setup Instructions
1. **Clone the repository:**
    ```sh
    git clone https://github.com/babahayo1/aas2024keamananjaringan.git
    cd aas2024keamananjaringan
    ```

2. **Build and start the services:**
    ```sh
    docker-compose up --build
    ```

3. **Verify the setup
    ```sh
    docker-compose ps
    ```  
    You should see the following services running:

    - vulnerable-web
    - db
    - fileserver
    - scanner

3. **Access the vulnerable web application:**
    - Open a web browser and go to `http://localhost:8080`.

4. **Access the scanner container:**
    - Open a terminal and run:
        ```sh
        docker exec -it aas2024keamananjaringan_scanner_1 /bin/bash
        ```

### Exercises

#### 1. Scanning the Network
**Objective:** Use `nmap` to identify the services running on the network.

**Instructions:**
- From within the scanner container, run an `nmap` scan to discover open ports and services.
    ```sh
    nmap -sV db
    nmap -sV vulnerable-web
    nmap -sV fileserver
    ```

**Questions:**
1. What services are running on the `vulnerable-web` container?
2. What ports are open on the `db` container?
3. Which services are exposed by the `fileserver`?

#### 2. Enumerating the Web Application
**Objective:** Use tools to enumerate and identify vulnerabilities in the web application.

**Instructions:**
- Use `nikto` to scan the web application for potential vulnerabilities.
    ```sh
    nikto -h http://vulnerable-web:5000
    ```

**Questions:**
1. What vulnerabilities did `nikto` identify on the web application?
2. What information can you gather about the web application from the `nikto` scan?

#### 3. Exploiting SQL Injection
**Objective:** Identify and exploit the SQL injection vulnerability in the web application.

**Instructions:**
- Explore the `/sql_injection` endpoint. Try accessing it with different `id` values to see if you can manipulate the SQL query.
    ```sh
    http://localhost:8080/sql_injection?id=1
    http://localhost:8080/sql_injection?id=1' OR '1'='1
    ```

**Questions:**
1. How can you confirm the presence of an SQL injection vulnerability?
2. What data can you extract from the database using SQL injection?

#### 4. Enumerating the File Server
**Objective:** Enumerate the file shares available on the Samba server.

**Instructions:**
- Use `smbclient` to list the available shares on the `fileserver`.
    ```sh
    smbclient -L //fileserver
    ```

**Questions:**
1. What shares are available on the Samba server?
2. Can you access any of the shares without authentication? If so, what files are available?

#### 5. Exploiting the File Server
**Objective:** Exploit the file server by accessing and modifying files in the public share.

**Instructions:**
- Access the public share on the Samba server.
    ```sh
    smbclient //fileserver/public
    ```
- Upload a file to the share and verify its presence.

**Questions:**
1. Were you able to upload a file to the public share?
2. What implications does the ability to upload files to the share have for security?

#### 6. Using Metasploit for Further Exploitation
**Objective:** Use Metasploit to identify and exploit vulnerabilities on the network.

**Instructions:**
- Start Metasploit in the scanner container.
    ```sh
    msfconsole
    ```
- Use Metasploit to exploit known vulnerabilities in the network services.

**Questions:**
1. Which Metasploit modules were effective in exploiting the vulnerabilities you discovered?
2. What additional information were you able to gather using Metasploit?

## Report Submission

After completing the network security assessment, students must submit a detailed report in PDF format and submit it to our learning application and the due date on 15 July 2024. The report should be clear and well-organized, including the following sections:

1. **Introduction:**
   - Overview of the assessment and objectives.

2. **Scanning Results:**
   - Screenshots or outputs of the scanning phase.
   - Analysis of open ports and services discovered.

3. **Enumeration Details:**
   - Screenshots or outputs from enumeration tools.
   - Detailed findings and information gathered.

4. **Exploitation Attempts:**
   - Step-by-step documentation of exploitation techniques used.
   - Evidence of successful exploitation (screenshots, logs, etc.).

5. **Conclusion:**
   - Summary of findings.
   - Recommendations for improving security based on the assessment.

Ensure the report includes evidence such as screenshots and command outputs to support your findings and conclusions.

## Cleanup

To stop and remove all the services, run:

```sh
docker-compose down
```

## Troubleshooting

If you encounter any issues, check the logs of the respective services:

```sh
docker-compose logs [service_name]
```

Replace `[service_name]` with the name of the service (e.g., `db`, `vulnerable-web`).

## Conclusion

This setup provides a practical environment for learning and practicing basic network security assessment techniques. Students can explore various aspects of network security, including scanning, enumeration, and exploitation, in a controlled environment.

Feel free to contribute to this project by submitting pull requests or opening issues.


### Directory Structure

Ensure your directory structure matches the following:

```sh
Foldername/
│
├── docker-compose.yml
│
├── README.md
│
├── vulnerable-web/
│   ├── Dockerfile
│   ├── app.py
│
├── db/
│   ├── Dockerfile
│   └── init.sql
│
├── fileserver/
│   ├── Dockerfile
│   └── smb.conf
│
└── scanner/
    ├── Dockerfile
```
