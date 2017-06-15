FROM mongo
COPY pie.json /pie.json
COPY force_directed.json /force_directed.json
COPY line_plus_bar.json /line_plus_bar.json
COPY line.json /line.json
COPY ohlc_bar.json /ohlc_bar.json
COPY stacked_area.json /stacked_area.json
COPY cumulative_line.json /cumulative_line.json
ADD run.sh /run.sh
RUN chmod +x /run.sh
CMD ["/run.sh"]
