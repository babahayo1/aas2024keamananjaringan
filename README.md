Certainly! Here’s a structured guide for students, including questions and instructions to help them understand and practice network security assessment concepts using the Docker Compose setup.

## Network Security Assessment Guide

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

3. **Access the vulnerable web application:**
    - Open a web browser and go to `http://localhost:8080`.

4. **Access the scanner container:**
    - Open a terminal and run:
        ```sh
        docker exec -it network-security-assessment_scanner_1 /bin/bash
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

### Conclusion
By completing these exercises, you should have a better understanding of the basic principles of network security assessment, including scanning, enumeration, and exploitation. Reflect on the findings and consider the implications of these vulnerabilities in real-world scenarios.

### Cleanup
After completing the exercises, you can stop and remove the Docker containers with:
```sh
docker-compose down
```

This guide provides a comprehensive, hands-on learning experience for students to understand network security assessment concepts.