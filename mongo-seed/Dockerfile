FROM mongo
COPY pie.json /pie.json
COPY force_directed.json /force_directed.json
COPY bullet_chart.json /bullet_chart.json
COPY line_plus_bar.json /line_plus_bar.json
COPY line.json /line.json
COPY line_with_focus.json /line_with_focus.json
COPY multi_bar_horizontal.json /multi_bar_horizontal.json
COPY ohlc_bar.json /ohlc_bar.json
COPY scatter_plus_line_chart.json /scatter_plus_line_chart.json
COPY stacked_area.json /stacked_area.json
COPY cumulative_line.json /cumulative_line.json
ADD run.sh /run.sh
RUN chmod +x /run.sh
CMD ["/run.sh"]
