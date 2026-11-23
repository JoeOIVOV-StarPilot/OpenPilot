"""Stateless parked preview. Returned coordinates are for display on the companion."""
from openpilot.starpilot.navigation.route_engine import NavigationRoute


def preview_route(payload):
  if not isinstance(payload, dict) or set(payload) != {'version', 'route'} or type(payload['version']) is not int or payload['version'] != 1:
    raise ValueError('Invalid preview version')
  data = payload['route']
  if not isinstance(data, dict) or len(data['legs']) != 1 or not 2 <= len(data['geometry']['coordinates']) <= 1500:
    raise ValueError('Invalid route shape')
  steps = data['legs'][0]['steps']
  if not isinstance(steps, list) or not 1 <= len(steps) <= 256:
    raise ValueError('Invalid steps')
  if any(not isinstance(step, dict) or 'bannerInstructions' in step or not isinstance(step.get('maneuver'), dict) for step in steps):
    raise ValueError('Invalid maneuver')
  route = NavigationRoute(data)
  first = route.progress(route.points[0], None).instruction
  return {'version': 1, 'points': route.preview(), 'steps': len(steps), 'firstInstruction': first['text']}
