from ipywidgets import interact
import plotly.express as px
from plotly.offline import init_notebook_mode


def show_histogram(features: pd.DataFrame,
                   hover_data: str | None = None,
                   fig_type: str = '1D',
                   nbins: int | None = None):

    if fig_type not in ['1D', '2D']:
        raise ValueError("fig_type must be either '1D' or '2D'")

    if fig_type == '2D':
        @interact
        def _show(x=features.columns, y=features.columns):
            fig = px.density_heatmap(
                features, x=x, y=y,
                hover_data=hover_data,
                color_continuous_scale='Viridis'
            )
            fig.update_layout(height=600)
            fig.show()
    else:
        @interact
        def _show(x=features.columns, color=[None] + list(features.columns)):

            color_arg = color if color is not None else None
            fig = px.histogram(
                features, x=x, color=color_arg,
                nbins=nbins,
                hover_data=hover_data
            )
            fig.update_layout(bargap=0.05, height=500)
            fig.show()

    return _show

def show_scatter(features: pd.DataFrame,
                 hover_data: str,
                 fig_type: str = '3D'):
    if fig_type not in ['2D', '3D']:
        raise ValueError('fig_type must be either 3D or 2D')

    if fig_type == '3D':
        @interact
        def show(x=features.columns, y=features.columns,
                 z=features.columns, color=features.columns):
            fig = px.scatter_3d(features, x=x, y=y, z=z, color=color,
                                hover_data=hover_data)
            fig.show()
    else:
        @interact
        def show(x=features.columns, y=features.columns,
                 color=features.columns):
            fig = px.scatter(features, x=x, y=y, color=color,
                             hover_data=hover_data)
            fig.show()
    return show
#
# show_scatter(processed_data, hover_data=['feature_1', 'feature_2', 'feature_3'], fig_type="2D");
#
# show_scatter(processed_data, hover_data=['feature_1', 'feature_2', 'feature_3'], fig_type="3D");