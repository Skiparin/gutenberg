# gutenberg

### Gruppe 8:
Laura Hartig  
Ørvur Guttesen  
Tim Hemmingsen  
Michael Daugbjerg  

Pojeketets database opgave kan findes her: [Database.pdf](https://github.com/Skiparin/gutenberg/blob/master/Database.pdf)

Dette projekt er baseret på en PostgreSQL- og en Mongodb database, hvor vi skal benytte fire queries til at lave en lille frontend applikation, som kan benytte sig af dette data, som vi får gennem disse queries.
Projektet kan:
- Hente titler på de bøger, som nævner en specifik by.
- Hente koordinater ud fra alle byer nævnt i en bog og plotte dem på et kort.
- Hente en liste over alle titler skrevet af en given author, og plotte alle byer nævnt i disse bøger.
- Hente alle titler, som nævner en by i nærheden af den angivet geolocation.

Hertil har vi lavet nogle performance test hvor vi køre hver query, fem gange med et array af data, og tager et tidsestimat på hvor langtid disse queries tager.
