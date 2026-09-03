from client import DynamicToolDependencyDagTopologicalResolverClient

def main():
    client = DynamicToolDependencyDagTopologicalResolverClient()
    res = client.resolve_tool_dag_execution_order({'a': [], 'b': ['a'], 'c': ['a', 'b']})
    print('Tool DAG Topological Resolver: ' + res['dag_resolution_id'])
    print('Stages: ' + str(res['topologically_sorted_execution_stages']) + ' | Circular: ' + str(res['circular_dependency_detected']))
    print('DAG URL: ' + res['dag_visual_graph_url'])

if __name__ == '__main__':
    main()
