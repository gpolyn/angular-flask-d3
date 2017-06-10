FROM mongo
COPY pie.json /pie.json
COPY forcedirected.json /forcedirected.json
ADD run.sh /run.sh
RUN chmod +x /run.sh
CMD ["/run.sh"]
